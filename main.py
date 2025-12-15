from FileSystem import FileSystem
from cli import CLI

if __name__ == "__main__":
    fs = FileSystem("sample.dat")
    cli = CLI(fs)
    cli.run()