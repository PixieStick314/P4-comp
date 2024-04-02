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
        4,1,50,381,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,4,0,80,
        8,0,11,0,12,0,81,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,94,
        8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,106,8,3,1,4,1,4,
        1,4,1,4,3,4,112,8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,
        124,8,6,10,6,12,6,127,9,6,1,6,1,6,1,6,1,6,1,6,3,6,134,8,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,5,9,147,8,9,10,9,12,9,150,
        9,9,1,10,1,10,1,11,5,11,155,8,11,10,11,12,11,158,9,11,1,12,5,12,
        161,8,12,10,12,12,12,164,9,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,
        172,8,13,10,13,12,13,175,9,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        1,14,5,14,185,8,14,10,14,12,14,188,9,14,1,14,1,14,1,15,1,15,1,15,
        1,15,3,15,196,8,15,1,15,1,15,1,15,5,15,201,8,15,10,15,12,15,204,
        9,15,1,15,1,15,1,16,1,16,1,16,3,16,211,8,16,1,16,3,16,214,8,16,1,
        16,1,16,1,17,1,17,1,17,1,17,1,17,5,17,223,8,17,10,17,12,17,226,9,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,5,19,238,8,
        19,10,19,12,19,241,9,19,1,20,1,20,1,21,1,21,1,21,1,21,5,21,249,8,
        21,10,21,12,21,252,9,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,
        1,23,1,23,1,23,1,23,1,23,4,23,267,8,23,11,23,12,23,268,1,23,1,23,
        1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,5,25,283,8,25,
        10,25,12,25,286,9,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,3,27,
        296,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,5,29,
        308,8,29,10,29,12,29,311,9,29,1,30,1,30,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,330,8,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,5,31,362,8,31,10,31,12,31,365,9,31,1,32,1,32,
        1,33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,1,38,1,38,1,38,
        0,1,62,39,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,0,5,3,0,
        3,5,44,45,49,49,2,0,32,33,40,40,1,0,30,31,1,0,34,39,1,0,41,42,390,
        0,79,1,0,0,0,2,93,1,0,0,0,4,95,1,0,0,0,6,100,1,0,0,0,8,107,1,0,0,
        0,10,113,1,0,0,0,12,115,1,0,0,0,14,135,1,0,0,0,16,143,1,0,0,0,18,
        148,1,0,0,0,20,151,1,0,0,0,22,156,1,0,0,0,24,162,1,0,0,0,26,165,
        1,0,0,0,28,178,1,0,0,0,30,191,1,0,0,0,32,207,1,0,0,0,34,217,1,0,
        0,0,36,229,1,0,0,0,38,233,1,0,0,0,40,242,1,0,0,0,42,244,1,0,0,0,
        44,253,1,0,0,0,46,260,1,0,0,0,48,272,1,0,0,0,50,278,1,0,0,0,52,287,
        1,0,0,0,54,295,1,0,0,0,56,297,1,0,0,0,58,303,1,0,0,0,60,312,1,0,
        0,0,62,329,1,0,0,0,64,366,1,0,0,0,66,368,1,0,0,0,68,370,1,0,0,0,
        70,372,1,0,0,0,72,374,1,0,0,0,74,376,1,0,0,0,76,378,1,0,0,0,78,80,
        3,2,1,0,79,78,1,0,0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,
        82,1,1,0,0,0,83,94,3,4,2,0,84,94,3,6,3,0,85,94,3,12,6,0,86,94,3,
        26,13,0,87,94,3,28,14,0,88,94,3,30,15,0,89,94,3,32,16,0,90,94,3,
        34,17,0,91,94,3,48,24,0,92,94,3,62,31,0,93,83,1,0,0,0,93,84,1,0,
        0,0,93,85,1,0,0,0,93,86,1,0,0,0,93,87,1,0,0,0,93,88,1,0,0,0,93,89,
        1,0,0,0,93,90,1,0,0,0,93,91,1,0,0,0,93,92,1,0,0,0,94,3,1,0,0,0,95,
        96,5,1,0,0,96,97,3,64,32,0,97,98,3,62,31,0,98,99,3,66,33,0,99,5,
        1,0,0,0,100,105,5,49,0,0,101,102,5,2,0,0,102,106,3,62,31,0,103,106,
        3,34,17,0,104,106,3,42,21,0,105,101,1,0,0,0,105,103,1,0,0,0,105,
        104,1,0,0,0,105,106,1,0,0,0,106,7,1,0,0,0,107,111,3,10,5,0,108,109,
        3,68,34,0,109,110,3,70,35,0,110,112,1,0,0,0,111,108,1,0,0,0,111,
        112,1,0,0,0,112,9,1,0,0,0,113,114,7,0,0,0,114,11,1,0,0,0,115,116,
        5,26,0,0,116,117,3,64,32,0,117,118,3,16,8,0,118,119,3,66,33,0,119,
        120,3,72,36,0,120,121,3,18,9,0,121,125,3,74,37,0,122,124,3,14,7,
        0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,
        0,126,133,1,0,0,0,127,125,1,0,0,0,128,129,5,28,0,0,129,130,3,72,
        36,0,130,131,3,24,12,0,131,132,3,74,37,0,132,134,1,0,0,0,133,128,
        1,0,0,0,133,134,1,0,0,0,134,13,1,0,0,0,135,136,5,27,0,0,136,137,
        3,64,32,0,137,138,3,20,10,0,138,139,3,66,33,0,139,140,3,72,36,0,
        140,141,3,22,11,0,141,142,3,74,37,0,142,15,1,0,0,0,143,144,3,62,
        31,0,144,17,1,0,0,0,145,147,3,2,1,0,146,145,1,0,0,0,147,150,1,0,
        0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,19,1,0,0,0,150,148,1,0,0,
        0,151,152,3,62,31,0,152,21,1,0,0,0,153,155,3,2,1,0,154,153,1,0,0,
        0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,23,1,0,0,0,
        158,156,1,0,0,0,159,161,3,2,1,0,160,159,1,0,0,0,161,164,1,0,0,0,
        162,160,1,0,0,0,162,163,1,0,0,0,163,25,1,0,0,0,164,162,1,0,0,0,165,
        166,5,6,0,0,166,167,3,6,3,0,167,168,5,7,0,0,168,169,3,62,31,0,169,
        173,3,72,36,0,170,172,3,2,1,0,171,170,1,0,0,0,172,175,1,0,0,0,173,
        171,1,0,0,0,173,174,1,0,0,0,174,176,1,0,0,0,175,173,1,0,0,0,176,
        177,3,74,37,0,177,27,1,0,0,0,178,179,5,8,0,0,179,180,3,64,32,0,180,
        181,3,62,31,0,181,182,3,66,33,0,182,186,3,72,36,0,183,185,3,2,1,
        0,184,183,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,
        0,187,189,1,0,0,0,188,186,1,0,0,0,189,190,3,74,37,0,190,29,1,0,0,
        0,191,192,5,9,0,0,192,193,5,49,0,0,193,195,3,64,32,0,194,196,3,38,
        19,0,195,194,1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,197,198,3,66,
        33,0,198,202,3,72,36,0,199,201,3,2,1,0,200,199,1,0,0,0,201,204,1,
        0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,205,1,0,0,0,204,202,1,
        0,0,0,205,206,3,74,37,0,206,31,1,0,0,0,207,208,5,49,0,0,208,210,
        3,64,32,0,209,211,3,42,21,0,210,209,1,0,0,0,210,211,1,0,0,0,211,
        213,1,0,0,0,212,214,5,29,0,0,213,212,1,0,0,0,213,214,1,0,0,0,214,
        215,1,0,0,0,215,216,3,66,33,0,216,33,1,0,0,0,217,218,3,72,36,0,218,
        224,3,62,31,0,219,220,3,76,38,0,220,221,3,62,31,0,221,223,1,0,0,
        0,222,219,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,
        0,225,227,1,0,0,0,226,224,1,0,0,0,227,228,3,74,37,0,228,35,1,0,0,
        0,229,230,5,10,0,0,230,231,3,54,27,0,231,232,3,56,28,0,232,37,1,
        0,0,0,233,239,3,40,20,0,234,235,3,76,38,0,235,236,3,40,20,0,236,
        238,1,0,0,0,237,234,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,
        240,1,0,0,0,240,39,1,0,0,0,241,239,1,0,0,0,242,243,5,49,0,0,243,
        41,1,0,0,0,244,250,3,62,31,0,245,246,3,76,38,0,246,247,3,62,31,0,
        247,249,1,0,0,0,248,245,1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,
        250,251,1,0,0,0,251,43,1,0,0,0,252,250,1,0,0,0,253,254,5,11,0,0,
        254,255,3,64,32,0,255,256,5,47,0,0,256,257,3,76,38,0,257,258,5,47,
        0,0,258,259,3,66,33,0,259,45,1,0,0,0,260,261,5,12,0,0,261,262,3,
        64,32,0,262,266,3,62,31,0,263,264,3,76,38,0,264,265,3,62,31,0,265,
        267,1,0,0,0,266,263,1,0,0,0,267,268,1,0,0,0,268,266,1,0,0,0,268,
        269,1,0,0,0,269,270,1,0,0,0,270,271,3,66,33,0,271,47,1,0,0,0,272,
        273,5,13,0,0,273,274,5,49,0,0,274,275,3,72,36,0,275,276,3,50,25,
        0,276,277,3,74,37,0,277,49,1,0,0,0,278,284,5,49,0,0,279,280,3,76,
        38,0,280,281,5,49,0,0,281,283,1,0,0,0,282,279,1,0,0,0,283,286,1,
        0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,51,1,0,0,0,286,284,1,0,
        0,0,287,288,5,49,0,0,288,289,5,14,0,0,289,290,5,49,0,0,290,53,1,
        0,0,0,291,296,5,15,0,0,292,296,5,16,0,0,293,294,5,47,0,0,294,296,
        5,17,0,0,295,291,1,0,0,0,295,292,1,0,0,0,295,293,1,0,0,0,296,55,
        1,0,0,0,297,298,3,64,32,0,298,299,3,58,29,0,299,300,3,76,38,0,300,
        301,3,60,30,0,301,302,3,66,33,0,302,57,1,0,0,0,303,309,5,47,0,0,
        304,305,3,76,38,0,305,306,5,47,0,0,306,308,1,0,0,0,307,304,1,0,0,
        0,308,311,1,0,0,0,309,307,1,0,0,0,309,310,1,0,0,0,310,59,1,0,0,0,
        311,309,1,0,0,0,312,313,5,47,0,0,313,61,1,0,0,0,314,315,6,31,-1,
        0,315,316,5,43,0,0,316,330,3,62,31,10,317,318,3,64,32,0,318,319,
        3,62,31,0,319,320,3,66,33,0,320,330,1,0,0,0,321,330,5,49,0,0,322,
        330,5,48,0,0,323,330,5,47,0,0,324,330,5,44,0,0,325,330,5,45,0,0,
        326,330,3,44,22,0,327,330,3,46,23,0,328,330,3,52,26,0,329,314,1,
        0,0,0,329,317,1,0,0,0,329,321,1,0,0,0,329,322,1,0,0,0,329,323,1,
        0,0,0,329,324,1,0,0,0,329,325,1,0,0,0,329,326,1,0,0,0,329,327,1,
        0,0,0,329,328,1,0,0,0,330,363,1,0,0,0,331,332,10,16,0,0,332,333,
        3,68,34,0,333,334,3,62,31,0,334,335,3,70,35,0,335,336,5,2,0,0,336,
        337,3,62,31,17,337,362,1,0,0,0,338,339,10,14,0,0,339,340,7,1,0,0,
        340,362,3,62,31,15,341,342,10,13,0,0,342,343,7,2,0,0,343,362,3,62,
        31,14,344,345,10,12,0,0,345,346,7,3,0,0,346,362,3,62,31,13,347,348,
        10,11,0,0,348,349,7,4,0,0,349,362,3,62,31,12,350,351,10,17,0,0,351,
        352,3,68,34,0,352,353,3,62,31,0,353,354,3,70,35,0,354,362,1,0,0,
        0,355,356,10,15,0,0,356,357,5,18,0,0,357,358,3,64,32,0,358,359,3,
        62,31,0,359,360,3,66,33,0,360,362,1,0,0,0,361,331,1,0,0,0,361,338,
        1,0,0,0,361,341,1,0,0,0,361,344,1,0,0,0,361,347,1,0,0,0,361,350,
        1,0,0,0,361,355,1,0,0,0,362,365,1,0,0,0,363,361,1,0,0,0,363,364,
        1,0,0,0,364,63,1,0,0,0,365,363,1,0,0,0,366,367,5,19,0,0,367,65,1,
        0,0,0,368,369,5,20,0,0,369,67,1,0,0,0,370,371,5,21,0,0,371,69,1,
        0,0,0,372,373,5,22,0,0,373,71,1,0,0,0,374,375,5,23,0,0,375,73,1,
        0,0,0,376,377,5,24,0,0,377,75,1,0,0,0,378,379,5,25,0,0,379,77,1,
        0,0,0,25,81,93,105,111,125,133,148,156,162,173,186,195,202,210,213,
        224,239,250,268,284,295,309,329,361,363
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'='", "'string'", "'bool'", 
                     "'number'", "'for'", "'in'", "'while'", "'def'", "'BSP'", 
                     "'randomNumber'", "'randomChoice'", "'enum'", "'.'", 
                     "'2D'", "'3D'", "'D'", "'.add'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "','", "'if'", "'elif'", "'else'", 
                     "'return'", "'+'", "'-'", "'*'", "'/'", "'>'", "'>='", 
                     "'<'", "'<='", "'=='", "'!='", "'%'", "'and'", "'or'", 
                     "'not'", "'True'", "'False'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IF", "ELIF", "ELSE", "RETURN", 
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
    RULE_elifBlockstat = 7
    RULE_ifExpr = 8
    RULE_ifBlock = 9
    RULE_elifExpr = 10
    RULE_elifBlock = 11
    RULE_elseBlock = 12
    RULE_forLoop = 13
    RULE_whileLoop = 14
    RULE_functionDecl = 15
    RULE_functionCall = 16
    RULE_arrayInit = 17
    RULE_bsp = 18
    RULE_params = 19
    RULE_param = 20
    RULE_args = 21
    RULE_randomNumber = 22
    RULE_randomChoice = 23
    RULE_enumDecl = 24
    RULE_enumBody = 25
    RULE_enumValue = 26
    RULE_bspDimension = 27
    RULE_bspParameters = 28
    RULE_dimensionList = 29
    RULE_minSize = 30
    RULE_expr = 31
    RULE_openParenth = 32
    RULE_closedParenth = 33
    RULE_openBrack = 34
    RULE_closedBrack = 35
    RULE_openCurlBrack = 36
    RULE_closedCurlBrack = 37
    RULE_comma = 38

    ruleNames =  [ "prog", "stat", "printStat", "varDecl", "dataType", "baseType", 
                   "ifStat", "elifBlockstat", "ifExpr", "ifBlock", "elifExpr", 
                   "elifBlock", "elseBlock", "forLoop", "whileLoop", "functionDecl", 
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
    IF=26
    ELIF=27
    ELSE=28
    RETURN=29
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
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self.stat()
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735145679682) != 0)):
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
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.ifStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.functionDecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 89
                self.functionCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 90
                self.arrayInit()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 91
                self.enumDecl()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 92
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
            self.state = 95
            self.match(RogueLangParser.T__0)
            self.state = 96
            self.openParenth()
            self.state = 97
            self.expr(0)
            self.state = 98
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
            self.state = 100
            self.match(RogueLangParser.ID)
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 101
                self.match(RogueLangParser.T__1)
                self.state = 102
                self.expr(0)

            elif la_ == 2:
                self.state = 103
                self.arrayInit()

            elif la_ == 3:
                self.state = 104
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
            self.state = 107
            self.baseType()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 108
                self.openBrack()
                self.state = 109
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
            self.state = 113
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

        def openParenth(self):
            return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,0)


        def ifExpr(self):
            return self.getTypedRuleContext(RogueLangParser.IfExprContext,0)


        def closedParenth(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,0)


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


        def elifBlockstat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ElifBlockstatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ElifBlockstatContext,i)


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
            self.state = 115
            self.match(RogueLangParser.IF)
            self.state = 116
            self.openParenth()
            self.state = 117
            self.ifExpr()
            self.state = 118
            self.closedParenth()
            self.state = 119
            self.openCurlBrack()
            self.state = 120
            self.ifBlock()
            self.state = 121
            self.closedCurlBrack()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 122
                self.elifBlockstat()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 128
                self.match(RogueLangParser.ELSE)
                self.state = 129
                self.openCurlBrack()
                self.state = 130
                self.elseBlock()
                self.state = 131
                self.closedCurlBrack()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifBlockstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(RogueLangParser.ELIF, 0)

        def openParenth(self):
            return self.getTypedRuleContext(RogueLangParser.OpenParenthContext,0)


        def elifExpr(self):
            return self.getTypedRuleContext(RogueLangParser.ElifExprContext,0)


        def closedParenth(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedParenthContext,0)


        def openCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.OpenCurlBrackContext,0)


        def elifBlock(self):
            return self.getTypedRuleContext(RogueLangParser.ElifBlockContext,0)


        def closedCurlBrack(self):
            return self.getTypedRuleContext(RogueLangParser.ClosedCurlBrackContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_elifBlockstat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifBlockstat" ):
                return visitor.visitElifBlockstat(self)
            else:
                return visitor.visitChildren(self)




    def elifBlockstat(self):

        localctx = RogueLangParser.ElifBlockstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elifBlockstat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(RogueLangParser.ELIF)
            self.state = 136
            self.openParenth()
            self.state = 137
            self.elifExpr()
            self.state = 138
            self.closedParenth()
            self.state = 139
            self.openCurlBrack()
            self.state = 140
            self.elifBlock()
            self.state = 141
            self.closedCurlBrack()
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
        self.enterRule(localctx, 16, self.RULE_ifExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
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
        self.enterRule(localctx, 18, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735145679682) != 0):
                self.state = 145
                self.stat()
                self.state = 150
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
        self.enterRule(localctx, 20, self.RULE_elifExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
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
        self.enterRule(localctx, 22, self.RULE_elifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735145679682) != 0):
                self.state = 153
                self.stat()
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
        self.enterRule(localctx, 24, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735145679682) != 0):
                self.state = 159
                self.stat()
                self.state = 164
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
        self.enterRule(localctx, 26, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(RogueLangParser.T__5)
            self.state = 166
            self.varDecl()
            self.state = 167
            self.match(RogueLangParser.T__6)
            self.state = 168
            self.expr(0)
            self.state = 169
            self.openCurlBrack()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735145679682) != 0):
                self.state = 170
                self.stat()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
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
        self.enterRule(localctx, 28, self.RULE_whileLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(RogueLangParser.T__7)
            self.state = 179
            self.openParenth()
            self.state = 180
            self.expr(0)
            self.state = 181
            self.closedParenth()
            self.state = 182
            self.openCurlBrack()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735145679682) != 0):
                self.state = 183
                self.stat()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 189
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
        self.enterRule(localctx, 30, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(RogueLangParser.T__8)
            self.state = 192
            self.match(RogueLangParser.ID)
            self.state = 193
            self.openParenth()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 194
                self.params()


            self.state = 197
            self.closedParenth()
            self.state = 198
            self.openCurlBrack()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735145679682) != 0):
                self.state = 199
                self.stat()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
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
        self.enterRule(localctx, 32, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(RogueLangParser.ID)
            self.state = 208
            self.openParenth()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046735070173184) != 0):
                self.state = 209
                self.args()


            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 212
                self.match(RogueLangParser.RETURN)


            self.state = 215
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
        self.enterRule(localctx, 34, self.RULE_arrayInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.openCurlBrack()
            self.state = 218
            self.expr(0)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 219
                self.comma()
                self.state = 220
                self.expr(0)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
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
        self.enterRule(localctx, 36, self.RULE_bsp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(RogueLangParser.T__9)
            self.state = 230
            self.bspDimension()
            self.state = 231
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
        self.enterRule(localctx, 38, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.param()
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 234
                self.comma()
                self.state = 235
                self.param()
                self.state = 241
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
        self.enterRule(localctx, 40, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
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
        self.enterRule(localctx, 42, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.expr(0)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 245
                self.comma()
                self.state = 246
                self.expr(0)
                self.state = 252
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
        self.enterRule(localctx, 44, self.RULE_randomNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(RogueLangParser.T__10)
            self.state = 254
            self.openParenth()
            self.state = 255
            self.match(RogueLangParser.NUMBER)
            self.state = 256
            self.comma()
            self.state = 257
            self.match(RogueLangParser.NUMBER)
            self.state = 258
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
        self.enterRule(localctx, 46, self.RULE_randomChoice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(RogueLangParser.T__11)
            self.state = 261
            self.openParenth()
            self.state = 262
            self.expr(0)
            self.state = 266 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 263
                self.comma()
                self.state = 264
                self.expr(0)
                self.state = 268 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 270
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
        self.enterRule(localctx, 48, self.RULE_enumDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(RogueLangParser.T__12)
            self.state = 273
            self.match(RogueLangParser.ID)
            self.state = 274
            self.openCurlBrack()
            self.state = 275
            self.enumBody()
            self.state = 276
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
        self.enterRule(localctx, 50, self.RULE_enumBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(RogueLangParser.ID)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 279
                self.comma()
                self.state = 280
                self.match(RogueLangParser.ID)
                self.state = 286
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
        self.enterRule(localctx, 52, self.RULE_enumValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(RogueLangParser.ID)
            self.state = 288
            self.match(RogueLangParser.T__13)
            self.state = 289
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
        self.enterRule(localctx, 54, self.RULE_bspDimension)
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(RogueLangParser.T__14)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.match(RogueLangParser.T__15)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 293
                self.match(RogueLangParser.NUMBER)
                self.state = 294
                self.match(RogueLangParser.T__16)
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
        self.enterRule(localctx, 56, self.RULE_bspParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.openParenth()
            self.state = 298
            self.dimensionList()
            self.state = 299
            self.comma()
            self.state = 300
            self.minSize()
            self.state = 301
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
        self.enterRule(localctx, 58, self.RULE_dimensionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(RogueLangParser.NUMBER)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 304
                    self.comma()
                    self.state = 305
                    self.match(RogueLangParser.NUMBER) 
                self.state = 311
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
        self.enterRule(localctx, 60, self.RULE_minSize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 315
                self.match(RogueLangParser.NOT)
                self.state = 316
                self.expr(10)
                pass

            elif la_ == 2:
                self.state = 317
                self.openParenth()
                self.state = 318
                self.expr(0)
                self.state = 319
                self.closedParenth()
                pass

            elif la_ == 3:
                self.state = 321
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 4:
                self.state = 322
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 5:
                self.state = 323
                self.match(RogueLangParser.NUMBER)
                pass

            elif la_ == 6:
                self.state = 324
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 7:
                self.state = 325
                self.match(RogueLangParser.FALSE)
                pass

            elif la_ == 8:
                self.state = 326
                self.randomNumber()
                pass

            elif la_ == 9:
                self.state = 327
                self.randomChoice()
                pass

            elif la_ == 10:
                self.state = 328
                self.enumValue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 361
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 331
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 332
                        self.openBrack()
                        self.state = 333
                        self.expr(0)
                        self.state = 334
                        self.closedBrack()
                        self.state = 335
                        self.match(RogueLangParser.T__1)
                        self.state = 336
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 338
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 339
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1112396529664) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 340
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 341
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 342
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==30 or _la==31):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 343
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 344
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 345
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 346
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 347
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 348
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==41 or _la==42):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 349
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 350
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 351
                        self.openBrack()
                        self.state = 352
                        self.expr(0)
                        self.state = 353
                        self.closedBrack()
                        pass

                    elif la_ == 7:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 355
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 356
                        self.match(RogueLangParser.T__17)
                        self.state = 357
                        self.openParenth()
                        self.state = 358
                        self.expr(0)
                        self.state = 359
                        self.closedParenth()
                        pass

             
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        self.enterRule(localctx, 64, self.RULE_openParenth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(RogueLangParser.T__18)
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
        self.enterRule(localctx, 66, self.RULE_closedParenth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(RogueLangParser.T__19)
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
        self.enterRule(localctx, 68, self.RULE_openBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(RogueLangParser.T__20)
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
        self.enterRule(localctx, 70, self.RULE_closedBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(RogueLangParser.T__21)
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
        self.enterRule(localctx, 72, self.RULE_openCurlBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(RogueLangParser.T__22)
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
        self.enterRule(localctx, 74, self.RULE_closedCurlBrack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(RogueLangParser.T__23)
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
        self.enterRule(localctx, 76, self.RULE_comma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(RogueLangParser.T__24)
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
        self._predicates[31] = self.expr_sempred
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
         




