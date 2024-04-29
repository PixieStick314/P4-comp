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
        4,1,50,318,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,5,0,67,
        8,0,10,0,12,0,70,9,0,1,1,1,1,1,1,1,1,1,1,5,1,77,8,1,10,1,12,1,80,
        9,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,104,8,4,1,5,1,5,1,5,1,6,1,6,3,6,
        111,8,6,1,7,1,7,5,7,115,8,7,10,7,12,7,118,9,7,1,7,1,7,1,8,1,8,1,
        8,1,8,3,8,126,8,8,1,9,1,9,1,9,1,9,3,9,132,8,9,1,9,1,9,1,9,1,10,1,
        10,1,10,3,10,140,8,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,148,8,11,
        10,11,12,11,151,9,11,3,11,153,8,11,1,11,1,11,1,12,1,12,3,12,159,
        8,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,167,8,13,1,14,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,
        1,19,3,19,199,8,19,1,19,3,19,202,8,19,1,20,1,20,1,20,1,20,1,20,1,
        20,3,20,210,8,20,1,21,1,21,1,21,1,22,1,22,5,22,217,8,22,10,22,12,
        22,220,9,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,
        24,1,24,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,3,26,246,8,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,254,8,27,1,28,
        1,28,1,28,1,28,1,28,1,29,1,29,1,29,5,29,264,8,29,10,29,12,29,267,
        9,29,1,30,1,30,1,30,5,30,272,8,30,10,30,12,30,275,9,30,1,31,1,31,
        1,31,1,31,4,31,281,8,31,11,31,12,31,282,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,299,8,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,313,
        8,31,10,31,12,31,316,9,31,1,31,0,1,62,32,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        0,4,2,0,20,21,30,30,1,0,18,19,1,0,22,27,1,0,31,32,334,0,64,1,0,0,
        0,2,71,1,0,0,0,4,83,1,0,0,0,6,86,1,0,0,0,8,103,1,0,0,0,10,105,1,
        0,0,0,12,108,1,0,0,0,14,112,1,0,0,0,16,125,1,0,0,0,18,127,1,0,0,
        0,20,136,1,0,0,0,22,143,1,0,0,0,24,158,1,0,0,0,26,166,1,0,0,0,28,
        168,1,0,0,0,30,173,1,0,0,0,32,179,1,0,0,0,34,183,1,0,0,0,36,187,
        1,0,0,0,38,192,1,0,0,0,40,203,1,0,0,0,42,211,1,0,0,0,44,214,1,0,
        0,0,46,223,1,0,0,0,48,229,1,0,0,0,50,235,1,0,0,0,52,238,1,0,0,0,
        54,253,1,0,0,0,56,255,1,0,0,0,58,260,1,0,0,0,60,268,1,0,0,0,62,298,
        1,0,0,0,64,68,3,2,1,0,65,67,3,8,4,0,66,65,1,0,0,0,67,70,1,0,0,0,
        68,66,1,0,0,0,68,69,1,0,0,0,69,1,1,0,0,0,70,68,1,0,0,0,71,72,5,40,
        0,0,72,73,5,45,0,0,73,78,3,4,2,0,74,77,3,6,3,0,75,77,3,8,4,0,76,
        74,1,0,0,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,
        0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,5,46,0,0,82,3,1,0,0,0,83,84,
        5,17,0,0,84,85,3,44,22,0,85,5,1,0,0,0,86,87,5,1,0,0,87,88,3,12,6,
        0,88,7,1,0,0,0,89,104,3,36,18,0,90,104,3,10,5,0,91,104,3,14,7,0,
        92,104,3,18,9,0,93,104,3,38,19,0,94,104,3,46,23,0,95,104,3,48,24,
        0,96,104,3,44,22,0,97,104,3,50,25,0,98,104,3,32,16,0,99,104,3,34,
        17,0,100,104,3,30,15,0,101,104,3,52,26,0,102,104,3,62,31,0,103,89,
        1,0,0,0,103,90,1,0,0,0,103,91,1,0,0,0,103,92,1,0,0,0,103,93,1,0,
        0,0,103,94,1,0,0,0,103,95,1,0,0,0,103,96,1,0,0,0,103,97,1,0,0,0,
        103,98,1,0,0,0,103,99,1,0,0,0,103,100,1,0,0,0,103,101,1,0,0,0,103,
        102,1,0,0,0,104,9,1,0,0,0,105,106,5,2,0,0,106,107,3,12,6,0,107,11,
        1,0,0,0,108,110,5,40,0,0,109,111,3,16,8,0,110,109,1,0,0,0,110,111,
        1,0,0,0,111,13,1,0,0,0,112,116,5,40,0,0,113,115,3,26,13,0,114,113,
        1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,119,
        1,0,0,0,118,116,1,0,0,0,119,120,3,16,8,0,120,15,1,0,0,0,121,122,
        5,49,0,0,122,126,3,62,31,0,123,124,5,49,0,0,124,126,3,22,11,0,125,
        121,1,0,0,0,125,123,1,0,0,0,126,17,1,0,0,0,127,128,5,15,0,0,128,
        129,5,40,0,0,129,131,5,41,0,0,130,132,3,58,29,0,131,130,1,0,0,0,
        131,132,1,0,0,0,132,133,1,0,0,0,133,134,5,42,0,0,134,135,3,44,22,
        0,135,19,1,0,0,0,136,137,5,40,0,0,137,139,5,41,0,0,138,140,3,60,
        30,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,142,5,42,
        0,0,142,21,1,0,0,0,143,152,5,43,0,0,144,149,3,24,12,0,145,146,5,
        47,0,0,146,148,3,24,12,0,147,145,1,0,0,0,148,151,1,0,0,0,149,147,
        1,0,0,0,149,150,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,152,144,
        1,0,0,0,152,153,1,0,0,0,153,154,1,0,0,0,154,155,5,44,0,0,155,23,
        1,0,0,0,156,159,3,62,31,0,157,159,3,22,11,0,158,156,1,0,0,0,158,
        157,1,0,0,0,159,25,1,0,0,0,160,161,5,43,0,0,161,162,5,37,0,0,162,
        167,5,44,0,0,163,164,5,43,0,0,164,165,5,40,0,0,165,167,5,44,0,0,
        166,160,1,0,0,0,166,163,1,0,0,0,167,27,1,0,0,0,168,169,5,3,0,0,169,
        170,5,41,0,0,170,171,5,40,0,0,171,172,5,42,0,0,172,29,1,0,0,0,173,
        174,5,40,0,0,174,175,5,48,0,0,175,176,5,4,0,0,176,177,5,41,0,0,177,
        178,5,42,0,0,178,31,1,0,0,0,179,180,5,40,0,0,180,181,5,28,0,0,181,
        182,3,62,31,0,182,33,1,0,0,0,183,184,5,40,0,0,184,185,5,29,0,0,185,
        186,3,62,31,0,186,35,1,0,0,0,187,188,5,11,0,0,188,189,5,41,0,0,189,
        190,3,62,31,0,190,191,5,42,0,0,191,37,1,0,0,0,192,193,5,7,0,0,193,
        194,5,41,0,0,194,195,3,62,31,0,195,196,5,42,0,0,196,198,3,44,22,
        0,197,199,3,40,20,0,198,197,1,0,0,0,198,199,1,0,0,0,199,201,1,0,
        0,0,200,202,3,42,21,0,201,200,1,0,0,0,201,202,1,0,0,0,202,39,1,0,
        0,0,203,204,5,8,0,0,204,205,5,41,0,0,205,206,3,62,31,0,206,207,5,
        42,0,0,207,209,3,44,22,0,208,210,3,40,20,0,209,208,1,0,0,0,209,210,
        1,0,0,0,210,41,1,0,0,0,211,212,5,9,0,0,212,213,3,44,22,0,213,43,
        1,0,0,0,214,218,5,45,0,0,215,217,3,8,4,0,216,215,1,0,0,0,217,220,
        1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,221,1,0,0,0,220,218,
        1,0,0,0,221,222,5,46,0,0,222,45,1,0,0,0,223,224,5,12,0,0,224,225,
        5,40,0,0,225,226,5,13,0,0,226,227,5,40,0,0,227,228,3,44,22,0,228,
        47,1,0,0,0,229,230,5,14,0,0,230,231,5,41,0,0,231,232,3,62,31,0,232,
        233,5,42,0,0,233,234,3,44,22,0,234,49,1,0,0,0,235,236,5,10,0,0,236,
        237,3,62,31,0,237,51,1,0,0,0,238,239,5,5,0,0,239,240,5,41,0,0,240,
        241,5,40,0,0,241,242,5,47,0,0,242,243,3,56,28,0,243,245,5,42,0,0,
        244,246,5,16,0,0,245,244,1,0,0,0,245,246,1,0,0,0,246,53,1,0,0,0,
        247,248,5,6,0,0,248,249,5,13,0,0,249,254,3,56,28,0,250,251,5,6,0,
        0,251,252,5,13,0,0,252,254,5,40,0,0,253,247,1,0,0,0,253,250,1,0,
        0,0,254,55,1,0,0,0,255,256,3,62,31,0,256,257,5,48,0,0,257,258,5,
        48,0,0,258,259,3,62,31,0,259,57,1,0,0,0,260,265,5,40,0,0,261,262,
        5,47,0,0,262,264,5,40,0,0,263,261,1,0,0,0,264,267,1,0,0,0,265,263,
        1,0,0,0,265,266,1,0,0,0,266,59,1,0,0,0,267,265,1,0,0,0,268,273,3,
        62,31,0,269,270,5,47,0,0,270,272,3,62,31,0,271,269,1,0,0,0,272,275,
        1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,61,1,0,0,0,275,273,1,
        0,0,0,276,277,6,31,-1,0,277,299,3,20,10,0,278,280,5,40,0,0,279,281,
        3,26,13,0,280,279,1,0,0,0,281,282,1,0,0,0,282,280,1,0,0,0,282,283,
        1,0,0,0,283,299,1,0,0,0,284,299,3,28,14,0,285,299,3,54,27,0,286,
        287,5,33,0,0,287,299,3,62,31,8,288,289,5,41,0,0,289,290,3,62,31,
        0,290,291,5,42,0,0,291,299,1,0,0,0,292,299,5,40,0,0,293,299,5,37,
        0,0,294,299,5,38,0,0,295,299,5,39,0,0,296,299,5,34,0,0,297,299,5,
        35,0,0,298,276,1,0,0,0,298,278,1,0,0,0,298,284,1,0,0,0,298,285,1,
        0,0,0,298,286,1,0,0,0,298,288,1,0,0,0,298,292,1,0,0,0,298,293,1,
        0,0,0,298,294,1,0,0,0,298,295,1,0,0,0,298,296,1,0,0,0,298,297,1,
        0,0,0,299,314,1,0,0,0,300,301,10,12,0,0,301,302,7,0,0,0,302,313,
        3,62,31,13,303,304,10,11,0,0,304,305,7,1,0,0,305,313,3,62,31,12,
        306,307,10,10,0,0,307,308,7,2,0,0,308,313,3,62,31,11,309,310,10,
        9,0,0,310,311,7,3,0,0,311,313,3,62,31,10,312,300,1,0,0,0,312,303,
        1,0,0,0,312,306,1,0,0,0,312,309,1,0,0,0,313,316,1,0,0,0,314,312,
        1,0,0,0,314,315,1,0,0,0,315,63,1,0,0,0,316,314,1,0,0,0,25,68,76,
        78,103,110,116,125,131,139,149,152,158,166,198,201,209,218,245,253,
        265,273,282,298,312,314
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'field'", "'let'", "'len'", "'pop'", 
                     "'WhiteNoise'", "'random'", "'if'", "'elif'", "'else'", 
                     "'return'", "'print'", "'for'", "'in'", "'while'", 
                     "'def'", "'layer'", "'procedure'", "'+'", "'-'", "'*'", 
                     "'/'", "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", 
                     "'+='", "'-='", "'%'", "'and'", "'or'", "'not'", "'True'", 
                     "'False'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "','", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELIF", 
                      "ELSE", "RETURN", "PRINT", "FOR", "IN", "WHILE", "DEF", 
                      "LAYER", "PROCEDURE", "PLUS", "MINUS", "MULT", "DIV", 
                      "GT", "GTE", "LT", "LTE", "EQ", "NEQ", "PEQ", "MEQ", 
                      "MOD", "AND", "OR", "NOT", "TRUE", "FALSE", "COMMENT_SINGLELINE", 
                      "INT", "FLOAT", "STRING", "ID", "OPEN_PARENTH", "CLOSED_PARENTH", 
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
    RULE_functionCall = 10
    RULE_list = 11
    RULE_listElement = 12
    RULE_listAccess = 13
    RULE_listLength = 14
    RULE_listPop = 15
    RULE_plusEquals = 16
    RULE_minusEquals = 17
    RULE_printStat = 18
    RULE_ifStat = 19
    RULE_elifStat = 20
    RULE_elseStat = 21
    RULE_statBlock = 22
    RULE_forLoop = 23
    RULE_whileLoop = 24
    RULE_returnStat = 25
    RULE_whiteNoiseStat = 26
    RULE_random = 27
    RULE_range = 28
    RULE_params = 29
    RULE_args = 30
    RULE_expr = 31

    ruleNames =  [ "prog", "object", "procedure", "field", "stat", "varDeclStat", 
                   "varDecl", "assignStat", "assignment", "functionDecl", 
                   "functionCall", "list", "listElement", "listAccess", 
                   "listLength", "listPop", "plusEquals", "minusEquals", 
                   "printStat", "ifStat", "elifStat", "elseStat", "statBlock", 
                   "forLoop", "whileLoop", "returnStat", "whiteNoiseStat", 
                   "random", "range", "params", "args", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    IF=7
    ELIF=8
    ELSE=9
    RETURN=10
    PRINT=11
    FOR=12
    IN=13
    WHILE=14
    DEF=15
    LAYER=16
    PROCEDURE=17
    PLUS=18
    MINUS=19
    MULT=20
    DIV=21
    GT=22
    GTE=23
    LT=24
    LTE=25
    EQ=26
    NEQ=27
    PEQ=28
    MEQ=29
    MOD=30
    AND=31
    OR=32
    NOT=33
    TRUE=34
    FALSE=35
    COMMENT_SINGLELINE=36
    INT=37
    FLOAT=38
    STRING=39
    ID=40
    OPEN_PARENTH=41
    CLOSED_PARENTH=42
    OPEN_BRACK=43
    CLOSED_BRACK=44
    OPEN_CURL=45
    CLOSED_CURL=46
    COMMA=47
    DOT=48
    EQUAL_SIGN=49
    WS=50

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
            self.state = 64
            self.object_()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39505109245164) != 0):
                self.state = 65
                self.stat()
                self.state = 70
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
            self.state = 71
            self.match(RogueLangParser.ID)
            self.state = 72
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 73
            self.procedure()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39505109245166) != 0):
                self.state = 76
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 74
                    self.field()
                    pass
                elif token in [2, 3, 5, 6, 7, 10, 11, 12, 14, 15, 33, 34, 35, 37, 38, 39, 40, 41, 45]:
                    self.state = 75
                    self.stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
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
            self.state = 83
            self.match(RogueLangParser.PROCEDURE)
            self.state = 84
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
            self.state = 86
            self.match(RogueLangParser.T__0)
            self.state = 87
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


        def whiteNoiseStat(self):
            return self.getTypedRuleContext(RogueLangParser.WhiteNoiseStatContext,0)


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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.varDeclStat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.assignStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.functionDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.ifStat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.forLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 95
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 96
                self.statBlock()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 97
                self.returnStat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 98
                self.plusEquals()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 99
                self.minusEquals()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 100
                self.listPop()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 101
                self.whiteNoiseStat()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 102
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
            self.state = 105
            self.match(RogueLangParser.T__1)
            self.state = 106
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
            self.state = 108
            self.match(RogueLangParser.ID)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 109
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


        def listAccess(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ListAccessContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ListAccessContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(RogueLangParser.ID)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 113
                self.listAccess()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
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
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 122
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 124
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
            self.state = 127
            self.match(RogueLangParser.DEF)
            self.state = 128
            self.match(RogueLangParser.ID)
            self.state = 129
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 130
                self.params()


            self.state = 133
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 134
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
        self.enterRule(localctx, 20, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(RogueLangParser.ID)
            self.state = 137
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4320737099848) != 0):
                self.state = 138
                self.args()


            self.state = 141
            self.match(RogueLangParser.CLOSED_PARENTH)
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

        def listElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ListElementContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ListElementContext,i)


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
        self.enterRule(localctx, 22, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(RogueLangParser.OPEN_BRACK)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 13116830122056) != 0):
                self.state = 144
                self.listElement()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==47:
                    self.state = 145
                    self.match(RogueLangParser.COMMA)
                    self.state = 146
                    self.listElement()
                    self.state = 151
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 154
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

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def list_(self):
            return self.getTypedRuleContext(RogueLangParser.ListContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_listElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListElement" ):
                return visitor.visitListElement(self)
            else:
                return visitor.visitChildren(self)




    def listElement(self):

        localctx = RogueLangParser.ListElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_listElement)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 6, 33, 34, 35, 37, 38, 39, 40, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.expr(0)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.list_()
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


    class ListAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACK(self):
            return self.getToken(RogueLangParser.OPEN_BRACK, 0)

        def INT(self):
            return self.getToken(RogueLangParser.INT, 0)

        def CLOSED_BRACK(self):
            return self.getToken(RogueLangParser.CLOSED_BRACK, 0)

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_listAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListAccess" ):
                return visitor.visitListAccess(self)
            else:
                return visitor.visitChildren(self)




    def listAccess(self):

        localctx = RogueLangParser.ListAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_listAccess)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 161
                self.match(RogueLangParser.INT)
                self.state = 162
                self.match(RogueLangParser.CLOSED_BRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 164
                self.match(RogueLangParser.ID)
                self.state = 165
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
        self.enterRule(localctx, 28, self.RULE_listLength)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(RogueLangParser.T__2)
            self.state = 169
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 170
            self.match(RogueLangParser.ID)
            self.state = 171
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
        self.enterRule(localctx, 30, self.RULE_listPop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(RogueLangParser.ID)
            self.state = 174
            self.match(RogueLangParser.DOT)
            self.state = 175
            self.match(RogueLangParser.T__3)
            self.state = 176
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 177
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
        self.enterRule(localctx, 32, self.RULE_plusEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(RogueLangParser.ID)
            self.state = 180
            self.match(RogueLangParser.PEQ)
            self.state = 181
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
        self.enterRule(localctx, 34, self.RULE_minusEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(RogueLangParser.ID)
            self.state = 184
            self.match(RogueLangParser.MEQ)
            self.state = 185
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
        self.enterRule(localctx, 36, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(RogueLangParser.PRINT)
            self.state = 188
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 189
            self.expr(0)
            self.state = 190
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
        self.enterRule(localctx, 38, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(RogueLangParser.IF)
            self.state = 193
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 194
            self.expr(0)
            self.state = 195
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 196
            self.statBlock()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 197
                self.elifStat()


            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 200
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
        self.enterRule(localctx, 40, self.RULE_elifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(RogueLangParser.ELIF)
            self.state = 204
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 205
            self.expr(0)
            self.state = 206
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 207
            self.statBlock()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 208
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
        self.enterRule(localctx, 42, self.RULE_elseStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(RogueLangParser.ELSE)
            self.state = 212
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
        self.enterRule(localctx, 44, self.RULE_statBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39505109245164) != 0):
                self.state = 215
                self.stat()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
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
        self.enterRule(localctx, 46, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(RogueLangParser.FOR)
            self.state = 224
            self.match(RogueLangParser.ID)
            self.state = 225
            self.match(RogueLangParser.IN)
            self.state = 226
            self.match(RogueLangParser.ID)
            self.state = 227
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
        self.enterRule(localctx, 48, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(RogueLangParser.WHILE)
            self.state = 230
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 231
            self.expr(0)
            self.state = 232
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 233
            self.statBlock()
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
        self.enterRule(localctx, 50, self.RULE_returnStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(RogueLangParser.RETURN)
            self.state = 236
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhiteNoiseStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.arrayParam = None # Token
            self.rangeParam = None # RangeContext

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def COMMA(self):
            return self.getToken(RogueLangParser.COMMA, 0)

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def range_(self):
            return self.getTypedRuleContext(RogueLangParser.RangeContext,0)


        def LAYER(self):
            return self.getToken(RogueLangParser.LAYER, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_whiteNoiseStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhiteNoiseStat" ):
                return visitor.visitWhiteNoiseStat(self)
            else:
                return visitor.visitChildren(self)




    def whiteNoiseStat(self):

        localctx = RogueLangParser.WhiteNoiseStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_whiteNoiseStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(RogueLangParser.T__4)
            self.state = 239
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 240
            localctx.arrayParam = self.match(RogueLangParser.ID)
            self.state = 241
            self.match(RogueLangParser.COMMA)
            self.state = 242
            localctx.rangeParam = self.range_()
            self.state = 243
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 244
                self.match(RogueLangParser.LAYER)


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
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(RogueLangParser.T__5)
                self.state = 248
                self.match(RogueLangParser.IN)
                self.state = 249
                self.range_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(RogueLangParser.T__5)
                self.state = 251
                self.match(RogueLangParser.IN)
                self.state = 252
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
            self.state = 255
            self.expr(0)
            self.state = 256
            self.match(RogueLangParser.DOT)
            self.state = 257
            self.match(RogueLangParser.DOT)
            self.state = 258
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
        self.enterRule(localctx, 58, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(RogueLangParser.ID)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 261
                self.match(RogueLangParser.COMMA)
                self.state = 262
                self.match(RogueLangParser.ID)
                self.state = 267
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
        self.enterRule(localctx, 60, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.expr(0)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 269
                self.match(RogueLangParser.COMMA)
                self.state = 270
                self.expr(0)
                self.state = 275
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


        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def listAccess(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ListAccessContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ListAccessContext,i)


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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 277
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 278
                self.match(RogueLangParser.ID)
                self.state = 280 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 279
                        self.listAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 282 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass

            elif la_ == 3:
                self.state = 284
                self.listLength()
                pass

            elif la_ == 4:
                self.state = 285
                self.random()
                pass

            elif la_ == 5:
                self.state = 286
                self.match(RogueLangParser.NOT)
                self.state = 287
                self.expr(8)
                pass

            elif la_ == 6:
                self.state = 288
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 289
                self.expr(0)
                self.state = 290
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 7:
                self.state = 292
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 8:
                self.state = 293
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 9:
                self.state = 294
                self.match(RogueLangParser.FLOAT)
                pass

            elif la_ == 10:
                self.state = 295
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 11:
                self.state = 296
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 12:
                self.state = 297
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 312
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 300
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 301
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1076887552) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 302
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 303
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 304
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 305
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 306
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 307
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 308
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 309
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 310
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==31 or _la==32):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 311
                        self.expr(10)
                        pass

             
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        self._predicates[31] = self.expr_sempred
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
         




