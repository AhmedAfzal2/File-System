import unittest
from unittest.mock import MagicMock, patch
from nodes import File, Directory
from settings import BLOCK_SIZE
from cli import FileSystemCommandVisitor
from FileSystem import FileSystem

class TestHelperFunctions(unittest.TestCase):

    @patch('FileSystem.DiskManager')
    def test_is_abs(self, MockDiskManager):
        fs = FileSystem("dummy")
        self.assertTrue(fs.is_abs("/absolute/path"))
        self.assertFalse(fs.is_abs("relative/path"))
        self.assertTrue(fs.is_abs("/"))
        self.assertFalse(fs.is_abs("file"))

    @patch('FileSystem.DiskManager')
    def test_str_to_path(self, MockDiskManager):
        fs = FileSystem("dummy")
        # create root manually as DiskManager is a mock
        root = Directory('/')
        fs.root = root
        fs.current_path = [root]

        # Case 1: Absolute path
        # "/a/b" -> split('/') -> ['', 'a', 'b'] -> [1:] -> ['a', 'b']
        node, parts = fs.str_to_path("/a/b")
        self.assertEqual(node, root)
        self.assertEqual(parts, ['a', 'b'])

        # Case 2: Relative path
        # "a/b" -> split('/') -> ['a', 'b']
        node, parts = fs.str_to_path("a/b")
        self.assertEqual(node, root) # current_path[-1] is root
        self.assertEqual(parts, ['a', 'b'])

        # Case 3: Root path
        # "/" -> split('/') -> ['', ''] -> [1:] -> [''] -> remove('') -> []
        node, parts = fs.str_to_path("/")
        self.assertEqual(node, root)    
        self.assertEqual(parts, [])

    def test_file_last_block_remaining_size(self):
        mock_fs = MagicMock()
        f = File("test_file", mock_fs)

        # Case 1: Empty file
        f.size = 0
        self.assertEqual(f.last_block_remaining_size(), BLOCK_SIZE)

        # Case 2: File size is exactly one block
        f.size = BLOCK_SIZE
        self.assertEqual(f.last_block_remaining_size(), 0)

        # Case 3: File size is half a block
        f.size = BLOCK_SIZE // 2
        self.assertEqual(f.last_block_remaining_size(), BLOCK_SIZE // 2)

        # Case 4: File size is 1.5 blocks
        f.size = int(BLOCK_SIZE * 1.5)
        self.assertEqual(f.last_block_remaining_size(), BLOCK_SIZE // 2)

    def test_visitor_get_text(self):
        # mock CLI module to run instantiate antlr visitor
        mock_cli = MagicMock()
        visitor = FileSystemCommandVisitor(mock_cli)

        # mock context of antlr
        mock_ctx = MagicMock()

        # Case 1: Normal text
        mock_ctx.getText.return_value = "filename"
        self.assertEqual(visitor.get_text(mock_ctx), "filename")

        # Case 2: Double quoted text
        mock_ctx.getText.return_value = '"filename"'
        self.assertEqual(visitor.get_text(mock_ctx), "filename")

        # Case 3: Single quoted text
        mock_ctx.getText.return_value = "'filename'"
        self.assertEqual(visitor.get_text(mock_ctx), "filename")

        # Case 4: Text with quotes inside
        mock_ctx.getText.return_value = '"file name"'
        self.assertEqual(visitor.get_text(mock_ctx), "file name")

if __name__ == '__main__':
    unittest.main()
