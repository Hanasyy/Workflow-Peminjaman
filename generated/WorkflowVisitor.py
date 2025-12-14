# Generated from Workflow.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WorkflowParser import WorkflowParser
else:
    from WorkflowParser import WorkflowParser

# This class defines a complete generic visitor for a parse tree produced by WorkflowParser.

class WorkflowVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WorkflowParser#program.
    def visitProgram(self, ctx:WorkflowParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#statement.
    def visitStatement(self, ctx:WorkflowParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#addStmt.
    def visitAddStmt(self, ctx:WorkflowParser.AddStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#borrowStmt.
    def visitBorrowStmt(self, ctx:WorkflowParser.BorrowStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#returnStmt.
    def visitReturnStmt(self, ctx:WorkflowParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#queryStmt.
    def visitQueryStmt(self, ctx:WorkflowParser.QueryStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#fieldList.
    def visitFieldList(self, ctx:WorkflowParser.FieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#fieldAssign.
    def visitFieldAssign(self, ctx:WorkflowParser.FieldAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#value.
    def visitValue(self, ctx:WorkflowParser.ValueContext):
        return self.visitChildren(ctx)



del WorkflowParser