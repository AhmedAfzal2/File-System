from FileSystem import FileSystem
from nodes import File

def extract_cmd(str: str):
    i = str.find(' ')
    if i == -1:
        return str.strip().lower()
    return str[:i].lower()

def extract_args(str: str):
    i = str.find(' ')
    if i == -1:
        return []
    
    str = str[i+1:]   # everything except cmd
    str = str.split(',')
    for i in range(len(str)):
        str[i] = str[i].strip()
    return str

def warn_args(cmd, takes, given):
    if given != takes:
        print(f"{cmd} takes exactly {takes} argument(s). {given} were provided.")
        return True
    return False

fs = FileSystem("sample.dat")

p = ''
opened_files: dict[str, File] = {}
try:
    while (p != "exit"):
        fs.print_current_path()
        p = input()
        cmd = extract_cmd(p)
        args = extract_args(p)
        l = len(args)
        match cmd:
            case "create":
                if warn_args("create", 1, l):
                    continue
                fs.create(args[0])

            case "delete_file":
                if warn_args("delete_file", 1, l):
                    continue
                fs.delete_file(args[0])

            case "delete_dir":
                if warn_args("delete_dir", 1, l):
                    continue
                fs.delete_dir(args[0])

            case "mkdir":
                if warn_args("mkdir", 1, l):
                    continue
                fs.mkdir(args[0])

            case "chdir":
                if warn_args("chdir", 1, l):
                    continue
                fs.chdir(args[0])

            case "move_file":
                if warn_args("move", 2, l):
                    continue
                fs.move_file(args[0], args[1])
                
            case "move_dir":
                if warn_args("move", 2, l):
                    continue
                fs.move_dir(args[0], args[1])
            
            case "open":
                if warn_args("open", 2, l):
                    continue
                file = fs.open(args[0], args[1])
                if file:
                    opened_files[args[0]] = file

            case "close":
                if warn_args("close", 1, l):
                    continue
                fs.close(opened_files[args[0]])
                if args[0] in opened_files:
                    del opened_files[args[0]]

            case "write_to_file":
                if l != 2 and l != 3:
                    print(f"write_to_file takes 2 or 3 arguments. {l} were provided.")
                    continue
                if args[0] not in opened_files:
                    print(f"{args[0]} is not opened. Cannot write.")
                    continue
                
                if l == 2:
                    opened_files[args[0]].write_to_file(args[1].strip('"').strip("'"))
                else:
                    opened_files[args[0]].write_to_file(args[1].strip('"').strip("'"), int(args[2]))

            case "read_from_file":
                if l != 1 and l != 3:
                    print(f"read_from_file takes 1 or 3 arguments. {l} were provided.")
                    continue
                if args[0] not in opened_files:
                    print(f"{args[0]} is not opened. Cannot read.")
                    continue
                
                if l == 1:
                    print(opened_files[args[0]].read_from_file())
                else:
                    print(opened_files[args[0]].read_from_file(int(args[1]), int(args[2])))
                    
            case "move_within_file":
                if warn_args("move_within_file", 4, l):
                    continue
                if args[0] not in opened_files:
                    print(f"{args[0]} is not opened. Cannot read.")
                    continue
                
                opened_files[args[0]].move_within_file(int(args[1]), int(args[2]), int(args[3]))

            case "truncate_file":
                if warn_args("truncate_file", 2, l):
                    continue
                if args[0] not in opened_files:
                    print(f"{args[0]} is not opened. Cannot truncate.")
                    continue
                opened_files[args[0]].truncate_file(int(args[1]))

            case "ls":
                if warn_args("ls", 0, l):
                    continue
                fs.ls()
                
            case "show_memory_map":
                if warn_args("show_memory_map", 0, l):
                    continue
                fs.show_memory_map()
                
            case 'exit':
                pass
                
            case _:
                print(f"Function {cmd} is not recognized.")
finally:
    del fs  # to close the file