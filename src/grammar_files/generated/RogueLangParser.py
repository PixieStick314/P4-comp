# Generated from C:/Users/lokes/PycharmProjects/P4-comp/src/grammar_files/RogueLang.g4 by ANTLR 4.13.1
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
        4,1,56,338,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,4,0,56,8,0,11,0,12,0,57,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,71,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,86,8,3,1,3,1,3,1,4,1,4,1,4,3,4,93,8,4,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,5,6,103,8,6,10,6,12,6,106,9,6,1,6,1,6,1,6,1,6,5,
        6,112,8,6,10,6,12,6,115,9,6,1,6,3,6,118,8,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,5,7,131,8,7,10,7,12,7,134,9,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,147,8,8,10,8,12,8,150,9,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,161,8,9,10,9,12,9,164,9,
        9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,173,8,10,1,10,1,10,1,10,5,
        10,178,8,10,10,10,12,10,181,9,10,1,10,1,10,1,10,1,11,1,11,1,11,3,
        11,189,8,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,198,8,12,10,
        12,12,12,201,9,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,
        14,5,14,213,8,14,10,14,12,14,216,9,14,1,15,1,15,1,15,1,16,1,16,1,
        16,5,16,224,8,16,10,16,12,16,227,9,16,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,
        17,247,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,5,17,275,8,17,10,17,12,17,278,9,17,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,4,19,292,8,19,11,19,12,
        19,293,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,5,
        21,307,8,21,10,21,12,21,310,9,21,1,22,1,22,1,22,1,22,1,23,1,23,1,
        23,1,23,3,23,320,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,
        25,5,25,331,8,25,10,25,12,25,334,9,25,1,26,1,26,1,26,0,1,34,27,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,0,4,3,0,9,15,46,47,55,55,1,0,43,44,1,0,41,42,1,0,28,33,
        361,0,55,1,0,0,0,2,70,1,0,0,0,4,72,1,0,0,0,6,78,1,0,0,0,8,89,1,0,
        0,0,10,94,1,0,0,0,12,96,1,0,0,0,14,121,1,0,0,0,16,138,1,0,0,0,18,
        154,1,0,0,0,20,168,1,0,0,0,22,185,1,0,0,0,24,193,1,0,0,0,26,205,
        1,0,0,0,28,209,1,0,0,0,30,217,1,0,0,0,32,220,1,0,0,0,34,246,1,0,
        0,0,36,279,1,0,0,0,38,286,1,0,0,0,40,297,1,0,0,0,42,303,1,0,0,0,
        44,311,1,0,0,0,46,319,1,0,0,0,48,321,1,0,0,0,50,327,1,0,0,0,52,335,
        1,0,0,0,54,56,3,2,1,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,
        57,58,1,0,0,0,58,1,1,0,0,0,59,71,3,4,2,0,60,71,3,6,3,0,61,71,3,12,
        6,0,62,71,3,14,7,0,63,71,3,16,8,0,64,71,3,18,9,0,65,71,3,20,10,0,
        66,71,3,22,11,0,67,71,3,24,12,0,68,71,3,40,20,0,69,71,3,34,17,0,
        70,59,1,0,0,0,70,60,1,0,0,0,70,61,1,0,0,0,70,62,1,0,0,0,70,63,1,
        0,0,0,70,64,1,0,0,0,70,65,1,0,0,0,70,66,1,0,0,0,70,67,1,0,0,0,70,
        68,1,0,0,0,70,69,1,0,0,0,71,3,1,0,0,0,72,73,5,1,0,0,73,74,5,2,0,
        0,74,75,3,34,17,0,75,76,5,3,0,0,76,77,5,4,0,0,77,5,1,0,0,0,78,79,
        5,5,0,0,79,80,3,8,4,0,80,85,5,55,0,0,81,82,5,6,0,0,82,86,3,34,17,
        0,83,86,3,24,12,0,84,86,3,32,16,0,85,81,1,0,0,0,85,83,1,0,0,0,85,
        84,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,5,4,0,0,88,7,1,0,0,
        0,89,92,3,10,5,0,90,91,5,7,0,0,91,93,5,8,0,0,92,90,1,0,0,0,92,93,
        1,0,0,0,93,9,1,0,0,0,94,95,7,0,0,0,95,11,1,0,0,0,96,97,5,16,0,0,
        97,98,5,2,0,0,98,99,3,34,17,0,99,100,5,3,0,0,100,104,5,17,0,0,101,
        103,3,2,1,0,102,101,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,
        105,1,0,0,0,105,107,1,0,0,0,106,104,1,0,0,0,107,117,5,18,0,0,108,
        109,5,19,0,0,109,113,5,17,0,0,110,112,3,2,1,0,111,110,1,0,0,0,112,
        115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,
        113,1,0,0,0,116,118,5,18,0,0,117,108,1,0,0,0,117,118,1,0,0,0,118,
        119,1,0,0,0,119,120,5,4,0,0,120,13,1,0,0,0,121,122,5,20,0,0,122,
        123,5,2,0,0,123,124,3,6,3,0,124,125,3,34,17,0,125,126,5,4,0,0,126,
        127,3,34,17,0,127,128,5,3,0,0,128,132,5,17,0,0,129,131,3,2,1,0,130,
        129,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,
        135,1,0,0,0,134,132,1,0,0,0,135,136,5,18,0,0,136,137,5,4,0,0,137,
        15,1,0,0,0,138,139,5,21,0,0,139,140,5,2,0,0,140,141,3,6,3,0,141,
        142,5,22,0,0,142,143,3,34,17,0,143,144,5,3,0,0,144,148,5,17,0,0,
        145,147,3,2,1,0,146,145,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,
        148,149,1,0,0,0,149,151,1,0,0,0,150,148,1,0,0,0,151,152,5,18,0,0,
        152,153,5,4,0,0,153,17,1,0,0,0,154,155,5,23,0,0,155,156,5,2,0,0,
        156,157,3,34,17,0,157,158,5,3,0,0,158,162,5,17,0,0,159,161,3,2,1,
        0,160,159,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,
        0,163,165,1,0,0,0,164,162,1,0,0,0,165,166,5,18,0,0,166,167,5,4,0,
        0,167,19,1,0,0,0,168,169,5,24,0,0,169,170,5,55,0,0,170,172,5,2,0,
        0,171,173,3,28,14,0,172,171,1,0,0,0,172,173,1,0,0,0,173,174,1,0,
        0,0,174,175,5,3,0,0,175,179,5,17,0,0,176,178,3,2,1,0,177,176,1,0,
        0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,182,1,0,
        0,0,181,179,1,0,0,0,182,183,5,18,0,0,183,184,5,4,0,0,184,21,1,0,
        0,0,185,186,5,55,0,0,186,188,5,2,0,0,187,189,3,32,16,0,188,187,1,
        0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,191,5,3,0,0,191,192,5,
        4,0,0,192,23,1,0,0,0,193,194,5,17,0,0,194,199,3,34,17,0,195,196,
        5,25,0,0,196,198,3,34,17,0,197,195,1,0,0,0,198,201,1,0,0,0,199,197,
        1,0,0,0,199,200,1,0,0,0,200,202,1,0,0,0,201,199,1,0,0,0,202,203,
        5,18,0,0,203,204,5,4,0,0,204,25,1,0,0,0,205,206,5,26,0,0,206,207,
        3,46,23,0,207,208,3,48,24,0,208,27,1,0,0,0,209,214,3,30,15,0,210,
        211,5,25,0,0,211,213,3,30,15,0,212,210,1,0,0,0,213,216,1,0,0,0,214,
        212,1,0,0,0,214,215,1,0,0,0,215,29,1,0,0,0,216,214,1,0,0,0,217,218,
        3,8,4,0,218,219,5,55,0,0,219,31,1,0,0,0,220,225,3,34,17,0,221,222,
        5,25,0,0,222,224,3,34,17,0,223,221,1,0,0,0,224,227,1,0,0,0,225,223,
        1,0,0,0,225,226,1,0,0,0,226,33,1,0,0,0,227,225,1,0,0,0,228,229,6,
        17,-1,0,229,230,5,2,0,0,230,231,3,34,17,0,231,232,5,3,0,0,232,247,
        1,0,0,0,233,247,5,55,0,0,234,247,5,49,0,0,235,247,5,50,0,0,236,247,
        5,51,0,0,237,247,5,46,0,0,238,247,5,47,0,0,239,247,5,48,0,0,240,
        247,5,52,0,0,241,247,5,53,0,0,242,247,5,54,0,0,243,247,3,36,18,0,
        244,247,3,38,19,0,245,247,3,44,22,0,246,228,1,0,0,0,246,233,1,0,
        0,0,246,234,1,0,0,0,246,235,1,0,0,0,246,236,1,0,0,0,246,237,1,0,
        0,0,246,238,1,0,0,0,246,239,1,0,0,0,246,240,1,0,0,0,246,241,1,0,
        0,0,246,242,1,0,0,0,246,243,1,0,0,0,246,244,1,0,0,0,246,245,1,0,
        0,0,247,276,1,0,0,0,248,249,10,19,0,0,249,250,5,7,0,0,250,251,3,
        34,17,0,251,252,5,8,0,0,252,253,5,6,0,0,253,254,3,34,17,20,254,275,
        1,0,0,0,255,256,10,17,0,0,256,257,7,1,0,0,257,275,3,34,17,18,258,
        259,10,16,0,0,259,260,7,2,0,0,260,275,3,34,17,17,261,262,10,15,0,
        0,262,263,7,3,0,0,263,275,3,34,17,16,264,265,10,20,0,0,265,266,5,
        7,0,0,266,267,3,34,17,0,267,268,5,8,0,0,268,275,1,0,0,0,269,270,
        10,18,0,0,270,271,5,27,0,0,271,272,3,34,17,0,272,273,5,3,0,0,273,
        275,1,0,0,0,274,248,1,0,0,0,274,255,1,0,0,0,274,258,1,0,0,0,274,
        261,1,0,0,0,274,264,1,0,0,0,274,269,1,0,0,0,275,278,1,0,0,0,276,
        274,1,0,0,0,276,277,1,0,0,0,277,35,1,0,0,0,278,276,1,0,0,0,279,280,
        5,34,0,0,280,281,5,2,0,0,281,282,5,49,0,0,282,283,5,25,0,0,283,284,
        5,49,0,0,284,285,5,3,0,0,285,37,1,0,0,0,286,287,5,35,0,0,287,288,
        5,2,0,0,288,291,3,34,17,0,289,290,5,25,0,0,290,292,3,34,17,0,291,
        289,1,0,0,0,292,293,1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,
        295,1,0,0,0,295,296,5,3,0,0,296,39,1,0,0,0,297,298,5,36,0,0,298,
        299,5,55,0,0,299,300,5,17,0,0,300,301,3,42,21,0,301,302,5,18,0,0,
        302,41,1,0,0,0,303,308,5,55,0,0,304,305,5,25,0,0,305,307,5,55,0,
        0,306,304,1,0,0,0,307,310,1,0,0,0,308,306,1,0,0,0,308,309,1,0,0,
        0,309,43,1,0,0,0,310,308,1,0,0,0,311,312,5,55,0,0,312,313,5,37,0,
        0,313,314,5,55,0,0,314,45,1,0,0,0,315,320,5,38,0,0,316,320,5,39,
        0,0,317,318,5,49,0,0,318,320,5,40,0,0,319,315,1,0,0,0,319,316,1,
        0,0,0,319,317,1,0,0,0,320,47,1,0,0,0,321,322,5,2,0,0,322,323,3,50,
        25,0,323,324,5,25,0,0,324,325,3,52,26,0,325,326,5,3,0,0,326,49,1,
        0,0,0,327,332,5,49,0,0,328,329,5,25,0,0,329,331,5,49,0,0,330,328,
        1,0,0,0,331,334,1,0,0,0,332,330,1,0,0,0,332,333,1,0,0,0,333,51,1,
        0,0,0,334,332,1,0,0,0,335,336,5,49,0,0,336,53,1,0,0,0,23,57,70,85,
        92,104,113,117,132,148,162,172,179,188,199,214,225,246,274,276,293,
        308,319,332
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'('", "')'", "';'", "'var'", 
                     "'='", "'['", "']'", "'int'", "'string'", "'bool'", 
                     "'double'", "'date'", "'time'", "'dateTime'", "'if'", 
                     "'{'", "'}'", "'else'", "'for'", "'foreach'", "'in'", 
                     "'while'", "'function'", "','", "'BSP'", "'.add('", 
                     "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", "'randomInt'", 
                     "'randomChoice'", "'enum'", "'.'", "'2D'", "'3D'", 
                     "'D'", "'+'", "'-'", "'*'", "'/'", "'%'", "'true'", 
                     "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PLUS", "MINUS", "MULT", "DIV", "MOD", 
                      "TRUE", "FALSE", "BOOL", "INT", "STRING", "DOUBLE", 
                      "DATE", "TIME", "DATETIME", "ID", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_printStat = 2
    RULE_varDecl = 3
    RULE_dataType = 4
    RULE_baseType = 5
    RULE_ifStat = 6
    RULE_forLoop = 7
    RULE_foreachLoop = 8
    RULE_whileLoop = 9
    RULE_functionDecl = 10
    RULE_functionCall = 11
    RULE_arrayInit = 12
    RULE_bsp = 13
    RULE_params = 14
    RULE_param = 15
    RULE_args = 16
    RULE_expr = 17
    RULE_randomInt = 18
    RULE_randomChoice = 19
    RULE_enumDecl = 20
    RULE_enumBody = 21
    RULE_enumValue = 22
    RULE_bspDimension = 23
    RULE_bspParameters = 24
    RULE_dimensionList = 25
    RULE_minSize = 26

    ruleNames =  [ "prog", "stat", "printStat", "varDecl", "dataType", "baseType", 
                   "ifStat", "forLoop", "foreachLoop", "whileLoop", "functionDecl", 
                   "functionCall", "arrayInit", "bsp", "params", "param", 
                   "args", "expr", "randomInt", "randomChoice", "enumDecl", 
                   "enumBody", "enumValue", "bspDimension", "bspParameters", 
                   "dimensionList", "minSize" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    PLUS=41
    MINUS=42
    MULT=43
    DIV=44
    MOD=45
    TRUE=46
    FALSE=47
    BOOL=48
    INT=49
    STRING=50
    DOUBLE=51
    DATE=52
    TIME=53
    DATETIME=54
    ID=55
    WS=56

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
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.stat()
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 71987345581342758) != 0)):
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


        def foreachLoop(self):
            return self.getTypedRuleContext(RogueLangParser.ForeachLoopContext,0)


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
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.ifStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.foreachLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 64
                self.whileLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 65
                self.functionDecl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 66
                self.functionCall()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 67
                self.arrayInit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 68
                self.enumDecl()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 69
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

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


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
            self.state = 72
            self.match(RogueLangParser.T__0)
            self.state = 73
            self.match(RogueLangParser.T__1)
            self.state = 74
            self.expr(0)
            self.state = 75
            self.match(RogueLangParser.T__2)
            self.state = 76
            self.match(RogueLangParser.T__3)
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

        def dataType(self):
            return self.getTypedRuleContext(RogueLangParser.DataTypeContext,0)


        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

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
            self.state = 78
            self.match(RogueLangParser.T__4)
            self.state = 79
            self.dataType()
            self.state = 80
            self.match(RogueLangParser.ID)
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 81
                self.match(RogueLangParser.T__5)
                self.state = 82
                self.expr(0)
                pass
            elif token in [17]:
                self.state = 83
                self.arrayInit()
                pass
            elif token in [2, 34, 35, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]:
                self.state = 84
                self.args()
                pass
            elif token in [4]:
                pass
            else:
                pass
            self.state = 87
            self.match(RogueLangParser.T__3)
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
            self.state = 89
            self.baseType()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 90
                self.match(RogueLangParser.T__6)
                self.state = 91
                self.match(RogueLangParser.T__7)


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
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 36239903251561984) != 0)):
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

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatContext,i)


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
            self.state = 96
            self.match(RogueLangParser.T__15)
            self.state = 97
            self.match(RogueLangParser.T__1)
            self.state = 98
            self.expr(0)
            self.state = 99
            self.match(RogueLangParser.T__2)
            self.state = 100
            self.match(RogueLangParser.T__16)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 71987345581342758) != 0):
                self.state = 101
                self.stat()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(RogueLangParser.T__17)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 108
                self.match(RogueLangParser.T__18)
                self.state = 109
                self.match(RogueLangParser.T__16)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 71987345581342758) != 0):
                    self.state = 110
                    self.stat()
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 116
                self.match(RogueLangParser.T__17)


            self.state = 119
            self.match(RogueLangParser.T__3)
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

        def varDecl(self):
            return self.getTypedRuleContext(RogueLangParser.VarDeclContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


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
        self.enterRule(localctx, 14, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(RogueLangParser.T__19)
            self.state = 122
            self.match(RogueLangParser.T__1)
            self.state = 123
            self.varDecl()
            self.state = 124
            self.expr(0)
            self.state = 125
            self.match(RogueLangParser.T__3)
            self.state = 126
            self.expr(0)
            self.state = 127
            self.match(RogueLangParser.T__2)
            self.state = 128
            self.match(RogueLangParser.T__16)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 71987345581342758) != 0):
                self.state = 129
                self.stat()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self.match(RogueLangParser.T__17)
            self.state = 136
            self.match(RogueLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForeachLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(RogueLangParser.VarDeclContext,0)


        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_foreachLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeachLoop" ):
                return visitor.visitForeachLoop(self)
            else:
                return visitor.visitChildren(self)




    def foreachLoop(self):

        localctx = RogueLangParser.ForeachLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_foreachLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(RogueLangParser.T__20)
            self.state = 139
            self.match(RogueLangParser.T__1)
            self.state = 140
            self.varDecl()
            self.state = 141
            self.match(RogueLangParser.T__21)
            self.state = 142
            self.expr(0)
            self.state = 143
            self.match(RogueLangParser.T__2)
            self.state = 144
            self.match(RogueLangParser.T__16)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 71987345581342758) != 0):
                self.state = 145
                self.stat()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(RogueLangParser.T__17)
            self.state = 152
            self.match(RogueLangParser.T__3)
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

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


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
        self.enterRule(localctx, 18, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(RogueLangParser.T__22)
            self.state = 155
            self.match(RogueLangParser.T__1)
            self.state = 156
            self.expr(0)
            self.state = 157
            self.match(RogueLangParser.T__2)
            self.state = 158
            self.match(RogueLangParser.T__16)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 71987345581342758) != 0):
                self.state = 159
                self.stat()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self.match(RogueLangParser.T__17)
            self.state = 166
            self.match(RogueLangParser.T__3)
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

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

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
        self.enterRule(localctx, 20, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(RogueLangParser.T__23)
            self.state = 169
            self.match(RogueLangParser.ID)
            self.state = 170
            self.match(RogueLangParser.T__1)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36239903251561984) != 0):
                self.state = 171
                self.params()


            self.state = 174
            self.match(RogueLangParser.T__2)
            self.state = 175
            self.match(RogueLangParser.T__16)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 71987345581342758) != 0):
                self.state = 176
                self.stat()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self.match(RogueLangParser.T__17)
            self.state = 183
            self.match(RogueLangParser.T__3)
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
        self.enterRule(localctx, 22, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(RogueLangParser.ID)
            self.state = 186
            self.match(RogueLangParser.T__1)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 71987276833357828) != 0):
                self.state = 187
                self.args()


            self.state = 190
            self.match(RogueLangParser.T__2)
            self.state = 191
            self.match(RogueLangParser.T__3)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_arrayInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayInit" ):
                return visitor.visitArrayInit(self)
            else:
                return visitor.visitChildren(self)




    def arrayInit(self):

        localctx = RogueLangParser.ArrayInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(RogueLangParser.T__16)
            self.state = 194
            self.expr(0)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 195
                self.match(RogueLangParser.T__24)
                self.state = 196
                self.expr(0)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.match(RogueLangParser.T__17)
            self.state = 203
            self.match(RogueLangParser.T__3)
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
        self.enterRule(localctx, 26, self.RULE_bsp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(RogueLangParser.T__25)
            self.state = 206
            self.bspDimension()
            self.state = 207
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
            self.state = 209
            self.param()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 210
                self.match(RogueLangParser.T__24)
                self.state = 211
                self.param()
                self.state = 216
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

        def dataType(self):
            return self.getTypedRuleContext(RogueLangParser.DataTypeContext,0)


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
            self.state = 217
            self.dataType()
            self.state = 218
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
            self.state = 220
            self.expr(0)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 221
                self.match(RogueLangParser.T__24)
                self.state = 222
                self.expr(0)
                self.state = 227
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def INT(self):
            return self.getToken(RogueLangParser.INT, 0)

        def STRING(self):
            return self.getToken(RogueLangParser.STRING, 0)

        def DOUBLE(self):
            return self.getToken(RogueLangParser.DOUBLE, 0)

        def TRUE(self):
            return self.getToken(RogueLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(RogueLangParser.FALSE, 0)

        def BOOL(self):
            return self.getToken(RogueLangParser.BOOL, 0)

        def DATE(self):
            return self.getToken(RogueLangParser.DATE, 0)

        def TIME(self):
            return self.getToken(RogueLangParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(RogueLangParser.DATETIME, 0)

        def randomInt(self):
            return self.getTypedRuleContext(RogueLangParser.RandomIntContext,0)


        def randomChoice(self):
            return self.getTypedRuleContext(RogueLangParser.RandomChoiceContext,0)


        def enumValue(self):
            return self.getTypedRuleContext(RogueLangParser.EnumValueContext,0)


        def MULT(self):
            return self.getToken(RogueLangParser.MULT, 0)

        def DIV(self):
            return self.getToken(RogueLangParser.DIV, 0)

        def PLUS(self):
            return self.getToken(RogueLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(RogueLangParser.MINUS, 0)

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
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 229
                self.match(RogueLangParser.T__1)
                self.state = 230
                self.expr(0)
                self.state = 231
                self.match(RogueLangParser.T__2)
                pass

            elif la_ == 2:
                self.state = 233
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 3:
                self.state = 234
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 4:
                self.state = 235
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 5:
                self.state = 236
                self.match(RogueLangParser.DOUBLE)
                pass

            elif la_ == 6:
                self.state = 237
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 7:
                self.state = 238
                self.match(RogueLangParser.FALSE)
                pass

            elif la_ == 8:
                self.state = 239
                self.match(RogueLangParser.BOOL)
                pass

            elif la_ == 9:
                self.state = 240
                self.match(RogueLangParser.DATE)
                pass

            elif la_ == 10:
                self.state = 241
                self.match(RogueLangParser.TIME)
                pass

            elif la_ == 11:
                self.state = 242
                self.match(RogueLangParser.DATETIME)
                pass

            elif la_ == 12:
                self.state = 243
                self.randomInt()
                pass

            elif la_ == 13:
                self.state = 244
                self.randomChoice()
                pass

            elif la_ == 14:
                self.state = 245
                self.enumValue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 274
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 248
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 249
                        self.match(RogueLangParser.T__6)
                        self.state = 250
                        self.expr(0)
                        self.state = 251
                        self.match(RogueLangParser.T__7)
                        self.state = 252
                        self.match(RogueLangParser.T__5)
                        self.state = 253
                        self.expr(20)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 255
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 256
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==43 or _la==44):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 257
                        self.expr(18)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 258
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 259
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==41 or _la==42):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 260
                        self.expr(17)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 261
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 262
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16911433728) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 263
                        self.expr(16)
                        pass

                    elif la_ == 5:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 264
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 265
                        self.match(RogueLangParser.T__6)
                        self.state = 266
                        self.expr(0)
                        self.state = 267
                        self.match(RogueLangParser.T__7)
                        pass

                    elif la_ == 6:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 269
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 270
                        self.match(RogueLangParser.T__26)
                        self.state = 271
                        self.expr(0)
                        self.state = 272
                        self.match(RogueLangParser.T__2)
                        pass

             
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RandomIntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.INT)
            else:
                return self.getToken(RogueLangParser.INT, i)

        def getRuleIndex(self):
            return RogueLangParser.RULE_randomInt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandomInt" ):
                return visitor.visitRandomInt(self)
            else:
                return visitor.visitChildren(self)




    def randomInt(self):

        localctx = RogueLangParser.RandomIntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_randomInt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(RogueLangParser.T__33)
            self.state = 280
            self.match(RogueLangParser.T__1)
            self.state = 281
            self.match(RogueLangParser.INT)
            self.state = 282
            self.match(RogueLangParser.T__24)
            self.state = 283
            self.match(RogueLangParser.INT)
            self.state = 284
            self.match(RogueLangParser.T__2)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_randomChoice

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandomChoice" ):
                return visitor.visitRandomChoice(self)
            else:
                return visitor.visitChildren(self)




    def randomChoice(self):

        localctx = RogueLangParser.RandomChoiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_randomChoice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(RogueLangParser.T__34)
            self.state = 287
            self.match(RogueLangParser.T__1)
            self.state = 288
            self.expr(0)
            self.state = 291 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 289
                self.match(RogueLangParser.T__24)
                self.state = 290
                self.expr(0)
                self.state = 293 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 295
            self.match(RogueLangParser.T__2)
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

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def enumBody(self):
            return self.getTypedRuleContext(RogueLangParser.EnumBodyContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_enumDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDecl" ):
                return visitor.visitEnumDecl(self)
            else:
                return visitor.visitChildren(self)




    def enumDecl(self):

        localctx = RogueLangParser.EnumDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_enumDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(RogueLangParser.T__35)
            self.state = 298
            self.match(RogueLangParser.ID)
            self.state = 299
            self.match(RogueLangParser.T__16)
            self.state = 300
            self.enumBody()
            self.state = 301
            self.match(RogueLangParser.T__17)
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

        def getRuleIndex(self):
            return RogueLangParser.RULE_enumBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumBody" ):
                return visitor.visitEnumBody(self)
            else:
                return visitor.visitChildren(self)




    def enumBody(self):

        localctx = RogueLangParser.EnumBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_enumBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(RogueLangParser.ID)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 304
                self.match(RogueLangParser.T__24)
                self.state = 305
                self.match(RogueLangParser.ID)
                self.state = 310
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

        def getRuleIndex(self):
            return RogueLangParser.RULE_enumValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumValue" ):
                return visitor.visitEnumValue(self)
            else:
                return visitor.visitChildren(self)




    def enumValue(self):

        localctx = RogueLangParser.EnumValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_enumValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(RogueLangParser.ID)
            self.state = 312
            self.match(RogueLangParser.T__36)
            self.state = 313
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

        def INT(self):
            return self.getToken(RogueLangParser.INT, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_bspDimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBspDimension" ):
                return visitor.visitBspDimension(self)
            else:
                return visitor.visitChildren(self)




    def bspDimension(self):

        localctx = RogueLangParser.BspDimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_bspDimension)
        try:
            self.state = 319
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(RogueLangParser.T__37)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.match(RogueLangParser.T__38)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
                self.match(RogueLangParser.INT)
                self.state = 318
                self.match(RogueLangParser.T__39)
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

        def dimensionList(self):
            return self.getTypedRuleContext(RogueLangParser.DimensionListContext,0)


        def minSize(self):
            return self.getTypedRuleContext(RogueLangParser.MinSizeContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_bspParameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBspParameters" ):
                return visitor.visitBspParameters(self)
            else:
                return visitor.visitChildren(self)




    def bspParameters(self):

        localctx = RogueLangParser.BspParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_bspParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(RogueLangParser.T__1)
            self.state = 322
            self.dimensionList()
            self.state = 323
            self.match(RogueLangParser.T__24)
            self.state = 324
            self.minSize()
            self.state = 325
            self.match(RogueLangParser.T__2)
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

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.INT)
            else:
                return self.getToken(RogueLangParser.INT, i)

        def getRuleIndex(self):
            return RogueLangParser.RULE_dimensionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensionList" ):
                return visitor.visitDimensionList(self)
            else:
                return visitor.visitChildren(self)




    def dimensionList(self):

        localctx = RogueLangParser.DimensionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_dimensionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(RogueLangParser.INT)
            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 328
                    self.match(RogueLangParser.T__24)
                    self.state = 329
                    self.match(RogueLangParser.INT) 
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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

        def INT(self):
            return self.getToken(RogueLangParser.INT, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_minSize

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinSize" ):
                return visitor.visitMinSize(self)
            else:
                return visitor.visitChildren(self)




    def minSize(self):

        localctx = RogueLangParser.MinSizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_minSize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(RogueLangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
                return self.precpred(self._ctx, 19)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 18)
         




