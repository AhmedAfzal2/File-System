from nodes import File
import csv
import io

class CLI:
    def __init__(self, fs):
        self.fs = fs
        self.opened_files: dict[str, File] = {}

    def extract_cmd(self, str: str):
        """
        Extracts the command from the input string.
        Args:
            str (str): The input string.
        Returns:
            str: The command.
        """
        i = str.find(' ')
        if i == -1:
            return str.strip().lower()
        return str[:i].lower()

    def extract_args(self, str: str):
        """
        Extracts the arguments from the input string.
        Args:
            str (str): The input string.
        Returns:
            list[str]: A list of arguments.
        """
        i = str.find(' ')
        if i == -1:
            return []
        
        str = str[i+1:]   # everything except cmd
        reader = csv.reader(io.StringIO(str), skipinitialspace=True)    # using csv reader to parse arguments
        try:
            str = next(reader)
        except StopIteration:
            return []
        for i in range(len(str)):
            str[i] = str[i].strip()
        return str

    def warn_args(self, cmd, takes, given):
        """
        Checks if the number of arguments provided matches the expected number.
        Args:
            cmd (str): The command name.
            takes (int): The expected number of arguments.
            given (int): The number of arguments provided.
        Returns:
            bool: True if the number of arguments is incorrect, False otherwise.
        """
        if given != takes:
            print(f"{cmd} takes exactly {takes} argument(s). {given} were provided.")
            return True
        return False

    def arg_to_int(self, arg):
        """
        Converts an argument to an integer safely.
        Args:
            arg (str): The argument to convert.
        Returns:
            bool: True if conversion was successful, False otherwise.
        """
        try:
            arg = int(arg)
            return True
        except ValueError:
            print(f"Error converting argument {arg} to integer.")
        return False

    def run(self):
        """
        Starts the CLI loop.
        """
        p = ''
        try:
            while (p != "exit"):
                self.fs.print_current_path()
                p = input()
                cmd = self.extract_cmd(p)
                args = self.extract_args(p)
                l = len(args)
                match cmd:
                    case "create":
                        if self.warn_args("create", 1, l):
                            continue
                        self.fs.create(args[0])

                    case "delete_file":
                        if self.warn_args("delete_file", 1, l):
                            continue
                        self.fs.delete_file(args[0])

                    case "delete_dir":
                        if self.warn_args("delete_dir", 1, l):
                            continue
                        self.fs.delete_dir(args[0])

                    case "mkdir":
                        if self.warn_args("mkdir", 1, l):
                            continue
                        self.fs.mkdir(args[0])

                    case "chdir":
                        if self.warn_args("chdir", 1, l):
                            continue
                        self.fs.chdir(args[0])

                    case "move_file":
                        if self.warn_args("move", 2, l):
                            continue
                        self.fs.move_file(args[0], args[1])
                        
                    case "move_dir":
                        if self.warn_args("move", 2, l):
                            continue
                        self.fs.move_dir(args[0], args[1])
                    
                    case "open":
                        if self.warn_args("open", 2, l):
                            continue
                        file = self.fs.open(args[0], args[1])
                        if file:
                            self.opened_files[args[0]] = file

                    case "close":
                        if self.warn_args("close", 1, l):
                            continue
                        if args[0] not in self.opened_files:
                            print(f"File {args[0]} is not open.")
                            continue
                        self.fs.close(self.opened_files[args[0]])
                        if args[0] in self.opened_files:
                            del self.opened_files[args[0]]

                    case "write_to_file":
                        if l != 2 and l != 3:
                            print(f"write_to_file takes 2 or 3 arguments. {l} were provided.")
                            continue
                        if args[0] not in self.opened_files:
                            print(f"{args[0]} is not opened. Cannot write.")
                            continue
                        
                        if l == 2:
                            self.opened_files[args[0]].write_to_file(args[1].strip('"').strip("'"))
                        elif self.arg_to_int(args[2]):
                            self.opened_files[args[0]].write_to_file(args[1].strip('"').strip("'"), int(args[2]))

                    case "read_from_file":
                        if l != 1 and l != 3:
                            print(f"read_from_file takes 1 or 3 arguments. {l} were provided.")
                            continue
                        if args[0] not in self.opened_files:
                            print(f"{args[0]} is not opened. Cannot read.")
                            continue
                        
                        if l == 1:
                            print(self.opened_files[args[0]].read_from_file())
                        elif self.arg_to_int(args[1]) and self.arg_to_int(args[2]):
                            print(self.opened_files[args[0]].read_from_file(int(args[1]), int(args[2])))

                    case "move_within_file":
                        if self.warn_args("move_within_file", 4, l):
                            continue
                        if args[0] not in self.opened_files:
                            print(f"{args[0]} is not opened. Cannot read.")
                            continue
                        if not self.arg_to_int(args[1]) or not self.arg_to_int(args[2]) or not self.arg_to_int(args[3]):
                            continue
                        self.opened_files[args[0]].move_within_file(int(args[1]), int(args[2]), int(args[3]))

                    case "truncate_file":
                        if self.warn_args("truncate_file", 2, l):
                            continue
                        if args[0] not in self.opened_files:
                            print(f"{args[0]} is not opened. Cannot truncate.")
                            continue
                        if not self.arg_to_int(args[1]):
                            continue
                        self.opened_files[args[0]].truncate_file(int(args[1]))

                    case "ls":
                        if self.warn_args("ls", 0, l):
                            continue
                        self.fs.ls()

                    case "show_memory_map":
                        if self.warn_args("show_memory_map", 0, l):
                            continue
                        self.fs.show_memory_map()

                    case "exit":
                        pass

                    case _:
                        print(f"Function {cmd} is not recognized.")

        except KeyboardInterrupt:
            print("\nExiting...")
        finally:
            del self.fs
