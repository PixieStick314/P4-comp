# Generated from C:/Users/Loke/PycharmProjects/P4-comp/src/grammar_files/RogueLang.g4 by ANTLR 4.13.1
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
        4,1,42,232,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,4,0,38,8,0,11,0,12,0,
        39,1,1,1,1,1,1,1,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,1,1,1,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,67,8,3,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,3,5,77,8,5,3,5,79,8,5,1,6,1,6,1,6,1,6,3,
        6,85,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,5,8,106,8,8,10,8,12,8,109,9,8,1,8,1,8,3,8,113,
        8,8,1,9,1,9,5,9,117,8,9,10,9,12,9,120,9,9,1,9,1,9,1,10,1,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,4,11,136,8,11,11,11,
        12,11,137,1,11,1,11,1,12,1,12,1,12,3,12,145,8,12,1,12,1,12,1,13,
        1,13,1,13,1,14,1,14,1,14,5,14,155,8,14,10,14,12,14,158,9,14,1,15,
        1,15,1,16,1,16,1,16,5,16,165,8,16,10,16,12,16,168,9,16,1,17,1,17,
        1,17,1,17,5,17,174,8,17,10,17,12,17,177,9,17,1,17,1,17,1,17,5,17,
        182,8,17,10,17,12,17,185,9,17,1,17,1,17,1,17,5,17,190,8,17,10,17,
        12,17,193,9,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,213,8,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,5,17,227,8,17,
        10,17,12,17,230,9,17,1,17,0,1,34,18,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,0,4,2,0,15,16,23,23,1,0,13,14,1,0,17,22,1,0,
        24,25,253,0,37,1,0,0,0,2,41,1,0,0,0,4,53,1,0,0,0,6,66,1,0,0,0,8,
        68,1,0,0,0,10,71,1,0,0,0,12,80,1,0,0,0,14,89,1,0,0,0,16,94,1,0,0,
        0,18,114,1,0,0,0,20,123,1,0,0,0,22,129,1,0,0,0,24,141,1,0,0,0,26,
        148,1,0,0,0,28,151,1,0,0,0,30,159,1,0,0,0,32,161,1,0,0,0,34,212,
        1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,
        39,40,1,0,0,0,40,1,1,0,0,0,41,42,5,32,0,0,42,43,5,37,0,0,43,48,3,
        4,2,0,44,47,3,8,4,0,45,47,3,6,3,0,46,44,1,0,0,0,46,45,1,0,0,0,47,
        50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,
        0,51,52,5,38,0,0,52,3,1,0,0,0,53,54,5,12,0,0,54,55,3,18,9,0,55,5,
        1,0,0,0,56,67,3,14,7,0,57,67,3,10,5,0,58,67,3,12,6,0,59,67,3,16,
        8,0,60,67,3,20,10,0,61,67,3,22,11,0,62,67,3,24,12,0,63,67,3,18,9,
        0,64,67,3,26,13,0,65,67,3,34,17,0,66,56,1,0,0,0,66,57,1,0,0,0,66,
        58,1,0,0,0,66,59,1,0,0,0,66,60,1,0,0,0,66,61,1,0,0,0,66,62,1,0,0,
        0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,7,1,0,0,0,68,69,5,
        1,0,0,69,70,3,10,5,0,70,9,1,0,0,0,71,78,5,32,0,0,72,76,5,41,0,0,
        73,77,3,34,17,0,74,77,3,32,16,0,75,77,3,24,12,0,76,73,1,0,0,0,76,
        74,1,0,0,0,76,75,1,0,0,0,77,79,1,0,0,0,78,72,1,0,0,0,78,79,1,0,0,
        0,79,11,1,0,0,0,80,81,5,11,0,0,81,82,5,32,0,0,82,84,5,33,0,0,83,
        85,3,28,14,0,84,83,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,34,
        0,0,87,88,3,18,9,0,88,13,1,0,0,0,89,90,5,7,0,0,90,91,5,33,0,0,91,
        92,3,34,17,0,92,93,5,34,0,0,93,15,1,0,0,0,94,95,5,3,0,0,95,96,5,
        33,0,0,96,97,3,34,17,0,97,98,5,34,0,0,98,107,3,18,9,0,99,100,5,4,
        0,0,100,101,5,33,0,0,101,102,3,34,17,0,102,103,5,34,0,0,103,104,
        3,18,9,0,104,106,1,0,0,0,105,99,1,0,0,0,106,109,1,0,0,0,107,105,
        1,0,0,0,107,108,1,0,0,0,108,112,1,0,0,0,109,107,1,0,0,0,110,111,
        5,5,0,0,111,113,3,18,9,0,112,110,1,0,0,0,112,113,1,0,0,0,113,17,
        1,0,0,0,114,118,5,37,0,0,115,117,3,6,3,0,116,115,1,0,0,0,117,120,
        1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,118,
        1,0,0,0,121,122,5,38,0,0,122,19,1,0,0,0,123,124,5,8,0,0,124,125,
        3,10,5,0,125,126,5,9,0,0,126,127,3,34,17,0,127,128,3,18,9,0,128,
        21,1,0,0,0,129,130,5,10,0,0,130,131,5,33,0,0,131,132,3,34,17,0,132,
        133,5,34,0,0,133,135,5,37,0,0,134,136,3,6,3,0,135,134,1,0,0,0,136,
        137,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,139,1,0,0,0,139,
        140,5,38,0,0,140,23,1,0,0,0,141,142,5,32,0,0,142,144,5,33,0,0,143,
        145,3,32,16,0,144,143,1,0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,
        147,5,34,0,0,147,25,1,0,0,0,148,149,5,6,0,0,149,150,3,34,17,0,150,
        27,1,0,0,0,151,156,3,30,15,0,152,153,5,39,0,0,153,155,3,30,15,0,
        154,152,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,
        157,29,1,0,0,0,158,156,1,0,0,0,159,160,5,32,0,0,160,31,1,0,0,0,161,
        166,3,34,17,0,162,163,5,39,0,0,163,165,3,34,17,0,164,162,1,0,0,0,
        165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,33,1,0,0,0,168,
        166,1,0,0,0,169,170,6,17,-1,0,170,213,3,24,12,0,171,175,5,35,0,0,
        172,174,3,34,17,0,173,172,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,
        0,175,176,1,0,0,0,176,178,1,0,0,0,177,175,1,0,0,0,178,213,5,36,0,
        0,179,183,5,35,0,0,180,182,3,34,17,0,181,180,1,0,0,0,182,185,1,0,
        0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,0,185,183,1,0,
        0,0,186,187,5,36,0,0,187,191,5,41,0,0,188,190,3,34,17,0,189,188,
        1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,213,
        1,0,0,0,193,191,1,0,0,0,194,195,5,32,0,0,195,196,5,40,0,0,196,197,
        5,2,0,0,197,198,5,33,0,0,198,199,3,34,17,0,199,200,5,34,0,0,200,
        213,1,0,0,0,201,202,5,26,0,0,202,213,3,34,17,7,203,204,5,33,0,0,
        204,205,3,34,17,0,205,206,5,34,0,0,206,213,1,0,0,0,207,213,5,32,
        0,0,208,213,5,30,0,0,209,213,5,31,0,0,210,213,5,27,0,0,211,213,5,
        28,0,0,212,169,1,0,0,0,212,171,1,0,0,0,212,179,1,0,0,0,212,194,1,
        0,0,0,212,201,1,0,0,0,212,203,1,0,0,0,212,207,1,0,0,0,212,208,1,
        0,0,0,212,209,1,0,0,0,212,210,1,0,0,0,212,211,1,0,0,0,213,228,1,
        0,0,0,214,215,10,11,0,0,215,216,7,0,0,0,216,227,3,34,17,12,217,218,
        10,10,0,0,218,219,7,1,0,0,219,227,3,34,17,11,220,221,10,9,0,0,221,
        222,7,2,0,0,222,227,3,34,17,10,223,224,10,8,0,0,224,225,7,3,0,0,
        225,227,3,34,17,9,226,214,1,0,0,0,226,217,1,0,0,0,226,220,1,0,0,
        0,226,223,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,
        0,229,35,1,0,0,0,230,228,1,0,0,0,20,39,46,48,66,76,78,84,107,112,
        118,137,144,156,166,175,183,191,212,226,228
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'field'", "'add'", "'if'", "'elif'", 
                     "'else'", "'return'", "'print'", "'for'", "'in'", "'while'", 
                     "'def'", "'procedure'", "'+'", "'-'", "'*'", "'/'", 
                     "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", "'%'", 
                     "'and'", "'or'", "'not'", "'True'", "'False'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELIF", 
                      "ELSE", "RETURN", "PRINT", "FOR", "IN", "WHILE", "DEF", 
                      "PROCEDURE", "PLUS", "MINUS", "MULT", "DIV", "GT", 
                      "GTE", "LT", "LTE", "EQ", "NEQ", "MOD", "AND", "OR", 
                      "NOT", "TRUE", "FALSE", "COMMENT_SINGLELINE", "NUMBER", 
                      "STRING", "ID", "OPEN_PARENTH", "CLOSED_PARENTH", 
                      "OPEN_BRACK", "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", 
                      "COMMA", "DOT", "EQUAL_SIGN", "WS" ]

    RULE_prog = 0
    RULE_object = 1
    RULE_procedure = 2
    RULE_stat = 3
    RULE_field = 4
    RULE_varDecl = 5
    RULE_functionDecl = 6
    RULE_printStat = 7
    RULE_ifStat = 8
    RULE_statBlock = 9
    RULE_forLoop = 10
    RULE_whileLoop = 11
    RULE_functionCall = 12
    RULE_returnStat = 13
    RULE_params = 14
    RULE_param = 15
    RULE_args = 16
    RULE_expr = 17

    ruleNames =  [ "prog", "object", "procedure", "stat", "field", "varDecl", 
                   "functionDecl", "printStat", "ifStat", "statBlock", "forLoop", 
                   "whileLoop", "functionCall", "returnStat", "params", 
                   "param", "args", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IF=3
    ELIF=4
    ELSE=5
    RETURN=6
    PRINT=7
    FOR=8
    IN=9
    WHILE=10
    DEF=11
    PROCEDURE=12
    PLUS=13
    MINUS=14
    MULT=15
    DIV=16
    GT=17
    GTE=18
    LT=19
    LTE=20
    EQ=21
    NEQ=22
    MOD=23
    AND=24
    OR=25
    NOT=26
    TRUE=27
    FALSE=28
    COMMENT_SINGLELINE=29
    NUMBER=30
    STRING=31
    ID=32
    OPEN_PARENTH=33
    CLOSED_PARENTH=34
    OPEN_BRACK=35
    CLOSED_BRACK=36
    OPEN_CURL=37
    CLOSED_CURL=38
    COMMA=39
    DOT=40
    EQUAL_SIGN=41
    WS=42

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

        def object_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ObjectContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ObjectContext,i)


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
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.object_()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

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
            self.state = 41
            self.match(RogueLangParser.ID)
            self.state = 42
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 43
            self.procedure()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 188374584778) != 0):
                self.state = 46
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 44
                    self.field()
                    pass
                elif token in [3, 6, 7, 8, 10, 11, 26, 27, 28, 30, 31, 32, 33, 35, 37]:
                    self.state = 45
                    self.stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
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
            self.state = 53
            self.match(RogueLangParser.PROCEDURE)
            self.state = 54
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


        def functionCall(self):
            return self.getTypedRuleContext(RogueLangParser.FunctionCallContext,0)


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
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.functionDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.ifStat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.forLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 61
                self.whileLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.functionCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 63
                self.statBlock()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 64
                self.returnStat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 65
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
            self.state = 68
            self.match(RogueLangParser.T__0)
            self.state = 69
            self.varDecl()
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


        def args(self):
            return self.getTypedRuleContext(RogueLangParser.ArgsContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(RogueLangParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = RogueLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(RogueLangParser.ID)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 72
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 76
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 73
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 74
                    self.args()
                    pass

                elif la_ == 3:
                    self.state = 75
                    self.functionCall()
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
        self.enterRule(localctx, 12, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(RogueLangParser.DEF)
            self.state = 81
            self.match(RogueLangParser.ID)
            self.state = 82
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 83
                self.params()


            self.state = 86
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 87
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
        self.enterRule(localctx, 14, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(RogueLangParser.PRINT)
            self.state = 90
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 91
            self.expr(0)
            self.state = 92
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

        def OPEN_PARENTH(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.OPEN_PARENTH)
            else:
                return self.getToken(RogueLangParser.OPEN_PARENTH, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def CLOSED_PARENTH(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.CLOSED_PARENTH)
            else:
                return self.getToken(RogueLangParser.CLOSED_PARENTH, i)

        def statBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatBlockContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatBlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.ELIF)
            else:
                return self.getToken(RogueLangParser.ELIF, i)

        def ELSE(self):
            return self.getToken(RogueLangParser.ELSE, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_ifStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)




    def ifStat(self):

        localctx = RogueLangParser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(RogueLangParser.IF)
            self.state = 95
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 96
            self.expr(0)
            self.state = 97
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 98
            self.statBlock()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 99
                self.match(RogueLangParser.ELIF)
                self.state = 100
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 101
                self.expr(0)
                self.state = 102
                self.match(RogueLangParser.CLOSED_PARENTH)
                self.state = 103
                self.statBlock()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 110
                self.match(RogueLangParser.ELSE)
                self.state = 111
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
        self.enterRule(localctx, 18, self.RULE_statBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 188374584776) != 0):
                self.state = 115
                self.stat()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
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
        self.enterRule(localctx, 20, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(RogueLangParser.FOR)
            self.state = 124
            self.varDecl()
            self.state = 125
            self.match(RogueLangParser.IN)
            self.state = 126
            self.expr(0)
            self.state = 127
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
            return RogueLangParser.RULE_whileLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = RogueLangParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(RogueLangParser.WHILE)
            self.state = 130
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 131
            self.expr(0)
            self.state = 132
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 133
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 135 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 134
                self.stat()
                self.state = 137 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 188374584776) != 0)):
                    break

            self.state = 139
            self.match(RogueLangParser.CLOSED_CURL)
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
        self.enterRule(localctx, 24, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(RogueLangParser.ID)
            self.state = 142
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 50935627776) != 0):
                self.state = 143
                self.args()


            self.state = 146
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
        self.enterRule(localctx, 26, self.RULE_returnStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(RogueLangParser.RETURN)
            self.state = 149
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
        self.enterRule(localctx, 28, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.param()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 152
                self.match(RogueLangParser.COMMA)
                self.state = 153
                self.param()
                self.state = 158
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
        self.enterRule(localctx, 30, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
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
        self.enterRule(localctx, 32, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.expr(0)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 162
                self.match(RogueLangParser.COMMA)
                self.state = 163
                self.expr(0)
                self.state = 168
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


        def OPEN_BRACK(self):
            return self.getToken(RogueLangParser.OPEN_BRACK, 0)

        def CLOSED_BRACK(self):
            return self.getToken(RogueLangParser.CLOSED_BRACK, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def EQUAL_SIGN(self):
            return self.getToken(RogueLangParser.EQUAL_SIGN, 0)

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def DOT(self):
            return self.getToken(RogueLangParser.DOT, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def NOT(self):
            return self.getToken(RogueLangParser.NOT, 0)

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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 170
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 171
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 50935627776) != 0):
                    self.state = 172
                    self.expr(0)
                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 178
                self.match(RogueLangParser.CLOSED_BRACK)
                pass

            elif la_ == 3:
                self.state = 179
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 50935627776) != 0):
                    self.state = 180
                    self.expr(0)
                    self.state = 185
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 186
                self.match(RogueLangParser.CLOSED_BRACK)
                self.state = 187
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 188
                        self.expr(0) 
                    self.state = 193
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                pass

            elif la_ == 4:
                self.state = 194
                self.match(RogueLangParser.ID)
                self.state = 195
                self.match(RogueLangParser.DOT)
                self.state = 196
                self.match(RogueLangParser.T__1)
                self.state = 197
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 198
                self.expr(0)
                self.state = 199
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 5:
                self.state = 201
                self.match(RogueLangParser.NOT)
                self.state = 202
                self.expr(7)
                pass

            elif la_ == 6:
                self.state = 203
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 204
                self.expr(0)
                self.state = 205
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 7:
                self.state = 207
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 8:
                self.state = 208
                self.match(RogueLangParser.NUMBER)
                pass

            elif la_ == 9:
                self.state = 209
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 10:
                self.state = 210
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 11:
                self.state = 211
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 226
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 214
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 215
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8486912) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 216
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 217
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 218
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 219
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 220
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 221
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 222
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 223
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 224
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 225
                        self.expr(9)
                        pass

             
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self._predicates[17] = self.expr_sempred
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
         




