# Generated from Workflow.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WorkflowParser import WorkflowParser
else:
    from WorkflowParser import WorkflowParser

# This class defines a complete listener for a parse tree produced by WorkflowParser.
class WorkflowListener(ParseTreeListener):

    # Enter a parse tree produced by WorkflowParser#program.
    def enterProgram(self, ctx:WorkflowParser.ProgramContext):
        pass

    # Exit a parse tree produced by WorkflowParser#program.
    def exitProgram(self, ctx:WorkflowParser.ProgramContext):
        pass


    # Enter a parse tree produced by WorkflowParser#statement.
    def enterStatement(self, ctx:WorkflowParser.StatementContext):
        pass

    # Exit a parse tree produced by WorkflowParser#statement.
    def exitStatement(self, ctx:WorkflowParser.StatementContext):
        pass


    # Enter a parse tree produced by WorkflowParser#addStmt.
    def enterAddStmt(self, ctx:WorkflowParser.AddStmtContext):
        pass

    # Exit a parse tree produced by WorkflowParser#addStmt.
    def exitAddStmt(self, ctx:WorkflowParser.AddStmtContext):
        pass


    # Enter a parse tree produced by WorkflowParser#borrowStmt.
    def enterBorrowStmt(self, ctx:WorkflowParser.BorrowStmtContext):
        pass

    # Exit a parse tree produced by WorkflowParser#borrowStmt.
    def exitBorrowStmt(self, ctx:WorkflowParser.BorrowStmtContext):
        pass


    # Enter a parse tree produced by WorkflowParser#returnStmt.
    def enterReturnStmt(self, ctx:WorkflowParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by WorkflowParser#returnStmt.
    def exitReturnStmt(self, ctx:WorkflowParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by WorkflowParser#queryStmt.
    def enterQueryStmt(self, ctx:WorkflowParser.QueryStmtContext):
        pass

    # Exit a parse tree produced by WorkflowParser#queryStmt.
    def exitQueryStmt(self, ctx:WorkflowParser.QueryStmtContext):
        pass


    # Enter a parse tree produced by WorkflowParser#fieldList.
    def enterFieldList(self, ctx:WorkflowParser.FieldListContext):
        pass

    # Exit a parse tree produced by WorkflowParser#fieldList.
    def exitFieldList(self, ctx:WorkflowParser.FieldListContext):
        pass


    # Enter a parse tree produced by WorkflowParser#fieldAssign.
    def enterFieldAssign(self, ctx:WorkflowParser.FieldAssignContext):
        pass

    # Exit a parse tree produced by WorkflowParser#fieldAssign.
    def exitFieldAssign(self, ctx:WorkflowParser.FieldAssignContext):
        pass


    # Enter a parse tree produced by WorkflowParser#value.
    def enterValue(self, ctx:WorkflowParser.ValueContext):
        pass

    # Exit a parse tree produced by WorkflowParser#value.
    def exitValue(self, ctx:WorkflowParser.ValueContext):
        pass



del WorkflowParser