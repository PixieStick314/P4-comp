# Generated from C:/Users/Lenovo/Documents/GitHub/P4-comp/src/grammar_files/RogueLang.g4 by ANTLR 4.13.1
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
        4,1,49,356,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        4,0,68,8,0,11,0,12,0,69,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,82,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,94,8,3,1,
        4,1,4,1,4,1,4,3,4,100,8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,110,
        8,6,10,6,12,6,113,9,6,1,6,1,6,1,6,1,6,5,6,119,8,6,10,6,12,6,122,
        9,6,1,6,1,6,5,6,126,8,6,10,6,12,6,129,9,6,1,6,1,6,1,6,5,6,134,8,
        6,10,6,12,6,137,9,6,1,6,1,6,3,6,141,8,6,1,7,1,7,1,7,1,7,1,7,1,7,
        5,7,149,8,7,10,7,12,7,152,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,
        8,162,8,8,10,8,12,8,165,9,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,173,8,9,
        1,9,1,9,1,9,5,9,178,8,9,10,9,12,9,181,9,9,1,9,1,9,1,10,1,10,1,10,
        3,10,188,8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,5,11,197,8,11,10,
        11,12,11,200,9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,
        13,5,13,212,8,13,10,13,12,13,215,9,13,1,14,1,14,1,14,1,15,1,15,1,
        15,1,15,5,15,224,8,15,10,15,12,15,227,9,15,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,4,17,242,8,17,11,17,12,
        17,243,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,
        19,5,19,258,8,19,10,19,12,19,261,9,19,1,20,1,20,1,20,1,20,1,21,1,
        21,1,21,1,21,3,21,271,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,
        23,1,23,1,23,5,23,283,8,23,10,23,12,23,286,9,23,1,24,1,24,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,3,25,305,8,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,337,8,25,10,25,12,25,
        340,9,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,31,
        1,31,1,32,1,32,1,32,0,1,50,33,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,5,
        3,0,3,5,43,44,48,48,2,0,31,32,39,39,1,0,29,30,1,0,33,38,1,0,40,41,
        370,0,67,1,0,0,0,2,81,1,0,0,0,4,83,1,0,0,0,6,88,1,0,0,0,8,95,1,0,
        0,0,10,101,1,0,0,0,12,103,1,0,0,0,14,142,1,0,0,0,16,155,1,0,0,0,
        18,168,1,0,0,0,20,184,1,0,0,0,22,191,1,0,0,0,24,203,1,0,0,0,26,207,
        1,0,0,0,28,216,1,0,0,0,30,219,1,0,0,0,32,228,1,0,0,0,34,235,1,0,
        0,0,36,247,1,0,0,0,38,253,1,0,0,0,40,262,1,0,0,0,42,270,1,0,0,0,
        44,272,1,0,0,0,46,278,1,0,0,0,48,287,1,0,0,0,50,304,1,0,0,0,52,341,
        1,0,0,0,54,343,1,0,0,0,56,345,1,0,0,0,58,347,1,0,0,0,60,349,1,0,
        0,0,62,351,1,0,0,0,64,353,1,0,0,0,66,68,3,2,1,0,67,66,1,0,0,0,68,
        69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,1,1,0,0,0,71,82,3,4,2,
        0,72,82,3,6,3,0,73,82,3,12,6,0,74,82,3,14,7,0,75,82,3,16,8,0,76,
        82,3,18,9,0,77,82,3,20,10,0,78,82,3,22,11,0,79,82,3,36,18,0,80,82,
        3,50,25,0,81,71,1,0,0,0,81,72,1,0,0,0,81,73,1,0,0,0,81,74,1,0,0,
        0,81,75,1,0,0,0,81,76,1,0,0,0,81,77,1,0,0,0,81,78,1,0,0,0,81,79,
        1,0,0,0,81,80,1,0,0,0,82,3,1,0,0,0,83,84,5,1,0,0,84,85,3,52,26,0,
        85,86,3,50,25,0,86,87,3,54,27,0,87,5,1,0,0,0,88,93,5,48,0,0,89,90,
        5,2,0,0,90,94,3,50,25,0,91,94,3,22,11,0,92,94,3,30,15,0,93,89,1,
        0,0,0,93,91,1,0,0,0,93,92,1,0,0,0,93,94,1,0,0,0,94,7,1,0,0,0,95,
        99,3,10,5,0,96,97,3,56,28,0,97,98,3,58,29,0,98,100,1,0,0,0,99,96,
        1,0,0,0,99,100,1,0,0,0,100,9,1,0,0,0,101,102,7,0,0,0,102,11,1,0,
        0,0,103,104,5,6,0,0,104,105,3,52,26,0,105,106,3,50,25,0,106,107,
        3,54,27,0,107,111,3,60,30,0,108,110,3,2,1,0,109,108,1,0,0,0,110,
        113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,
        111,1,0,0,0,114,127,3,62,31,0,115,116,5,27,0,0,116,120,3,60,30,0,
        117,119,3,2,1,0,118,117,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,
        120,121,1,0,0,0,121,123,1,0,0,0,122,120,1,0,0,0,123,124,3,58,29,
        0,124,126,1,0,0,0,125,115,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,
        0,127,128,1,0,0,0,128,140,1,0,0,0,129,127,1,0,0,0,130,131,5,28,0,
        0,131,135,3,60,30,0,132,134,3,2,1,0,133,132,1,0,0,0,134,137,1,0,
        0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,135,1,0,
        0,0,138,139,3,62,31,0,139,141,1,0,0,0,140,130,1,0,0,0,140,141,1,
        0,0,0,141,13,1,0,0,0,142,143,5,7,0,0,143,144,3,6,3,0,144,145,5,8,
        0,0,145,146,3,50,25,0,146,150,3,60,30,0,147,149,3,2,1,0,148,147,
        1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,153,
        1,0,0,0,152,150,1,0,0,0,153,154,3,62,31,0,154,15,1,0,0,0,155,156,
        5,9,0,0,156,157,3,52,26,0,157,158,3,50,25,0,158,159,3,54,27,0,159,
        163,3,60,30,0,160,162,3,2,1,0,161,160,1,0,0,0,162,165,1,0,0,0,163,
        161,1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,163,1,0,0,0,166,
        167,3,62,31,0,167,17,1,0,0,0,168,169,5,10,0,0,169,170,5,48,0,0,170,
        172,3,52,26,0,171,173,3,26,13,0,172,171,1,0,0,0,172,173,1,0,0,0,
        173,174,1,0,0,0,174,175,3,54,27,0,175,179,3,60,30,0,176,178,3,2,
        1,0,177,176,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,
        0,0,180,182,1,0,0,0,181,179,1,0,0,0,182,183,3,62,31,0,183,19,1,0,
        0,0,184,185,5,48,0,0,185,187,3,52,26,0,186,188,3,30,15,0,187,186,
        1,0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,189,190,3,54,27,0,190,21,
        1,0,0,0,191,192,3,60,30,0,192,198,3,50,25,0,193,194,3,64,32,0,194,
        195,3,50,25,0,195,197,1,0,0,0,196,193,1,0,0,0,197,200,1,0,0,0,198,
        196,1,0,0,0,198,199,1,0,0,0,199,201,1,0,0,0,200,198,1,0,0,0,201,
        202,3,62,31,0,202,23,1,0,0,0,203,204,5,11,0,0,204,205,3,42,21,0,
        205,206,3,44,22,0,206,25,1,0,0,0,207,213,3,28,14,0,208,209,3,64,
        32,0,209,210,3,28,14,0,210,212,1,0,0,0,211,208,1,0,0,0,212,215,1,
        0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,27,1,0,0,0,215,213,1,0,
        0,0,216,217,3,8,4,0,217,218,5,48,0,0,218,29,1,0,0,0,219,225,3,50,
        25,0,220,221,3,64,32,0,221,222,3,50,25,0,222,224,1,0,0,0,223,220,
        1,0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,31,1,
        0,0,0,227,225,1,0,0,0,228,229,5,12,0,0,229,230,3,52,26,0,230,231,
        5,46,0,0,231,232,3,64,32,0,232,233,5,46,0,0,233,234,3,54,27,0,234,
        33,1,0,0,0,235,236,5,13,0,0,236,237,3,52,26,0,237,241,3,50,25,0,
        238,239,3,64,32,0,239,240,3,50,25,0,240,242,1,0,0,0,241,238,1,0,
        0,0,242,243,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,245,1,0,
        0,0,245,246,3,54,27,0,246,35,1,0,0,0,247,248,5,14,0,0,248,249,5,
        48,0,0,249,250,3,60,30,0,250,251,3,38,19,0,251,252,3,62,31,0,252,
        37,1,0,0,0,253,259,5,48,0,0,254,255,3,64,32,0,255,256,5,48,0,0,256,
        258,1,0,0,0,257,254,1,0,0,0,258,261,1,0,0,0,259,257,1,0,0,0,259,
        260,1,0,0,0,260,39,1,0,0,0,261,259,1,0,0,0,262,263,5,48,0,0,263,
        264,5,15,0,0,264,265,5,48,0,0,265,41,1,0,0,0,266,271,5,16,0,0,267,
        271,5,17,0,0,268,269,5,46,0,0,269,271,5,18,0,0,270,266,1,0,0,0,270,
        267,1,0,0,0,270,268,1,0,0,0,271,43,1,0,0,0,272,273,3,52,26,0,273,
        274,3,46,23,0,274,275,3,64,32,0,275,276,3,48,24,0,276,277,3,54,27,
        0,277,45,1,0,0,0,278,284,5,46,0,0,279,280,3,64,32,0,280,281,5,46,
        0,0,281,283,1,0,0,0,282,279,1,0,0,0,283,286,1,0,0,0,284,282,1,0,
        0,0,284,285,1,0,0,0,285,47,1,0,0,0,286,284,1,0,0,0,287,288,5,46,
        0,0,288,49,1,0,0,0,289,290,6,25,-1,0,290,291,5,42,0,0,291,305,3,
        50,25,10,292,293,3,52,26,0,293,294,3,50,25,0,294,295,3,54,27,0,295,
        305,1,0,0,0,296,305,5,48,0,0,297,305,5,47,0,0,298,305,5,46,0,0,299,
        305,5,43,0,0,300,305,5,44,0,0,301,305,3,32,16,0,302,305,3,34,17,
        0,303,305,3,40,20,0,304,289,1,0,0,0,304,292,1,0,0,0,304,296,1,0,
        0,0,304,297,1,0,0,0,304,298,1,0,0,0,304,299,1,0,0,0,304,300,1,0,
        0,0,304,301,1,0,0,0,304,302,1,0,0,0,304,303,1,0,0,0,305,338,1,0,
        0,0,306,307,10,16,0,0,307,308,3,56,28,0,308,309,3,50,25,0,309,310,
        3,58,29,0,310,311,5,2,0,0,311,312,3,50,25,17,312,337,1,0,0,0,313,
        314,10,14,0,0,314,315,7,1,0,0,315,337,3,50,25,15,316,317,10,13,0,
        0,317,318,7,2,0,0,318,337,3,50,25,14,319,320,10,12,0,0,320,321,7,
        3,0,0,321,337,3,50,25,13,322,323,10,11,0,0,323,324,7,4,0,0,324,337,
        3,50,25,12,325,326,10,17,0,0,326,327,3,56,28,0,327,328,3,50,25,0,
        328,329,3,58,29,0,329,337,1,0,0,0,330,331,10,15,0,0,331,332,5,19,
        0,0,332,333,3,52,26,0,333,334,3,50,25,0,334,335,3,54,27,0,335,337,
        1,0,0,0,336,306,1,0,0,0,336,313,1,0,0,0,336,316,1,0,0,0,336,319,
        1,0,0,0,336,322,1,0,0,0,336,325,1,0,0,0,336,330,1,0,0,0,337,340,
        1,0,0,0,338,336,1,0,0,0,338,339,1,0,0,0,339,51,1,0,0,0,340,338,1,
        0,0,0,341,342,5,20,0,0,342,53,1,0,0,0,343,344,5,21,0,0,344,55,1,
        0,0,0,345,346,5,22,0,0,346,57,1,0,0,0,347,348,5,23,0,0,348,59,1,
        0,0,0,349,350,5,24,0,0,350,61,1,0,0,0,351,352,5,25,0,0,352,63,1,
        0,0,0,353,354,5,26,0,0,354,65,1,0,0,0,24,69,81,93,99,111,120,127,
        135,140,150,163,172,179,187,198,213,225,243,259,270,284,304,336,
        338
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'='", "'string'", "'bool'", 
                     "'number'", "'if'", "'for'", "'in'", "'while'", "'def'", 
                     "'BSP'", "'randomNumber'", "'randomChoice'", "'enum'", 
                     "'.'", "'2D'", "'3D'", "'D'", "'.add'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "'elif'", "'else'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'>='", "'<'", "'<='", 
                     "'=='", "'!='", "'%'", "'and'", "'or'", "'not'", "'true'", 
                     "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ELIF", "ELSE", 
                      "PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", "LT", 
                      "LTE", "EQ", "NEQ", "MOD", "AND", "OR", "NOT", "TRUE", 
                      "FALSE", "COMMENT_SINGLELINE", "NUMBER", "STRING", 
                      "ID", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_printStat = 2
    RULE_varDecl = 3
    RULE_dataType = 4
    RULE_baseType = 5
    RULE_ifStat = 6
    RULE_forLoop = 7
    RULE_whileLoop = 8
    RULE_functionDecl = 9
    RULE_functionCall = 10
    RULE_arrayInit = 11
    RULE_bsp = 12
    RULE_params = 13
    RULE_param = 14
    RULE_args = 15
    RULE_randomNumber = 16
    RULE_randomChoice = 17
    RULE_enumDecl = 18
    RULE_enumBody = 19
    RULE_enumValue = 20
    RULE_bspDimension = 21
    RULE_bspParameters = 22
    RULE_dimensionList = 23
    RULE_minSize = 24
    RULE_expr = 25
    RULE_openParenth = 26
    RULE_closedParenth = 27
    RULE_openBrack = 28
    RULE_closedBrack = 29
    RULE_openCurlBrack = 30
    RULE_closedCurlBrack = 31
    RULE_comma = 32

    ruleNames =  [ "prog", "stat", "printStat", "varDecl", "dataType", "baseType", 
                   "ifStat", "forLoop", "whileLoop", "functionDecl", "functionCall", 
                   "arrayInit", "bsp", "params", "param", "args", "randomNumber", 
                   "randomChoice", "enumDecl", "enumBody", "enumValue", 
                   "bspDimension", "bspParameters", "dimensionList", "minSize", 
                   "expr", "openParenth", "closedParenth", "openBrack", 
                   "closedBrack", "openCurlBrack", "closedCurlBrack", "comma" ]

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
    ELIF=27
    ELSE=28
    PLUS=29
    MINUS=30
    MULT=31
    DIV=32
    GT=33
    GTE=34
    LT=35
    LTE=36
    EQ=37
    NEQ=38
    MOD=39
    AND=40
    OR=41
    NOT=42
    TRUE=43
    FALSE=44
    COMMENT_SINGLELINE=45
    NUMBER=46
    STRING=47
    ID=48
    WS=49

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
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.stat()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 523367552677570) != 0)):
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
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.ifStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 76
                self.functionDecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.functionCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 78
                self.arrayInit()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 79
                self.enumDecl()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 80
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

        def openParenth(self):
            return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,0)


        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def closedParenth(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,0)


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
            self.state = 83
            self.match(RogueLangParser.T__0)
            self.state = 84
            self.openParenth()
            self.state = 85
            self.expr(0)
            self.state = 86
            self.closedParenth()
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
            self.state = 88
            self.match(RogueLangParser.ID)
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 89
                self.match(RogueLangParser.T__1)
                self.state = 90
                self.expr(0)

            elif la_ == 2:
                self.state = 91
                self.arrayInit()

            elif la_ == 3:
                self.state = 92
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


        def openBrack(self):
            return self.getTypedRuleContext(RogueLangParser.OpenBrackContext,0)


        def closedBrack(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedBrackContext,0)


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
            self.state = 95
            self.baseType()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 96
                self.openBrack()
                self.state = 97
                self.closedBrack()


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
            self.state = 101
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 307863255777336) != 0)):
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

        def openParenth(self):
            return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,0)


        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def closedParenth(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,0)


        def openCurlBrack(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.OpenCurlBrackContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.OpenCurlBrackContext,i)


        def closedCurlBrack(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ClosedCurlBrackContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ClosedCurlBrackContext,i)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.ELIF)
            else:
                return self.getToken(RogueLangParser.ELIF, i)

        def closedBrack(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ClosedBrackContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ClosedBrackContext,i)


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
        self.enterRule(localctx, 12, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(RogueLangParser.T__5)
            self.state = 104
            self.openParenth()
            self.state = 105
            self.expr(0)
            self.state = 106
            self.closedParenth()
            self.state = 107
            self.openCurlBrack()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367552677570) != 0):
                self.state = 108
                self.stat()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.closedCurlBrack()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 115
                self.match(RogueLangParser.ELIF)
                self.state = 116
                self.openCurlBrack()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367552677570) != 0):
                    self.state = 117
                    self.stat()
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 123
                self.closedBrack()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 130
                self.match(RogueLangParser.ELSE)
                self.state = 131
                self.openCurlBrack()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367552677570) != 0):
                    self.state = 132
                    self.stat()
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 138
                self.closedCurlBrack()


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


        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def openCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.OpenCurlBrackContext,0)


        def closedCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedCurlBrackContext,0)


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
            self.state = 142
            self.match(RogueLangParser.T__6)
            self.state = 143
            self.varDecl()
            self.state = 144
            self.match(RogueLangParser.T__7)
            self.state = 145
            self.expr(0)
            self.state = 146
            self.openCurlBrack()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367552677570) != 0):
                self.state = 147
                self.stat()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.closedCurlBrack()
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

        def openParenth(self):
            return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,0)


        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def closedParenth(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,0)


        def openCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.OpenCurlBrackContext,0)


        def closedCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedCurlBrackContext,0)


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
        self.enterRule(localctx, 16, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(RogueLangParser.T__8)
            self.state = 156
            self.openParenth()
            self.state = 157
            self.expr(0)
            self.state = 158
            self.closedParenth()
            self.state = 159
            self.openCurlBrack()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367552677570) != 0):
                self.state = 160
                self.stat()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self.closedCurlBrack()
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

        def openParenth(self):
            return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,0)


        def closedParenth(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,0)


        def openCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.OpenCurlBrackContext,0)


        def closedCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedCurlBrackContext,0)


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
        self.enterRule(localctx, 18, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(RogueLangParser.T__9)
            self.state = 169
            self.match(RogueLangParser.ID)
            self.state = 170
            self.openParenth()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 307863255777336) != 0):
                self.state = 171
                self.params()


            self.state = 174
            self.closedParenth()
            self.state = 175
            self.openCurlBrack()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367552677570) != 0):
                self.state = 176
                self.stat()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self.closedCurlBrack()
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

        def openParenth(self):
            return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,0)


        def closedParenth(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,0)


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
            self.state = 184
            self.match(RogueLangParser.ID)
            self.state = 185
            self.openParenth()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367535882240) != 0):
                self.state = 186
                self.args()


            self.state = 189
            self.closedParenth()
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

        def openCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.OpenCurlBrackContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def closedCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedCurlBrackContext,0)


        def comma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.CommaContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.CommaContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_arrayInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayInit" ):
                return visitor.visitArrayInit(self)
            else:
                return visitor.visitChildren(self)




    def arrayInit(self):

        localctx = RogueLangParser.ArrayInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.openCurlBrack()
            self.state = 192
            self.expr(0)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 193
                self.comma()
                self.state = 194
                self.expr(0)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.closedCurlBrack()
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
        self.enterRule(localctx, 24, self.RULE_bsp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(RogueLangParser.T__10)
            self.state = 204
            self.bspDimension()
            self.state = 205
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


        def comma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.CommaContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.CommaContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = RogueLangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.param()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 208
                self.comma()
                self.state = 209
                self.param()
                self.state = 215
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
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.dataType()
            self.state = 217
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


        def comma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.CommaContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.CommaContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = RogueLangParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.expr(0)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 220
                self.comma()
                self.state = 221
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


    class RandomNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def openParenth(self):
            return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,0)


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.NUMBER)
            else:
                return self.getToken(RogueLangParser.NUMBER, i)

        def comma(self):
            return self.getTypedRuleContext(RogueLangParser.CommaContext,0)


        def closedParenth(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_randomNumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandomNumber" ):
                return visitor.visitRandomNumber(self)
            else:
                return visitor.visitChildren(self)




    def randomNumber(self):

        localctx = RogueLangParser.RandomNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_randomNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(RogueLangParser.T__11)
            self.state = 229
            self.openParenth()
            self.state = 230
            self.match(RogueLangParser.NUMBER)
            self.state = 231
            self.comma()
            self.state = 232
            self.match(RogueLangParser.NUMBER)
            self.state = 233
            self.closedParenth()
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

        def openParenth(self):
            return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def closedParenth(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,0)


        def comma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.CommaContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.CommaContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_randomChoice

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandomChoice" ):
                return visitor.visitRandomChoice(self)
            else:
                return visitor.visitChildren(self)




    def randomChoice(self):

        localctx = RogueLangParser.RandomChoiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_randomChoice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(RogueLangParser.T__12)
            self.state = 236
            self.openParenth()
            self.state = 237
            self.expr(0)
            self.state = 241 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 238
                self.comma()
                self.state = 239
                self.expr(0)
                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==26):
                    break

            self.state = 245
            self.closedParenth()
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

        def openCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.OpenCurlBrackContext,0)


        def enumBody(self):
            return self.getTypedRuleContext(RogueLangParser.EnumBodyContext,0)


        def closedCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedCurlBrackContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_enumDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDecl" ):
                return visitor.visitEnumDecl(self)
            else:
                return visitor.visitChildren(self)




    def enumDecl(self):

        localctx = RogueLangParser.EnumDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_enumDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(RogueLangParser.T__13)
            self.state = 248
            self.match(RogueLangParser.ID)
            self.state = 249
            self.openCurlBrack()
            self.state = 250
            self.enumBody()
            self.state = 251
            self.closedCurlBrack()
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

        def comma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.CommaContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.CommaContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_enumBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumBody" ):
                return visitor.visitEnumBody(self)
            else:
                return visitor.visitChildren(self)




    def enumBody(self):

        localctx = RogueLangParser.EnumBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_enumBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(RogueLangParser.ID)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 254
                self.comma()
                self.state = 255
                self.match(RogueLangParser.ID)
                self.state = 261
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
        self.enterRule(localctx, 40, self.RULE_enumValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(RogueLangParser.ID)
            self.state = 263
            self.match(RogueLangParser.T__14)
            self.state = 264
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
        self.enterRule(localctx, 42, self.RULE_bspDimension)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(RogueLangParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.match(RogueLangParser.T__16)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.match(RogueLangParser.NUMBER)
                self.state = 269
                self.match(RogueLangParser.T__17)
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

        def openParenth(self):
            return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,0)


        def dimensionList(self):
            return self.getTypedRuleContext(RogueLangParser.DimensionListContext,0)


        def comma(self):
            return self.getTypedRuleContext(RogueLangParser.CommaContext,0)


        def minSize(self):
            return self.getTypedRuleContext(RogueLangParser.MinSizeContext,0)


        def closedParenth(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_bspParameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBspParameters" ):
                return visitor.visitBspParameters(self)
            else:
                return visitor.visitChildren(self)




    def bspParameters(self):

        localctx = RogueLangParser.BspParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_bspParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.openParenth()
            self.state = 273
            self.dimensionList()
            self.state = 274
            self.comma()
            self.state = 275
            self.minSize()
            self.state = 276
            self.closedParenth()
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

        def comma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.CommaContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.CommaContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_dimensionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensionList" ):
                return visitor.visitDimensionList(self)
            else:
                return visitor.visitChildren(self)




    def dimensionList(self):

        localctx = RogueLangParser.DimensionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_dimensionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(RogueLangParser.NUMBER)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 279
                    self.comma()
                    self.state = 280
                    self.match(RogueLangParser.NUMBER) 
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_minSize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
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


        def openParenth(self):
            return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,0)


        def closedParenth(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,0)


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


        def openBrack(self):
            return self.getTypedRuleContext(RogueLangParser.OpenBrackContext,0)


        def closedBrack(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedBrackContext,0)


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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 290
                self.match(RogueLangParser.NOT)
                self.state = 291
                self.expr(10)
                pass

            elif la_ == 2:
                self.state = 292
                self.openParenth()
                self.state = 293
                self.expr(0)
                self.state = 294
                self.closedParenth()
                pass

            elif la_ == 3:
                self.state = 296
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 4:
                self.state = 297
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 5:
                self.state = 298
                self.match(RogueLangParser.NUMBER)
                pass

            elif la_ == 6:
                self.state = 299
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 7:
                self.state = 300
                self.match(RogueLangParser.FALSE)
                pass

            elif la_ == 8:
                self.state = 301
                self.randomNumber()
                pass

            elif la_ == 9:
                self.state = 302
                self.randomChoice()
                pass

            elif la_ == 10:
                self.state = 303
                self.enumValue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 336
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 306
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 307
                        self.openBrack()
                        self.state = 308
                        self.expr(0)
                        self.state = 309
                        self.closedBrack()
                        self.state = 310
                        self.match(RogueLangParser.T__1)
                        self.state = 311
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 313
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 314
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 556198264832) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 315
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 316
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 317
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==30):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 318
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 319
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 320
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 541165879296) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 321
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 322
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 323
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==40 or _la==41):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 324
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 325
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 326
                        self.openBrack()
                        self.state = 327
                        self.expr(0)
                        self.state = 328
                        self.closedBrack()
                        pass

                    elif la_ == 7:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 330
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 331
                        self.match(RogueLangParser.T__18)
                        self.state = 332
                        self.openParenth()
                        self.state = 333
                        self.expr(0)
                        self.state = 334
                        self.closedParenth()
                        pass

             
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpenParenthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RogueLangParser.RULE_openParenth

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpenParenth" ):
                return visitor.visitOpenParenth(self)
            else:
                return visitor.visitChildren(self)




    def openParenth(self):

        localctx = RogueLangParser.OpenParenthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_openParenth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(RogueLangParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClosedParenthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RogueLangParser.RULE_closedParenth

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosedParenth" ):
                return visitor.visitClosedParenth(self)
            else:
                return visitor.visitChildren(self)




    def closedParenth(self):

        localctx = RogueLangParser.ClosedParenthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_closedParenth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(RogueLangParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpenBrackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RogueLangParser.RULE_openBrack

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpenBrack" ):
                return visitor.visitOpenBrack(self)
            else:
                return visitor.visitChildren(self)




    def openBrack(self):

        localctx = RogueLangParser.OpenBrackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_openBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(RogueLangParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClosedBrackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RogueLangParser.RULE_closedBrack

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosedBrack" ):
                return visitor.visitClosedBrack(self)
            else:
                return visitor.visitChildren(self)




    def closedBrack(self):

        localctx = RogueLangParser.ClosedBrackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_closedBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(RogueLangParser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpenCurlBrackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RogueLangParser.RULE_openCurlBrack

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpenCurlBrack" ):
                return visitor.visitOpenCurlBrack(self)
            else:
                return visitor.visitChildren(self)




    def openCurlBrack(self):

        localctx = RogueLangParser.OpenCurlBrackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_openCurlBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(RogueLangParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClosedCurlBrackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RogueLangParser.RULE_closedCurlBrack

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosedCurlBrack" ):
                return visitor.visitClosedCurlBrack(self)
            else:
                return visitor.visitChildren(self)




    def closedCurlBrack(self):

        localctx = RogueLangParser.ClosedCurlBrackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_closedCurlBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(RogueLangParser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RogueLangParser.RULE_comma

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma" ):
                return visitor.visitComma(self)
            else:
                return visitor.visitChildren(self)




    def comma(self):

        localctx = RogueLangParser.CommaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_comma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(RogueLangParser.T__25)
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
        self._predicates[25] = self.expr_sempred
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
         




