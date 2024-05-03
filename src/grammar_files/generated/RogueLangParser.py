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
        4,1,54,402,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,5,0,77,8,0,10,0,12,0,
        80,9,0,1,1,1,1,1,1,1,1,1,1,5,1,87,8,1,10,1,12,1,90,9,1,1,1,1,1,1,
        2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,3,4,115,8,4,1,5,1,5,1,5,1,6,1,6,3,6,122,8,6,1,
        7,1,7,5,7,126,8,7,10,7,12,7,129,9,7,1,7,5,7,132,8,7,10,7,12,7,135,
        9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,145,8,8,1,9,1,9,1,9,1,9,
        3,9,151,8,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,159,8,10,1,10,1,10,1,
        11,1,11,1,11,1,11,5,11,167,8,11,10,11,12,11,170,9,11,3,11,172,8,
        11,1,11,1,11,1,12,1,12,3,12,178,8,12,1,13,1,13,1,13,1,13,1,13,1,
        13,3,13,186,8,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,
        15,1,15,1,16,1,16,1,16,1,16,1,16,5,16,204,8,16,10,16,12,16,207,9,
        16,1,16,1,16,1,17,1,17,1,17,1,17,4,17,215,8,17,11,17,12,17,216,1,
        17,1,17,1,18,1,18,1,19,1,19,1,19,5,19,226,8,19,10,19,12,19,229,9,
        19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,
        22,1,23,1,23,1,23,1,23,1,23,1,23,3,23,250,8,23,1,23,3,23,253,8,23,
        1,24,1,24,1,24,1,24,1,24,1,24,3,24,261,8,24,1,25,1,25,1,25,1,26,
        1,26,5,26,268,8,26,10,26,12,26,271,9,26,1,26,1,26,1,27,1,27,1,27,
        1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,30,
        1,30,1,30,1,30,1,30,3,30,295,8,30,1,30,1,30,3,30,299,8,30,1,31,1,
        31,1,31,1,31,1,31,3,31,306,8,31,1,31,1,31,1,31,1,31,1,31,3,31,313,
        8,31,3,31,315,8,31,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,
        1,33,1,34,1,34,1,34,5,34,330,8,34,10,34,12,34,333,9,34,1,35,1,35,
        1,35,5,35,338,8,35,10,35,12,35,341,9,35,1,36,1,36,1,36,1,36,4,36,
        347,8,36,11,36,12,36,348,1,36,1,36,4,36,353,8,36,11,36,12,36,354,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
        3,36,383,8,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,5,36,397,8,36,10,36,12,36,400,9,36,1,36,0,1,72,37,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,0,4,2,0,22,23,32,32,1,0,20,21,
        1,0,24,29,1,0,33,34,426,0,74,1,0,0,0,2,81,1,0,0,0,4,93,1,0,0,0,6,
        96,1,0,0,0,8,114,1,0,0,0,10,116,1,0,0,0,12,119,1,0,0,0,14,123,1,
        0,0,0,16,144,1,0,0,0,18,146,1,0,0,0,20,155,1,0,0,0,22,162,1,0,0,
        0,24,177,1,0,0,0,26,185,1,0,0,0,28,187,1,0,0,0,30,192,1,0,0,0,32,
        198,1,0,0,0,34,210,1,0,0,0,36,220,1,0,0,0,38,222,1,0,0,0,40,230,
        1,0,0,0,42,234,1,0,0,0,44,238,1,0,0,0,46,243,1,0,0,0,48,254,1,0,
        0,0,50,262,1,0,0,0,52,265,1,0,0,0,54,274,1,0,0,0,56,280,1,0,0,0,
        58,286,1,0,0,0,60,289,1,0,0,0,62,314,1,0,0,0,64,316,1,0,0,0,66,321,
        1,0,0,0,68,326,1,0,0,0,70,334,1,0,0,0,72,382,1,0,0,0,74,78,3,2,1,
        0,75,77,3,8,4,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,
        1,0,0,0,79,1,1,0,0,0,80,78,1,0,0,0,81,82,5,44,0,0,82,83,5,49,0,0,
        83,88,3,4,2,0,84,87,3,6,3,0,85,87,3,8,4,0,86,84,1,0,0,0,86,85,1,
        0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,
        88,1,0,0,0,91,92,5,50,0,0,92,3,1,0,0,0,93,94,5,17,0,0,94,95,3,52,
        26,0,95,5,1,0,0,0,96,97,5,1,0,0,97,98,3,12,6,0,98,7,1,0,0,0,99,115,
        3,44,22,0,100,115,3,10,5,0,101,115,3,14,7,0,102,115,3,18,9,0,103,
        115,3,46,23,0,104,115,3,54,27,0,105,115,3,56,28,0,106,115,3,52,26,
        0,107,115,3,58,29,0,108,115,3,40,20,0,109,115,3,42,21,0,110,115,
        3,30,15,0,111,115,3,60,30,0,112,115,3,34,17,0,113,115,3,72,36,0,
        114,99,1,0,0,0,114,100,1,0,0,0,114,101,1,0,0,0,114,102,1,0,0,0,114,
        103,1,0,0,0,114,104,1,0,0,0,114,105,1,0,0,0,114,106,1,0,0,0,114,
        107,1,0,0,0,114,108,1,0,0,0,114,109,1,0,0,0,114,110,1,0,0,0,114,
        111,1,0,0,0,114,112,1,0,0,0,114,113,1,0,0,0,115,9,1,0,0,0,116,117,
        5,2,0,0,117,118,3,12,6,0,118,11,1,0,0,0,119,121,5,44,0,0,120,122,
        3,16,8,0,121,120,1,0,0,0,121,122,1,0,0,0,122,13,1,0,0,0,123,127,
        5,44,0,0,124,126,3,38,19,0,125,124,1,0,0,0,126,129,1,0,0,0,127,125,
        1,0,0,0,127,128,1,0,0,0,128,133,1,0,0,0,129,127,1,0,0,0,130,132,
        3,26,13,0,131,130,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,
        1,0,0,0,134,136,1,0,0,0,135,133,1,0,0,0,136,137,3,16,8,0,137,15,
        1,0,0,0,138,139,5,53,0,0,139,145,3,32,16,0,140,141,5,53,0,0,141,
        145,3,22,11,0,142,143,5,53,0,0,143,145,3,72,36,0,144,138,1,0,0,0,
        144,140,1,0,0,0,144,142,1,0,0,0,145,17,1,0,0,0,146,147,5,15,0,0,
        147,148,5,44,0,0,148,150,5,45,0,0,149,151,3,68,34,0,150,149,1,0,
        0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,153,5,46,0,0,153,154,3,52,
        26,0,154,19,1,0,0,0,155,156,5,44,0,0,156,158,5,45,0,0,157,159,3,
        70,35,0,158,157,1,0,0,0,158,159,1,0,0,0,159,160,1,0,0,0,160,161,
        5,46,0,0,161,21,1,0,0,0,162,171,5,47,0,0,163,168,3,24,12,0,164,165,
        5,51,0,0,165,167,3,24,12,0,166,164,1,0,0,0,167,170,1,0,0,0,168,166,
        1,0,0,0,168,169,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,171,163,
        1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,48,0,0,174,23,
        1,0,0,0,175,178,3,72,36,0,176,178,3,22,11,0,177,175,1,0,0,0,177,
        176,1,0,0,0,178,25,1,0,0,0,179,180,5,47,0,0,180,181,5,41,0,0,181,
        186,5,48,0,0,182,183,5,47,0,0,183,184,5,44,0,0,184,186,5,48,0,0,
        185,179,1,0,0,0,185,182,1,0,0,0,186,27,1,0,0,0,187,188,5,3,0,0,188,
        189,5,45,0,0,189,190,5,44,0,0,190,191,5,46,0,0,191,29,1,0,0,0,192,
        193,5,44,0,0,193,194,5,52,0,0,194,195,5,4,0,0,195,196,5,45,0,0,196,
        197,5,46,0,0,197,31,1,0,0,0,198,199,5,44,0,0,199,205,5,49,0,0,200,
        201,3,36,18,0,201,202,3,16,8,0,202,204,1,0,0,0,203,200,1,0,0,0,204,
        207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,208,1,0,0,0,207,
        205,1,0,0,0,208,209,5,50,0,0,209,33,1,0,0,0,210,211,5,5,0,0,211,
        212,5,44,0,0,212,214,5,49,0,0,213,215,3,36,18,0,214,213,1,0,0,0,
        215,216,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,218,1,0,0,0,
        218,219,5,50,0,0,219,35,1,0,0,0,220,221,5,44,0,0,221,37,1,0,0,0,
        222,223,5,52,0,0,223,227,5,44,0,0,224,226,3,26,13,0,225,224,1,0,
        0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,39,1,0,0,
        0,229,227,1,0,0,0,230,231,5,44,0,0,231,232,5,30,0,0,232,233,3,72,
        36,0,233,41,1,0,0,0,234,235,5,44,0,0,235,236,5,31,0,0,236,237,3,
        72,36,0,237,43,1,0,0,0,238,239,5,11,0,0,239,240,5,45,0,0,240,241,
        3,72,36,0,241,242,5,46,0,0,242,45,1,0,0,0,243,244,5,7,0,0,244,245,
        5,45,0,0,245,246,3,72,36,0,246,247,5,46,0,0,247,249,3,52,26,0,248,
        250,3,48,24,0,249,248,1,0,0,0,249,250,1,0,0,0,250,252,1,0,0,0,251,
        253,3,50,25,0,252,251,1,0,0,0,252,253,1,0,0,0,253,47,1,0,0,0,254,
        255,5,8,0,0,255,256,5,45,0,0,256,257,3,72,36,0,257,258,5,46,0,0,
        258,260,3,52,26,0,259,261,3,48,24,0,260,259,1,0,0,0,260,261,1,0,
        0,0,261,49,1,0,0,0,262,263,5,9,0,0,263,264,3,52,26,0,264,51,1,0,
        0,0,265,269,5,49,0,0,266,268,3,8,4,0,267,266,1,0,0,0,268,271,1,0,
        0,0,269,267,1,0,0,0,269,270,1,0,0,0,270,272,1,0,0,0,271,269,1,0,
        0,0,272,273,5,50,0,0,273,53,1,0,0,0,274,275,5,12,0,0,275,276,5,44,
        0,0,276,277,5,13,0,0,277,278,5,44,0,0,278,279,3,52,26,0,279,55,1,
        0,0,0,280,281,5,14,0,0,281,282,5,45,0,0,282,283,3,72,36,0,283,284,
        5,46,0,0,284,285,3,52,26,0,285,57,1,0,0,0,286,287,5,10,0,0,287,288,
        3,72,36,0,288,59,1,0,0,0,289,290,5,6,0,0,290,291,5,45,0,0,291,294,
        5,44,0,0,292,293,5,51,0,0,293,295,3,66,33,0,294,292,1,0,0,0,294,
        295,1,0,0,0,295,296,1,0,0,0,296,298,5,46,0,0,297,299,5,16,0,0,298,
        297,1,0,0,0,298,299,1,0,0,0,299,61,1,0,0,0,300,301,5,19,0,0,301,
        302,5,13,0,0,302,305,3,66,33,0,303,304,5,51,0,0,304,306,3,64,32,
        0,305,303,1,0,0,0,305,306,1,0,0,0,306,315,1,0,0,0,307,308,5,19,0,
        0,308,309,5,13,0,0,309,312,5,44,0,0,310,311,5,51,0,0,311,313,3,64,
        32,0,312,310,1,0,0,0,312,313,1,0,0,0,313,315,1,0,0,0,314,300,1,0,
        0,0,314,307,1,0,0,0,315,63,1,0,0,0,316,317,5,18,0,0,317,318,5,45,
        0,0,318,319,3,72,36,0,319,320,5,46,0,0,320,65,1,0,0,0,321,322,3,
        72,36,0,322,323,5,52,0,0,323,324,5,52,0,0,324,325,3,72,36,0,325,
        67,1,0,0,0,326,331,5,44,0,0,327,328,5,51,0,0,328,330,5,44,0,0,329,
        327,1,0,0,0,330,333,1,0,0,0,331,329,1,0,0,0,331,332,1,0,0,0,332,
        69,1,0,0,0,333,331,1,0,0,0,334,339,3,72,36,0,335,336,5,51,0,0,336,
        338,3,72,36,0,337,335,1,0,0,0,338,341,1,0,0,0,339,337,1,0,0,0,339,
        340,1,0,0,0,340,71,1,0,0,0,341,339,1,0,0,0,342,343,6,36,-1,0,343,
        383,3,20,10,0,344,346,5,44,0,0,345,347,3,38,19,0,346,345,1,0,0,0,
        347,348,1,0,0,0,348,346,1,0,0,0,348,349,1,0,0,0,349,383,1,0,0,0,
        350,352,5,44,0,0,351,353,3,26,13,0,352,351,1,0,0,0,353,354,1,0,0,
        0,354,352,1,0,0,0,354,355,1,0,0,0,355,383,1,0,0,0,356,383,3,28,14,
        0,357,383,3,62,31,0,358,359,5,35,0,0,359,383,3,72,36,10,360,361,
        5,38,0,0,361,362,5,45,0,0,362,363,3,72,36,0,363,364,5,46,0,0,364,
        383,1,0,0,0,365,366,5,39,0,0,366,367,5,45,0,0,367,368,3,72,36,0,
        368,369,5,51,0,0,369,370,3,72,36,0,370,371,5,46,0,0,371,383,1,0,
        0,0,372,373,5,45,0,0,373,374,3,72,36,0,374,375,5,46,0,0,375,383,
        1,0,0,0,376,383,5,44,0,0,377,383,5,41,0,0,378,383,5,42,0,0,379,383,
        5,43,0,0,380,383,5,36,0,0,381,383,5,37,0,0,382,342,1,0,0,0,382,344,
        1,0,0,0,382,350,1,0,0,0,382,356,1,0,0,0,382,357,1,0,0,0,382,358,
        1,0,0,0,382,360,1,0,0,0,382,365,1,0,0,0,382,372,1,0,0,0,382,376,
        1,0,0,0,382,377,1,0,0,0,382,378,1,0,0,0,382,379,1,0,0,0,382,380,
        1,0,0,0,382,381,1,0,0,0,383,398,1,0,0,0,384,385,10,14,0,0,385,386,
        7,0,0,0,386,397,3,72,36,15,387,388,10,13,0,0,388,389,7,1,0,0,389,
        397,3,72,36,14,390,391,10,12,0,0,391,392,7,2,0,0,392,397,3,72,36,
        13,393,394,10,11,0,0,394,395,7,3,0,0,395,397,3,72,36,12,396,384,
        1,0,0,0,396,387,1,0,0,0,396,390,1,0,0,0,396,393,1,0,0,0,397,400,
        1,0,0,0,398,396,1,0,0,0,398,399,1,0,0,0,399,73,1,0,0,0,400,398,1,
        0,0,0,33,78,86,88,114,121,127,133,144,150,158,168,171,177,185,205,
        216,227,249,252,260,269,294,298,305,312,314,331,339,348,354,382,
        396,398
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'field'", "'let'", "'len'", "'pop'", 
                     "'struct'", "'WhiteNoise'", "'if'", "'elif'", "'else'", 
                     "'return'", "'print'", "'for'", "'in'", "'while'", 
                     "'def'", "'layer'", "'procedure'", "'seed'", "'random'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'>='", "'<'", "'<='", 
                     "'=='", "'!='", "'+='", "'-='", "'%'", "'and'", "'or'", 
                     "'not'", "'True'", "'False'", "'sqrt'", "'pow'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'.'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELIF", 
                      "ELSE", "RETURN", "PRINT", "FOR", "IN", "WHILE", "DEF", 
                      "LAYER", "PROCEDURE", "SEED", "RANDOM", "PLUS", "MINUS", 
                      "MULT", "DIV", "GT", "GTE", "LT", "LTE", "EQ", "NEQ", 
                      "PEQ", "MEQ", "MOD", "AND", "OR", "NOT", "TRUE", "FALSE", 
                      "SQRT", "POW", "COMMENT_SINGLELINE", "INT", "FLOAT", 
                      "STRING", "ID", "OPEN_PARENTH", "CLOSED_PARENTH", 
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
    RULE_struct = 16
    RULE_structDef = 17
    RULE_structField = 18
    RULE_structFieldAccess = 19
    RULE_plusEquals = 20
    RULE_minusEquals = 21
    RULE_printStat = 22
    RULE_ifStat = 23
    RULE_elifStat = 24
    RULE_elseStat = 25
    RULE_statBlock = 26
    RULE_forLoop = 27
    RULE_whileLoop = 28
    RULE_returnStat = 29
    RULE_whiteNoiseStat = 30
    RULE_random = 31
    RULE_seedRule = 32
    RULE_range = 33
    RULE_params = 34
    RULE_args = 35
    RULE_expr = 36

    ruleNames =  [ "prog", "object", "procedure", "field", "stat", "varDeclStat", 
                   "varDecl", "assignStat", "assignment", "functionDecl", 
                   "functionCall", "list", "listElement", "listAccess", 
                   "listLength", "listPop", "struct", "structDef", "structField", 
                   "structFieldAccess", "plusEquals", "minusEquals", "printStat", 
                   "ifStat", "elifStat", "elseStat", "statBlock", "forLoop", 
                   "whileLoop", "returnStat", "whiteNoiseStat", "random", 
                   "seedRule", "range", "params", "args", "expr" ]

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
    SEED=18
    RANDOM=19
    PLUS=20
    MINUS=21
    MULT=22
    DIV=23
    GT=24
    GTE=25
    LT=26
    LTE=27
    EQ=28
    NEQ=29
    PEQ=30
    MEQ=31
    MOD=32
    AND=33
    OR=34
    NOT=35
    TRUE=36
    FALSE=37
    SQRT=38
    POW=39
    COMMENT_SINGLELINE=40
    INT=41
    FLOAT=42
    STRING=43
    ID=44
    OPEN_PARENTH=45
    CLOSED_PARENTH=46
    OPEN_BRACK=47
    CLOSED_BRACK=48
    OPEN_CURL=49
    CLOSED_CURL=50
    COMMA=51
    DOT=52
    EQUAL_SIGN=53
    WS=54

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
            self.state = 74
            self.object_()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 632184826813676) != 0):
                self.state = 75
                self.stat()
                self.state = 80
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
            self.state = 81
            self.match(RogueLangParser.ID)
            self.state = 82
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 83
            self.procedure()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 632184826813678) != 0):
                self.state = 86
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 84
                    self.field()
                    pass
                elif token in [2, 3, 5, 6, 7, 10, 11, 12, 14, 15, 19, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 49]:
                    self.state = 85
                    self.stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
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
            self.state = 93
            self.match(RogueLangParser.PROCEDURE)
            self.state = 94
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
            self.state = 96
            self.match(RogueLangParser.T__0)
            self.state = 97
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


        def structDef(self):
            return self.getTypedRuleContext(RogueLangParser.StructDefContext,0)


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
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.varDeclStat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.assignStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.functionDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 103
                self.ifStat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 104
                self.forLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 105
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 106
                self.statBlock()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 107
                self.returnStat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 108
                self.plusEquals()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 109
                self.minusEquals()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 110
                self.listPop()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 111
                self.whiteNoiseStat()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 112
                self.structDef()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 113
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
            self.state = 116
            self.match(RogueLangParser.T__1)
            self.state = 117
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
            self.state = 119
            self.match(RogueLangParser.ID)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 120
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


        def structFieldAccess(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StructFieldAccessContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StructFieldAccessContext,i)


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
            self.state = 123
            self.match(RogueLangParser.ID)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 124
                self.structFieldAccess()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 130
                self.listAccess()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
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

        def struct(self):
            return self.getTypedRuleContext(RogueLangParser.StructContext,0)


        def list_(self):
            return self.getTypedRuleContext(RogueLangParser.ListContext,0)


        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


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
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 139
                self.struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 141
                self.list_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 143
                self.expr(0)
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
            self.state = 146
            self.match(RogueLangParser.DEF)
            self.state = 147
            self.match(RogueLangParser.ID)
            self.state = 148
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 149
                self.params()


            self.state = 152
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 153
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
            self.state = 155
            self.match(RogueLangParser.ID)
            self.state = 156
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 69234873335816) != 0):
                self.state = 157
                self.args()


            self.state = 160
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
            self.state = 162
            self.match(RogueLangParser.OPEN_BRACK)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 209972361691144) != 0):
                self.state = 163
                self.listElement()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 164
                    self.match(RogueLangParser.COMMA)
                    self.state = 165
                    self.listElement()
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 173
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
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 19, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.expr(0)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
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
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 180
                self.match(RogueLangParser.INT)
                self.state = 181
                self.match(RogueLangParser.CLOSED_BRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 183
                self.match(RogueLangParser.ID)
                self.state = 184
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
            self.state = 187
            self.match(RogueLangParser.T__2)
            self.state = 188
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 189
            self.match(RogueLangParser.ID)
            self.state = 190
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
            self.state = 192
            self.match(RogueLangParser.ID)
            self.state = 193
            self.match(RogueLangParser.DOT)
            self.state = 194
            self.match(RogueLangParser.T__3)
            self.state = 195
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 196
            self.match(RogueLangParser.CLOSED_PARENTH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def OPEN_CURL(self):
            return self.getToken(RogueLangParser.OPEN_CURL, 0)

        def CLOSED_CURL(self):
            return self.getToken(RogueLangParser.CLOSED_CURL, 0)

        def structField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StructFieldContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StructFieldContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.AssignmentContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct" ):
                return visitor.visitStruct(self)
            else:
                return visitor.visitChildren(self)




    def struct(self):

        localctx = RogueLangParser.StructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(RogueLangParser.ID)
            self.state = 199
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 200
                self.structField()
                self.state = 201
                self.assignment()
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


    class StructDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def OPEN_CURL(self):
            return self.getToken(RogueLangParser.OPEN_CURL, 0)

        def CLOSED_CURL(self):
            return self.getToken(RogueLangParser.CLOSED_CURL, 0)

        def structField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StructFieldContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StructFieldContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_structDef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDef" ):
                return visitor.visitStructDef(self)
            else:
                return visitor.visitChildren(self)




    def structDef(self):

        localctx = RogueLangParser.StructDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_structDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(RogueLangParser.T__4)
            self.state = 211
            self.match(RogueLangParser.ID)
            self.state = 212
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 214 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 213
                self.structField()
                self.state = 216 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==44):
                    break

            self.state = 218
            self.match(RogueLangParser.CLOSED_CURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_structField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructField" ):
                return visitor.visitStructField(self)
            else:
                return visitor.visitChildren(self)




    def structField(self):

        localctx = RogueLangParser.StructFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_structField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(RogueLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(RogueLangParser.DOT, 0)

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def listAccess(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ListAccessContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ListAccessContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_structFieldAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldAccess" ):
                return visitor.visitStructFieldAccess(self)
            else:
                return visitor.visitChildren(self)




    def structFieldAccess(self):

        localctx = RogueLangParser.StructFieldAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_structFieldAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(RogueLangParser.DOT)
            self.state = 223
            self.match(RogueLangParser.ID)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 224
                    self.listAccess() 
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 40, self.RULE_plusEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(RogueLangParser.ID)
            self.state = 231
            self.match(RogueLangParser.PEQ)
            self.state = 232
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
        self.enterRule(localctx, 42, self.RULE_minusEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(RogueLangParser.ID)
            self.state = 235
            self.match(RogueLangParser.MEQ)
            self.state = 236
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
        self.enterRule(localctx, 44, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(RogueLangParser.PRINT)
            self.state = 239
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 240
            self.expr(0)
            self.state = 241
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
        self.enterRule(localctx, 46, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(RogueLangParser.IF)
            self.state = 244
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 245
            self.expr(0)
            self.state = 246
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 247
            self.statBlock()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 248
                self.elifStat()


            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 251
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
        self.enterRule(localctx, 48, self.RULE_elifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(RogueLangParser.ELIF)
            self.state = 255
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 256
            self.expr(0)
            self.state = 257
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 258
            self.statBlock()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 259
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
        self.enterRule(localctx, 50, self.RULE_elseStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(RogueLangParser.ELSE)
            self.state = 263
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
        self.enterRule(localctx, 52, self.RULE_statBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 632184826813676) != 0):
                self.state = 266
                self.stat()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
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
        self.enterRule(localctx, 54, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(RogueLangParser.FOR)
            self.state = 275
            self.match(RogueLangParser.ID)
            self.state = 276
            self.match(RogueLangParser.IN)
            self.state = 277
            self.match(RogueLangParser.ID)
            self.state = 278
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
        self.enterRule(localctx, 56, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(RogueLangParser.WHILE)
            self.state = 281
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 282
            self.expr(0)
            self.state = 283
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 284
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
        self.enterRule(localctx, 58, self.RULE_returnStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(RogueLangParser.RETURN)
            self.state = 287
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
        self.enterRule(localctx, 60, self.RULE_whiteNoiseStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(RogueLangParser.T__5)
            self.state = 290
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 291
            self.match(RogueLangParser.ID)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 292
                self.match(RogueLangParser.COMMA)
                self.state = 293
                self.range_()


            self.state = 296
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 297
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

        def RANDOM(self):
            return self.getToken(RogueLangParser.RANDOM, 0)

        def IN(self):
            return self.getToken(RogueLangParser.IN, 0)

        def range_(self):
            return self.getTypedRuleContext(RogueLangParser.RangeContext,0)


        def COMMA(self):
            return self.getToken(RogueLangParser.COMMA, 0)

        def seedRule(self):
            return self.getTypedRuleContext(RogueLangParser.SeedRuleContext,0)


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
        self.enterRule(localctx, 62, self.RULE_random)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(RogueLangParser.RANDOM)
                self.state = 301
                self.match(RogueLangParser.IN)
                self.state = 302
                self.range_()
                self.state = 305
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 303
                    self.match(RogueLangParser.COMMA)
                    self.state = 304
                    self.seedRule()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.match(RogueLangParser.RANDOM)
                self.state = 308
                self.match(RogueLangParser.IN)
                self.state = 309
                self.match(RogueLangParser.ID)
                self.state = 312
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 310
                    self.match(RogueLangParser.COMMA)
                    self.state = 311
                    self.seedRule()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeedRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEED(self):
            return self.getToken(RogueLangParser.SEED, 0)

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_seedRule

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeedRule" ):
                return visitor.visitSeedRule(self)
            else:
                return visitor.visitChildren(self)




    def seedRule(self):

        localctx = RogueLangParser.SeedRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_seedRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(RogueLangParser.SEED)
            self.state = 317
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 318
            self.expr(0)
            self.state = 319
            self.match(RogueLangParser.CLOSED_PARENTH)
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
        self.enterRule(localctx, 66, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.expr(0)
            self.state = 322
            self.match(RogueLangParser.DOT)
            self.state = 323
            self.match(RogueLangParser.DOT)
            self.state = 324
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
        self.enterRule(localctx, 68, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(RogueLangParser.ID)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 327
                self.match(RogueLangParser.COMMA)
                self.state = 328
                self.match(RogueLangParser.ID)
                self.state = 333
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
        self.enterRule(localctx, 70, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.expr(0)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 335
                self.match(RogueLangParser.COMMA)
                self.state = 336
                self.expr(0)
                self.state = 341
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

        def structFieldAccess(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StructFieldAccessContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StructFieldAccessContext,i)


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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 343
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 344
                self.match(RogueLangParser.ID)
                self.state = 346 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 345
                        self.structFieldAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 348 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                pass

            elif la_ == 3:
                self.state = 350
                self.match(RogueLangParser.ID)
                self.state = 352 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 351
                        self.listAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 354 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                pass

            elif la_ == 4:
                self.state = 356
                self.listLength()
                pass

            elif la_ == 5:
                self.state = 357
                self.random()
                pass

            elif la_ == 6:
                self.state = 358
                self.match(RogueLangParser.NOT)
                self.state = 359
                self.expr(10)
                pass

            elif la_ == 7:
                self.state = 360
                self.match(RogueLangParser.SQRT)
                self.state = 361
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 362
                self.expr(0)
                self.state = 363
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 8:
                self.state = 365
                self.match(RogueLangParser.POW)
                self.state = 366
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 367
                self.expr(0)
                self.state = 368
                self.match(RogueLangParser.COMMA)
                self.state = 369
                self.expr(0)
                self.state = 370
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 9:
                self.state = 372
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 373
                self.expr(0)
                self.state = 374
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 10:
                self.state = 376
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 11:
                self.state = 377
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 12:
                self.state = 378
                self.match(RogueLangParser.FLOAT)
                pass

            elif la_ == 13:
                self.state = 379
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 14:
                self.state = 380
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 15:
                self.state = 381
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 396
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 384
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 385
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4307550208) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 386
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 387
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 388
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 389
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 390
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 391
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 392
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 393
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 394
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==33 or _la==34):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 395
                        self.expr(12)
                        pass

             
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        self._predicates[36] = self.expr_sempred
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
         




