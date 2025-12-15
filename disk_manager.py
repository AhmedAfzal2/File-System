from settings import BLOCK_SIZE, FREE_START, TOTAL_MEMORY
from bitarray import bitarray
import pickle
import os

class DiskManager:
    def __init__(self, file_name):
        self.file_name = file_name
        if os.path.exists(file_name):
            self.file = open(file_name, 'r+b')
            self.root = None # Will be loaded
            self.free_spaces = None # Will be loaded
            self.load_metadata()
        else:
            self.file = open(file_name, 'w+b')
            self.free_spaces = bitarray((TOTAL_MEMORY - FREE_START) // BLOCK_SIZE)
            self.free_spaces.setall(True)
            self.root = None    # only for loading
            
    def save_metadata(self, root):
        # as root contains references to all its children which further contain references, simply pickling the root stores the entire tree
        metadata = {
            'free': self.free_spaces,
            'root': root
        }
        
        data = pickle.dumps(metadata)
        
        if len(data) > FREE_START:
            raise MemoryError("Directory tree is too big to store in provided space, consider increasing FREE_START in settings.")
        
        # pad nulls for cleanliness
        data += b'\x00' * (FREE_START - len(data))
        
        self.file.seek(0)
        self.file.write(data)
        
    def load_metadata(self):
        self.file.seek(0)
        data = self.file.read(FREE_START)
        try:
            metadata = pickle.loads(data.rstrip(b'\x00'))   # rstrip to remove null padding
            self.free_spaces = metadata['free']
            self.root = metadata['root']
        except EOFError:
            # file exists but is empty
            pass
        
    # returns start index of a free block
    def allocate(self) -> int:
        for i, space in enumerate(self.free_spaces):
            if space:
                self.free_spaces[i] = False
                return (i + FREE_START // BLOCK_SIZE) * BLOCK_SIZE
        raise MemoryError("No free spaces available in file. Consider truncating existing files or changing TOTAL_MEMORY in settings.")

    def deallocate(self, block_index):
        # block_index is the byte offset, convert to index in free_spaces
        idx = (block_index - FREE_START) // BLOCK_SIZE
        if 0 <= idx < len(self.free_spaces):
            self.free_spaces[idx] = True

    def __del__(self):
        if hasattr(self, 'file') and self.file:
            self.file.close()
