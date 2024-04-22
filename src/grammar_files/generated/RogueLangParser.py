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
        4,1,48,291,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,5,0,63,8,0,10,0,12,0,66,9,
        0,1,1,1,1,1,1,1,1,1,1,5,1,73,8,1,10,1,12,1,76,9,1,1,1,1,1,1,2,1,
        2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,99,8,4,1,5,1,5,1,5,1,6,1,6,3,6,106,8,6,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,3,8,115,8,8,1,9,1,9,1,9,1,9,3,9,121,8,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,5,10,130,8,10,10,10,12,10,133,9,10,3,10,135,
        8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,147,
        8,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,1,17,1,17,1,17,3,17,179,8,17,1,17,3,17,182,8,17,1,18,1,
        18,1,18,1,18,1,18,1,18,3,18,190,8,18,1,19,1,19,1,19,1,20,1,20,5,
        20,197,8,20,10,20,12,20,200,9,20,1,20,1,20,1,21,1,21,1,21,1,21,1,
        21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,3,23,219,8,
        23,1,23,1,23,1,24,1,24,1,24,5,24,226,8,24,10,24,12,24,229,9,24,1,
        25,1,25,1,25,5,25,234,8,25,10,25,12,25,237,9,25,1,26,1,26,1,26,1,
        27,1,27,1,27,1,27,1,27,1,27,3,27,248,8,27,1,28,1,28,1,28,1,28,1,
        28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,1,29,1,29,3,29,272,8,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,1,29,5,29,286,8,29,10,29,12,29,289,9,
        29,1,29,0,1,58,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,0,4,2,0,18,19,28,28,1,0,16,
        17,1,0,20,25,1,0,29,30,304,0,60,1,0,0,0,2,67,1,0,0,0,4,79,1,0,0,
        0,6,82,1,0,0,0,8,98,1,0,0,0,10,100,1,0,0,0,12,103,1,0,0,0,14,107,
        1,0,0,0,16,114,1,0,0,0,18,116,1,0,0,0,20,125,1,0,0,0,22,146,1,0,
        0,0,24,148,1,0,0,0,26,153,1,0,0,0,28,159,1,0,0,0,30,163,1,0,0,0,
        32,167,1,0,0,0,34,172,1,0,0,0,36,183,1,0,0,0,38,191,1,0,0,0,40,194,
        1,0,0,0,42,203,1,0,0,0,44,209,1,0,0,0,46,215,1,0,0,0,48,222,1,0,
        0,0,50,230,1,0,0,0,52,238,1,0,0,0,54,247,1,0,0,0,56,249,1,0,0,0,
        58,271,1,0,0,0,60,64,3,2,1,0,61,63,3,8,4,0,62,61,1,0,0,0,63,66,1,
        0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,1,1,0,0,0,66,64,1,0,0,0,67,
        68,5,38,0,0,68,69,5,43,0,0,69,74,3,4,2,0,70,73,3,6,3,0,71,73,3,8,
        4,0,72,70,1,0,0,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,
        1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,78,5,44,0,0,78,3,1,0,0,0,
        79,80,5,15,0,0,80,81,3,40,20,0,81,5,1,0,0,0,82,83,5,1,0,0,83,84,
        3,12,6,0,84,7,1,0,0,0,85,99,3,32,16,0,86,99,3,10,5,0,87,99,3,14,
        7,0,88,99,3,18,9,0,89,99,3,34,17,0,90,99,3,42,21,0,91,99,3,44,22,
        0,92,99,3,40,20,0,93,99,3,52,26,0,94,99,3,28,14,0,95,99,3,30,15,
        0,96,99,3,26,13,0,97,99,3,58,29,0,98,85,1,0,0,0,98,86,1,0,0,0,98,
        87,1,0,0,0,98,88,1,0,0,0,98,89,1,0,0,0,98,90,1,0,0,0,98,91,1,0,0,
        0,98,92,1,0,0,0,98,93,1,0,0,0,98,94,1,0,0,0,98,95,1,0,0,0,98,96,
        1,0,0,0,98,97,1,0,0,0,99,9,1,0,0,0,100,101,5,2,0,0,101,102,3,12,
        6,0,102,11,1,0,0,0,103,105,5,38,0,0,104,106,3,16,8,0,105,104,1,0,
        0,0,105,106,1,0,0,0,106,13,1,0,0,0,107,108,5,38,0,0,108,109,3,16,
        8,0,109,15,1,0,0,0,110,111,5,47,0,0,111,115,3,58,29,0,112,113,5,
        47,0,0,113,115,3,20,10,0,114,110,1,0,0,0,114,112,1,0,0,0,115,17,
        1,0,0,0,116,117,5,14,0,0,117,118,5,38,0,0,118,120,5,39,0,0,119,121,
        3,48,24,0,120,119,1,0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,
        5,40,0,0,123,124,3,40,20,0,124,19,1,0,0,0,125,134,5,41,0,0,126,131,
        3,58,29,0,127,128,5,45,0,0,128,130,3,58,29,0,129,127,1,0,0,0,130,
        133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,135,1,0,0,0,133,
        131,1,0,0,0,134,126,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,
        137,5,42,0,0,137,21,1,0,0,0,138,139,5,38,0,0,139,140,5,41,0,0,140,
        141,5,35,0,0,141,147,5,42,0,0,142,143,5,38,0,0,143,144,5,41,0,0,
        144,145,5,38,0,0,145,147,5,42,0,0,146,138,1,0,0,0,146,142,1,0,0,
        0,147,23,1,0,0,0,148,149,5,3,0,0,149,150,5,39,0,0,150,151,5,38,0,
        0,151,152,5,40,0,0,152,25,1,0,0,0,153,154,5,38,0,0,154,155,5,46,
        0,0,155,156,5,4,0,0,156,157,5,39,0,0,157,158,5,40,0,0,158,27,1,0,
        0,0,159,160,5,38,0,0,160,161,5,26,0,0,161,162,3,58,29,0,162,29,1,
        0,0,0,163,164,5,38,0,0,164,165,5,27,0,0,165,166,3,58,29,0,166,31,
        1,0,0,0,167,168,5,10,0,0,168,169,5,39,0,0,169,170,3,58,29,0,170,
        171,5,40,0,0,171,33,1,0,0,0,172,173,5,6,0,0,173,174,5,39,0,0,174,
        175,3,58,29,0,175,176,5,40,0,0,176,178,3,40,20,0,177,179,3,36,18,
        0,178,177,1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,0,180,182,3,38,19,
        0,181,180,1,0,0,0,181,182,1,0,0,0,182,35,1,0,0,0,183,184,5,7,0,0,
        184,185,5,39,0,0,185,186,3,58,29,0,186,187,5,40,0,0,187,189,3,40,
        20,0,188,190,3,36,18,0,189,188,1,0,0,0,189,190,1,0,0,0,190,37,1,
        0,0,0,191,192,5,8,0,0,192,193,3,40,20,0,193,39,1,0,0,0,194,198,5,
        43,0,0,195,197,3,8,4,0,196,195,1,0,0,0,197,200,1,0,0,0,198,196,1,
        0,0,0,198,199,1,0,0,0,199,201,1,0,0,0,200,198,1,0,0,0,201,202,5,
        44,0,0,202,41,1,0,0,0,203,204,5,11,0,0,204,205,5,38,0,0,205,206,
        5,12,0,0,206,207,5,38,0,0,207,208,3,40,20,0,208,43,1,0,0,0,209,210,
        5,13,0,0,210,211,5,39,0,0,211,212,3,58,29,0,212,213,5,40,0,0,213,
        214,3,40,20,0,214,45,1,0,0,0,215,216,5,38,0,0,216,218,5,39,0,0,217,
        219,3,50,25,0,218,217,1,0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,
        221,5,40,0,0,221,47,1,0,0,0,222,227,5,38,0,0,223,224,5,45,0,0,224,
        226,5,38,0,0,225,223,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,
        228,1,0,0,0,228,49,1,0,0,0,229,227,1,0,0,0,230,235,3,58,29,0,231,
        232,5,45,0,0,232,234,3,58,29,0,233,231,1,0,0,0,234,237,1,0,0,0,235,
        233,1,0,0,0,235,236,1,0,0,0,236,51,1,0,0,0,237,235,1,0,0,0,238,239,
        5,9,0,0,239,240,3,58,29,0,240,53,1,0,0,0,241,242,5,5,0,0,242,243,
        5,12,0,0,243,248,3,56,28,0,244,245,5,5,0,0,245,246,5,12,0,0,246,
        248,5,38,0,0,247,241,1,0,0,0,247,244,1,0,0,0,248,55,1,0,0,0,249,
        250,3,58,29,0,250,251,5,46,0,0,251,252,5,46,0,0,252,253,3,58,29,
        0,253,57,1,0,0,0,254,255,6,29,-1,0,255,272,3,46,23,0,256,272,3,22,
        11,0,257,272,3,24,12,0,258,272,3,54,27,0,259,260,5,31,0,0,260,272,
        3,58,29,8,261,262,5,39,0,0,262,263,3,58,29,0,263,264,5,40,0,0,264,
        272,1,0,0,0,265,272,5,38,0,0,266,272,5,35,0,0,267,272,5,36,0,0,268,
        272,5,37,0,0,269,272,5,32,0,0,270,272,5,33,0,0,271,254,1,0,0,0,271,
        256,1,0,0,0,271,257,1,0,0,0,271,258,1,0,0,0,271,259,1,0,0,0,271,
        261,1,0,0,0,271,265,1,0,0,0,271,266,1,0,0,0,271,267,1,0,0,0,271,
        268,1,0,0,0,271,269,1,0,0,0,271,270,1,0,0,0,272,287,1,0,0,0,273,
        274,10,12,0,0,274,275,7,0,0,0,275,286,3,58,29,13,276,277,10,11,0,
        0,277,278,7,1,0,0,278,286,3,58,29,12,279,280,10,10,0,0,280,281,7,
        2,0,0,281,286,3,58,29,11,282,283,10,9,0,0,283,284,7,3,0,0,284,286,
        3,58,29,10,285,273,1,0,0,0,285,276,1,0,0,0,285,279,1,0,0,0,285,282,
        1,0,0,0,286,289,1,0,0,0,287,285,1,0,0,0,287,288,1,0,0,0,288,59,1,
        0,0,0,289,287,1,0,0,0,21,64,72,74,98,105,114,120,131,134,146,178,
        181,189,198,218,227,235,247,271,285,287
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'field'", "'let'", "'len'", "'pop'", 
                     "'random'", "'if'", "'elif'", "'else'", "'return'", 
                     "'print'", "'for'", "'in'", "'while'", "'def'", "'procedure'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'>='", "'<'", "'<='", 
                     "'=='", "'!='", "'+='", "'-='", "'%'", "'and'", "'or'", 
                     "'not'", "'True'", "'False'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IF", "ELIF", "ELSE", "RETURN", 
                      "PRINT", "FOR", "IN", "WHILE", "DEF", "PROCEDURE", 
                      "PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", "LT", 
                      "LTE", "EQ", "NEQ", "PEQ", "MEQ", "MOD", "AND", "OR", 
                      "NOT", "TRUE", "FALSE", "COMMENT_SINGLELINE", "INT", 
                      "FLOAT", "STRING", "ID", "OPEN_PARENTH", "CLOSED_PARENTH", 
                      "OPEN_BRACK", "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", 
                      "COMMA", "DOT", "EQUAL_SIGN", "WS" ]

    RULE_prog = 0
    RULE_object = 1
    RULE_procedure = 2
    RULE_field = 3
    RULE_stat = 4
    RULE_varDeclStat = 5
    RULE_varDecl = 6
    RULE_assignStat = 7
    RULE_assignment = 8
    RULE_functionDecl = 9
    RULE_list = 10
    RULE_listElement = 11
    RULE_listLength = 12
    RULE_listPop = 13
    RULE_plusEquals = 14
    RULE_minusEquals = 15
    RULE_printStat = 16
    RULE_ifStat = 17
    RULE_elifStat = 18
    RULE_elseStat = 19
    RULE_statBlock = 20
    RULE_forLoop = 21
    RULE_whileLoop = 22
    RULE_functionCall = 23
    RULE_params = 24
    RULE_args = 25
    RULE_returnStat = 26
    RULE_random = 27
    RULE_range = 28
    RULE_expr = 29

    ruleNames =  [ "prog", "object", "procedure", "field", "stat", "varDeclStat", 
                   "varDecl", "assignStat", "assignment", "functionDecl", 
                   "list", "listElement", "listLength", "listPop", "plusEquals", 
                   "minusEquals", "printStat", "ifStat", "elifStat", "elseStat", 
                   "statBlock", "forLoop", "whileLoop", "functionCall", 
                   "params", "args", "returnStat", "random", "range", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    IF=6
    ELIF=7
    ELSE=8
    RETURN=9
    PRINT=10
    FOR=11
    IN=12
    WHILE=13
    DEF=14
    PROCEDURE=15
    PLUS=16
    MINUS=17
    MULT=18
    DIV=19
    GT=20
    GTE=21
    LT=22
    LTE=23
    EQ=24
    NEQ=25
    PEQ=26
    MEQ=27
    MOD=28
    AND=29
    OR=30
    NOT=31
    TRUE=32
    FALSE=33
    COMMENT_SINGLELINE=34
    INT=35
    FLOAT=36
    STRING=37
    ID=38
    OPEN_PARENTH=39
    CLOSED_PARENTH=40
    OPEN_BRACK=41
    CLOSED_BRACK=42
    OPEN_CURL=43
    CLOSED_CURL=44
    COMMA=45
    DOT=46
    EQUAL_SIGN=47
    WS=48

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
            self.state = 60
            self.object_()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9876277325420) != 0):
                self.state = 61
                self.stat()
                self.state = 66
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
            self.state = 67
            self.match(RogueLangParser.ID)
            self.state = 68
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 69
            self.procedure()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9876277325422) != 0):
                self.state = 72
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 70
                    self.field()
                    pass
                elif token in [2, 3, 5, 6, 9, 10, 11, 13, 14, 31, 32, 33, 35, 36, 37, 38, 39, 43]:
                    self.state = 71
                    self.stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
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
            self.state = 79
            self.match(RogueLangParser.PROCEDURE)
            self.state = 80
            self.statBlock()
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
        self.enterRule(localctx, 6, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(RogueLangParser.T__0)
            self.state = 83
            self.varDecl()
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


        def varDeclStat(self):
            return self.getTypedRuleContext(RogueLangParser.VarDeclStatContext,0)


        def assignStat(self):
            return self.getTypedRuleContext(RogueLangParser.AssignStatContext,0)


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


        def plusEquals(self):
            return self.getTypedRuleContext(RogueLangParser.PlusEqualsContext,0)


        def minusEquals(self):
            return self.getTypedRuleContext(RogueLangParser.MinusEqualsContext,0)


        def listPop(self):
            return self.getTypedRuleContext(RogueLangParser.ListPopContext,0)


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
        self.enterRule(localctx, 8, self.RULE_stat)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.varDeclStat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.assignStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.functionDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.ifStat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
                self.forLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 91
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 92
                self.statBlock()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 93
                self.returnStat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 94
                self.plusEquals()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 95
                self.minusEquals()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 96
                self.listPop()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 97
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(RogueLangParser.VarDeclContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_varDeclStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclStat" ):
                return visitor.visitVarDeclStat(self)
            else:
                return visitor.visitChildren(self)




    def varDeclStat(self):

        localctx = RogueLangParser.VarDeclStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDeclStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(RogueLangParser.T__1)
            self.state = 101
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

        def assignment(self):
            return self.getTypedRuleContext(RogueLangParser.AssignmentContext,0)


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
            self.state = 103
            self.match(RogueLangParser.ID)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 104
                self.assignment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def assignment(self):
            return self.getTypedRuleContext(RogueLangParser.AssignmentContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_assignStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStat" ):
                return visitor.visitAssignStat(self)
            else:
                return visitor.visitChildren(self)




    def assignStat(self):

        localctx = RogueLangParser.AssignStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(RogueLangParser.ID)
            self.state = 108
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(RogueLangParser.EQUAL_SIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def list_(self):
            return self.getTypedRuleContext(RogueLangParser.ListContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = RogueLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 111
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 113
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
        self.enterRule(localctx, 18, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(RogueLangParser.DEF)
            self.state = 117
            self.match(RogueLangParser.ID)
            self.state = 118
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 119
                self.params()


            self.state = 122
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 123
            self.statBlock()
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
        self.enterRule(localctx, 20, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(RogueLangParser.OPEN_BRACK)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080184274984) != 0):
                self.state = 126
                self.expr(0)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 127
                    self.match(RogueLangParser.COMMA)
                    self.state = 128
                    self.expr(0)
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 136
            self.match(RogueLangParser.CLOSED_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.ID)
            else:
                return self.getToken(RogueLangParser.ID, i)

        def OPEN_BRACK(self):
            return self.getToken(RogueLangParser.OPEN_BRACK, 0)

        def INT(self):
            return self.getToken(RogueLangParser.INT, 0)

        def CLOSED_BRACK(self):
            return self.getToken(RogueLangParser.CLOSED_BRACK, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_listElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListElement" ):
                return visitor.visitListElement(self)
            else:
                return visitor.visitChildren(self)




    def listElement(self):

        localctx = RogueLangParser.ListElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listElement)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(RogueLangParser.ID)
                self.state = 139
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 140
                self.match(RogueLangParser.INT)
                self.state = 141
                self.match(RogueLangParser.CLOSED_BRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(RogueLangParser.ID)
                self.state = 143
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 144
                self.match(RogueLangParser.ID)
                self.state = 145
                self.match(RogueLangParser.CLOSED_BRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListLengthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_listLength

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLength" ):
                return visitor.visitListLength(self)
            else:
                return visitor.visitChildren(self)




    def listLength(self):

        localctx = RogueLangParser.ListLengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_listLength)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(RogueLangParser.T__2)
            self.state = 149
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 150
            self.match(RogueLangParser.ID)
            self.state = 151
            self.match(RogueLangParser.CLOSED_PARENTH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListPopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def DOT(self):
            return self.getToken(RogueLangParser.DOT, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_listPop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListPop" ):
                return visitor.visitListPop(self)
            else:
                return visitor.visitChildren(self)




    def listPop(self):

        localctx = RogueLangParser.ListPopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_listPop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(RogueLangParser.ID)
            self.state = 154
            self.match(RogueLangParser.DOT)
            self.state = 155
            self.match(RogueLangParser.T__3)
            self.state = 156
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 157
            self.match(RogueLangParser.CLOSED_PARENTH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlusEqualsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def PEQ(self):
            return self.getToken(RogueLangParser.PEQ, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_plusEquals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusEquals" ):
                return visitor.visitPlusEquals(self)
            else:
                return visitor.visitChildren(self)




    def plusEquals(self):

        localctx = RogueLangParser.PlusEqualsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_plusEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(RogueLangParser.ID)
            self.state = 160
            self.match(RogueLangParser.PEQ)
            self.state = 161
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MinusEqualsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def MEQ(self):
            return self.getToken(RogueLangParser.MEQ, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_minusEquals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinusEquals" ):
                return visitor.visitMinusEquals(self)
            else:
                return visitor.visitChildren(self)




    def minusEquals(self):

        localctx = RogueLangParser.MinusEqualsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_minusEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(RogueLangParser.ID)
            self.state = 164
            self.match(RogueLangParser.MEQ)
            self.state = 165
            self.expr(0)
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
        self.enterRule(localctx, 32, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(RogueLangParser.PRINT)
            self.state = 168
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 169
            self.expr(0)
            self.state = 170
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
        self.enterRule(localctx, 34, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(RogueLangParser.IF)
            self.state = 173
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 174
            self.expr(0)
            self.state = 175
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 176
            self.statBlock()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 177
                self.elifStat()


            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 180
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
        self.enterRule(localctx, 36, self.RULE_elifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(RogueLangParser.ELIF)
            self.state = 184
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 185
            self.expr(0)
            self.state = 186
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 187
            self.statBlock()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 188
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
        self.enterRule(localctx, 38, self.RULE_elseStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(RogueLangParser.ELSE)
            self.state = 192
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
        self.enterRule(localctx, 40, self.RULE_statBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9876277325420) != 0):
                self.state = 195
                self.stat()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.ID)
            else:
                return self.getToken(RogueLangParser.ID, i)

        def IN(self):
            return self.getToken(RogueLangParser.IN, 0)

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
        self.enterRule(localctx, 42, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(RogueLangParser.FOR)
            self.state = 204
            self.match(RogueLangParser.ID)
            self.state = 205
            self.match(RogueLangParser.IN)
            self.state = 206
            self.match(RogueLangParser.ID)
            self.state = 207
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
        self.enterRule(localctx, 44, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(RogueLangParser.WHILE)
            self.state = 210
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 211
            self.expr(0)
            self.state = 212
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 213
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
        self.enterRule(localctx, 46, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(RogueLangParser.ID)
            self.state = 216
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080184274984) != 0):
                self.state = 217
                self.args()


            self.state = 220
            self.match(RogueLangParser.CLOSED_PARENTH)
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.ID)
            else:
                return self.getToken(RogueLangParser.ID, i)

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
        self.enterRule(localctx, 48, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(RogueLangParser.ID)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 223
                self.match(RogueLangParser.COMMA)
                self.state = 224
                self.match(RogueLangParser.ID)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 50, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.expr(0)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 231
                self.match(RogueLangParser.COMMA)
                self.state = 232
                self.expr(0)
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 52, self.RULE_returnStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(RogueLangParser.RETURN)
            self.state = 239
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RandomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(RogueLangParser.IN, 0)

        def range_(self):
            return self.getTypedRuleContext(RogueLangParser.RangeContext,0)


        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_random

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandom" ):
                return visitor.visitRandom(self)
            else:
                return visitor.visitChildren(self)




    def random(self):

        localctx = RogueLangParser.RandomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_random)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(RogueLangParser.T__4)
                self.state = 242
                self.match(RogueLangParser.IN)
                self.state = 243
                self.range_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(RogueLangParser.T__4)
                self.state = 245
                self.match(RogueLangParser.IN)
                self.state = 246
                self.match(RogueLangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.DOT)
            else:
                return self.getToken(RogueLangParser.DOT, i)

        def getRuleIndex(self):
            return RogueLangParser.RULE_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = RogueLangParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.expr(0)
            self.state = 250
            self.match(RogueLangParser.DOT)
            self.state = 251
            self.match(RogueLangParser.DOT)
            self.state = 252
            self.expr(0)
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


        def listElement(self):
            return self.getTypedRuleContext(RogueLangParser.ListElementContext,0)


        def listLength(self):
            return self.getTypedRuleContext(RogueLangParser.ListLengthContext,0)


        def random(self):
            return self.getTypedRuleContext(RogueLangParser.RandomContext,0)


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

        def INT(self):
            return self.getToken(RogueLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(RogueLangParser.FLOAT, 0)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 255
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 256
                self.listElement()
                pass

            elif la_ == 3:
                self.state = 257
                self.listLength()
                pass

            elif la_ == 4:
                self.state = 258
                self.random()
                pass

            elif la_ == 5:
                self.state = 259
                self.match(RogueLangParser.NOT)
                self.state = 260
                self.expr(8)
                pass

            elif la_ == 6:
                self.state = 261
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 262
                self.expr(0)
                self.state = 263
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 7:
                self.state = 265
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 8:
                self.state = 266
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 9:
                self.state = 267
                self.match(RogueLangParser.FLOAT)
                pass

            elif la_ == 10:
                self.state = 268
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 11:
                self.state = 269
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 12:
                self.state = 270
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 287
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 285
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 273
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 274
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 269221888) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 275
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 276
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 277
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 278
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 279
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 280
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 281
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 282
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 283
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==30):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 284
                        self.expr(10)
                        pass

             
                self.state = 289
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self._predicates[29] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         




