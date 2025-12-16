from nodes import Directory, File
from disk_manager import DiskManager
import re

class FileSystem:
    def __init__(self, file_name):
        self.disk_manager = DiskManager(file_name)
        if self.disk_manager.root:
            self.root = self.disk_manager.root
            self.set_fs(self.root)
        else:
            self.root = Directory('/')
            self.save()

        self.current_path: list[Directory] = [self.root]
        self.opened_files = []
        
    def save(self):
        """
        Saves the file system metadata to the disk.
        """
        self.disk_manager.save_metadata(self.root)
    def set_fs(self, root):
        """
        Recursively sets the file system reference for all files in the directory tree.
        Args:
            root (Directory): The root directory to start from.
        """
        for child in root.children:
            if type(child) == File:
                child.fs = self
            else:
                self.set_fs(child)
                
    def is_abs(self, path: str):
        """
        Checks if a path is absolute.
        Args:
            path (str): The path to check.
        Returns:
            bool: True if the path is absolute, False otherwise.
        """
        if path.startswith('/'):
            return True
        return False
                
    def str_to_path(self, path: str):
        """
        Converts a string path to a starting node and a list of path components.
        Args:
            path (str): The path string.
        Returns:
            tuple: A tuple containing the starting node (Directory) and a list of path components (strings).
        """
        if self.is_abs(path):
            node = self.root
            path_list = path.split('/')[1:]     # first is just ''
        else:   # relative path
            node = self.current_path[-1]
            path_list = path.split('/')
            
        while '' in path_list:
            path_list.remove('')
            
        return node, path_list
    
    def search_dir(self, dir: Directory, name: str, t):
        """
        Searches for a node with a specific name and type in a directory.
        Args:
            dir (Directory): The directory to search in.
            name (str): The name of the node to search for.
            t (type): The type of the node (File or Directory).
        Returns:
            TreeNode: The found node, or None if not found.
        """
        for node in dir.children:
            if node.name == name and type(node) == t:
                return node
        return None
    
    def search_path(self, path: str, t, parent=False, warn=False):
        """
        Searches for a node at a specific path.
        Args:
            path (str): The path to the node.
            t (type): The type of the node (File or Directory).
            parent (bool, optional): If True, returns the parent directory as well. Defaults to False.
            warn (bool, optional): If True, prints a warning if the path does not exist. Defaults to False.
        Returns:
            TreeNode or tuple: The found node, or (node, parent) if parent is True. Returns None if not found.
        """
        node, path_list = self.str_to_path(path)
        prev_node = node
        for i in range(len(path_list) - 1):
            prev_node = node
            node = self.search_dir(node, path_list[i], Directory)
            if node == None:
                if warn:
                    print(f"Directory {'/' + '/'.join(path_list[:i+1])} does not exist.")
                return None
                
        node = self.search_dir(node, path_list[-1], t)
        if node == None and warn:
            print(f"{path} does not exist.")
        
        if not parent:
            return node
        else:
            return node, prev_node
        
    def mkdir(self, path: str, file=False):
        """
        Creates a directory (or file) at the specified path.
        Args:
            path (str): The path where the directory/file should be created.
            file (bool, optional): If True, creates a file. If False, creates a directory. Defaults to False.
        Returns:
            TreeNode: The created node.
        """
        node, path_list = self.str_to_path(path)
        
        i = 0
        while i < len(path_list) - 1:
            new_node = self.search_dir(node, path_list[i], Directory)
            if new_node == None:
                break
            node = new_node
            i += 1

        # create each directory
        for dir_name in path_list[i:-1]:
            this_dir = Directory(dir_name)
            node.children.append(this_dir)
            node = this_dir
            
        if file:
            if self.search_dir(node, path_list[-1], File):
                print(f"File {'/' * self.is_abs(path) + path_list} already exists.")
            else:
                node.children.append(File(path_list[-1], self))
        else:
            if self.search_dir(node, path_list[-1], Directory):
                print(f"Directory {'/' * self.is_abs(path) + path_list} already exists.")
            else:
                node.children.append(Directory(path_list[-1]))

        self.save()
        
        return node.children[-1]

    def chdir(self, path: str):
        """
        Changes the current working directory.
        Args:
            path (str): The path to the new directory.
        """
        # to go backwards
        if path == ".." and len(self.current_path) > 1:
            self.current_path.pop()
            return
        
        node, path_list = self.str_to_path(path)
        if self.is_abs(path):
            self.current_path = [self.root]
        
        for i in range(len(path_list)):
            found = self.search_dir(self.current_path[-1], path_list[i], Directory)
            if found:
                self.current_path.append(found)
            else:
                print(f"Directory {'/' * self.is_abs(path) + '/'.join(path_list[:i+1])} does not exist.")
            
    def ls(self):
        """
        Lists the contents of the current directory.
        """
        if len(self.current_path[-1].children) == 0:
            print("Empty")
        else:
            for child in self.current_path[-1].children:
                print(child.name)

    def create(self, path: str) -> File:
        """
        Creates a new file.
        Args:
            path (str): The path to the new file.
        Returns:
            File: The created file.
        """
        return self.mkdir(path, True)

    def delete_file(self, path: str):
        """
        Deletes a file.
        Args:
            path (str): The path to the file to delete.
        """
        found, parent = self.search_path(path, File, True, True)
        if found:
            found.truncate_file(0)
            parent.children.remove(found)
            del found
            self.save()

    def delete_file_t(self, file: File, parent: Directory):
        """
        Helper method to delete a file node.
        Args:
            file (File): The file node to delete.
            parent (Directory): The parent directory of the file.
        """
        file.truncate_file(0)
        parent.children.remove(file)
        del file
        self.save()
        
    def delete_dir_t(self, dir: Directory, parent: Directory):
        """
        Helper method to recursively delete a directory node.
        Args:
            dir (Directory): The directory node to delete.
            parent (Directory): The parent directory.
        """
        for child in dir.children:
            if type(child) == File:
                self.delete_file_t(child, dir)
            else:
                self.delete_dir_t(child, dir) 
        parent.children.remove(dir)
        del dir
        self.save()

    def delete_dir(self, name: str):
        """
        Deletes a directory.
        Args:
            name (str): The path to the directory to delete.
        """
        dir, parent = self.search_path(name, Directory, parent=True)
        if dir:
            for child in dir.children:
                if type(child) == File:
                    self.delete_file_t(child, dir)
                else:
                    self.delete_dir_t(child, dir)
            parent.children.remove(dir)
            del dir
            self.save()
            
    def move_file(self, src: str, dest: str):
        """
        Moves a file from source to destination.
        Args:
            src (str): The source path of the file.
            dest (str): The destination directory path.
        """
        found_src, parent_src = self.search_path(src, File, True, True)
        found_dest = self.search_path(dest, Directory, False, True)
        if not found_src or not found_dest:
            return
        
        found_dest.children.append(found_src)
        parent_src.children.remove(found_src)
        
    def move_dir(self, src: str, dest: str):
        """
        Moves a directory from source to destination.
        Args:
            src (str): The source path of the directory.
            dest (str): The destination directory path.
        """
        found_src, parent_src = self.search_path(src, Directory, True, True)
        found_dest = self.search_path(dest, Directory, False, True)
        if not found_src or not found_dest:
            return
        
        found_dest.children.append(found_src)
        parent_src.children.remove(found_src)

    def open(self, name: str, mode: str) -> File:
        """
        Opens a file with the specified mode. Mutates the self.opened_files array.
        Args:
            name (str): The path to the file.
            mode (str): The mode to open the file in.
        Returns:
            File: The opened file object, or None if failed.
        """
        if re.fullmatch(r'[raw]\+?$', mode) is None:    # valid modes are r, a, w, r+, a+, w+
            print(f"Invalid mode: {mode}")
            return
        
        found = self.search_path(name, File)
        
        if mode[0] == 'w':
            if found:
                self.delete_file(name)      # rewrite file in 'w'
            found = self.create(name)
        elif mode[0] == 'a' and not found:
            found = self.create(name)   # create if not exists in 'a'
        elif not found:
            print(f"File {name} does not exist.")
            return
        elif found in self.opened_files:
            print(f"File {name} already opened.")
            return
        
        if len(mode) == 2:      # if r+, a+, or w+, both read and write are allowed
            found.set_mode('all')
        else:
            found.set_mode(mode[0])     # only first letter is allowed
        self.opened_files.append(found)
        return found
    
    def close(self, file: File):
        """
        Closes an opened file. Mutates the self.opened_files array.
        Args:
            file (File): The file object to close.
        """
        if file in self.opened_files:
            self.opened_files.remove(file)
        else:
            print("File not open.")
        
    def print_current_path(self):
        """
        Prints the current working directory path in a shell-like format.
        """
        print("PS /", end='')
        for dir in self.current_path[1:-1]:
            print(dir.name, end='/')
        if len(self.current_path) > 1:
            print(f"{self.current_path[-1].name}", end='')
        print("> ", end='')
        
    def print_dir_tree(self, file_details: list[str], node=None, prefix='', is_last=True):
        """
        Recursively prints the directory tree structure.
        Args:
            file_details (list[str]): A list to collect file details.
            node (TreeNode, optional): The current node being processed. Defaults to None (root).
            prefix (str, optional): The prefix string for indentation. Defaults to ''.
            is_last (bool, optional): Whether the current node is the last child. Defaults to True.
        """
        if not node:
            node = self.root
            print(node.name)
        else:
            icon = '📁' if type(node) == Directory else '📄'
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{icon} {node.name}")
            prefix += "     " if is_last else "│    "
    
        if type(node) == Directory:
            for index, child in enumerate(node.children):
                is_last_child = index == len(node.children) - 1
                self.print_dir_tree(file_details, child, prefix, is_last_child)
        else:
            file_details.append(node.get_details())
        
    def show_memory_map(self):
        """
        Displays the directory tree and file memory details.
        """
        file_details = []
        self.print_dir_tree(file_details)
        
        if len(file_details) > 0:
            print("\nFile Memory")
            for details in file_details:
                print(details)
            print()
            
    def __del__(self):
        pass