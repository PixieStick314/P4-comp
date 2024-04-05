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
        4,1,50,344,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,4,0,64,8,0,11,0,12,0,
        65,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,78,8,1,1,2,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,90,8,3,1,4,1,4,1,4,3,4,95,8,4,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,5,6,114,8,6,10,6,12,6,117,9,6,1,6,1,6,1,6,1,6,1,6,3,6,124,8,
        6,1,7,1,7,1,8,5,8,129,8,8,10,8,12,8,132,9,8,1,9,1,9,1,10,5,10,137,
        8,10,10,10,12,10,140,9,10,1,11,5,11,143,8,11,10,11,12,11,146,9,11,
        1,12,1,12,1,12,1,12,1,12,1,12,5,12,154,8,12,10,12,12,12,157,9,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,167,8,13,10,13,12,13,
        170,9,13,1,13,1,13,1,14,1,14,1,14,1,14,3,14,178,8,14,1,14,1,14,1,
        14,5,14,183,8,14,10,14,12,14,186,9,14,1,14,1,14,1,15,1,15,1,15,3,
        15,193,8,15,1,15,3,15,196,8,15,1,15,1,15,1,16,1,16,1,16,1,16,5,16,
        204,8,16,10,16,12,16,207,9,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,
        1,18,1,18,5,18,218,8,18,10,18,12,18,221,9,18,1,19,1,19,1,20,1,20,
        1,20,5,20,228,8,20,10,20,12,20,231,9,20,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,22,1,22,1,22,1,22,1,22,4,22,245,8,22,11,22,12,22,246,
        1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,5,24,260,
        8,24,10,24,12,24,263,9,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,
        3,26,273,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,5,28,
        284,8,28,10,28,12,28,287,9,28,1,29,1,29,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,306,8,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,5,30,339,8,30,10,30,12,30,342,9,30,1,30,
        0,1,60,31,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,0,5,3,0,1,3,35,36,40,40,2,0,23,
        24,31,31,1,0,21,22,1,0,25,30,1,0,32,33,361,0,63,1,0,0,0,2,77,1,0,
        0,0,4,79,1,0,0,0,6,84,1,0,0,0,8,91,1,0,0,0,10,96,1,0,0,0,12,98,1,
        0,0,0,14,125,1,0,0,0,16,130,1,0,0,0,18,133,1,0,0,0,20,138,1,0,0,
        0,22,144,1,0,0,0,24,147,1,0,0,0,26,160,1,0,0,0,28,173,1,0,0,0,30,
        189,1,0,0,0,32,199,1,0,0,0,34,210,1,0,0,0,36,214,1,0,0,0,38,222,
        1,0,0,0,40,224,1,0,0,0,42,232,1,0,0,0,44,239,1,0,0,0,46,250,1,0,
        0,0,48,256,1,0,0,0,50,264,1,0,0,0,52,272,1,0,0,0,54,274,1,0,0,0,
        56,280,1,0,0,0,58,288,1,0,0,0,60,305,1,0,0,0,62,64,3,2,1,0,63,62,
        1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,1,1,0,0,0,67,
        78,3,4,2,0,68,78,3,6,3,0,69,78,3,12,6,0,70,78,3,24,12,0,71,78,3,
        26,13,0,72,78,3,28,14,0,73,78,3,30,15,0,74,78,3,32,16,0,75,78,3,
        46,23,0,76,78,3,60,30,0,77,67,1,0,0,0,77,68,1,0,0,0,77,69,1,0,0,
        0,77,70,1,0,0,0,77,71,1,0,0,0,77,72,1,0,0,0,77,73,1,0,0,0,77,74,
        1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,3,1,0,0,0,79,80,5,13,0,0,
        80,81,5,41,0,0,81,82,3,60,30,0,82,83,5,42,0,0,83,5,1,0,0,0,84,89,
        5,40,0,0,85,86,5,49,0,0,86,90,3,60,30,0,87,90,3,32,16,0,88,90,3,
        40,20,0,89,85,1,0,0,0,89,87,1,0,0,0,89,88,1,0,0,0,89,90,1,0,0,0,
        90,7,1,0,0,0,91,94,3,10,5,0,92,93,5,43,0,0,93,95,5,44,0,0,94,92,
        1,0,0,0,94,95,1,0,0,0,95,9,1,0,0,0,96,97,7,0,0,0,97,11,1,0,0,0,98,
        99,5,9,0,0,99,100,5,41,0,0,100,101,3,14,7,0,101,102,5,42,0,0,102,
        103,5,45,0,0,103,104,3,16,8,0,104,115,5,46,0,0,105,106,5,10,0,0,
        106,107,5,41,0,0,107,108,3,18,9,0,108,109,5,42,0,0,109,110,5,45,
        0,0,110,111,3,20,10,0,111,112,5,46,0,0,112,114,1,0,0,0,113,105,1,
        0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,123,1,
        0,0,0,117,115,1,0,0,0,118,119,5,11,0,0,119,120,5,45,0,0,120,121,
        3,22,11,0,121,122,5,46,0,0,122,124,1,0,0,0,123,118,1,0,0,0,123,124,
        1,0,0,0,124,13,1,0,0,0,125,126,3,60,30,0,126,15,1,0,0,0,127,129,
        3,2,1,0,128,127,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,
        1,0,0,0,131,17,1,0,0,0,132,130,1,0,0,0,133,134,3,60,30,0,134,19,
        1,0,0,0,135,137,3,2,1,0,136,135,1,0,0,0,137,140,1,0,0,0,138,136,
        1,0,0,0,138,139,1,0,0,0,139,21,1,0,0,0,140,138,1,0,0,0,141,143,3,
        2,1,0,142,141,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,
        0,0,0,145,23,1,0,0,0,146,144,1,0,0,0,147,148,5,14,0,0,148,149,3,
        6,3,0,149,150,5,15,0,0,150,151,3,60,30,0,151,155,5,45,0,0,152,154,
        3,2,1,0,153,152,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,
        1,0,0,0,156,158,1,0,0,0,157,155,1,0,0,0,158,159,5,46,0,0,159,25,
        1,0,0,0,160,161,5,16,0,0,161,162,5,41,0,0,162,163,3,60,30,0,163,
        164,5,42,0,0,164,168,5,45,0,0,165,167,3,2,1,0,166,165,1,0,0,0,167,
        170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,171,1,0,0,0,170,
        168,1,0,0,0,171,172,5,46,0,0,172,27,1,0,0,0,173,174,5,17,0,0,174,
        175,5,40,0,0,175,177,5,41,0,0,176,178,3,36,18,0,177,176,1,0,0,0,
        177,178,1,0,0,0,178,179,1,0,0,0,179,180,5,42,0,0,180,184,5,45,0,
        0,181,183,3,2,1,0,182,181,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,
        0,184,185,1,0,0,0,185,187,1,0,0,0,186,184,1,0,0,0,187,188,5,46,0,
        0,188,29,1,0,0,0,189,190,5,40,0,0,190,192,5,41,0,0,191,193,3,40,
        20,0,192,191,1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,0,194,196,5,12,
        0,0,195,194,1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,197,198,5,42,
        0,0,198,31,1,0,0,0,199,200,5,45,0,0,200,205,3,60,30,0,201,202,5,
        47,0,0,202,204,3,60,30,0,203,201,1,0,0,0,204,207,1,0,0,0,205,203,
        1,0,0,0,205,206,1,0,0,0,206,208,1,0,0,0,207,205,1,0,0,0,208,209,
        5,46,0,0,209,33,1,0,0,0,210,211,5,4,0,0,211,212,3,52,26,0,212,213,
        3,54,27,0,213,35,1,0,0,0,214,219,3,38,19,0,215,216,5,47,0,0,216,
        218,3,38,19,0,217,215,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,
        220,1,0,0,0,220,37,1,0,0,0,221,219,1,0,0,0,222,223,5,40,0,0,223,
        39,1,0,0,0,224,229,3,60,30,0,225,226,5,47,0,0,226,228,3,60,30,0,
        227,225,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,
        230,41,1,0,0,0,231,229,1,0,0,0,232,233,5,18,0,0,233,234,5,41,0,0,
        234,235,5,38,0,0,235,236,5,47,0,0,236,237,5,38,0,0,237,238,5,42,
        0,0,238,43,1,0,0,0,239,240,5,19,0,0,240,241,5,41,0,0,241,244,3,60,
        30,0,242,243,5,47,0,0,243,245,3,60,30,0,244,242,1,0,0,0,245,246,
        1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,248,1,0,0,0,248,249,
        5,42,0,0,249,45,1,0,0,0,250,251,5,20,0,0,251,252,5,40,0,0,252,253,
        5,45,0,0,253,254,3,48,24,0,254,255,5,46,0,0,255,47,1,0,0,0,256,261,
        5,40,0,0,257,258,5,47,0,0,258,260,5,40,0,0,259,257,1,0,0,0,260,263,
        1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,49,1,0,0,0,263,261,1,
        0,0,0,264,265,5,40,0,0,265,266,5,48,0,0,266,267,5,40,0,0,267,51,
        1,0,0,0,268,273,5,5,0,0,269,273,5,6,0,0,270,271,5,38,0,0,271,273,
        5,7,0,0,272,268,1,0,0,0,272,269,1,0,0,0,272,270,1,0,0,0,273,53,1,
        0,0,0,274,275,5,41,0,0,275,276,3,56,28,0,276,277,5,47,0,0,277,278,
        3,58,29,0,278,279,5,42,0,0,279,55,1,0,0,0,280,285,5,38,0,0,281,282,
        5,47,0,0,282,284,5,38,0,0,283,281,1,0,0,0,284,287,1,0,0,0,285,283,
        1,0,0,0,285,286,1,0,0,0,286,57,1,0,0,0,287,285,1,0,0,0,288,289,5,
        38,0,0,289,59,1,0,0,0,290,291,6,30,-1,0,291,292,5,34,0,0,292,306,
        3,60,30,10,293,294,5,41,0,0,294,295,3,60,30,0,295,296,5,42,0,0,296,
        306,1,0,0,0,297,306,5,40,0,0,298,306,5,39,0,0,299,306,5,38,0,0,300,
        306,5,35,0,0,301,306,5,36,0,0,302,306,3,42,21,0,303,306,3,44,22,
        0,304,306,3,50,25,0,305,290,1,0,0,0,305,293,1,0,0,0,305,297,1,0,
        0,0,305,298,1,0,0,0,305,299,1,0,0,0,305,300,1,0,0,0,305,301,1,0,
        0,0,305,302,1,0,0,0,305,303,1,0,0,0,305,304,1,0,0,0,306,340,1,0,
        0,0,307,308,10,16,0,0,308,309,5,43,0,0,309,310,3,60,30,0,310,311,
        5,44,0,0,311,312,5,49,0,0,312,313,3,60,30,17,313,339,1,0,0,0,314,
        315,10,14,0,0,315,316,7,1,0,0,316,339,3,60,30,15,317,318,10,13,0,
        0,318,319,7,2,0,0,319,339,3,60,30,14,320,321,10,12,0,0,321,322,7,
        3,0,0,322,339,3,60,30,13,323,324,10,11,0,0,324,325,7,4,0,0,325,339,
        3,60,30,12,326,327,10,17,0,0,327,328,5,43,0,0,328,329,3,60,30,0,
        329,330,5,44,0,0,330,339,1,0,0,0,331,332,10,15,0,0,332,333,5,48,
        0,0,333,334,5,8,0,0,334,335,5,41,0,0,335,336,3,60,30,0,336,337,5,
        42,0,0,337,339,1,0,0,0,338,307,1,0,0,0,338,314,1,0,0,0,338,317,1,
        0,0,0,338,320,1,0,0,0,338,323,1,0,0,0,338,326,1,0,0,0,338,331,1,
        0,0,0,339,342,1,0,0,0,340,338,1,0,0,0,340,341,1,0,0,0,341,61,1,0,
        0,0,342,340,1,0,0,0,25,65,77,89,94,115,123,130,138,144,155,168,177,
        184,192,195,205,219,229,246,261,272,285,305,338,340
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'string'", "'bool'", "'number'", "'BSP'", 
                     "'2D'", "'3D'", "'D'", "'add'", "'if'", "'elif'", "'else'", 
                     "'return'", "'print'", "'for'", "'in'", "'while'", 
                     "'def'", "'randomNumber'", "'randomChoice'", "'enum'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'>='", "'<'", "'<='", 
                     "'=='", "'!='", "'%'", "'and'", "'or'", "'not'", "'True'", 
                     "'False'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'.'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IF", "ELIF", "ELSE", "RETURN", "PRINT", 
                      "FOR", "IN", "WHILE", "DEF", "RANDOM_NUMBER", "RANDOM_CHOICE", 
                      "ENUM", "PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", 
                      "LT", "LTE", "EQ", "NEQ", "MOD", "AND", "OR", "NOT", 
                      "TRUE", "FALSE", "COMMENT_SINGLELINE", "NUMBER", "STRING", 
                      "ID", "OPEN_PARENTH", "CLOSED_PARENTH", "OPEN_BRACK", 
                      "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", "COMMA", 
                      "DOT", "EQUAL_SIGN", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_printStat = 2
    RULE_varDecl = 3
    RULE_dataType = 4
    RULE_baseType = 5
    RULE_ifStat = 6
    RULE_ifExpr = 7
    RULE_ifBlock = 8
    RULE_elifExpr = 9
    RULE_elifBlock = 10
    RULE_elseBlock = 11
    RULE_forLoop = 12
    RULE_whileLoop = 13
    RULE_functionDecl = 14
    RULE_functionCall = 15
    RULE_arrayInit = 16
    RULE_bsp = 17
    RULE_params = 18
    RULE_param = 19
    RULE_args = 20
    RULE_randomNumber = 21
    RULE_randomChoice = 22
    RULE_enumDecl = 23
    RULE_enumBody = 24
    RULE_enumValue = 25
    RULE_bspDimension = 26
    RULE_bspParameters = 27
    RULE_dimensionList = 28
    RULE_minSize = 29
    RULE_expr = 30

    ruleNames =  [ "prog", "stat", "printStat", "varDecl", "dataType", "baseType", 
                   "ifStat", "ifExpr", "ifBlock", "elifExpr", "elifBlock", 
                   "elseBlock", "forLoop", "whileLoop", "functionDecl", 
                   "functionCall", "arrayInit", "bsp", "params", "param", 
                   "args", "randomNumber", "randomChoice", "enumDecl", "enumBody", 
                   "enumValue", "bspDimension", "bspParameters", "dimensionList", 
                   "minSize", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    IF=9
    ELIF=10
    ELSE=11
    RETURN=12
    PRINT=13
    FOR=14
    IN=15
    WHILE=16
    DEF=17
    RANDOM_NUMBER=18
    RANDOM_CHOICE=19
    ENUM=20
    PLUS=21
    MINUS=22
    MULT=23
    DIV=24
    GT=25
    GTE=26
    LT=27
    LTE=28
    EQ=29
    NEQ=30
    MOD=31
    AND=32
    OR=33
    NOT=34
    TRUE=35
    FALSE=36
    COMMENT_SINGLELINE=37
    NUMBER=38
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
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.stat()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 39427801833984) != 0)):
                    break

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


        def ifStat(self):
            return self.getTypedRuleContext(RogueLangParser.IfStatContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(RogueLangParser.ForLoopContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(RogueLangParser.WhileLoopContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(RogueLangParser.FunctionDeclContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(RogueLangParser.FunctionCallContext,0)


        def arrayInit(self):
            return self.getTypedRuleContext(RogueLangParser.ArrayInitContext,0)


        def enumDecl(self):
            return self.getTypedRuleContext(RogueLangParser.EnumDeclContext,0)


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
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.ifStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 71
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 72
                self.functionDecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 73
                self.functionCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 74
                self.arrayInit()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 75
                self.enumDecl()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 76
                self.expr(0)
                pass


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
        self.enterRule(localctx, 4, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(RogueLangParser.PRINT)
            self.state = 80
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 81
            self.expr(0)
            self.state = 82
            self.match(RogueLangParser.CLOSED_PARENTH)
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


        def arrayInit(self):
            return self.getTypedRuleContext(RogueLangParser.ArrayInitContext,0)


        def args(self):
            return self.getTypedRuleContext(RogueLangParser.ArgsContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = RogueLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(RogueLangParser.ID)
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 85
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 86
                self.expr(0)

            elif la_ == 2:
                self.state = 87
                self.arrayInit()

            elif la_ == 3:
                self.state = 88
                self.args()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseType(self):
            return self.getTypedRuleContext(RogueLangParser.BaseTypeContext,0)


        def OPEN_BRACK(self):
            return self.getToken(RogueLangParser.OPEN_BRACK, 0)

        def CLOSED_BRACK(self):
            return self.getToken(RogueLangParser.CLOSED_BRACK, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_dataType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = RogueLangParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.baseType()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 92
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 93
                self.match(RogueLangParser.CLOSED_BRACK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(RogueLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(RogueLangParser.FALSE, 0)

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_baseType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseType" ):
                return visitor.visitBaseType(self)
            else:
                return visitor.visitChildren(self)




    def baseType(self):

        localctx = RogueLangParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1202590842894) != 0)):
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

        def ifExpr(self):
            return self.getTypedRuleContext(RogueLangParser.IfExprContext,0)


        def CLOSED_PARENTH(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.CLOSED_PARENTH)
            else:
                return self.getToken(RogueLangParser.CLOSED_PARENTH, i)

        def OPEN_CURL(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.OPEN_CURL)
            else:
                return self.getToken(RogueLangParser.OPEN_CURL, i)

        def ifBlock(self):
            return self.getTypedRuleContext(RogueLangParser.IfBlockContext,0)


        def CLOSED_CURL(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.CLOSED_CURL)
            else:
                return self.getToken(RogueLangParser.CLOSED_CURL, i)

        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.ELIF)
            else:
                return self.getToken(RogueLangParser.ELIF, i)

        def elifExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ElifExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ElifExprContext,i)


        def elifBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ElifBlockContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ElifBlockContext,i)


        def ELSE(self):
            return self.getToken(RogueLangParser.ELSE, 0)

        def elseBlock(self):
            return self.getTypedRuleContext(RogueLangParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_ifStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)




    def ifStat(self):

        localctx = RogueLangParser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(RogueLangParser.IF)
            self.state = 99
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 100
            self.ifExpr()
            self.state = 101
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 102
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 103
            self.ifBlock()
            self.state = 104
            self.match(RogueLangParser.CLOSED_CURL)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 105
                self.match(RogueLangParser.ELIF)
                self.state = 106
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 107
                self.elifExpr()
                self.state = 108
                self.match(RogueLangParser.CLOSED_PARENTH)
                self.state = 109
                self.match(RogueLangParser.OPEN_CURL)
                self.state = 110
                self.elifBlock()
                self.state = 111
                self.match(RogueLangParser.CLOSED_CURL)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 118
                self.match(RogueLangParser.ELSE)
                self.state = 119
                self.match(RogueLangParser.OPEN_CURL)
                self.state = 120
                self.elseBlock()
                self.state = 121
                self.match(RogueLangParser.CLOSED_CURL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_ifExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpr" ):
                return visitor.visitIfExpr(self)
            else:
                return visitor.visitChildren(self)




    def ifExpr(self):

        localctx = RogueLangParser.IfExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_ifBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifBlock(self):

        localctx = RogueLangParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39427801833984) != 0):
                self.state = 127
                self.stat()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_elifExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifExpr" ):
                return visitor.visitElifExpr(self)
            else:
                return visitor.visitChildren(self)




    def elifExpr(self):

        localctx = RogueLangParser.ElifExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_elifExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_elifBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifBlock" ):
                return visitor.visitElifBlock(self)
            else:
                return visitor.visitChildren(self)




    def elifBlock(self):

        localctx = RogueLangParser.ElifBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39427801833984) != 0):
                self.state = 135
                self.stat()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_elseBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBlock" ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = RogueLangParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39427801833984) != 0):
                self.state = 141
                self.stat()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return RogueLangParser.RULE_forLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = RogueLangParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(RogueLangParser.FOR)
            self.state = 148
            self.varDecl()
            self.state = 149
            self.match(RogueLangParser.IN)
            self.state = 150
            self.expr(0)
            self.state = 151
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39427801833984) != 0):
                self.state = 152
                self.stat()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
            self.match(RogueLangParser.CLOSED_CURL)
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
        self.enterRule(localctx, 26, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(RogueLangParser.WHILE)
            self.state = 161
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 162
            self.expr(0)
            self.state = 163
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 164
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39427801833984) != 0):
                self.state = 165
                self.stat()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 171
            self.match(RogueLangParser.CLOSED_CURL)
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

        def OPEN_CURL(self):
            return self.getToken(RogueLangParser.OPEN_CURL, 0)

        def CLOSED_CURL(self):
            return self.getToken(RogueLangParser.CLOSED_CURL, 0)

        def params(self):
            return self.getTypedRuleContext(RogueLangParser.ParamsContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_functionDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = RogueLangParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(RogueLangParser.DEF)
            self.state = 174
            self.match(RogueLangParser.ID)
            self.state = 175
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 176
                self.params()


            self.state = 179
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 180
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39427801833984) != 0):
                self.state = 181
                self.stat()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
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


        def RETURN(self):
            return self.getToken(RogueLangParser.RETURN, 0)

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
            self.state = 189
            self.match(RogueLangParser.ID)
            self.state = 190
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4243428474880) != 0):
                self.state = 191
                self.args()


            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 194
                self.match(RogueLangParser.RETURN)


            self.state = 197
            self.match(RogueLangParser.CLOSED_PARENTH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_CURL(self):
            return self.getToken(RogueLangParser.OPEN_CURL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def CLOSED_CURL(self):
            return self.getToken(RogueLangParser.CLOSED_CURL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.COMMA)
            else:
                return self.getToken(RogueLangParser.COMMA, i)

        def getRuleIndex(self):
            return RogueLangParser.RULE_arrayInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayInit" ):
                return visitor.visitArrayInit(self)
            else:
                return visitor.visitChildren(self)




    def arrayInit(self):

        localctx = RogueLangParser.ArrayInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arrayInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 200
            self.expr(0)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 201
                self.match(RogueLangParser.COMMA)
                self.state = 202
                self.expr(0)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 208
            self.match(RogueLangParser.CLOSED_CURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BspContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bspDimension(self):
            return self.getTypedRuleContext(RogueLangParser.BspDimensionContext,0)


        def bspParameters(self):
            return self.getTypedRuleContext(RogueLangParser.BspParametersContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_bsp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBsp" ):
                return visitor.visitBsp(self)
            else:
                return visitor.visitChildren(self)




    def bsp(self):

        localctx = RogueLangParser.BspContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_bsp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(RogueLangParser.T__3)
            self.state = 211
            self.bspDimension()
            self.state = 212
            self.bspParameters()
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
        self.enterRule(localctx, 36, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.param()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 215
                self.match(RogueLangParser.COMMA)
                self.state = 216
                self.param()
                self.state = 221
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
        self.enterRule(localctx, 38, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
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
        self.enterRule(localctx, 40, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.expr(0)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 225
                self.match(RogueLangParser.COMMA)
                self.state = 226
                self.expr(0)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RandomNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANDOM_NUMBER(self):
            return self.getToken(RogueLangParser.RANDOM_NUMBER, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.NUMBER)
            else:
                return self.getToken(RogueLangParser.NUMBER, i)

        def COMMA(self):
            return self.getToken(RogueLangParser.COMMA, 0)

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_randomNumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandomNumber" ):
                return visitor.visitRandomNumber(self)
            else:
                return visitor.visitChildren(self)




    def randomNumber(self):

        localctx = RogueLangParser.RandomNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_randomNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(RogueLangParser.RANDOM_NUMBER)
            self.state = 233
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 234
            self.match(RogueLangParser.NUMBER)
            self.state = 235
            self.match(RogueLangParser.COMMA)
            self.state = 236
            self.match(RogueLangParser.NUMBER)
            self.state = 237
            self.match(RogueLangParser.CLOSED_PARENTH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RandomChoiceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANDOM_CHOICE(self):
            return self.getToken(RogueLangParser.RANDOM_CHOICE, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.COMMA)
            else:
                return self.getToken(RogueLangParser.COMMA, i)

        def getRuleIndex(self):
            return RogueLangParser.RULE_randomChoice

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandomChoice" ):
                return visitor.visitRandomChoice(self)
            else:
                return visitor.visitChildren(self)




    def randomChoice(self):

        localctx = RogueLangParser.RandomChoiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_randomChoice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(RogueLangParser.RANDOM_CHOICE)
            self.state = 240
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 241
            self.expr(0)
            self.state = 244 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 242
                self.match(RogueLangParser.COMMA)
                self.state = 243
                self.expr(0)
                self.state = 246 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==47):
                    break

            self.state = 248
            self.match(RogueLangParser.CLOSED_PARENTH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(RogueLangParser.ENUM, 0)

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def OPEN_CURL(self):
            return self.getToken(RogueLangParser.OPEN_CURL, 0)

        def enumBody(self):
            return self.getTypedRuleContext(RogueLangParser.EnumBodyContext,0)


        def CLOSED_CURL(self):
            return self.getToken(RogueLangParser.CLOSED_CURL, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_enumDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDecl" ):
                return visitor.visitEnumDecl(self)
            else:
                return visitor.visitChildren(self)




    def enumDecl(self):

        localctx = RogueLangParser.EnumDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_enumDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(RogueLangParser.ENUM)
            self.state = 251
            self.match(RogueLangParser.ID)
            self.state = 252
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 253
            self.enumBody()
            self.state = 254
            self.match(RogueLangParser.CLOSED_CURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumBodyContext(ParserRuleContext):
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
            return RogueLangParser.RULE_enumBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumBody" ):
                return visitor.visitEnumBody(self)
            else:
                return visitor.visitChildren(self)




    def enumBody(self):

        localctx = RogueLangParser.EnumBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_enumBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(RogueLangParser.ID)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 257
                self.match(RogueLangParser.COMMA)
                self.state = 258
                self.match(RogueLangParser.ID)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.ID)
            else:
                return self.getToken(RogueLangParser.ID, i)

        def DOT(self):
            return self.getToken(RogueLangParser.DOT, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_enumValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumValue" ):
                return visitor.visitEnumValue(self)
            else:
                return visitor.visitChildren(self)




    def enumValue(self):

        localctx = RogueLangParser.EnumValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_enumValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(RogueLangParser.ID)
            self.state = 265
            self.match(RogueLangParser.DOT)
            self.state = 266
            self.match(RogueLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BspDimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RogueLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_bspDimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBspDimension" ):
                return visitor.visitBspDimension(self)
            else:
                return visitor.visitChildren(self)




    def bspDimension(self):

        localctx = RogueLangParser.BspDimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_bspDimension)
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(RogueLangParser.T__4)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(RogueLangParser.T__5)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.match(RogueLangParser.NUMBER)
                self.state = 271
                self.match(RogueLangParser.T__6)
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


    class BspParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def dimensionList(self):
            return self.getTypedRuleContext(RogueLangParser.DimensionListContext,0)


        def COMMA(self):
            return self.getToken(RogueLangParser.COMMA, 0)

        def minSize(self):
            return self.getTypedRuleContext(RogueLangParser.MinSizeContext,0)


        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_bspParameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBspParameters" ):
                return visitor.visitBspParameters(self)
            else:
                return visitor.visitChildren(self)




    def bspParameters(self):

        localctx = RogueLangParser.BspParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_bspParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 275
            self.dimensionList()
            self.state = 276
            self.match(RogueLangParser.COMMA)
            self.state = 277
            self.minSize()
            self.state = 278
            self.match(RogueLangParser.CLOSED_PARENTH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.NUMBER)
            else:
                return self.getToken(RogueLangParser.NUMBER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.COMMA)
            else:
                return self.getToken(RogueLangParser.COMMA, i)

        def getRuleIndex(self):
            return RogueLangParser.RULE_dimensionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensionList" ):
                return visitor.visitDimensionList(self)
            else:
                return visitor.visitChildren(self)




    def dimensionList(self):

        localctx = RogueLangParser.DimensionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_dimensionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(RogueLangParser.NUMBER)
            self.state = 285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 281
                    self.match(RogueLangParser.COMMA)
                    self.state = 282
                    self.match(RogueLangParser.NUMBER) 
                self.state = 287
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MinSizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RogueLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_minSize

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinSize" ):
                return visitor.visitMinSize(self)
            else:
                return visitor.visitChildren(self)




    def minSize(self):

        localctx = RogueLangParser.MinSizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_minSize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(RogueLangParser.NUMBER)
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

        def STRING(self):
            return self.getToken(RogueLangParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(RogueLangParser.NUMBER, 0)

        def TRUE(self):
            return self.getToken(RogueLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(RogueLangParser.FALSE, 0)

        def randomNumber(self):
            return self.getTypedRuleContext(RogueLangParser.RandomNumberContext,0)


        def randomChoice(self):
            return self.getTypedRuleContext(RogueLangParser.RandomChoiceContext,0)


        def enumValue(self):
            return self.getTypedRuleContext(RogueLangParser.EnumValueContext,0)


        def OPEN_BRACK(self):
            return self.getToken(RogueLangParser.OPEN_BRACK, 0)

        def CLOSED_BRACK(self):
            return self.getToken(RogueLangParser.CLOSED_BRACK, 0)

        def EQUAL_SIGN(self):
            return self.getToken(RogueLangParser.EQUAL_SIGN, 0)

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

        def DOT(self):
            return self.getToken(RogueLangParser.DOT, 0)

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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 291
                self.match(RogueLangParser.NOT)
                self.state = 292
                self.expr(10)
                pass

            elif la_ == 2:
                self.state = 293
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 294
                self.expr(0)
                self.state = 295
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 3:
                self.state = 297
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 4:
                self.state = 298
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 5:
                self.state = 299
                self.match(RogueLangParser.NUMBER)
                pass

            elif la_ == 6:
                self.state = 300
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 7:
                self.state = 301
                self.match(RogueLangParser.FALSE)
                pass

            elif la_ == 8:
                self.state = 302
                self.randomNumber()
                pass

            elif la_ == 9:
                self.state = 303
                self.randomChoice()
                pass

            elif la_ == 10:
                self.state = 304
                self.enumValue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 338
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 307
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 308
                        self.match(RogueLangParser.OPEN_BRACK)
                        self.state = 309
                        self.expr(0)
                        self.state = 310
                        self.match(RogueLangParser.CLOSED_BRACK)
                        self.state = 311
                        self.match(RogueLangParser.EQUAL_SIGN)
                        self.state = 312
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 314
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 315
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2172649472) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 316
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 317
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 318
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 319
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 320
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 321
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 322
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 323
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 324
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 325
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 326
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 327
                        self.match(RogueLangParser.OPEN_BRACK)
                        self.state = 328
                        self.expr(0)
                        self.state = 329
                        self.match(RogueLangParser.CLOSED_BRACK)
                        pass

                    elif la_ == 7:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 331
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 332
                        self.match(RogueLangParser.DOT)
                        self.state = 333
                        self.match(RogueLangParser.T__7)
                        self.state = 334
                        self.match(RogueLangParser.OPEN_PARENTH)
                        self.state = 335
                        self.expr(0)
                        self.state = 336
                        self.match(RogueLangParser.CLOSED_PARENTH)
                        pass

             
                self.state = 342
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
        self._predicates[30] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 15)
         




