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
        4,1,50,377,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,4,0,78,8,0,11,0,
        12,0,79,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,92,8,1,1,2,1,
        2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,104,8,3,1,4,1,4,1,4,1,4,3,
        4,110,8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,5,6,129,8,6,10,6,12,6,132,9,6,1,6,1,6,1,6,1,6,1,6,
        3,6,139,8,6,1,6,1,6,1,7,1,7,1,8,5,8,146,8,8,10,8,12,8,149,9,8,1,
        9,1,9,1,10,5,10,154,8,10,10,10,12,10,157,9,10,1,11,5,11,160,8,11,
        10,11,12,11,163,9,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,171,8,12,
        10,12,12,12,174,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,
        184,8,13,10,13,12,13,187,9,13,1,13,1,13,1,14,1,14,1,14,1,14,3,14,
        195,8,14,1,14,1,14,1,14,5,14,200,8,14,10,14,12,14,203,9,14,1,14,
        1,14,1,15,1,15,1,15,3,15,210,8,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,5,16,219,8,16,10,16,12,16,222,9,16,1,16,1,16,1,17,1,17,1,17,
        1,17,1,18,1,18,1,18,1,18,5,18,234,8,18,10,18,12,18,237,9,18,1,19,
        1,19,1,20,1,20,1,20,1,20,5,20,245,8,20,10,20,12,20,248,9,20,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,4,22,
        263,8,22,11,22,12,22,264,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,
        1,24,1,24,1,24,1,24,5,24,279,8,24,10,24,12,24,282,9,24,1,25,1,25,
        1,25,1,25,1,26,1,26,1,26,1,26,3,26,292,8,26,1,27,1,27,1,27,1,27,
        1,27,1,27,1,28,1,28,1,28,1,28,5,28,304,8,28,10,28,12,28,307,9,28,
        1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,3,30,326,8,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,5,30,358,
        8,30,10,30,12,30,361,9,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,
        1,35,1,35,1,36,1,36,1,37,1,37,1,37,0,1,60,38,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,0,5,3,0,3,5,44,45,49,49,2,0,32,33,40,40,
        1,0,30,31,1,0,34,39,1,0,41,42,386,0,77,1,0,0,0,2,91,1,0,0,0,4,93,
        1,0,0,0,6,98,1,0,0,0,8,105,1,0,0,0,10,111,1,0,0,0,12,113,1,0,0,0,
        14,142,1,0,0,0,16,147,1,0,0,0,18,150,1,0,0,0,20,155,1,0,0,0,22,161,
        1,0,0,0,24,164,1,0,0,0,26,177,1,0,0,0,28,190,1,0,0,0,30,206,1,0,
        0,0,32,213,1,0,0,0,34,225,1,0,0,0,36,229,1,0,0,0,38,238,1,0,0,0,
        40,240,1,0,0,0,42,249,1,0,0,0,44,256,1,0,0,0,46,268,1,0,0,0,48,274,
        1,0,0,0,50,283,1,0,0,0,52,291,1,0,0,0,54,293,1,0,0,0,56,299,1,0,
        0,0,58,308,1,0,0,0,60,325,1,0,0,0,62,362,1,0,0,0,64,364,1,0,0,0,
        66,366,1,0,0,0,68,368,1,0,0,0,70,370,1,0,0,0,72,372,1,0,0,0,74,374,
        1,0,0,0,76,78,3,2,1,0,77,76,1,0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,
        79,80,1,0,0,0,80,1,1,0,0,0,81,92,3,4,2,0,82,92,3,6,3,0,83,92,3,12,
        6,0,84,92,3,24,12,0,85,92,3,26,13,0,86,92,3,28,14,0,87,92,3,30,15,
        0,88,92,3,32,16,0,89,92,3,46,23,0,90,92,3,60,30,0,91,81,1,0,0,0,
        91,82,1,0,0,0,91,83,1,0,0,0,91,84,1,0,0,0,91,85,1,0,0,0,91,86,1,
        0,0,0,91,87,1,0,0,0,91,88,1,0,0,0,91,89,1,0,0,0,91,90,1,0,0,0,92,
        3,1,0,0,0,93,94,5,1,0,0,94,95,3,62,31,0,95,96,3,60,30,0,96,97,3,
        64,32,0,97,5,1,0,0,0,98,103,5,49,0,0,99,100,5,2,0,0,100,104,3,60,
        30,0,101,104,3,32,16,0,102,104,3,40,20,0,103,99,1,0,0,0,103,101,
        1,0,0,0,103,102,1,0,0,0,103,104,1,0,0,0,104,7,1,0,0,0,105,109,3,
        10,5,0,106,107,3,66,33,0,107,108,3,68,34,0,108,110,1,0,0,0,109,106,
        1,0,0,0,109,110,1,0,0,0,110,9,1,0,0,0,111,112,7,0,0,0,112,11,1,0,
        0,0,113,114,5,27,0,0,114,115,3,62,31,0,115,116,3,14,7,0,116,117,
        3,64,32,0,117,118,3,70,35,0,118,119,3,16,8,0,119,130,3,72,36,0,120,
        121,5,28,0,0,121,122,3,62,31,0,122,123,3,18,9,0,123,124,3,64,32,
        0,124,125,3,70,35,0,125,126,3,20,10,0,126,127,3,68,34,0,127,129,
        1,0,0,0,128,120,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,
        1,0,0,0,131,138,1,0,0,0,132,130,1,0,0,0,133,134,5,29,0,0,134,135,
        3,70,35,0,135,136,3,22,11,0,136,137,3,72,36,0,137,139,1,0,0,0,138,
        133,1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,141,5,6,0,0,141,
        13,1,0,0,0,142,143,3,60,30,0,143,15,1,0,0,0,144,146,3,2,1,0,145,
        144,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,
        17,1,0,0,0,149,147,1,0,0,0,150,151,3,60,30,0,151,19,1,0,0,0,152,
        154,3,2,1,0,153,152,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,
        156,1,0,0,0,156,21,1,0,0,0,157,155,1,0,0,0,158,160,3,2,1,0,159,158,
        1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,23,1,
        0,0,0,163,161,1,0,0,0,164,165,5,7,0,0,165,166,3,6,3,0,166,167,5,
        8,0,0,167,168,3,60,30,0,168,172,3,70,35,0,169,171,3,2,1,0,170,169,
        1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,175,
        1,0,0,0,174,172,1,0,0,0,175,176,3,72,36,0,176,25,1,0,0,0,177,178,
        5,9,0,0,178,179,3,62,31,0,179,180,3,60,30,0,180,181,3,64,32,0,181,
        185,3,70,35,0,182,184,3,2,1,0,183,182,1,0,0,0,184,187,1,0,0,0,185,
        183,1,0,0,0,185,186,1,0,0,0,186,188,1,0,0,0,187,185,1,0,0,0,188,
        189,3,72,36,0,189,27,1,0,0,0,190,191,5,10,0,0,191,192,5,49,0,0,192,
        194,3,62,31,0,193,195,3,36,18,0,194,193,1,0,0,0,194,195,1,0,0,0,
        195,196,1,0,0,0,196,197,3,64,32,0,197,201,3,70,35,0,198,200,3,2,
        1,0,199,198,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,
        0,0,202,204,1,0,0,0,203,201,1,0,0,0,204,205,3,72,36,0,205,29,1,0,
        0,0,206,207,5,49,0,0,207,209,3,62,31,0,208,210,3,40,20,0,209,208,
        1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,212,3,64,32,0,212,31,
        1,0,0,0,213,214,3,70,35,0,214,220,3,60,30,0,215,216,3,74,37,0,216,
        217,3,60,30,0,217,219,1,0,0,0,218,215,1,0,0,0,219,222,1,0,0,0,220,
        218,1,0,0,0,220,221,1,0,0,0,221,223,1,0,0,0,222,220,1,0,0,0,223,
        224,3,72,36,0,224,33,1,0,0,0,225,226,5,11,0,0,226,227,3,52,26,0,
        227,228,3,54,27,0,228,35,1,0,0,0,229,235,3,38,19,0,230,231,3,74,
        37,0,231,232,3,38,19,0,232,234,1,0,0,0,233,230,1,0,0,0,234,237,1,
        0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,37,1,0,0,0,237,235,1,0,
        0,0,238,239,5,49,0,0,239,39,1,0,0,0,240,246,3,60,30,0,241,242,3,
        74,37,0,242,243,3,60,30,0,243,245,1,0,0,0,244,241,1,0,0,0,245,248,
        1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,41,1,0,0,0,248,246,1,
        0,0,0,249,250,5,12,0,0,250,251,3,62,31,0,251,252,5,47,0,0,252,253,
        3,74,37,0,253,254,5,47,0,0,254,255,3,64,32,0,255,43,1,0,0,0,256,
        257,5,13,0,0,257,258,3,62,31,0,258,262,3,60,30,0,259,260,3,74,37,
        0,260,261,3,60,30,0,261,263,1,0,0,0,262,259,1,0,0,0,263,264,1,0,
        0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,266,1,0,0,0,266,267,3,64,
        32,0,267,45,1,0,0,0,268,269,5,14,0,0,269,270,5,49,0,0,270,271,3,
        70,35,0,271,272,3,48,24,0,272,273,3,72,36,0,273,47,1,0,0,0,274,280,
        5,49,0,0,275,276,3,74,37,0,276,277,5,49,0,0,277,279,1,0,0,0,278,
        275,1,0,0,0,279,282,1,0,0,0,280,278,1,0,0,0,280,281,1,0,0,0,281,
        49,1,0,0,0,282,280,1,0,0,0,283,284,5,49,0,0,284,285,5,15,0,0,285,
        286,5,49,0,0,286,51,1,0,0,0,287,292,5,16,0,0,288,292,5,17,0,0,289,
        290,5,47,0,0,290,292,5,18,0,0,291,287,1,0,0,0,291,288,1,0,0,0,291,
        289,1,0,0,0,292,53,1,0,0,0,293,294,3,62,31,0,294,295,3,56,28,0,295,
        296,3,74,37,0,296,297,3,58,29,0,297,298,3,64,32,0,298,55,1,0,0,0,
        299,305,5,47,0,0,300,301,3,74,37,0,301,302,5,47,0,0,302,304,1,0,
        0,0,303,300,1,0,0,0,304,307,1,0,0,0,305,303,1,0,0,0,305,306,1,0,
        0,0,306,57,1,0,0,0,307,305,1,0,0,0,308,309,5,47,0,0,309,59,1,0,0,
        0,310,311,6,30,-1,0,311,312,5,43,0,0,312,326,3,60,30,10,313,314,
        3,62,31,0,314,315,3,60,30,0,315,316,3,64,32,0,316,326,1,0,0,0,317,
        326,5,49,0,0,318,326,5,48,0,0,319,326,5,47,0,0,320,326,5,44,0,0,
        321,326,5,45,0,0,322,326,3,42,21,0,323,326,3,44,22,0,324,326,3,50,
        25,0,325,310,1,0,0,0,325,313,1,0,0,0,325,317,1,0,0,0,325,318,1,0,
        0,0,325,319,1,0,0,0,325,320,1,0,0,0,325,321,1,0,0,0,325,322,1,0,
        0,0,325,323,1,0,0,0,325,324,1,0,0,0,326,359,1,0,0,0,327,328,10,16,
        0,0,328,329,3,66,33,0,329,330,3,60,30,0,330,331,3,68,34,0,331,332,
        5,2,0,0,332,333,3,60,30,17,333,358,1,0,0,0,334,335,10,14,0,0,335,
        336,7,1,0,0,336,358,3,60,30,15,337,338,10,13,0,0,338,339,7,2,0,0,
        339,358,3,60,30,14,340,341,10,12,0,0,341,342,7,3,0,0,342,358,3,60,
        30,13,343,344,10,11,0,0,344,345,7,4,0,0,345,358,3,60,30,12,346,347,
        10,17,0,0,347,348,3,66,33,0,348,349,3,60,30,0,349,350,3,68,34,0,
        350,358,1,0,0,0,351,352,10,15,0,0,352,353,5,19,0,0,353,354,3,62,
        31,0,354,355,3,60,30,0,355,356,3,64,32,0,356,358,1,0,0,0,357,327,
        1,0,0,0,357,334,1,0,0,0,357,337,1,0,0,0,357,340,1,0,0,0,357,343,
        1,0,0,0,357,346,1,0,0,0,357,351,1,0,0,0,358,361,1,0,0,0,359,357,
        1,0,0,0,359,360,1,0,0,0,360,61,1,0,0,0,361,359,1,0,0,0,362,363,5,
        20,0,0,363,63,1,0,0,0,364,365,5,21,0,0,365,65,1,0,0,0,366,367,5,
        22,0,0,367,67,1,0,0,0,368,369,5,23,0,0,369,69,1,0,0,0,370,371,5,
        24,0,0,371,71,1,0,0,0,372,373,5,25,0,0,373,73,1,0,0,0,374,375,5,
        26,0,0,375,75,1,0,0,0,24,79,91,103,109,130,138,147,155,161,172,185,
        194,201,209,220,235,246,264,280,291,305,325,357,359
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'='", "'string'", "'bool'", 
                     "'number'", "';'", "'for'", "'in'", "'while'", "'def'", 
                     "'BSP'", "'randomNumber'", "'randomChoice'", "'enum'", 
                     "'.'", "'2D'", "'3D'", "'D'", "'.add'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "'if'", "'elif'", 
                     "'else'", "'+'", "'-'", "'*'", "'/'", "'>'", "'>='", 
                     "'<'", "'<='", "'=='", "'!='", "'%'", "'and'", "'or'", 
                     "'not'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELIF", 
                      "ELSE", "PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", 
                      "LT", "LTE", "EQ", "NEQ", "MOD", "AND", "OR", "NOT", 
                      "TRUE", "FALSE", "COMMENT_SINGLELINE", "NUMBER", "STRING", 
                      "ID", "WS" ]

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
    RULE_openParenth = 31
    RULE_closedParenth = 32
    RULE_openBrack = 33
    RULE_closedBrack = 34
    RULE_openCurlBrack = 35
    RULE_closedCurlBrack = 36
    RULE_comma = 37

    ruleNames =  [ "prog", "stat", "printStat", "varDecl", "dataType", "baseType", 
                   "ifStat", "ifExpr", "ifBlock", "elifExpr", "elifBlock", 
                   "elseBlock", "forLoop", "whileLoop", "functionDecl", 
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
    IF=27
    ELIF=28
    ELSE=29
    PLUS=30
    MINUS=31
    MULT=32
    DIV=33
    GT=34
    GTE=35
    LT=36
    LTE=37
    EQ=38
    NEQ=39
    MOD=40
    AND=41
    OR=42
    NOT=43
    TRUE=44
    FALSE=45
    COMMENT_SINGLELINE=46
    NUMBER=47
    STRING=48
    ID=49
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
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.stat()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735221716610) != 0)):
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
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.ifStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 85
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.functionDecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 87
                self.functionCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 88
                self.arrayInit()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 89
                self.enumDecl()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 90
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
            self.state = 93
            self.match(RogueLangParser.T__0)
            self.state = 94
            self.openParenth()
            self.state = 95
            self.expr(0)
            self.state = 96
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
            self.state = 98
            self.match(RogueLangParser.ID)
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 99
                self.match(RogueLangParser.T__1)
                self.state = 100
                self.expr(0)

            elif la_ == 2:
                self.state = 101
                self.arrayInit()

            elif la_ == 3:
                self.state = 102
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
            self.state = 105
            self.baseType()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 106
                self.openBrack()
                self.state = 107
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
            self.state = 111
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 615726511554616) != 0)):
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

        def openParenth(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.OpenParenthContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,i)


        def ifExpr(self):
            return self.getTypedRuleContext(RogueLangParser.IfExprContext,0)


        def closedParenth(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ClosedParenthContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,i)


        def openCurlBrack(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.OpenCurlBrackContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.OpenCurlBrackContext,i)


        def ifBlock(self):
            return self.getTypedRuleContext(RogueLangParser.IfBlockContext,0)


        def closedCurlBrack(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ClosedCurlBrackContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ClosedCurlBrackContext,i)


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


        def closedBrack(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ClosedBrackContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ClosedBrackContext,i)


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
            self.state = 113
            self.match(RogueLangParser.IF)
            self.state = 114
            self.openParenth()
            self.state = 115
            self.ifExpr()
            self.state = 116
            self.closedParenth()
            self.state = 117
            self.openCurlBrack()
            self.state = 118
            self.ifBlock()
            self.state = 119
            self.closedCurlBrack()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 120
                self.match(RogueLangParser.ELIF)
                self.state = 121
                self.openParenth()
                self.state = 122
                self.elifExpr()
                self.state = 123
                self.closedParenth()
                self.state = 124
                self.openCurlBrack()
                self.state = 125
                self.elifBlock()
                self.state = 126
                self.closedBrack()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 133
                self.match(RogueLangParser.ELSE)
                self.state = 134
                self.openCurlBrack()
                self.state = 135
                self.elseBlock()
                self.state = 136
                self.closedCurlBrack()


            self.state = 140
            self.match(RogueLangParser.T__5)
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
            self.state = 142
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
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735221716610) != 0):
                self.state = 144
                self.stat()
                self.state = 149
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
            self.state = 150
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
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735221716610) != 0):
                self.state = 152
                self.stat()
                self.state = 157
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
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735221716610) != 0):
                self.state = 158
                self.stat()
                self.state = 163
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
        self.enterRule(localctx, 24, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(RogueLangParser.T__6)
            self.state = 165
            self.varDecl()
            self.state = 166
            self.match(RogueLangParser.T__7)
            self.state = 167
            self.expr(0)
            self.state = 168
            self.openCurlBrack()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735221716610) != 0):
                self.state = 169
                self.stat()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 175
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
        self.enterRule(localctx, 26, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(RogueLangParser.T__8)
            self.state = 178
            self.openParenth()
            self.state = 179
            self.expr(0)
            self.state = 180
            self.closedParenth()
            self.state = 181
            self.openCurlBrack()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735221716610) != 0):
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
        self.enterRule(localctx, 28, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(RogueLangParser.T__9)
            self.state = 191
            self.match(RogueLangParser.ID)
            self.state = 192
            self.openParenth()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 193
                self.params()


            self.state = 196
            self.closedParenth()
            self.state = 197
            self.openCurlBrack()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735221716610) != 0):
                self.state = 198
                self.stat()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
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
        self.enterRule(localctx, 30, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(RogueLangParser.ID)
            self.state = 207
            self.openParenth()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735070703616) != 0):
                self.state = 208
                self.args()


            self.state = 211
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
        self.enterRule(localctx, 32, self.RULE_arrayInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.openCurlBrack()
            self.state = 214
            self.expr(0)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 215
                self.comma()
                self.state = 216
                self.expr(0)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
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
        self.enterRule(localctx, 34, self.RULE_bsp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(RogueLangParser.T__10)
            self.state = 226
            self.bspDimension()
            self.state = 227
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
        self.enterRule(localctx, 36, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.param()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 230
                self.comma()
                self.state = 231
                self.param()
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
            self.state = 238
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
        self.enterRule(localctx, 40, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.expr(0)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 241
                self.comma()
                self.state = 242
                self.expr(0)
                self.state = 248
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
        self.enterRule(localctx, 42, self.RULE_randomNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(RogueLangParser.T__11)
            self.state = 250
            self.openParenth()
            self.state = 251
            self.match(RogueLangParser.NUMBER)
            self.state = 252
            self.comma()
            self.state = 253
            self.match(RogueLangParser.NUMBER)
            self.state = 254
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
        self.enterRule(localctx, 44, self.RULE_randomChoice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(RogueLangParser.T__12)
            self.state = 257
            self.openParenth()
            self.state = 258
            self.expr(0)
            self.state = 262 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 259
                self.comma()
                self.state = 260
                self.expr(0)
                self.state = 264 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==26):
                    break

            self.state = 266
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
        self.enterRule(localctx, 46, self.RULE_enumDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(RogueLangParser.T__13)
            self.state = 269
            self.match(RogueLangParser.ID)
            self.state = 270
            self.openCurlBrack()
            self.state = 271
            self.enumBody()
            self.state = 272
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
        self.enterRule(localctx, 48, self.RULE_enumBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(RogueLangParser.ID)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 275
                self.comma()
                self.state = 276
                self.match(RogueLangParser.ID)
                self.state = 282
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
        self.enterRule(localctx, 50, self.RULE_enumValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(RogueLangParser.ID)
            self.state = 284
            self.match(RogueLangParser.T__14)
            self.state = 285
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
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(RogueLangParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.match(RogueLangParser.T__16)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 289
                self.match(RogueLangParser.NUMBER)
                self.state = 290
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
        self.enterRule(localctx, 54, self.RULE_bspParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.openParenth()
            self.state = 294
            self.dimensionList()
            self.state = 295
            self.comma()
            self.state = 296
            self.minSize()
            self.state = 297
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
        self.enterRule(localctx, 56, self.RULE_dimensionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(RogueLangParser.NUMBER)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 300
                    self.comma()
                    self.state = 301
                    self.match(RogueLangParser.NUMBER) 
                self.state = 307
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
        self.enterRule(localctx, 58, self.RULE_minSize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 311
                self.match(RogueLangParser.NOT)
                self.state = 312
                self.expr(10)
                pass

            elif la_ == 2:
                self.state = 313
                self.openParenth()
                self.state = 314
                self.expr(0)
                self.state = 315
                self.closedParenth()
                pass

            elif la_ == 3:
                self.state = 317
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 4:
                self.state = 318
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 5:
                self.state = 319
                self.match(RogueLangParser.NUMBER)
                pass

            elif la_ == 6:
                self.state = 320
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 7:
                self.state = 321
                self.match(RogueLangParser.FALSE)
                pass

            elif la_ == 8:
                self.state = 322
                self.randomNumber()
                pass

            elif la_ == 9:
                self.state = 323
                self.randomChoice()
                pass

            elif la_ == 10:
                self.state = 324
                self.enumValue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 357
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 327
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 328
                        self.openBrack()
                        self.state = 329
                        self.expr(0)
                        self.state = 330
                        self.closedBrack()
                        self.state = 331
                        self.match(RogueLangParser.T__1)
                        self.state = 332
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 334
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 335
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1112396529664) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 336
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 337
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 338
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==30 or _la==31):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 339
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 340
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 341
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 342
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 343
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 344
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==41 or _la==42):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 345
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 346
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 347
                        self.openBrack()
                        self.state = 348
                        self.expr(0)
                        self.state = 349
                        self.closedBrack()
                        pass

                    elif la_ == 7:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 351
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 352
                        self.match(RogueLangParser.T__18)
                        self.state = 353
                        self.openParenth()
                        self.state = 354
                        self.expr(0)
                        self.state = 355
                        self.closedParenth()
                        pass

             
                self.state = 361
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
        self.enterRule(localctx, 62, self.RULE_openParenth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
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
        self.enterRule(localctx, 64, self.RULE_closedParenth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
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
        self.enterRule(localctx, 66, self.RULE_openBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
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
        self.enterRule(localctx, 68, self.RULE_closedBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
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
        self.enterRule(localctx, 70, self.RULE_openCurlBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
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
        self.enterRule(localctx, 72, self.RULE_closedCurlBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
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
        self.enterRule(localctx, 74, self.RULE_comma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
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
         




