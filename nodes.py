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
        """
        Calculates the remaining empty space in the last allocated block of the file.
        Returns:
            int: The number of bytes remaining in the last block.
        """
        if self.size % BLOCK_SIZE == 0 and self.size != 0:
            return 0
        else:
            return BLOCK_SIZE - (self.size % BLOCK_SIZE)
    
    def set_mode(self, mode: str):
        """
        Sets the mode of the file.
        Args:
            mode (str): The mode to set (e.g., 'r', 'w', 'a', 'r+', 'w+', 'a+').
        """
        self.mode = mode
    
    def append_to_file(self, data: str):
        """
        Appends data to the end of the file.
        Args:
            data (str): The data to append.
        """
        self.writer.append_to_file(data)
            
    def write_to_file(self, data: str, write_at: int = None):
        """
        Writes data to the file, optionally at a specific position.
        Args:
            data (str): The data to write.
            write_at (int, optional): The byte offset to start writing at. Defaults to None (append).
        """
        self.writer.write_to_file(data, write_at)
        
    def read_entire_file(self) -> bytes:
        """
        Reads the entire content of the file.
        Returns:
            bytes: The content of the file.
        """
        return self.reader.read_entire_file()

    def read_from_file(self, start: int = None, size: int = None) -> bytes:
        """
        Reads a specific range of bytes from the file.
        Args:
            start (int, optional): The starting byte index. Defaults to None (start of file).
            size (int, optional): The number of bytes to read. Defaults to None (until end of file).
        Returns:
            bytes: The read data.
        """
        return self.reader.read_from_file(start, size)
    
    def move_within_file(self, source, dest, size):
        """
        Moves a block of data within the file.
        Args:
            source (int): The source byte offset.
            dest (int): The destination byte offset.
            size (int): The number of bytes to move.
        """
        self.writer.move_within_file(source, dest, size)
    
    def truncate_file(self, size):
        """
        Truncates the file to a specific size.
        Args:
            size (int): The new size of the file.
        """
        self.writer.truncate_file(size)
        
    def get_details(self):
        """
        Returns a string with details about the file.
        Returns:
            str: A string containing the file name, size, and allocated blocks.
        """
        details = f"{self.name} of {self.size} bytes"
        if len(self.blocks) > 0:
            details += f" at blocks {self.blocks}"
        return details