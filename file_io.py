from settings import BLOCK_SIZE

class FileReader:
    def __init__(self, file_node):
        self.file_node = file_node

    @property
    def disk_manager(self):
        return self.file_node.fs.disk_manager

    def read_entire_file(self) -> bytes:
        """
        Reads the entire content of the file.
        Returns:
            bytes: The content of the file.
        """
        if self.file_node.mode != 'r' and self.file_node.mode != 'all':
            print("Attempt to read in wrong mode.")
            return
        
        f = self.disk_manager.file
        data = b''
        remaining = self.file_node.size
        for block in self.file_node.blocks:
            f.seek(block)
            if remaining > BLOCK_SIZE:
                data += f.read(BLOCK_SIZE)
            else:
                data += f.read(remaining)
            remaining -= BLOCK_SIZE
        
        return data

    def read_from_file(self, start: int = None, size: int = None) -> bytes:
        """
        Reads a specific range of bytes from the file.
        Args:
            start (int, optional): The starting byte index. Defaults to None (start of file).
            size (int, optional): The number of bytes to read. Defaults to None (until end of file).
        Returns:
            bytes: The read data.
        """
        # overloading
        if start == None and size == None:
            return self.read_entire_file()
        
        if start < 0 or size < 0:
            print("Arguments cannot be negative.")
            return
        
        if self.file_node.mode != 'r' and self.file_node.mode != 'all':
            print("Attempt to read in wrong mode.")
            return
        
        if start > self.file_node.size:   # reading outside file
            return b''
        
        if start + size > self.file_node.size:
            size = self.file_node.size - start
        
        f = self.disk_manager.file
        start_block = start // BLOCK_SIZE
        start_block_offset = start % BLOCK_SIZE
    
        data = b''
        remaining = size
        current_block = start_block

        while remaining > 0 and current_block < len(self.file_node.blocks):
            f.seek(self.file_node.blocks[current_block])
            block_data = f.read(BLOCK_SIZE)

            # if start block, remove initial data before start
            if current_block == start_block:
                block_data = block_data[start_block_offset:]

            data += block_data[:remaining]  # slices trailing data from last block, otherwise appends entire block to data
            remaining -= len(block_data[:remaining])
            current_block += 1

        return data

class FileWriter:
    def __init__(self, file_node):
        self.file_node = file_node

    @property
    def disk_manager(self):
        return self.file_node.fs.disk_manager

    # returns remaining empty space in the last allocated block
    def last_block_remaining_size(self):
        """
        Calculates the remaining empty space in the last allocated block of the file.
        Returns:
            int: The number of bytes remaining in the last block.
        """
        if self.file_node.size % BLOCK_SIZE == 0 and self.file_node.size != 0:
            return 0
        else:
            return BLOCK_SIZE - (self.file_node.size % BLOCK_SIZE)

    def append_to_file(self, data: str):
        """
        Appends data to the end of the file.
        Args:
            data (str): The data to append.
        """
        if self.file_node.mode == 'r':
            print("Attempt to write in read mode.")
            return

        if len(self.file_node.blocks) == 0:
            self.file_node.blocks.append(self.disk_manager.allocate())
            
        f = self.disk_manager.file
        if type(data) != bytes:
            data = data.encode()
        last_block_offset = self.file_node.size % BLOCK_SIZE
        remaining = self.last_block_remaining_size()
        
        # enough space in current block
        if len(data) <= remaining:
            f.seek(self.file_node.blocks[-1] + last_block_offset)
            f.write(data)
            self.file_node.size += len(data)
        
        else:   # data more than space in current block
            this_block_data = data[:remaining]
            data = data[remaining:]
            chunk_data = [data[i:i+BLOCK_SIZE] for i in range(0, len(data), BLOCK_SIZE)]    # split the data into chunks the size of a block
            
            # fill current last block
            f.seek(self.file_node.blocks[-1] + last_block_offset)
            f.write(this_block_data)
            
            # new blocks
            for chunk in chunk_data:
                self.file_node.blocks.append(self.disk_manager.allocate())
                f.seek(self.file_node.blocks[-1])
                f.write(chunk)
                
            # + this_block_data as that was removed from data originally
            self.file_node.size += len(data) + len(this_block_data)
        self.file_node.fs.save()

    def write_to_file(self, data: str, write_at: int = None):
        """
        Writes data to the file, optionally at a specific position.
        Args:
            data (str): The data to write.
            write_at (int, optional): The byte offset to start writing at. Defaults to None (append).
        """
        # because python does not support overloading
        if write_at == None:
            self.append_to_file(data)
            return
        
        if self.file_node.mode == 'r':
            print("Attempt to write in read mode.")
            return
        
        if write_at < 0:
            print("Arguments cannot be negative.")
            return
        
        if len(self.file_node.blocks) == 0:
            self.file_node.blocks.append(self.disk_manager.allocate())
        
        f = self.disk_manager.file
        if type(data) != bytes:
            data = data.encode()
        last_block_offset = self.file_node.size % BLOCK_SIZE
        remaining = self.last_block_remaining_size()
        
        # write_at is after end of file, pad nulls until write_at
        if write_at >= self.file_node.size:
            # write_at is in the last block
            if write_at - self.file_node.size < remaining:
                  f.seek(self.file_node.blocks[-1] + last_block_offset)
                  f.write(b'\x00' * (write_at - self.file_node.size))      # pad null bytes
                  
            else:   # write_at is further ahead, more blocks are needed
                f.seek(self.file_node.blocks[-1] + last_block_offset)
                f.write(b'\x00' * remaining)   # fill last block
                
                for i in range((write_at - self.file_node.size) // BLOCK_SIZE):   # new null blocks
                    this_block = self.disk_manager.allocate()
                    self.file_node.blocks.append(this_block)
                    f.seek(this_block)
                    f.write(b'\x00' * BLOCK_SIZE)
                
                self.file_node.blocks.append(self.disk_manager.allocate())
                f.seek(self.file_node.blocks[-1])
                f.write(b'\x00' * (write_at % BLOCK_SIZE))       # last block partially null
            
            # f now contains padded nulls upto relevant point, simply writing data remains
            self.file_node.size = write_at
            self.write_to_file(data)      # same logic as normal writing
        
        else:
            start_block = write_at // BLOCK_SIZE
            start_block_offset = write_at % BLOCK_SIZE
            
            required_size = write_at + len(data)
            # add new blocks if required
            while required_size > len(self.file_node.blocks) * BLOCK_SIZE:
                self.file_node.blocks.append(self.disk_manager.allocate())
            
            # write remaining start block data
            start_block_data = data[:(BLOCK_SIZE - start_block_offset)]
            data = data[(BLOCK_SIZE - start_block_offset):]
            f.seek(self.file_node.blocks[start_block] + start_block_offset)
            f.write(start_block_data)
            
            # split remaining data into chunks
            chunk_data = [data[i:i+BLOCK_SIZE] for i in range(0, len(data), BLOCK_SIZE)]
            
            # write chunks
            for i in range(len(chunk_data)):
                f.seek(self.file_node.blocks[i + start_block + 1])
                f.write(chunk_data[i])
            
            # either the data is still bound within original f size, or it has exceeded
            # update size accordingly
            self.file_node.size = max(self.file_node.size, write_at + len(data) + len(start_block_data))
        self.file_node.fs.save()

    def truncate_file(self, size):
        """
        Truncates the file to a specific size.
        Args:
            size (int): The new size of the file.
        """
        start_block = size // BLOCK_SIZE
        if size % BLOCK_SIZE != 0:
            start_block += 1
            
        for i in range(start_block, len(self.file_node.blocks)):
            self.disk_manager.deallocate(self.file_node.blocks[i])
        self.file_node.blocks = self.file_node.blocks[:start_block]
        self.file_node.size = size
        self.file_node.fs.save()
    
    def move_within_file(self, source, dest, size):
        """
        Moves a block of data within the file.
        Args:
            source (int): The source byte offset.
            dest (int): The destination byte offset.
            size (int): The number of bytes to move.
        """
        if source < 0 or dest < 0 or size < 0:
            print("Arguments cannot be negative.")
            return
        
        data = self.file_node.read_from_file(source, size)
        self.write_to_file(b'\x00' * size, source)
        self.write_to_file(data, dest)
