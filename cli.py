import sys
import os
# add the .antlr directory to the path so we can import the generated files
sys.path.append(os.path.join(os.path.dirname(__file__), '.antlr'))

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from nodes import File
from FileSystemLexer import FileSystemLexer
from FileSystemParser import FileSystemParser
from FileSystemVisitor import FileSystemVisitor

class FileSystemCommandVisitor(FileSystemVisitor):
    def __init__(self, cli):
        self.cli = cli
        self.fs = cli.fs

    def visitCreate_cmd(self, ctx:FileSystemParser.Create_cmdContext):
        path = self.get_text(ctx.path())
        self.fs.create(path)

    def visitDelete_file_cmd(self, ctx:FileSystemParser.Delete_file_cmdContext):
        path = self.get_text(ctx.path())
        self.fs.delete_file(path)

    def visitDelete_dir_cmd(self, ctx:FileSystemParser.Delete_dir_cmdContext):
        path = self.get_text(ctx.path())
        self.fs.delete_dir(path)

    def visitMkdir_cmd(self, ctx:FileSystemParser.Mkdir_cmdContext):
        path = self.get_text(ctx.path())
        self.fs.mkdir(path)

    def visitChdir_cmd(self, ctx:FileSystemParser.Chdir_cmdContext):
        path = self.get_text(ctx.path())
        self.fs.chdir(path)

    def visitMove_file_cmd(self, ctx:FileSystemParser.Move_file_cmdContext):
        src = self.get_text(ctx.src)
        dest = self.get_text(ctx.dest)
        self.fs.move_file(src, dest)

    def visitMove_dir_cmd(self, ctx:FileSystemParser.Move_dir_cmdContext):
        src = self.get_text(ctx.src)
        dest = self.get_text(ctx.dest)
        self.fs.move_dir(src, dest)

    def visitOpen_cmd(self, ctx:FileSystemParser.Open_cmdContext):
        path = self.get_text(ctx.path())
        mode = self.get_text(ctx.open_mode())
        file = self.fs.open(path, mode)
        if file:
            self.cli.opened_files[path] = file

    def visitClose_cmd(self, ctx:FileSystemParser.Close_cmdContext):
        path = self.get_text(ctx.path())
        if path not in self.cli.opened_files:
            print(f"File {path} is not open.")
            return
        self.fs.close(self.cli.opened_files[path])
        del self.cli.opened_files[path]

    def visitWrite_to_file_cmd(self, ctx:FileSystemParser.Write_to_file_cmdContext):
        path = self.get_text(ctx.path())
        data = self.get_text(ctx.data())
        
        if path not in self.cli.opened_files:
            print(f"{path} is not opened. Cannot write.")
            return

        if ctx.offset:
            offset = int(ctx.offset.text)
            self.cli.opened_files[path].write_to_file(data, offset)
        else:
            self.cli.opened_files[path].write_to_file(data)

    def visitRead_from_file_cmd(self, ctx:FileSystemParser.Read_from_file_cmdContext):
        path = self.get_text(ctx.path())
        if path not in self.cli.opened_files:
            print(f"{path} is not opened. Cannot read.")
            return

        if ctx.start and ctx.size:
            start = int(ctx.start.text)
            size = int(ctx.size.text)
            print(self.cli.opened_files[path].read_from_file(start, size))
        else:
            print(self.cli.opened_files[path].read_from_file())

    def visitMove_within_file_cmd(self, ctx:FileSystemParser.Move_within_file_cmdContext):
        path = self.get_text(ctx.path())
        if path not in self.cli.opened_files:
            print(f"{path} is not opened. Cannot move within file.")
            return
        
        src = int(ctx.src.text)
        dest = int(ctx.dest.text)
        size = int(ctx.size.text)
        self.cli.opened_files[path].move_within_file(src, dest, size)

    def visitTruncate_file_cmd(self, ctx:FileSystemParser.Truncate_file_cmdContext):
        path = self.get_text(ctx.path())
        if path not in self.cli.opened_files:
            print(f"{path} is not opened. Cannot truncate.")
            return
        
        size = int(ctx.size.text)
        self.cli.opened_files[path].truncate_file(size)

    def visitLs_cmd(self, ctx:FileSystemParser.Ls_cmdContext):
        self.fs.ls()

    def visitShow_memory_map_cmd(self, ctx:FileSystemParser.Show_memory_map_cmdContext):
        self.fs.show_memory_map()

    def visitExit_cmd(self, ctx:FileSystemParser.Exit_cmdContext):
        sys.exit(0)

    def get_text(self, ctx):
        text = ctx.getText()
        if text.startswith('"') and text.endswith('"'):
            return text[1:-1]
        if text.startswith("'") and text.endswith("'"):
            return text[1:-1]
        return text

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column} {msg}")

class CLI:
    def __init__(self, fs):
        self.fs = fs
        self.opened_files: dict[str, File] = {}

    def run(self):
        """
        Starts the CLI loop.
        """
        print("Welcome to the File System CLI. Type 'exit' to quit.")
        while True:
            self.fs.print_current_path()
            try:
                user_input = input()
                if not user_input.strip():
                    continue
                
                input_stream = InputStream(user_input)
                lexer = FileSystemLexer(input_stream)
                lexer.removeErrorListeners()
                lexer.addErrorListener(ThrowingErrorListener())
                
                stream = CommonTokenStream(lexer)
                parser = FileSystemParser(stream)
                parser.removeErrorListeners()
                parser.addErrorListener(ThrowingErrorListener())
                
                tree = parser.root()
                visitor = FileSystemCommandVisitor(self)
                visitor.visit(tree)

            except SystemExit:
                break
            except Exception as e:
                print(f"Error: {e}")
            except KeyboardInterrupt:
                print("\nExiting...")
                break
        
        del self.fs
