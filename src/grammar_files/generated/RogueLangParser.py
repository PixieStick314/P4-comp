# Generated from C:/Users/nedim/Documents/GitHub/P4-comp/src/grammar_files/RogueLang.g4 by ANTLR 4.13.1
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
        4,1,52,315,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,5,0,65,8,0,10,0,
        12,0,68,9,0,1,1,1,1,1,1,1,1,1,1,5,1,75,8,1,10,1,12,1,78,9,1,1,1,
        1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,3,4,102,8,4,1,5,1,5,1,5,1,6,1,6,3,6,109,8,6,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,118,8,8,1,9,1,9,1,9,1,9,3,9,124,
        8,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,132,8,10,1,10,1,10,1,11,1,11,
        1,11,1,11,5,11,140,8,11,10,11,12,11,143,9,11,3,11,145,8,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,157,8,12,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,
        1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,
        1,18,1,18,1,18,3,18,189,8,18,1,18,3,18,192,8,18,1,19,1,19,1,19,1,
        19,1,19,1,19,3,19,200,8,19,1,20,1,20,1,20,1,21,1,21,5,21,207,8,21,
        10,21,12,21,210,9,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,
        1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,3,25,236,8,25,1,26,1,26,1,26,1,26,1,26,1,26,3,26,244,8,
        26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,5,28,254,8,28,10,28,12,
        28,257,9,28,1,29,1,29,1,29,5,29,262,8,29,10,29,12,29,265,9,29,1,
        30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,
        30,1,30,1,30,3,30,296,8,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,5,30,310,8,30,10,30,12,30,313,9,30,1,30,0,
        1,60,31,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,0,4,2,0,20,21,30,30,1,0,18,19,1,0,
        22,27,1,0,31,32,331,0,62,1,0,0,0,2,69,1,0,0,0,4,81,1,0,0,0,6,84,
        1,0,0,0,8,101,1,0,0,0,10,103,1,0,0,0,12,106,1,0,0,0,14,110,1,0,0,
        0,16,117,1,0,0,0,18,119,1,0,0,0,20,128,1,0,0,0,22,135,1,0,0,0,24,
        156,1,0,0,0,26,158,1,0,0,0,28,163,1,0,0,0,30,169,1,0,0,0,32,173,
        1,0,0,0,34,177,1,0,0,0,36,182,1,0,0,0,38,193,1,0,0,0,40,201,1,0,
        0,0,42,204,1,0,0,0,44,213,1,0,0,0,46,219,1,0,0,0,48,225,1,0,0,0,
        50,228,1,0,0,0,52,243,1,0,0,0,54,245,1,0,0,0,56,250,1,0,0,0,58,258,
        1,0,0,0,60,295,1,0,0,0,62,66,3,2,1,0,63,65,3,8,4,0,64,63,1,0,0,0,
        65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,1,1,0,0,0,68,66,1,0,
        0,0,69,70,5,42,0,0,70,71,5,47,0,0,71,76,3,4,2,0,72,75,3,6,3,0,73,
        75,3,8,4,0,74,72,1,0,0,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,
        0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,48,0,0,80,3,
        1,0,0,0,81,82,5,17,0,0,82,83,3,42,21,0,83,5,1,0,0,0,84,85,5,1,0,
        0,85,86,3,12,6,0,86,7,1,0,0,0,87,102,3,34,17,0,88,102,3,10,5,0,89,
        102,3,14,7,0,90,102,3,18,9,0,91,102,3,36,18,0,92,102,3,44,22,0,93,
        102,3,46,23,0,94,102,3,42,21,0,95,102,3,48,24,0,96,102,3,30,15,0,
        97,102,3,32,16,0,98,102,3,28,14,0,99,102,3,50,25,0,100,102,3,60,
        30,0,101,87,1,0,0,0,101,88,1,0,0,0,101,89,1,0,0,0,101,90,1,0,0,0,
        101,91,1,0,0,0,101,92,1,0,0,0,101,93,1,0,0,0,101,94,1,0,0,0,101,
        95,1,0,0,0,101,96,1,0,0,0,101,97,1,0,0,0,101,98,1,0,0,0,101,99,1,
        0,0,0,101,100,1,0,0,0,102,9,1,0,0,0,103,104,5,2,0,0,104,105,3,12,
        6,0,105,11,1,0,0,0,106,108,5,42,0,0,107,109,3,16,8,0,108,107,1,0,
        0,0,108,109,1,0,0,0,109,13,1,0,0,0,110,111,5,42,0,0,111,112,3,16,
        8,0,112,15,1,0,0,0,113,114,5,51,0,0,114,118,3,60,30,0,115,116,5,
        51,0,0,116,118,3,22,11,0,117,113,1,0,0,0,117,115,1,0,0,0,118,17,
        1,0,0,0,119,120,5,15,0,0,120,121,5,42,0,0,121,123,5,43,0,0,122,124,
        3,56,28,0,123,122,1,0,0,0,123,124,1,0,0,0,124,125,1,0,0,0,125,126,
        5,44,0,0,126,127,3,42,21,0,127,19,1,0,0,0,128,129,5,42,0,0,129,131,
        5,43,0,0,130,132,3,58,29,0,131,130,1,0,0,0,131,132,1,0,0,0,132,133,
        1,0,0,0,133,134,5,44,0,0,134,21,1,0,0,0,135,144,5,45,0,0,136,141,
        3,60,30,0,137,138,5,49,0,0,138,140,3,60,30,0,139,137,1,0,0,0,140,
        143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,145,1,0,0,0,143,
        141,1,0,0,0,144,136,1,0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,
        147,5,46,0,0,147,23,1,0,0,0,148,149,5,42,0,0,149,150,5,45,0,0,150,
        151,5,39,0,0,151,157,5,46,0,0,152,153,5,42,0,0,153,154,5,45,0,0,
        154,155,5,42,0,0,155,157,5,46,0,0,156,148,1,0,0,0,156,152,1,0,0,
        0,157,25,1,0,0,0,158,159,5,3,0,0,159,160,5,43,0,0,160,161,5,42,0,
        0,161,162,5,44,0,0,162,27,1,0,0,0,163,164,5,42,0,0,164,165,5,50,
        0,0,165,166,5,4,0,0,166,167,5,43,0,0,167,168,5,44,0,0,168,29,1,0,
        0,0,169,170,5,42,0,0,170,171,5,28,0,0,171,172,3,60,30,0,172,31,1,
        0,0,0,173,174,5,42,0,0,174,175,5,29,0,0,175,176,3,60,30,0,176,33,
        1,0,0,0,177,178,5,11,0,0,178,179,5,43,0,0,179,180,3,60,30,0,180,
        181,5,44,0,0,181,35,1,0,0,0,182,183,5,7,0,0,183,184,5,43,0,0,184,
        185,3,60,30,0,185,186,5,44,0,0,186,188,3,42,21,0,187,189,3,38,19,
        0,188,187,1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,192,3,40,20,
        0,191,190,1,0,0,0,191,192,1,0,0,0,192,37,1,0,0,0,193,194,5,8,0,0,
        194,195,5,43,0,0,195,196,3,60,30,0,196,197,5,44,0,0,197,199,3,42,
        21,0,198,200,3,38,19,0,199,198,1,0,0,0,199,200,1,0,0,0,200,39,1,
        0,0,0,201,202,5,9,0,0,202,203,3,42,21,0,203,41,1,0,0,0,204,208,5,
        47,0,0,205,207,3,8,4,0,206,205,1,0,0,0,207,210,1,0,0,0,208,206,1,
        0,0,0,208,209,1,0,0,0,209,211,1,0,0,0,210,208,1,0,0,0,211,212,5,
        48,0,0,212,43,1,0,0,0,213,214,5,12,0,0,214,215,5,42,0,0,215,216,
        5,13,0,0,216,217,5,42,0,0,217,218,3,42,21,0,218,45,1,0,0,0,219,220,
        5,14,0,0,220,221,5,43,0,0,221,222,3,60,30,0,222,223,5,44,0,0,223,
        224,3,42,21,0,224,47,1,0,0,0,225,226,5,10,0,0,226,227,3,60,30,0,
        227,49,1,0,0,0,228,229,5,5,0,0,229,230,5,43,0,0,230,231,5,42,0,0,
        231,232,5,49,0,0,232,233,3,54,27,0,233,235,5,44,0,0,234,236,5,16,
        0,0,235,234,1,0,0,0,235,236,1,0,0,0,236,51,1,0,0,0,237,238,5,6,0,
        0,238,239,5,13,0,0,239,244,3,54,27,0,240,241,5,6,0,0,241,242,5,13,
        0,0,242,244,5,42,0,0,243,237,1,0,0,0,243,240,1,0,0,0,244,53,1,0,
        0,0,245,246,3,60,30,0,246,247,5,50,0,0,247,248,5,50,0,0,248,249,
        3,60,30,0,249,55,1,0,0,0,250,255,5,42,0,0,251,252,5,49,0,0,252,254,
        5,42,0,0,253,251,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,
        1,0,0,0,256,57,1,0,0,0,257,255,1,0,0,0,258,263,3,60,30,0,259,260,
        5,49,0,0,260,262,3,60,30,0,261,259,1,0,0,0,262,265,1,0,0,0,263,261,
        1,0,0,0,263,264,1,0,0,0,264,59,1,0,0,0,265,263,1,0,0,0,266,267,6,
        30,-1,0,267,296,3,20,10,0,268,296,3,24,12,0,269,296,3,26,13,0,270,
        296,3,52,26,0,271,272,5,33,0,0,272,296,3,60,30,10,273,274,5,36,0,
        0,274,275,5,43,0,0,275,276,3,60,30,0,276,277,5,44,0,0,277,296,1,
        0,0,0,278,279,5,37,0,0,279,280,5,43,0,0,280,281,3,60,30,0,281,282,
        5,49,0,0,282,283,3,60,30,0,283,284,5,44,0,0,284,296,1,0,0,0,285,
        286,5,43,0,0,286,287,3,60,30,0,287,288,5,44,0,0,288,296,1,0,0,0,
        289,296,5,42,0,0,290,296,5,39,0,0,291,296,5,40,0,0,292,296,5,41,
        0,0,293,296,5,34,0,0,294,296,5,35,0,0,295,266,1,0,0,0,295,268,1,
        0,0,0,295,269,1,0,0,0,295,270,1,0,0,0,295,271,1,0,0,0,295,273,1,
        0,0,0,295,278,1,0,0,0,295,285,1,0,0,0,295,289,1,0,0,0,295,290,1,
        0,0,0,295,291,1,0,0,0,295,292,1,0,0,0,295,293,1,0,0,0,295,294,1,
        0,0,0,296,311,1,0,0,0,297,298,10,14,0,0,298,299,7,0,0,0,299,310,
        3,60,30,15,300,301,10,13,0,0,301,302,7,1,0,0,302,310,3,60,30,14,
        303,304,10,12,0,0,304,305,7,2,0,0,305,310,3,60,30,13,306,307,10,
        11,0,0,307,308,7,3,0,0,308,310,3,60,30,12,309,297,1,0,0,0,309,300,
        1,0,0,0,309,303,1,0,0,0,309,306,1,0,0,0,310,313,1,0,0,0,311,309,
        1,0,0,0,311,312,1,0,0,0,312,61,1,0,0,0,313,311,1,0,0,0,22,66,74,
        76,101,108,117,123,131,141,144,156,188,191,199,208,235,243,255,263,
        295,309,311
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
                     "'False'", "'sqrt'", "'pow'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELIF", 
                      "ELSE", "RETURN", "PRINT", "FOR", "IN", "WHILE", "DEF", 
                      "LAYER", "PROCEDURE", "PLUS", "MINUS", "MULT", "DIV", 
                      "GT", "GTE", "LT", "LTE", "EQ", "NEQ", "PEQ", "MEQ", 
                      "MOD", "AND", "OR", "NOT", "TRUE", "FALSE", "SQRT", 
                      "POW", "COMMENT_SINGLELINE", "INT", "FLOAT", "STRING", 
                      "ID", "OPEN_PARENTH", "CLOSED_PARENTH", "OPEN_BRACK", 
                      "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", "COMMA", 
                      "DOT", "EQUAL_SIGN", "WS" ]

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
    SQRT=36
    POW=37
    COMMENT_SINGLELINE=38
    INT=39
    FLOAT=40
    STRING=41
    ID=42
    OPEN_PARENTH=43
    CLOSED_PARENTH=44
    OPEN_BRACK=45
    CLOSED_BRACK=46
    OPEN_CURL=47
    CLOSED_CURL=48
    COMMA=49
    DOT=50
    EQUAL_SIGN=51
    WS=52

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 158046206614764) != 0):
                self.state = 63
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 158046206614766) != 0):
                self.state = 74
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 74
                    self.field()
                    pass
                elif token in [2, 3, 5, 6, 7, 10, 11, 12, 14, 15, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 47]:
                    self.state = 73
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
            if _la==51:
                self.state = 107
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
            if _la==42:
                self.state = 122
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17308718202952) != 0):
                self.state = 130
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17308718202952) != 0):
                self.state = 136
                self.expr(0)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==49:
                    self.state = 137
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 158046206614764) != 0):
                self.state = 205
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

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def COMMA(self):
            return self.getToken(RogueLangParser.COMMA, 0)

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
            self.match(RogueLangParser.ID)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 241
                self.match(RogueLangParser.COMMA)
                self.state = 242
                self.range_()


            self.state = 245
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 246
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
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(RogueLangParser.T__5)
                self.state = 250
                self.match(RogueLangParser.IN)
                self.state = 251
                self.range_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.match(RogueLangParser.T__5)
                self.state = 253
                self.match(RogueLangParser.IN)
                self.state = 254
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
            self.state = 257
            self.expr(0)
            self.state = 258
            self.match(RogueLangParser.DOT)
            self.state = 259
            self.match(RogueLangParser.DOT)
            self.state = 260
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
            self.state = 262
            self.match(RogueLangParser.ID)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 251
                self.match(RogueLangParser.COMMA)
                self.state = 264
                self.match(RogueLangParser.ID)
                self.state = 269
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
            self.state = 270
            self.expr(0)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 259
                self.match(RogueLangParser.COMMA)
                self.state = 272
                self.expr(0)
                self.state = 277
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


        def SQRT(self):
            return self.getToken(RogueLangParser.SQRT, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def POW(self):
            return self.getToken(RogueLangParser.POW, 0)

        def COMMA(self):
            return self.getToken(RogueLangParser.COMMA, 0)

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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 279
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 280
                self.match(RogueLangParser.ID)
                self.state = 282 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 281
                        self.listAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 284 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass

            elif la_ == 3:
                self.state = 286
                self.listLength()
                pass

            elif la_ == 4:
                self.state = 287
                self.random()
                pass

            elif la_ == 5:
                self.state = 288
                self.match(RogueLangParser.NOT)
                self.state = 272
                self.expr(10)
                pass

            elif la_ == 6:
                self.state = 273
                self.match(RogueLangParser.SQRT)
                self.state = 274
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 275
                self.expr(0)
                self.state = 276
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 7:
                self.state = 278
                self.match(RogueLangParser.POW)
                self.state = 279
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 280
                self.expr(0)
                self.state = 281
                self.match(RogueLangParser.COMMA)
                self.state = 282
                self.expr(0)
                self.state = 283
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 8:
                self.state = 285
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 286
                self.expr(0)
                self.state = 287
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 9:
                self.state = 289
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 10:
                self.state = 290
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 11:
                self.state = 291
                self.match(RogueLangParser.FLOAT)
                pass

            elif la_ == 12:
                self.state = 292
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 13:
                self.state = 293
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 14:
                self.state = 294
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 309
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 297
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 298
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1076887552) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 299
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 300
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 301
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 302
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 303
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 304
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 305
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 306
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 307
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==31 or _la==32):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 308
                        self.expr(12)
                        pass

             
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         




