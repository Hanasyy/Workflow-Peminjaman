# Generated from Workflow.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,1,
        1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,5,1,5,1,6,4,6,48,8,6,11,6,12,6,49,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,7,8,53,0,21,1,0,0,0,2,30,1,
        0,0,0,4,32,1,0,0,0,6,36,1,0,0,0,8,40,1,0,0,0,10,44,1,0,0,0,12,47,
        1,0,0,0,14,51,1,0,0,0,16,55,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,
        20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,
        0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,31,3,4,2,0,27,31,3,6,3,0,28,
        31,3,8,4,0,29,31,3,10,5,0,30,26,1,0,0,0,30,27,1,0,0,0,30,28,1,0,
        0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,5,1,0,0,33,34,5,2,0,0,34,35,
        3,12,6,0,35,5,1,0,0,0,36,37,5,3,0,0,37,38,5,7,0,0,38,39,3,12,6,0,
        39,7,1,0,0,0,40,41,5,4,0,0,41,42,5,7,0,0,42,43,3,12,6,0,43,9,1,0,
        0,0,44,45,5,5,0,0,45,11,1,0,0,0,46,48,3,14,7,0,47,46,1,0,0,0,48,
        49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,13,1,0,0,0,51,52,5,7,0,
        0,52,53,5,6,0,0,53,54,3,16,8,0,54,15,1,0,0,0,55,56,7,0,0,0,56,17,
        1,0,0,0,3,21,30,49
    ]

class WorkflowParser ( Parser ):

    grammarFileName = "Workflow.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'add'", "'resource'", "'borrow'", "'return'", 
                     "'query'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "STRING", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_addStmt = 2
    RULE_borrowStmt = 3
    RULE_returnStmt = 4
    RULE_queryStmt = 5
    RULE_fieldList = 6
    RULE_fieldAssign = 7
    RULE_value = 8

    ruleNames =  [ "program", "statement", "addStmt", "borrowStmt", "returnStmt", 
                   "queryStmt", "fieldList", "fieldAssign", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ID=7
    STRING=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WorkflowParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowParser.StatementContext)
            else:
                return self.getTypedRuleContext(WorkflowParser.StatementContext,i)


        def getRuleIndex(self):
            return WorkflowParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = WorkflowParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 58) != 0):
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(WorkflowParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addStmt(self):
            return self.getTypedRuleContext(WorkflowParser.AddStmtContext,0)


        def borrowStmt(self):
            return self.getTypedRuleContext(WorkflowParser.BorrowStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(WorkflowParser.ReturnStmtContext,0)


        def queryStmt(self):
            return self.getTypedRuleContext(WorkflowParser.QueryStmtContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = WorkflowParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.addStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.borrowStmt()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.returnStmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.queryStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldList(self):
            return self.getTypedRuleContext(WorkflowParser.FieldListContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_addStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddStmt" ):
                listener.enterAddStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddStmt" ):
                listener.exitAddStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddStmt" ):
                return visitor.visitAddStmt(self)
            else:
                return visitor.visitChildren(self)




    def addStmt(self):

        localctx = WorkflowParser.AddStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_addStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(WorkflowParser.T__0)
            self.state = 33
            self.match(WorkflowParser.T__1)
            self.state = 34
            self.fieldList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BorrowStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WorkflowParser.ID, 0)

        def fieldList(self):
            return self.getTypedRuleContext(WorkflowParser.FieldListContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_borrowStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBorrowStmt" ):
                listener.enterBorrowStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBorrowStmt" ):
                listener.exitBorrowStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBorrowStmt" ):
                return visitor.visitBorrowStmt(self)
            else:
                return visitor.visitChildren(self)




    def borrowStmt(self):

        localctx = WorkflowParser.BorrowStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_borrowStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(WorkflowParser.T__2)
            self.state = 37
            self.match(WorkflowParser.ID)
            self.state = 38
            self.fieldList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WorkflowParser.ID, 0)

        def fieldList(self):
            return self.getTypedRuleContext(WorkflowParser.FieldListContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = WorkflowParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(WorkflowParser.T__3)
            self.state = 41
            self.match(WorkflowParser.ID)
            self.state = 42
            self.fieldList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WorkflowParser.RULE_queryStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryStmt" ):
                listener.enterQueryStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryStmt" ):
                listener.exitQueryStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryStmt" ):
                return visitor.visitQueryStmt(self)
            else:
                return visitor.visitChildren(self)




    def queryStmt(self):

        localctx = WorkflowParser.QueryStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_queryStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(WorkflowParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldAssign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowParser.FieldAssignContext)
            else:
                return self.getTypedRuleContext(WorkflowParser.FieldAssignContext,i)


        def getRuleIndex(self):
            return WorkflowParser.RULE_fieldList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldList" ):
                listener.enterFieldList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldList" ):
                listener.exitFieldList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldList" ):
                return visitor.visitFieldList(self)
            else:
                return visitor.visitChildren(self)




    def fieldList(self):

        localctx = WorkflowParser.FieldListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_fieldList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.fieldAssign()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WorkflowParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(WorkflowParser.ValueContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_fieldAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldAssign" ):
                listener.enterFieldAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldAssign" ):
                listener.exitFieldAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldAssign" ):
                return visitor.visitFieldAssign(self)
            else:
                return visitor.visitChildren(self)




    def fieldAssign(self):

        localctx = WorkflowParser.FieldAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fieldAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(WorkflowParser.ID)
            self.state = 52
            self.match(WorkflowParser.T__5)
            self.state = 53
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(WorkflowParser.STRING, 0)

        def ID(self):
            return self.getToken(WorkflowParser.ID, 0)

        def getRuleIndex(self):
            return WorkflowParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = WorkflowParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





