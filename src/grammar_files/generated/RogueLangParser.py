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
        4,1,49,362,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,4,0,70,8,0,11,0,12,0,71,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,84,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,96,
        8,3,1,4,1,4,1,4,1,4,3,4,102,8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        5,6,112,8,6,10,6,12,6,115,9,6,1,6,1,6,5,6,119,8,6,10,6,12,6,122,
        9,6,1,6,1,6,1,6,5,6,127,8,6,10,6,12,6,130,9,6,1,6,1,6,3,6,134,8,
        6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,142,8,7,10,7,12,7,145,9,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,8,1,8,5,8,155,8,8,10,8,12,8,158,9,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,5,9,168,8,9,10,9,12,9,171,9,9,1,9,1,9,1,10,
        1,10,1,10,1,10,3,10,179,8,10,1,10,1,10,1,10,5,10,184,8,10,10,10,
        12,10,187,9,10,1,10,1,10,1,11,1,11,1,11,3,11,194,8,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,5,12,203,8,12,10,12,12,12,206,9,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,5,14,218,8,14,10,14,
        12,14,221,9,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,5,16,230,8,16,
        10,16,12,16,233,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,
        1,18,1,18,1,18,1,18,4,18,248,8,18,11,18,12,18,249,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,5,20,264,8,20,10,20,
        12,20,267,9,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,277,
        8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,5,24,289,
        8,24,10,24,12,24,292,9,24,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,311,8,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,5,26,343,8,26,10,26,12,26,346,9,26,1,27,1,27,1,28,
        1,28,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,33,0,1,
        52,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,0,5,3,0,3,5,43,44,48,48,2,
        0,31,32,39,39,1,0,29,30,1,0,33,38,1,0,40,41,375,0,69,1,0,0,0,2,83,
        1,0,0,0,4,85,1,0,0,0,6,90,1,0,0,0,8,97,1,0,0,0,10,103,1,0,0,0,12,
        105,1,0,0,0,14,135,1,0,0,0,16,148,1,0,0,0,18,161,1,0,0,0,20,174,
        1,0,0,0,22,190,1,0,0,0,24,197,1,0,0,0,26,209,1,0,0,0,28,213,1,0,
        0,0,30,222,1,0,0,0,32,225,1,0,0,0,34,234,1,0,0,0,36,241,1,0,0,0,
        38,253,1,0,0,0,40,259,1,0,0,0,42,268,1,0,0,0,44,276,1,0,0,0,46,278,
        1,0,0,0,48,284,1,0,0,0,50,293,1,0,0,0,52,310,1,0,0,0,54,347,1,0,
        0,0,56,349,1,0,0,0,58,351,1,0,0,0,60,353,1,0,0,0,62,355,1,0,0,0,
        64,357,1,0,0,0,66,359,1,0,0,0,68,70,3,2,1,0,69,68,1,0,0,0,70,71,
        1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,1,1,0,0,0,73,84,3,4,2,0,74,
        84,3,6,3,0,75,84,3,12,6,0,76,84,3,16,8,0,77,84,3,18,9,0,78,84,3,
        20,10,0,79,84,3,22,11,0,80,84,3,24,12,0,81,84,3,38,19,0,82,84,3,
        52,26,0,83,73,1,0,0,0,83,74,1,0,0,0,83,75,1,0,0,0,83,76,1,0,0,0,
        83,77,1,0,0,0,83,78,1,0,0,0,83,79,1,0,0,0,83,80,1,0,0,0,83,81,1,
        0,0,0,83,82,1,0,0,0,84,3,1,0,0,0,85,86,5,1,0,0,86,87,3,54,27,0,87,
        88,3,52,26,0,88,89,3,56,28,0,89,5,1,0,0,0,90,95,5,48,0,0,91,92,5,
        2,0,0,92,96,3,52,26,0,93,96,3,24,12,0,94,96,3,32,16,0,95,91,1,0,
        0,0,95,93,1,0,0,0,95,94,1,0,0,0,95,96,1,0,0,0,96,7,1,0,0,0,97,101,
        3,10,5,0,98,99,3,58,29,0,99,100,3,60,30,0,100,102,1,0,0,0,101,98,
        1,0,0,0,101,102,1,0,0,0,102,9,1,0,0,0,103,104,7,0,0,0,104,11,1,0,
        0,0,105,106,5,6,0,0,106,107,3,54,27,0,107,108,3,52,26,0,108,109,
        3,56,28,0,109,113,3,62,31,0,110,112,3,2,1,0,111,110,1,0,0,0,112,
        115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,
        113,1,0,0,0,116,120,3,64,32,0,117,119,3,14,7,0,118,117,1,0,0,0,119,
        122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,133,1,0,0,0,122,
        120,1,0,0,0,123,124,5,7,0,0,124,128,3,62,31,0,125,127,3,2,1,0,126,
        125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,
        131,1,0,0,0,130,128,1,0,0,0,131,132,3,64,32,0,132,134,1,0,0,0,133,
        123,1,0,0,0,133,134,1,0,0,0,134,13,1,0,0,0,135,136,5,8,0,0,136,137,
        3,54,27,0,137,138,3,52,26,0,138,139,3,56,28,0,139,143,3,62,31,0,
        140,142,3,2,1,0,141,140,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,
        143,144,1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,147,3,64,32,
        0,147,15,1,0,0,0,148,149,5,9,0,0,149,150,3,6,3,0,150,151,5,10,0,
        0,151,152,3,52,26,0,152,156,3,62,31,0,153,155,3,2,1,0,154,153,1,
        0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,159,1,
        0,0,0,158,156,1,0,0,0,159,160,3,64,32,0,160,17,1,0,0,0,161,162,5,
        11,0,0,162,163,3,54,27,0,163,164,3,52,26,0,164,165,3,56,28,0,165,
        169,3,62,31,0,166,168,3,2,1,0,167,166,1,0,0,0,168,171,1,0,0,0,169,
        167,1,0,0,0,169,170,1,0,0,0,170,172,1,0,0,0,171,169,1,0,0,0,172,
        173,3,64,32,0,173,19,1,0,0,0,174,175,5,12,0,0,175,176,5,48,0,0,176,
        178,3,54,27,0,177,179,3,28,14,0,178,177,1,0,0,0,178,179,1,0,0,0,
        179,180,1,0,0,0,180,181,3,56,28,0,181,185,3,62,31,0,182,184,3,2,
        1,0,183,182,1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,
        0,0,186,188,1,0,0,0,187,185,1,0,0,0,188,189,3,64,32,0,189,21,1,0,
        0,0,190,191,5,48,0,0,191,193,3,54,27,0,192,194,3,32,16,0,193,192,
        1,0,0,0,193,194,1,0,0,0,194,195,1,0,0,0,195,196,3,56,28,0,196,23,
        1,0,0,0,197,198,3,62,31,0,198,204,3,52,26,0,199,200,3,66,33,0,200,
        201,3,52,26,0,201,203,1,0,0,0,202,199,1,0,0,0,203,206,1,0,0,0,204,
        202,1,0,0,0,204,205,1,0,0,0,205,207,1,0,0,0,206,204,1,0,0,0,207,
        208,3,64,32,0,208,25,1,0,0,0,209,210,5,13,0,0,210,211,3,44,22,0,
        211,212,3,46,23,0,212,27,1,0,0,0,213,219,3,30,15,0,214,215,3,66,
        33,0,215,216,3,30,15,0,216,218,1,0,0,0,217,214,1,0,0,0,218,221,1,
        0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,29,1,0,0,0,221,219,1,0,
        0,0,222,223,3,8,4,0,223,224,5,48,0,0,224,31,1,0,0,0,225,231,3,52,
        26,0,226,227,3,66,33,0,227,228,3,52,26,0,228,230,1,0,0,0,229,226,
        1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,33,1,
        0,0,0,233,231,1,0,0,0,234,235,5,14,0,0,235,236,3,54,27,0,236,237,
        5,46,0,0,237,238,3,66,33,0,238,239,5,46,0,0,239,240,3,56,28,0,240,
        35,1,0,0,0,241,242,5,15,0,0,242,243,3,54,27,0,243,247,3,52,26,0,
        244,245,3,66,33,0,245,246,3,52,26,0,246,248,1,0,0,0,247,244,1,0,
        0,0,248,249,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,251,1,0,
        0,0,251,252,3,56,28,0,252,37,1,0,0,0,253,254,5,16,0,0,254,255,5,
        48,0,0,255,256,3,62,31,0,256,257,3,40,20,0,257,258,3,64,32,0,258,
        39,1,0,0,0,259,265,5,48,0,0,260,261,3,66,33,0,261,262,5,48,0,0,262,
        264,1,0,0,0,263,260,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,
        266,1,0,0,0,266,41,1,0,0,0,267,265,1,0,0,0,268,269,5,48,0,0,269,
        270,5,17,0,0,270,271,5,48,0,0,271,43,1,0,0,0,272,277,5,18,0,0,273,
        277,5,19,0,0,274,275,5,46,0,0,275,277,5,20,0,0,276,272,1,0,0,0,276,
        273,1,0,0,0,276,274,1,0,0,0,277,45,1,0,0,0,278,279,3,54,27,0,279,
        280,3,48,24,0,280,281,3,66,33,0,281,282,3,50,25,0,282,283,3,56,28,
        0,283,47,1,0,0,0,284,290,5,46,0,0,285,286,3,66,33,0,286,287,5,46,
        0,0,287,289,1,0,0,0,288,285,1,0,0,0,289,292,1,0,0,0,290,288,1,0,
        0,0,290,291,1,0,0,0,291,49,1,0,0,0,292,290,1,0,0,0,293,294,5,46,
        0,0,294,51,1,0,0,0,295,296,6,26,-1,0,296,297,5,42,0,0,297,311,3,
        52,26,10,298,299,3,54,27,0,299,300,3,52,26,0,300,301,3,56,28,0,301,
        311,1,0,0,0,302,311,5,48,0,0,303,311,5,47,0,0,304,311,5,46,0,0,305,
        311,5,43,0,0,306,311,5,44,0,0,307,311,3,34,17,0,308,311,3,36,18,
        0,309,311,3,42,21,0,310,295,1,0,0,0,310,298,1,0,0,0,310,302,1,0,
        0,0,310,303,1,0,0,0,310,304,1,0,0,0,310,305,1,0,0,0,310,306,1,0,
        0,0,310,307,1,0,0,0,310,308,1,0,0,0,310,309,1,0,0,0,311,344,1,0,
        0,0,312,313,10,16,0,0,313,314,3,58,29,0,314,315,3,52,26,0,315,316,
        3,60,30,0,316,317,5,2,0,0,317,318,3,52,26,17,318,343,1,0,0,0,319,
        320,10,14,0,0,320,321,7,1,0,0,321,343,3,52,26,15,322,323,10,13,0,
        0,323,324,7,2,0,0,324,343,3,52,26,14,325,326,10,12,0,0,326,327,7,
        3,0,0,327,343,3,52,26,13,328,329,10,11,0,0,329,330,7,4,0,0,330,343,
        3,52,26,12,331,332,10,17,0,0,332,333,3,58,29,0,333,334,3,52,26,0,
        334,335,3,60,30,0,335,343,1,0,0,0,336,337,10,15,0,0,337,338,5,21,
        0,0,338,339,3,54,27,0,339,340,3,52,26,0,340,341,3,56,28,0,341,343,
        1,0,0,0,342,312,1,0,0,0,342,319,1,0,0,0,342,322,1,0,0,0,342,325,
        1,0,0,0,342,328,1,0,0,0,342,331,1,0,0,0,342,336,1,0,0,0,343,346,
        1,0,0,0,344,342,1,0,0,0,344,345,1,0,0,0,345,53,1,0,0,0,346,344,1,
        0,0,0,347,348,5,22,0,0,348,55,1,0,0,0,349,350,5,23,0,0,350,57,1,
        0,0,0,351,352,5,24,0,0,352,59,1,0,0,0,353,354,5,25,0,0,354,61,1,
        0,0,0,355,356,5,26,0,0,356,63,1,0,0,0,357,358,5,27,0,0,358,65,1,
        0,0,0,359,360,5,28,0,0,360,67,1,0,0,0,24,71,83,95,101,113,120,128,
        133,143,156,169,178,185,193,204,219,231,249,265,276,290,310,342,
        344
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'='", "'string'", "'bool'", 
                     "'number'", "'if'", "'else'", "'elif'", "'for'", "'in'", 
                     "'while'", "'def'", "'BSP'", "'randomNumber'", "'randomChoice'", 
                     "'enum'", "'.'", "'2D'", "'3D'", "'D'", "'.add'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "','", "'+'", "'-'", 
                     "'*'", "'/'", "'>'", "'>='", "'<'", "'<='", "'=='", 
                     "'!='", "'%'", "'and'", "'or'", "'not'", "'true'", 
                     "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PLUS", "MINUS", "MULT", "DIV", "GT", 
                      "GTE", "LT", "LTE", "EQ", "NEQ", "MOD", "AND", "OR", 
                      "NOT", "TRUE", "FALSE", "COMMENT_SINGLELINE", "NUMBER", 
                      "STRING", "ID", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_printStat = 2
    RULE_varDecl = 3
    RULE_dataType = 4
    RULE_baseType = 5
    RULE_ifStat = 6
    RULE_elifStat = 7
    RULE_forLoop = 8
    RULE_whileLoop = 9
    RULE_functionDecl = 10
    RULE_functionCall = 11
    RULE_arrayInit = 12
    RULE_bsp = 13
    RULE_params = 14
    RULE_param = 15
    RULE_args = 16
    RULE_randomNumber = 17
    RULE_randomChoice = 18
    RULE_enumDecl = 19
    RULE_enumBody = 20
    RULE_enumValue = 21
    RULE_bspDimension = 22
    RULE_bspParameters = 23
    RULE_dimensionList = 24
    RULE_minSize = 25
    RULE_expr = 26
    RULE_openParenth = 27
    RULE_closedParenth = 28
    RULE_openBrack = 29
    RULE_closedBrack = 30
    RULE_openCurlBrack = 31
    RULE_closedCurlBrack = 32
    RULE_comma = 33

    ruleNames =  [ "prog", "stat", "printStat", "varDecl", "dataType", "baseType", 
                   "ifStat", "elifStat", "forLoop", "whileLoop", "functionDecl", 
                   "functionCall", "arrayInit", "bsp", "params", "param", 
                   "args", "randomNumber", "randomChoice", "enumDecl", "enumBody", 
                   "enumValue", "bspDimension", "bspParameters", "dimensionList", 
                   "minSize", "expr", "openParenth", "closedParenth", "openBrack", 
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
    T__26=27
    T__27=28
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
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.stat()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 523367606245954) != 0)):
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
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.ifStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.functionDecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 79
                self.functionCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 80
                self.arrayInit()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 81
                self.enumDecl()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 82
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
            self.state = 85
            self.match(RogueLangParser.T__0)
            self.state = 86
            self.openParenth()
            self.state = 87
            self.expr(0)
            self.state = 88
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
            self.state = 90
            self.match(RogueLangParser.ID)
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 91
                self.match(RogueLangParser.T__1)
                self.state = 92
                self.expr(0)

            elif la_ == 2:
                self.state = 93
                self.arrayInit()

            elif la_ == 3:
                self.state = 94
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
            self.state = 97
            self.baseType()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 98
                self.openBrack()
                self.state = 99
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
            self.state = 103
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


        def elifStat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ElifStatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ElifStatContext,i)


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
            self.state = 105
            self.match(RogueLangParser.T__5)
            self.state = 106
            self.openParenth()
            self.state = 107
            self.expr(0)
            self.state = 108
            self.closedParenth()
            self.state = 109
            self.openCurlBrack()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367606245954) != 0):
                self.state = 110
                self.stat()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.closedCurlBrack()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 117
                self.elifStat()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 123
                self.match(RogueLangParser.T__6)
                self.state = 124
                self.openCurlBrack()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367606245954) != 0):
                    self.state = 125
                    self.stat()
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 131
                self.closedCurlBrack()


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
            return RogueLangParser.RULE_elifStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifStat" ):
                return visitor.visitElifStat(self)
            else:
                return visitor.visitChildren(self)




    def elifStat(self):

        localctx = RogueLangParser.ElifStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(RogueLangParser.T__7)
            self.state = 136
            self.openParenth()
            self.state = 137
            self.expr(0)
            self.state = 138
            self.closedParenth()
            self.state = 139
            self.openCurlBrack()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367606245954) != 0):
                self.state = 140
                self.stat()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
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
        self.enterRule(localctx, 16, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(RogueLangParser.T__8)
            self.state = 149
            self.varDecl()
            self.state = 150
            self.match(RogueLangParser.T__9)
            self.state = 151
            self.expr(0)
            self.state = 152
            self.openCurlBrack()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367606245954) != 0):
                self.state = 153
                self.stat()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
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
        self.enterRule(localctx, 18, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(RogueLangParser.T__10)
            self.state = 162
            self.openParenth()
            self.state = 163
            self.expr(0)
            self.state = 164
            self.closedParenth()
            self.state = 165
            self.openCurlBrack()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367606245954) != 0):
                self.state = 166
                self.stat()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
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
        self.enterRule(localctx, 20, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(RogueLangParser.T__11)
            self.state = 175
            self.match(RogueLangParser.ID)
            self.state = 176
            self.openParenth()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 307863255777336) != 0):
                self.state = 177
                self.params()


            self.state = 180
            self.closedParenth()
            self.state = 181
            self.openCurlBrack()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367606245954) != 0):
                self.state = 182
                self.stat()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
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
        self.enterRule(localctx, 22, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(RogueLangParser.ID)
            self.state = 191
            self.openParenth()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 523367539064832) != 0):
                self.state = 192
                self.args()


            self.state = 195
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
        self.enterRule(localctx, 24, self.RULE_arrayInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.openCurlBrack()
            self.state = 198
            self.expr(0)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 199
                self.comma()
                self.state = 200
                self.expr(0)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
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
        self.enterRule(localctx, 26, self.RULE_bsp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(RogueLangParser.T__12)
            self.state = 210
            self.bspDimension()
            self.state = 211
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
        self.enterRule(localctx, 28, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.param()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 214
                self.comma()
                self.state = 215
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
            self.state = 222
            self.dataType()
            self.state = 223
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
        self.enterRule(localctx, 32, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.expr(0)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 226
                self.comma()
                self.state = 227
                self.expr(0)
                self.state = 233
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
        self.enterRule(localctx, 34, self.RULE_randomNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(RogueLangParser.T__13)
            self.state = 235
            self.openParenth()
            self.state = 236
            self.match(RogueLangParser.NUMBER)
            self.state = 237
            self.comma()
            self.state = 238
            self.match(RogueLangParser.NUMBER)
            self.state = 239
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
        self.enterRule(localctx, 36, self.RULE_randomChoice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(RogueLangParser.T__14)
            self.state = 242
            self.openParenth()
            self.state = 243
            self.expr(0)
            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 244
                self.comma()
                self.state = 245
                self.expr(0)
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==28):
                    break

            self.state = 251
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
        self.enterRule(localctx, 38, self.RULE_enumDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(RogueLangParser.T__15)
            self.state = 254
            self.match(RogueLangParser.ID)
            self.state = 255
            self.openCurlBrack()
            self.state = 256
            self.enumBody()
            self.state = 257
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
        self.enterRule(localctx, 40, self.RULE_enumBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(RogueLangParser.ID)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 260
                self.comma()
                self.state = 261
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
        self.enterRule(localctx, 42, self.RULE_enumValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(RogueLangParser.ID)
            self.state = 269
            self.match(RogueLangParser.T__16)
            self.state = 270
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
        self.enterRule(localctx, 44, self.RULE_bspDimension)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(RogueLangParser.T__17)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(RogueLangParser.T__18)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 274
                self.match(RogueLangParser.NUMBER)
                self.state = 275
                self.match(RogueLangParser.T__19)
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
        self.enterRule(localctx, 46, self.RULE_bspParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.openParenth()
            self.state = 279
            self.dimensionList()
            self.state = 280
            self.comma()
            self.state = 281
            self.minSize()
            self.state = 282
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
        self.enterRule(localctx, 48, self.RULE_dimensionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(RogueLangParser.NUMBER)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 285
                    self.comma()
                    self.state = 286
                    self.match(RogueLangParser.NUMBER) 
                self.state = 292
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
        self.enterRule(localctx, 50, self.RULE_minSize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 296
                self.match(RogueLangParser.NOT)
                self.state = 297
                self.expr(10)
                pass

            elif la_ == 2:
                self.state = 298
                self.openParenth()
                self.state = 299
                self.expr(0)
                self.state = 300
                self.closedParenth()
                pass

            elif la_ == 3:
                self.state = 302
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 4:
                self.state = 303
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 5:
                self.state = 304
                self.match(RogueLangParser.NUMBER)
                pass

            elif la_ == 6:
                self.state = 305
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 7:
                self.state = 306
                self.match(RogueLangParser.FALSE)
                pass

            elif la_ == 8:
                self.state = 307
                self.randomNumber()
                pass

            elif la_ == 9:
                self.state = 308
                self.randomChoice()
                pass

            elif la_ == 10:
                self.state = 309
                self.enumValue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 342
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 312
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 313
                        self.openBrack()
                        self.state = 314
                        self.expr(0)
                        self.state = 315
                        self.closedBrack()
                        self.state = 316
                        self.match(RogueLangParser.T__1)
                        self.state = 317
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 319
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 320
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 556198264832) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 321
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 322
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 323
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==30):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 324
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 325
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 326
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 541165879296) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 327
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 328
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 329
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==40 or _la==41):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 330
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 331
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 332
                        self.openBrack()
                        self.state = 333
                        self.expr(0)
                        self.state = 334
                        self.closedBrack()
                        pass

                    elif la_ == 7:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 336
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 337
                        self.match(RogueLangParser.T__20)
                        self.state = 338
                        self.openParenth()
                        self.state = 339
                        self.expr(0)
                        self.state = 340
                        self.closedParenth()
                        pass

             
                self.state = 346
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
        self.enterRule(localctx, 54, self.RULE_openParenth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(RogueLangParser.T__21)
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
        self.enterRule(localctx, 56, self.RULE_closedParenth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(RogueLangParser.T__22)
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
        self.enterRule(localctx, 58, self.RULE_openBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(RogueLangParser.T__23)
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
        self.enterRule(localctx, 60, self.RULE_closedBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(RogueLangParser.T__24)
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
        self.enterRule(localctx, 62, self.RULE_openCurlBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(RogueLangParser.T__25)
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
        self.enterRule(localctx, 64, self.RULE_closedCurlBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(RogueLangParser.T__26)
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
        self.enterRule(localctx, 66, self.RULE_comma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(RogueLangParser.T__27)
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
        self._predicates[26] = self.expr_sempred
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
         




