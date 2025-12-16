grammar FileSystem;

root: command EOF;

command:
	create_cmd
	| delete_file_cmd
	| delete_dir_cmd
	| mkdir_cmd
	| chdir_cmd
	| move_file_cmd
	| move_dir_cmd
	| open_cmd
	| close_cmd
	| write_to_file_cmd
	| read_from_file_cmd
	| move_within_file_cmd
	| truncate_file_cmd
	| ls_cmd
	| show_memory_map_cmd
	| exit_cmd;

create_cmd: CREATE path;
delete_file_cmd: DELETE_FILE path;
delete_dir_cmd: DELETE_DIR path;
mkdir_cmd: MKDIR path;
chdir_cmd: CHDIR path;
move_file_cmd: MOVE_FILE src = path dest = path;
move_dir_cmd: MOVE_DIR src = path dest = path;
open_cmd: OPEN path open_mode;
close_cmd: CLOSE path;
write_to_file_cmd: WRITE_TO_FILE path data (offset = INT)?;
read_from_file_cmd:
	READ_FROM_FILE path (start = INT size = INT)?;
move_within_file_cmd:
	MOVE_WITHIN_FILE path src = INT dest = INT size = INT;
truncate_file_cmd: TRUNCATE_FILE path size = INT;
ls_cmd: LS;
show_memory_map_cmd: SHOW_MEMORY_MAP;
exit_cmd: EXIT;

path: STRING | ID;
open_mode: STRING | ID;
data: STRING | ID;

CREATE: [Cc][Rr][Ee][Aa][Tt][Ee];
DELETE_FILE:
	[Dd][Ee][Ll][Ee][Tt][Ee] '_' [Ff][Ii][Ll][Ee];
DELETE_DIR: [Dd][Ee][Ll][Ee][Tt][Ee] '_' [Dd][Ii][Rr];
MKDIR: [Mm][Kk][Dd][Ii][Rr];
CHDIR: [Cc][Hh][Dd][Ii][Rr];
MOVE_FILE: [Mm][Oo][Vv][Ee] '_' [Ff][Ii][Ll][Ee];
MOVE_DIR: [Mm][Oo][Vv][Ee] '_' [Dd][Ii][Rr];
OPEN: [Oo][Pp][Ee][Nn];
CLOSE: [Cc][Ll][Oo][Ss][Ee];
WRITE_TO_FILE:
	[Ww][Rr][Ii][Tt][Ee] '_' [Tt][Oo] '_' [Ff][Ii][Ll][Ee];
READ_FROM_FILE:
	[Rr][Ee][Aa][Dd] '_' [Ff][Rr][Oo][Mm] '_' [Ff][Ii][Ll][Ee];
MOVE_WITHIN_FILE:
	[Mm][Oo][Vv][Ee] '_' [Ww][Ii][Tt][Hh][Ii][Nn] '_' [Ff][Ii][Ll][Ee];
TRUNCATE_FILE:
	[Tt][Rr][Uu][Nn][Cc][Aa][Tt][Ee] '_' [Ff][Ii][Ll][Ee];
LS: [Ll][Ss];
SHOW_MEMORY_MAP:
	[Ss][Hh][Oo][Ww] '_' [Mm][Ee][Mm][Oo][Rr][Yy] '_' [Mm][Aa][Pp];
EXIT: [Ee][Xx][Ii][Tt];

INT: [0-9]+;
ID: [a-zA-Z0-9_./-]+;
STRING: '"' (~'"')* '"' | '\'' (~'\'')* '\'';
WS: [ \t\r\n]+ -> skip;