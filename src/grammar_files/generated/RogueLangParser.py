# Generated from /home/ronaldj/code/P4-comp/src/grammar_files/RogueLang.g4 by ANTLR 4.13.1
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
        4,1,41,218,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,5,0,45,8,0,10,0,12,0,48,9,0,1,1,1,1,1,1,1,1,1,1,5,1,
        55,8,1,10,1,12,1,58,9,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,74,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,83,8,
        5,10,5,12,5,86,9,5,3,5,88,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,97,
        8,6,3,6,99,8,6,1,7,1,7,1,7,1,7,3,7,105,8,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,121,8,9,1,9,3,9,124,8,9,1,
        10,1,10,1,10,1,10,1,10,1,10,3,10,132,8,10,1,11,1,11,1,11,1,12,1,
        12,5,12,139,8,12,10,12,12,12,142,9,12,1,12,1,12,1,13,1,13,1,13,1,
        13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,3,15,161,
        8,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,5,17,171,8,17,10,17,
        12,17,174,9,17,1,18,1,18,1,19,1,19,1,19,5,19,181,8,19,10,19,12,19,
        184,9,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,3,20,199,8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,5,20,213,8,20,10,20,12,20,216,9,20,1,20,0,1,
        40,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        0,4,2,0,14,15,22,22,1,0,12,13,1,0,16,21,1,0,23,24,231,0,42,1,0,0,
        0,2,49,1,0,0,0,4,61,1,0,0,0,6,73,1,0,0,0,8,75,1,0,0,0,10,78,1,0,
        0,0,12,91,1,0,0,0,14,100,1,0,0,0,16,109,1,0,0,0,18,114,1,0,0,0,20,
        125,1,0,0,0,22,133,1,0,0,0,24,136,1,0,0,0,26,145,1,0,0,0,28,151,
        1,0,0,0,30,157,1,0,0,0,32,164,1,0,0,0,34,167,1,0,0,0,36,175,1,0,
        0,0,38,177,1,0,0,0,40,198,1,0,0,0,42,46,3,2,1,0,43,45,3,6,3,0,44,
        43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,1,1,0,0,
        0,48,46,1,0,0,0,49,50,5,31,0,0,50,51,5,36,0,0,51,56,3,4,2,0,52,55,
        3,8,4,0,53,55,3,6,3,0,54,52,1,0,0,0,54,53,1,0,0,0,55,58,1,0,0,0,
        56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,56,1,0,0,0,59,60,5,
        37,0,0,60,3,1,0,0,0,61,62,5,11,0,0,62,63,3,24,12,0,63,5,1,0,0,0,
        64,74,3,16,8,0,65,74,3,12,6,0,66,74,3,14,7,0,67,74,3,18,9,0,68,74,
        3,26,13,0,69,74,3,28,14,0,70,74,3,24,12,0,71,74,3,32,16,0,72,74,
        3,40,20,0,73,64,1,0,0,0,73,65,1,0,0,0,73,66,1,0,0,0,73,67,1,0,0,
        0,73,68,1,0,0,0,73,69,1,0,0,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,
        1,0,0,0,74,7,1,0,0,0,75,76,5,1,0,0,76,77,3,12,6,0,77,9,1,0,0,0,78,
        87,5,34,0,0,79,84,3,40,20,0,80,81,5,38,0,0,81,83,3,40,20,0,82,80,
        1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,88,1,0,0,0,
        86,84,1,0,0,0,87,79,1,0,0,0,87,88,1,0,0,0,88,89,1,0,0,0,89,90,5,
        35,0,0,90,11,1,0,0,0,91,98,5,31,0,0,92,96,5,40,0,0,93,97,3,40,20,
        0,94,97,3,30,15,0,95,97,3,10,5,0,96,93,1,0,0,0,96,94,1,0,0,0,96,
        95,1,0,0,0,97,99,1,0,0,0,98,92,1,0,0,0,98,99,1,0,0,0,99,13,1,0,0,
        0,100,101,5,10,0,0,101,102,5,31,0,0,102,104,5,32,0,0,103,105,3,34,
        17,0,104,103,1,0,0,0,104,105,1,0,0,0,105,106,1,0,0,0,106,107,5,33,
        0,0,107,108,3,24,12,0,108,15,1,0,0,0,109,110,5,6,0,0,110,111,5,32,
        0,0,111,112,3,40,20,0,112,113,5,33,0,0,113,17,1,0,0,0,114,115,5,
        2,0,0,115,116,5,32,0,0,116,117,3,40,20,0,117,118,5,33,0,0,118,120,
        3,24,12,0,119,121,3,20,10,0,120,119,1,0,0,0,120,121,1,0,0,0,121,
        123,1,0,0,0,122,124,3,22,11,0,123,122,1,0,0,0,123,124,1,0,0,0,124,
        19,1,0,0,0,125,126,5,3,0,0,126,127,5,32,0,0,127,128,3,40,20,0,128,
        129,5,33,0,0,129,131,3,24,12,0,130,132,3,20,10,0,131,130,1,0,0,0,
        131,132,1,0,0,0,132,21,1,0,0,0,133,134,5,4,0,0,134,135,3,24,12,0,
        135,23,1,0,0,0,136,140,5,36,0,0,137,139,3,6,3,0,138,137,1,0,0,0,
        139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,0,
        142,140,1,0,0,0,143,144,5,37,0,0,144,25,1,0,0,0,145,146,5,7,0,0,
        146,147,3,12,6,0,147,148,5,8,0,0,148,149,3,40,20,0,149,150,3,24,
        12,0,150,27,1,0,0,0,151,152,5,9,0,0,152,153,5,32,0,0,153,154,3,40,
        20,0,154,155,5,33,0,0,155,156,3,24,12,0,156,29,1,0,0,0,157,158,5,
        31,0,0,158,160,5,32,0,0,159,161,3,38,19,0,160,159,1,0,0,0,160,161,
        1,0,0,0,161,162,1,0,0,0,162,163,5,33,0,0,163,31,1,0,0,0,164,165,
        5,5,0,0,165,166,3,40,20,0,166,33,1,0,0,0,167,172,3,36,18,0,168,169,
        5,38,0,0,169,171,3,36,18,0,170,168,1,0,0,0,171,174,1,0,0,0,172,170,
        1,0,0,0,172,173,1,0,0,0,173,35,1,0,0,0,174,172,1,0,0,0,175,176,5,
        31,0,0,176,37,1,0,0,0,177,182,3,40,20,0,178,179,5,38,0,0,179,181,
        3,40,20,0,180,178,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,183,
        1,0,0,0,183,39,1,0,0,0,184,182,1,0,0,0,185,186,6,20,-1,0,186,199,
        3,30,15,0,187,188,5,25,0,0,188,199,3,40,20,7,189,190,5,32,0,0,190,
        191,3,40,20,0,191,192,5,33,0,0,192,199,1,0,0,0,193,199,5,31,0,0,
        194,199,5,29,0,0,195,199,5,30,0,0,196,199,5,26,0,0,197,199,5,27,
        0,0,198,185,1,0,0,0,198,187,1,0,0,0,198,189,1,0,0,0,198,193,1,0,
        0,0,198,194,1,0,0,0,198,195,1,0,0,0,198,196,1,0,0,0,198,197,1,0,
        0,0,199,214,1,0,0,0,200,201,10,11,0,0,201,202,7,0,0,0,202,213,3,
        40,20,12,203,204,10,10,0,0,204,205,7,1,0,0,205,213,3,40,20,11,206,
        207,10,9,0,0,207,208,7,2,0,0,208,213,3,40,20,10,209,210,10,8,0,0,
        210,211,7,3,0,0,211,213,3,40,20,9,212,200,1,0,0,0,212,203,1,0,0,
        0,212,206,1,0,0,0,212,209,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,
        0,214,215,1,0,0,0,215,41,1,0,0,0,216,214,1,0,0,0,19,46,54,56,73,
        84,87,96,98,104,120,123,131,140,160,172,182,198,212,214
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'field'", "'if'", "'elif'", "'else'", 
                     "'return'", "'print'", "'for'", "'in'", "'while'", 
                     "'def'", "'procedure'", "'+'", "'-'", "'*'", "'/'", 
                     "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", "'%'", 
                     "'and'", "'or'", "'not'", "'True'", "'False'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IF", "ELIF", "ELSE", "RETURN", 
                      "PRINT", "FOR", "IN", "WHILE", "DEF", "PROCEDURE", 
                      "PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", "LT", 
                      "LTE", "EQ", "NEQ", "MOD", "AND", "OR", "NOT", "TRUE", 
                      "FALSE", "COMMENT_SINGLELINE", "NUMBER", "STRING", 
                      "ID", "OPEN_PARENTH", "CLOSED_PARENTH", "OPEN_BRACK", 
                      "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", "COMMA", 
                      "DOT", "EQUAL_SIGN", "WS" ]

    RULE_prog = 0
    RULE_object = 1
    RULE_procedure = 2
    RULE_stat = 3
    RULE_field = 4
    RULE_list = 5
    RULE_varDecl = 6
    RULE_functionDecl = 7
    RULE_printStat = 8
    RULE_ifStat = 9
    RULE_elifStat = 10
    RULE_elseStat = 11
    RULE_statBlock = 12
    RULE_forLoop = 13
    RULE_whileLoop = 14
    RULE_functionCall = 15
    RULE_returnStat = 16
    RULE_params = 17
    RULE_param = 18
    RULE_args = 19
    RULE_expr = 20

    ruleNames =  [ "prog", "object", "procedure", "stat", "field", "list", 
                   "varDecl", "functionDecl", "printStat", "ifStat", "elifStat", 
                   "elseStat", "statBlock", "forLoop", "whileLoop", "functionCall", 
                   "returnStat", "params", "param", "args", "expr" ]

    EOF = Token.EOF
    T__0=1
    IF=2
    ELIF=3
    ELSE=4
    RETURN=5
    PRINT=6
    FOR=7
    IN=8
    WHILE=9
    DEF=10
    PROCEDURE=11
    PLUS=12
    MINUS=13
    MULT=14
    DIV=15
    GT=16
    GTE=17
    LT=18
    LTE=19
    EQ=20
    NEQ=21
    MOD=22
    AND=23
    OR=24
    NOT=25
    TRUE=26
    FALSE=27
    COMMENT_SINGLELINE=28
    NUMBER=29
    STRING=30
    ID=31
    OPEN_PARENTH=32
    CLOSED_PARENTH=33
    OPEN_BRACK=34
    CLOSED_BRACK=35
    OPEN_CURL=36
    CLOSED_CURL=37
    COMMA=38
    DOT=39
    EQUAL_SIGN=40
    WS=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_(self):
            return self.getTypedRuleContext(RogueLangParser.ObjectContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = RogueLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.object_()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 77007423204) != 0):
                self.state = 43
                self.stat()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def OPEN_CURL(self):
            return self.getToken(RogueLangParser.OPEN_CURL, 0)

        def procedure(self):
            return self.getTypedRuleContext(RogueLangParser.ProcedureContext,0)


        def CLOSED_CURL(self):
            return self.getToken(RogueLangParser.CLOSED_CURL, 0)

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.FieldContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.FieldContext,i)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_object

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject" ):
                return visitor.visitObject(self)
            else:
                return visitor.visitChildren(self)




    def object_(self):

        localctx = RogueLangParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(RogueLangParser.ID)
            self.state = 50
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 51
            self.procedure()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 77007423206) != 0):
                self.state = 54
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 52
                    self.field()
                    pass
                elif token in [2, 5, 6, 7, 9, 10, 25, 26, 27, 29, 30, 31, 32, 36]:
                    self.state = 53
                    self.stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(RogueLangParser.CLOSED_CURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE(self):
            return self.getToken(RogueLangParser.PROCEDURE, 0)

        def statBlock(self):
            return self.getTypedRuleContext(RogueLangParser.StatBlockContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_procedure

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure" ):
                return visitor.visitProcedure(self)
            else:
                return visitor.visitChildren(self)




    def procedure(self):

        localctx = RogueLangParser.ProcedureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_procedure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(RogueLangParser.PROCEDURE)
            self.state = 62
            self.statBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printStat(self):
            return self.getTypedRuleContext(RogueLangParser.PrintStatContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(RogueLangParser.VarDeclContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(RogueLangParser.FunctionDeclContext,0)


        def ifStat(self):
            return self.getTypedRuleContext(RogueLangParser.IfStatContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(RogueLangParser.ForLoopContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(RogueLangParser.WhileLoopContext,0)


        def statBlock(self):
            return self.getTypedRuleContext(RogueLangParser.StatBlockContext,0)


        def returnStat(self):
            return self.getTypedRuleContext(RogueLangParser.ReturnStatContext,0)


        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = RogueLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.functionDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.ifStat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.forLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 69
                self.whileLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 70
                self.statBlock()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 71
                self.returnStat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 72
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(RogueLangParser.VarDeclContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = RogueLangParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(RogueLangParser.T__0)
            self.state = 76
            self.varDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACK(self):
            return self.getToken(RogueLangParser.OPEN_BRACK, 0)

        def CLOSED_BRACK(self):
            return self.getToken(RogueLangParser.CLOSED_BRACK, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.COMMA)
            else:
                return self.getToken(RogueLangParser.COMMA, i)

        def getRuleIndex(self):
            return RogueLangParser.RULE_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = RogueLangParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(RogueLangParser.OPEN_BRACK)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8287944704) != 0):
                self.state = 79
                self.expr(0)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 80
                    self.match(RogueLangParser.COMMA)
                    self.state = 81
                    self.expr(0)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 89
            self.match(RogueLangParser.CLOSED_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def EQUAL_SIGN(self):
            return self.getToken(RogueLangParser.EQUAL_SIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(RogueLangParser.FunctionCallContext,0)


        def list_(self):
            return self.getTypedRuleContext(RogueLangParser.ListContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = RogueLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(RogueLangParser.ID)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 92
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 96
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 93
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 94
                    self.functionCall()
                    pass

                elif la_ == 3:
                    self.state = 95
                    self.list_()
                    pass




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(RogueLangParser.DEF, 0)

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def statBlock(self):
            return self.getTypedRuleContext(RogueLangParser.StatBlockContext,0)


        def params(self):
            return self.getTypedRuleContext(RogueLangParser.ParamsContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_functionDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = RogueLangParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(RogueLangParser.DEF)
            self.state = 101
            self.match(RogueLangParser.ID)
            self.state = 102
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 103
                self.params()


            self.state = 106
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 107
            self.statBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(RogueLangParser.PRINT, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_printStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)




    def printStat(self):

        localctx = RogueLangParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(RogueLangParser.PRINT)
            self.state = 110
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 111
            self.expr(0)
            self.state = 112
            self.match(RogueLangParser.CLOSED_PARENTH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(RogueLangParser.IF, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def statBlock(self):
            return self.getTypedRuleContext(RogueLangParser.StatBlockContext,0)


        def elifStat(self):
            return self.getTypedRuleContext(RogueLangParser.ElifStatContext,0)


        def elseStat(self):
            return self.getTypedRuleContext(RogueLangParser.ElseStatContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_ifStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)




    def ifStat(self):

        localctx = RogueLangParser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(RogueLangParser.IF)
            self.state = 115
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 116
            self.expr(0)
            self.state = 117
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 118
            self.statBlock()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 119
                self.elifStat()


            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 122
                self.elseStat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(RogueLangParser.ELIF, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def statBlock(self):
            return self.getTypedRuleContext(RogueLangParser.StatBlockContext,0)


        def elifStat(self):
            return self.getTypedRuleContext(RogueLangParser.ElifStatContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_elifStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifStat" ):
                return visitor.visitElifStat(self)
            else:
                return visitor.visitChildren(self)




    def elifStat(self):

        localctx = RogueLangParser.ElifStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(RogueLangParser.ELIF)
            self.state = 126
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 127
            self.expr(0)
            self.state = 128
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 129
            self.statBlock()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 130
                self.elifStat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(RogueLangParser.ELSE, 0)

        def statBlock(self):
            return self.getTypedRuleContext(RogueLangParser.StatBlockContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_elseStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStat" ):
                return visitor.visitElseStat(self)
            else:
                return visitor.visitChildren(self)




    def elseStat(self):

        localctx = RogueLangParser.ElseStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elseStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(RogueLangParser.ELSE)
            self.state = 134
            self.statBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_CURL(self):
            return self.getToken(RogueLangParser.OPEN_CURL, 0)

        def CLOSED_CURL(self):
            return self.getToken(RogueLangParser.CLOSED_CURL, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_statBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatBlock" ):
                return visitor.visitStatBlock(self)
            else:
                return visitor.visitChildren(self)




    def statBlock(self):

        localctx = RogueLangParser.StatBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 77007423204) != 0):
                self.state = 137
                self.stat()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(RogueLangParser.CLOSED_CURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(RogueLangParser.FOR, 0)

        def varDecl(self):
            return self.getTypedRuleContext(RogueLangParser.VarDeclContext,0)


        def IN(self):
            return self.getToken(RogueLangParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def statBlock(self):
            return self.getTypedRuleContext(RogueLangParser.StatBlockContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_forLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = RogueLangParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(RogueLangParser.FOR)
            self.state = 146
            self.varDecl()
            self.state = 147
            self.match(RogueLangParser.IN)
            self.state = 148
            self.expr(0)
            self.state = 149
            self.statBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(RogueLangParser.WHILE, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def statBlock(self):
            return self.getTypedRuleContext(RogueLangParser.StatBlockContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_whileLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = RogueLangParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(RogueLangParser.WHILE)
            self.state = 152
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 153
            self.expr(0)
            self.state = 154
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 155
            self.statBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def args(self):
            return self.getTypedRuleContext(RogueLangParser.ArgsContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = RogueLangParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(RogueLangParser.ID)
            self.state = 158
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8287944704) != 0):
                self.state = 159
                self.args()


            self.state = 162
            self.match(RogueLangParser.CLOSED_PARENTH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(RogueLangParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_returnStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStat" ):
                return visitor.visitReturnStat(self)
            else:
                return visitor.visitChildren(self)




    def returnStat(self):

        localctx = RogueLangParser.ReturnStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(RogueLangParser.RETURN)
            self.state = 165
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.COMMA)
            else:
                return self.getToken(RogueLangParser.COMMA, i)

        def getRuleIndex(self):
            return RogueLangParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = RogueLangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.param()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 168
                self.match(RogueLangParser.COMMA)
                self.state = 169
                self.param()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = RogueLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(RogueLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.COMMA)
            else:
                return self.getToken(RogueLangParser.COMMA, i)

        def getRuleIndex(self):
            return RogueLangParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = RogueLangParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.expr(0)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 178
                self.match(RogueLangParser.COMMA)
                self.state = 179
                self.expr(0)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def functionCall(self):
            return self.getTypedRuleContext(RogueLangParser.FunctionCallContext,0)


        def NOT(self):
            return self.getToken(RogueLangParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def NUMBER(self):
            return self.getToken(RogueLangParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(RogueLangParser.STRING, 0)

        def TRUE(self):
            return self.getToken(RogueLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(RogueLangParser.FALSE, 0)

        def MULT(self):
            return self.getToken(RogueLangParser.MULT, 0)

        def DIV(self):
            return self.getToken(RogueLangParser.DIV, 0)

        def MOD(self):
            return self.getToken(RogueLangParser.MOD, 0)

        def PLUS(self):
            return self.getToken(RogueLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(RogueLangParser.MINUS, 0)

        def GT(self):
            return self.getToken(RogueLangParser.GT, 0)

        def GTE(self):
            return self.getToken(RogueLangParser.GTE, 0)

        def LT(self):
            return self.getToken(RogueLangParser.LT, 0)

        def LTE(self):
            return self.getToken(RogueLangParser.LTE, 0)

        def EQ(self):
            return self.getToken(RogueLangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(RogueLangParser.NEQ, 0)

        def AND(self):
            return self.getToken(RogueLangParser.AND, 0)

        def OR(self):
            return self.getToken(RogueLangParser.OR, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RogueLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 186
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 187
                self.match(RogueLangParser.NOT)
                self.state = 188
                self.expr(7)
                pass

            elif la_ == 3:
                self.state = 189
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 190
                self.expr(0)
                self.state = 191
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 4:
                self.state = 193
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 5:
                self.state = 194
                self.match(RogueLangParser.NUMBER)
                pass

            elif la_ == 6:
                self.state = 195
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 7:
                self.state = 196
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 8:
                self.state = 197
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 212
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 200
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 201
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4243456) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 202
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 203
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 204
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 205
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 206
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 207
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 208
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 209
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 210
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 211
                        self.expr(9)
                        pass

             
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




