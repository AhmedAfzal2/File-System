from settings import BLOCK_SIZE
import FileSystem
from file_io import FileReader, FileWriter

class TreeNode:
    def __init__(self, name):
        self.name: str = name

class Directory(TreeNode):
    def __init__(self, name):
        super().__init__(name)
        self.children: list[TreeNode] = []

class File(TreeNode):
    def __init__(self, name, fs):
        super().__init__(name)
        self.size: int = 0
        self.blocks: list[int] = []
        self.fs: FileSystem = fs
        self.reader = FileReader(self)
        self.writer = FileWriter(self)
        
    # part of a solution for pickling files - taken from chatGPT
    # pickling causes problems if files contain a reference to FileSystem, which contains a file object
    # so remove this reference before pickling and add it back after
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['fs']
        if 'reader' in state: del state['reader']
        if 'writer' in state: del state['writer']
        return state
        
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.fs = None
        self.reader = FileReader(self)
        self.writer = FileWriter(self)
        
    # returns remaining empty space in the last allocated block
    def last_block_remaining_size(self):
        if self.size % BLOCK_SIZE == 0 and self.size != 0:
            return 0
        else:
            return BLOCK_SIZE - (self.size % BLOCK_SIZE)
    
    def set_mode(self, mode: str):
        self.mode = mode
    
    def append_to_file(self, data: str):
        self.writer.append_to_file(data)
            
    def write_to_file(self, data: str, write_at: int = None):
        self.writer.write_to_file(data, write_at)
        
    def read_entire_file(self) -> bytes:
        return self.reader.read_entire_file()

    def read_from_file(self, start: int = None, size: int = None) -> bytes:
        return self.reader.read_from_file(start, size)
    
    def move_within_file(self, source, dest, size):
        self.writer.move_within_file(source, dest, size)
    
    def truncate_file(self, size):
        self.writer.truncate_file(size)
        
    def get_details(self):
        details = f"{self.name} of {self.size} bytes"
        if len(self.blocks) > 0:
            details += f" at blocks {self.blocks}"
        return details