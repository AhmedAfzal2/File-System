# Generated from FileSystem.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FileSystemParser import FileSystemParser
else:
    from FileSystemParser import FileSystemParser

# This class defines a complete generic visitor for a parse tree produced by FileSystemParser.

class FileSystemVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FileSystemParser#root.
    def visitRoot(self, ctx:FileSystemParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#command.
    def visitCommand(self, ctx:FileSystemParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#create_cmd.
    def visitCreate_cmd(self, ctx:FileSystemParser.Create_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#delete_file_cmd.
    def visitDelete_file_cmd(self, ctx:FileSystemParser.Delete_file_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#delete_dir_cmd.
    def visitDelete_dir_cmd(self, ctx:FileSystemParser.Delete_dir_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#mkdir_cmd.
    def visitMkdir_cmd(self, ctx:FileSystemParser.Mkdir_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#chdir_cmd.
    def visitChdir_cmd(self, ctx:FileSystemParser.Chdir_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#move_file_cmd.
    def visitMove_file_cmd(self, ctx:FileSystemParser.Move_file_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#move_dir_cmd.
    def visitMove_dir_cmd(self, ctx:FileSystemParser.Move_dir_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#open_cmd.
    def visitOpen_cmd(self, ctx:FileSystemParser.Open_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#close_cmd.
    def visitClose_cmd(self, ctx:FileSystemParser.Close_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#write_to_file_cmd.
    def visitWrite_to_file_cmd(self, ctx:FileSystemParser.Write_to_file_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#read_from_file_cmd.
    def visitRead_from_file_cmd(self, ctx:FileSystemParser.Read_from_file_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#move_within_file_cmd.
    def visitMove_within_file_cmd(self, ctx:FileSystemParser.Move_within_file_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#truncate_file_cmd.
    def visitTruncate_file_cmd(self, ctx:FileSystemParser.Truncate_file_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#ls_cmd.
    def visitLs_cmd(self, ctx:FileSystemParser.Ls_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#show_memory_map_cmd.
    def visitShow_memory_map_cmd(self, ctx:FileSystemParser.Show_memory_map_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#exit_cmd.
    def visitExit_cmd(self, ctx:FileSystemParser.Exit_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#path.
    def visitPath(self, ctx:FileSystemParser.PathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#open_mode.
    def visitOpen_mode(self, ctx:FileSystemParser.Open_modeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileSystemParser#data.
    def visitData(self, ctx:FileSystemParser.DataContext):
        return self.visitChildren(ctx)



del FileSystemParser