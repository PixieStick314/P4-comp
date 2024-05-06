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
        4,1,55,406,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,5,0,76,8,0,10,0,12,0,79,9,
        0,1,0,1,0,5,0,83,8,0,10,0,12,0,86,9,0,1,1,1,1,1,1,1,1,1,1,1,1,5,
        1,94,8,1,10,1,12,1,97,9,1,1,1,1,1,1,1,5,1,102,8,1,10,1,12,1,105,
        9,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,132,8,5,1,6,1,6,1,6,
        1,7,1,7,3,7,139,8,7,1,8,1,8,5,8,143,8,8,10,8,12,8,146,9,8,1,8,5,
        8,149,8,8,10,8,12,8,152,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,
        162,8,9,1,10,1,10,1,10,1,10,3,10,168,8,10,1,10,1,10,1,10,1,11,1,
        11,1,11,3,11,176,8,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,184,8,12,
        10,12,12,12,187,9,12,3,12,189,8,12,1,12,1,12,1,13,1,13,3,13,195,
        8,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,203,8,14,1,15,1,15,1,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        5,17,221,8,17,10,17,12,17,224,9,17,1,17,1,17,1,18,1,18,1,18,1,18,
        4,18,232,8,18,11,18,12,18,233,1,18,1,18,1,19,1,19,1,20,1,20,1,20,
        5,20,243,8,20,10,20,12,20,246,9,20,1,21,1,21,1,21,1,21,1,22,1,22,
        1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,
        3,24,267,8,24,1,24,3,24,270,8,24,1,25,1,25,1,25,1,25,1,25,1,25,3,
        25,278,8,25,1,26,1,26,1,26,1,27,1,27,5,27,285,8,27,10,27,12,27,288,
        9,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,
        1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,3,31,312,8,31,
        1,31,1,31,3,31,316,8,31,1,32,1,32,1,32,1,32,1,32,1,32,3,32,324,8,
        32,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,5,34,334,8,34,10,34,12,
        34,337,9,34,1,35,1,35,1,35,5,35,342,8,35,10,35,12,35,345,9,35,1,
        36,1,36,1,36,1,36,4,36,351,8,36,11,36,12,36,352,1,36,1,36,4,36,357,
        8,36,11,36,12,36,358,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,3,36,387,8,36,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,5,36,401,8,36,10,36,12,36,404,9,36,
        1,36,0,1,72,37,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,0,5,1,0,
        2,3,2,0,23,24,33,33,1,0,21,22,1,0,25,30,1,0,34,35,431,0,77,1,0,0,
        0,2,87,1,0,0,0,4,108,1,0,0,0,6,110,1,0,0,0,8,113,1,0,0,0,10,131,
        1,0,0,0,12,133,1,0,0,0,14,136,1,0,0,0,16,140,1,0,0,0,18,161,1,0,
        0,0,20,163,1,0,0,0,22,172,1,0,0,0,24,179,1,0,0,0,26,194,1,0,0,0,
        28,202,1,0,0,0,30,204,1,0,0,0,32,209,1,0,0,0,34,215,1,0,0,0,36,227,
        1,0,0,0,38,237,1,0,0,0,40,239,1,0,0,0,42,247,1,0,0,0,44,251,1,0,
        0,0,46,255,1,0,0,0,48,260,1,0,0,0,50,271,1,0,0,0,52,279,1,0,0,0,
        54,282,1,0,0,0,56,291,1,0,0,0,58,297,1,0,0,0,60,303,1,0,0,0,62,306,
        1,0,0,0,64,323,1,0,0,0,66,325,1,0,0,0,68,330,1,0,0,0,70,338,1,0,
        0,0,72,386,1,0,0,0,74,76,3,10,5,0,75,74,1,0,0,0,76,79,1,0,0,0,77,
        75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,84,3,2,1,
        0,81,83,3,10,5,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,
        1,0,0,0,85,1,1,0,0,0,86,84,1,0,0,0,87,88,5,1,0,0,88,89,3,4,2,0,89,
        90,5,45,0,0,90,95,5,50,0,0,91,94,3,8,4,0,92,94,3,10,5,0,93,91,1,
        0,0,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,
        98,1,0,0,0,97,95,1,0,0,0,98,103,3,6,3,0,99,102,3,8,4,0,100,102,3,
        10,5,0,101,99,1,0,0,0,101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,
        0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,
        51,0,0,107,3,1,0,0,0,108,109,7,0,0,0,109,5,1,0,0,0,110,111,5,20,
        0,0,111,112,3,54,27,0,112,7,1,0,0,0,113,114,5,1,0,0,114,115,3,14,
        7,0,115,9,1,0,0,0,116,132,3,46,23,0,117,132,3,12,6,0,118,132,3,16,
        8,0,119,132,3,20,10,0,120,132,3,48,24,0,121,132,3,56,28,0,122,132,
        3,58,29,0,123,132,3,54,27,0,124,132,3,60,30,0,125,132,3,42,21,0,
        126,132,3,44,22,0,127,132,3,32,16,0,128,132,3,62,31,0,129,132,3,
        36,18,0,130,132,3,72,36,0,131,116,1,0,0,0,131,117,1,0,0,0,131,118,
        1,0,0,0,131,119,1,0,0,0,131,120,1,0,0,0,131,121,1,0,0,0,131,122,
        1,0,0,0,131,123,1,0,0,0,131,124,1,0,0,0,131,125,1,0,0,0,131,126,
        1,0,0,0,131,127,1,0,0,0,131,128,1,0,0,0,131,129,1,0,0,0,131,130,
        1,0,0,0,132,11,1,0,0,0,133,134,5,4,0,0,134,135,3,14,7,0,135,13,1,
        0,0,0,136,138,5,45,0,0,137,139,3,18,9,0,138,137,1,0,0,0,138,139,
        1,0,0,0,139,15,1,0,0,0,140,144,5,45,0,0,141,143,3,40,20,0,142,141,
        1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,150,
        1,0,0,0,146,144,1,0,0,0,147,149,3,28,14,0,148,147,1,0,0,0,149,152,
        1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,150,
        1,0,0,0,153,154,3,18,9,0,154,17,1,0,0,0,155,156,5,54,0,0,156,162,
        3,34,17,0,157,158,5,54,0,0,158,162,3,24,12,0,159,160,5,54,0,0,160,
        162,3,72,36,0,161,155,1,0,0,0,161,157,1,0,0,0,161,159,1,0,0,0,162,
        19,1,0,0,0,163,164,5,18,0,0,164,165,5,45,0,0,165,167,5,46,0,0,166,
        168,3,68,34,0,167,166,1,0,0,0,167,168,1,0,0,0,168,169,1,0,0,0,169,
        170,5,47,0,0,170,171,3,54,27,0,171,21,1,0,0,0,172,173,5,45,0,0,173,
        175,5,46,0,0,174,176,3,70,35,0,175,174,1,0,0,0,175,176,1,0,0,0,176,
        177,1,0,0,0,177,178,5,47,0,0,178,23,1,0,0,0,179,188,5,48,0,0,180,
        185,3,26,13,0,181,182,5,52,0,0,182,184,3,26,13,0,183,181,1,0,0,0,
        184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,189,1,0,0,0,
        187,185,1,0,0,0,188,180,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,
        190,191,5,49,0,0,191,25,1,0,0,0,192,195,3,72,36,0,193,195,3,24,12,
        0,194,192,1,0,0,0,194,193,1,0,0,0,195,27,1,0,0,0,196,197,5,48,0,
        0,197,198,5,42,0,0,198,203,5,49,0,0,199,200,5,48,0,0,200,201,5,45,
        0,0,201,203,5,49,0,0,202,196,1,0,0,0,202,199,1,0,0,0,203,29,1,0,
        0,0,204,205,5,5,0,0,205,206,5,46,0,0,206,207,5,45,0,0,207,208,5,
        47,0,0,208,31,1,0,0,0,209,210,5,45,0,0,210,211,5,53,0,0,211,212,
        5,6,0,0,212,213,5,46,0,0,213,214,5,47,0,0,214,33,1,0,0,0,215,216,
        5,45,0,0,216,222,5,50,0,0,217,218,3,38,19,0,218,219,3,18,9,0,219,
        221,1,0,0,0,220,217,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,
        223,1,0,0,0,223,225,1,0,0,0,224,222,1,0,0,0,225,226,5,51,0,0,226,
        35,1,0,0,0,227,228,5,7,0,0,228,229,5,45,0,0,229,231,5,50,0,0,230,
        232,3,38,19,0,231,230,1,0,0,0,232,233,1,0,0,0,233,231,1,0,0,0,233,
        234,1,0,0,0,234,235,1,0,0,0,235,236,5,51,0,0,236,37,1,0,0,0,237,
        238,5,45,0,0,238,39,1,0,0,0,239,240,5,53,0,0,240,244,5,45,0,0,241,
        243,3,28,14,0,242,241,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,
        245,1,0,0,0,245,41,1,0,0,0,246,244,1,0,0,0,247,248,5,45,0,0,248,
        249,5,31,0,0,249,250,3,72,36,0,250,43,1,0,0,0,251,252,5,45,0,0,252,
        253,5,32,0,0,253,254,3,72,36,0,254,45,1,0,0,0,255,256,5,14,0,0,256,
        257,5,46,0,0,257,258,3,72,36,0,258,259,5,47,0,0,259,47,1,0,0,0,260,
        261,5,10,0,0,261,262,5,46,0,0,262,263,3,72,36,0,263,264,5,47,0,0,
        264,266,3,54,27,0,265,267,3,50,25,0,266,265,1,0,0,0,266,267,1,0,
        0,0,267,269,1,0,0,0,268,270,3,52,26,0,269,268,1,0,0,0,269,270,1,
        0,0,0,270,49,1,0,0,0,271,272,5,11,0,0,272,273,5,46,0,0,273,274,3,
        72,36,0,274,275,5,47,0,0,275,277,3,54,27,0,276,278,3,50,25,0,277,
        276,1,0,0,0,277,278,1,0,0,0,278,51,1,0,0,0,279,280,5,12,0,0,280,
        281,3,54,27,0,281,53,1,0,0,0,282,286,5,50,0,0,283,285,3,10,5,0,284,
        283,1,0,0,0,285,288,1,0,0,0,286,284,1,0,0,0,286,287,1,0,0,0,287,
        289,1,0,0,0,288,286,1,0,0,0,289,290,5,51,0,0,290,55,1,0,0,0,291,
        292,5,15,0,0,292,293,5,45,0,0,293,294,5,16,0,0,294,295,5,45,0,0,
        295,296,3,54,27,0,296,57,1,0,0,0,297,298,5,17,0,0,298,299,5,46,0,
        0,299,300,3,72,36,0,300,301,5,47,0,0,301,302,3,54,27,0,302,59,1,
        0,0,0,303,304,5,13,0,0,304,305,3,72,36,0,305,61,1,0,0,0,306,307,
        5,8,0,0,307,308,5,46,0,0,308,311,5,45,0,0,309,310,5,52,0,0,310,312,
        3,66,33,0,311,309,1,0,0,0,311,312,1,0,0,0,312,313,1,0,0,0,313,315,
        5,47,0,0,314,316,5,19,0,0,315,314,1,0,0,0,315,316,1,0,0,0,316,63,
        1,0,0,0,317,318,5,9,0,0,318,319,5,16,0,0,319,324,3,66,33,0,320,321,
        5,9,0,0,321,322,5,16,0,0,322,324,5,45,0,0,323,317,1,0,0,0,323,320,
        1,0,0,0,324,65,1,0,0,0,325,326,3,72,36,0,326,327,5,53,0,0,327,328,
        5,53,0,0,328,329,3,72,36,0,329,67,1,0,0,0,330,335,5,45,0,0,331,332,
        5,52,0,0,332,334,5,45,0,0,333,331,1,0,0,0,334,337,1,0,0,0,335,333,
        1,0,0,0,335,336,1,0,0,0,336,69,1,0,0,0,337,335,1,0,0,0,338,343,3,
        72,36,0,339,340,5,52,0,0,340,342,3,72,36,0,341,339,1,0,0,0,342,345,
        1,0,0,0,343,341,1,0,0,0,343,344,1,0,0,0,344,71,1,0,0,0,345,343,1,
        0,0,0,346,347,6,36,-1,0,347,387,3,22,11,0,348,350,5,45,0,0,349,351,
        3,40,20,0,350,349,1,0,0,0,351,352,1,0,0,0,352,350,1,0,0,0,352,353,
        1,0,0,0,353,387,1,0,0,0,354,356,5,45,0,0,355,357,3,28,14,0,356,355,
        1,0,0,0,357,358,1,0,0,0,358,356,1,0,0,0,358,359,1,0,0,0,359,387,
        1,0,0,0,360,387,3,30,15,0,361,387,3,64,32,0,362,363,5,36,0,0,363,
        387,3,72,36,10,364,365,5,39,0,0,365,366,5,46,0,0,366,367,3,72,36,
        0,367,368,5,47,0,0,368,387,1,0,0,0,369,370,5,40,0,0,370,371,5,46,
        0,0,371,372,3,72,36,0,372,373,5,52,0,0,373,374,3,72,36,0,374,375,
        5,47,0,0,375,387,1,0,0,0,376,377,5,46,0,0,377,378,3,72,36,0,378,
        379,5,47,0,0,379,387,1,0,0,0,380,387,5,45,0,0,381,387,5,42,0,0,382,
        387,5,43,0,0,383,387,5,44,0,0,384,387,5,37,0,0,385,387,5,38,0,0,
        386,346,1,0,0,0,386,348,1,0,0,0,386,354,1,0,0,0,386,360,1,0,0,0,
        386,361,1,0,0,0,386,362,1,0,0,0,386,364,1,0,0,0,386,369,1,0,0,0,
        386,376,1,0,0,0,386,380,1,0,0,0,386,381,1,0,0,0,386,382,1,0,0,0,
        386,383,1,0,0,0,386,384,1,0,0,0,386,385,1,0,0,0,387,402,1,0,0,0,
        388,389,10,14,0,0,389,390,7,1,0,0,390,401,3,72,36,15,391,392,10,
        13,0,0,392,393,7,2,0,0,393,401,3,72,36,14,394,395,10,12,0,0,395,
        396,7,3,0,0,396,401,3,72,36,13,397,398,10,11,0,0,398,399,7,4,0,0,
        399,401,3,72,36,12,400,388,1,0,0,0,400,391,1,0,0,0,400,394,1,0,0,
        0,400,397,1,0,0,0,401,404,1,0,0,0,402,400,1,0,0,0,402,403,1,0,0,
        0,403,73,1,0,0,0,404,402,1,0,0,0,34,77,84,93,95,101,103,131,138,
        144,150,161,167,175,185,188,194,202,222,233,244,266,269,277,286,
        311,315,323,335,343,352,358,386,400,402
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'output'", "'Custom'", "'TileMap'", "'let'", 
                     "'len'", "'pop'", "'struct'", "'WhiteNoise'", "'random'", 
                     "'if'", "'elif'", "'else'", "'return'", "'print'", 
                     "'for'", "'in'", "'while'", "'def'", "'layer'", "'procedure'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'>='", "'<'", "'<='", 
                     "'=='", "'!='", "'+='", "'-='", "'%'", "'and'", "'or'", 
                     "'not'", "'True'", "'False'", "'sqrt'", "'pow'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'.'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IF", "ELIF", "ELSE", "RETURN", 
                      "PRINT", "FOR", "IN", "WHILE", "DEF", "LAYER", "PROCEDURE", 
                      "PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", "LT", 
                      "LTE", "EQ", "NEQ", "PEQ", "MEQ", "MOD", "AND", "OR", 
                      "NOT", "TRUE", "FALSE", "SQRT", "POW", "COMMENT_SINGLELINE", 
                      "INT", "FLOAT", "STRING", "ID", "OPEN_PARENTH", "CLOSED_PARENTH", 
                      "OPEN_BRACK", "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", 
                      "COMMA", "DOT", "EQUAL_SIGN", "WS" ]

    RULE_prog = 0
    RULE_outputObject = 1
    RULE_type = 2
    RULE_procedure = 3
    RULE_outputField = 4
    RULE_stat = 5
    RULE_varDeclStat = 6
    RULE_varDecl = 7
    RULE_assignStat = 8
    RULE_assignment = 9
    RULE_functionDecl = 10
    RULE_functionCall = 11
    RULE_list = 12
    RULE_listElement = 13
    RULE_listAccess = 14
    RULE_listLength = 15
    RULE_listPop = 16
    RULE_struct = 17
    RULE_structDef = 18
    RULE_structField = 19
    RULE_structFieldAccess = 20
    RULE_plusEquals = 21
    RULE_minusEquals = 22
    RULE_printStat = 23
    RULE_ifStat = 24
    RULE_elifStat = 25
    RULE_elseStat = 26
    RULE_statBlock = 27
    RULE_forLoop = 28
    RULE_whileLoop = 29
    RULE_returnStat = 30
    RULE_whiteNoiseStat = 31
    RULE_random = 32
    RULE_range = 33
    RULE_params = 34
    RULE_args = 35
    RULE_expr = 36

    ruleNames =  [ "prog", "outputObject", "type", "procedure", "outputField", 
                   "stat", "varDeclStat", "varDecl", "assignStat", "assignment", 
                   "functionDecl", "functionCall", "list", "listElement", 
                   "listAccess", "listLength", "listPop", "struct", "structDef", 
                   "structField", "structFieldAccess", "plusEquals", "minusEquals", 
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
    T__6=7
    T__7=8
    T__8=9
    IF=10
    ELIF=11
    ELSE=12
    RETURN=13
    PRINT=14
    FOR=15
    IN=16
    WHILE=17
    DEF=18
    LAYER=19
    PROCEDURE=20
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
    PEQ=31
    MEQ=32
    MOD=33
    AND=34
    OR=35
    NOT=36
    TRUE=37
    FALSE=38
    SQRT=39
    POW=40
    COMMENT_SINGLELINE=41
    INT=42
    FLOAT=43
    STRING=44
    ID=45
    OPEN_PARENTH=46
    CLOSED_PARENTH=47
    OPEN_BRACK=48
    CLOSED_BRACK=49
    OPEN_CURL=50
    CLOSED_CURL=51
    COMMA=52
    DOT=53
    EQUAL_SIGN=54
    WS=55

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

        def outputObject(self):
            return self.getTypedRuleContext(RogueLangParser.OutputObjectContext,0)


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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1264369652918192) != 0):
                self.state = 74
                self.stat()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.outputObject()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1264369652918192) != 0):
                self.state = 81
                self.stat()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(RogueLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def OPEN_CURL(self):
            return self.getToken(RogueLangParser.OPEN_CURL, 0)

        def procedure(self):
            return self.getTypedRuleContext(RogueLangParser.ProcedureContext,0)


        def CLOSED_CURL(self):
            return self.getToken(RogueLangParser.CLOSED_CURL, 0)

        def outputField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.OutputFieldContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.OutputFieldContext,i)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatContext,i)


        def getRuleIndex(self):
            return RogueLangParser.RULE_outputObject

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputObject" ):
                return visitor.visitOutputObject(self)
            else:
                return visitor.visitChildren(self)




    def outputObject(self):

        localctx = RogueLangParser.OutputObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_outputObject)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(RogueLangParser.T__0)
            self.state = 88
            self.type_()
            self.state = 89
            self.match(RogueLangParser.ID)
            self.state = 90
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1264369652918194) != 0):
                self.state = 93
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 91
                    self.outputField()
                    pass
                elif token in [4, 5, 7, 8, 9, 10, 13, 14, 15, 17, 18, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 50]:
                    self.state = 92
                    self.stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.procedure()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1264369652918194) != 0):
                self.state = 101
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 99
                    self.outputField()
                    pass
                elif token in [4, 5, 7, 8, 9, 10, 13, 14, 15, 17, 18, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 50]:
                    self.state = 100
                    self.stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(RogueLangParser.CLOSED_CURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RogueLangParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = RogueLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
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
        self.enterRule(localctx, 6, self.RULE_procedure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(RogueLangParser.PROCEDURE)
            self.state = 111
            self.statBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(RogueLangParser.VarDeclContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_outputField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputField" ):
                return visitor.visitOutputField(self)
            else:
                return visitor.visitChildren(self)




    def outputField(self):

        localctx = RogueLangParser.OutputFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_outputField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(RogueLangParser.T__0)
            self.state = 114
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
        self.enterRule(localctx, 10, self.RULE_stat)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.varDeclStat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.assignStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                self.functionDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 120
                self.ifStat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 121
                self.forLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 122
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 123
                self.statBlock()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 124
                self.returnStat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 125
                self.plusEquals()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 126
                self.minusEquals()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 127
                self.listPop()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 128
                self.whiteNoiseStat()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 129
                self.structDef()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 130
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
        self.enterRule(localctx, 12, self.RULE_varDeclStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(RogueLangParser.T__3)
            self.state = 134
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
        self.enterRule(localctx, 14, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(RogueLangParser.ID)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 137
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
        self.enterRule(localctx, 16, self.RULE_assignStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(RogueLangParser.ID)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 141
                self.structFieldAccess()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 147
                self.listAccess()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
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
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 156
                self.struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 158
                self.list_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 160
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
        self.enterRule(localctx, 20, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(RogueLangParser.DEF)
            self.state = 164
            self.match(RogueLangParser.ID)
            self.state = 165
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 166
                self.params()


            self.state = 169
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 170
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
        self.enterRule(localctx, 22, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(RogueLangParser.ID)
            self.state = 173
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 138469745623584) != 0):
                self.state = 174
                self.args()


            self.state = 177
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
        self.enterRule(localctx, 24, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(RogueLangParser.OPEN_BRACK)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 419944722334240) != 0):
                self.state = 180
                self.listElement()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==52:
                    self.state = 181
                    self.match(RogueLangParser.COMMA)
                    self.state = 182
                    self.listElement()
                    self.state = 187
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 190
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
        self.enterRule(localctx, 26, self.RULE_listElement)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 9, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.expr(0)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
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
        self.enterRule(localctx, 28, self.RULE_listAccess)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 197
                self.match(RogueLangParser.INT)
                self.state = 198
                self.match(RogueLangParser.CLOSED_BRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 200
                self.match(RogueLangParser.ID)
                self.state = 201
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
        self.enterRule(localctx, 30, self.RULE_listLength)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(RogueLangParser.T__4)
            self.state = 205
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 206
            self.match(RogueLangParser.ID)
            self.state = 207
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
        self.enterRule(localctx, 32, self.RULE_listPop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(RogueLangParser.ID)
            self.state = 210
            self.match(RogueLangParser.DOT)
            self.state = 211
            self.match(RogueLangParser.T__5)
            self.state = 212
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 213
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
        self.enterRule(localctx, 34, self.RULE_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(RogueLangParser.ID)
            self.state = 216
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 217
                self.structField()
                self.state = 218
                self.assignment()
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
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
        self.enterRule(localctx, 36, self.RULE_structDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(RogueLangParser.T__6)
            self.state = 228
            self.match(RogueLangParser.ID)
            self.state = 229
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 231 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 230
                self.structField()
                self.state = 233 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==45):
                    break

            self.state = 235
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
        self.enterRule(localctx, 38, self.RULE_structField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
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
        self.enterRule(localctx, 40, self.RULE_structFieldAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(RogueLangParser.DOT)
            self.state = 240
            self.match(RogueLangParser.ID)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 241
                    self.listAccess() 
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_plusEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(RogueLangParser.ID)
            self.state = 248
            self.match(RogueLangParser.PEQ)
            self.state = 249
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
        self.enterRule(localctx, 44, self.RULE_minusEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(RogueLangParser.ID)
            self.state = 252
            self.match(RogueLangParser.MEQ)
            self.state = 253
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
        self.enterRule(localctx, 46, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(RogueLangParser.PRINT)
            self.state = 256
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 257
            self.expr(0)
            self.state = 258
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
        self.enterRule(localctx, 48, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(RogueLangParser.IF)
            self.state = 261
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 262
            self.expr(0)
            self.state = 263
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 264
            self.statBlock()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 265
                self.elifStat()


            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 268
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
        self.enterRule(localctx, 50, self.RULE_elifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(RogueLangParser.ELIF)
            self.state = 272
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 273
            self.expr(0)
            self.state = 274
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 275
            self.statBlock()
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 276
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
        self.enterRule(localctx, 52, self.RULE_elseStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(RogueLangParser.ELSE)
            self.state = 280
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
        self.enterRule(localctx, 54, self.RULE_statBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1264369652918192) != 0):
                self.state = 283
                self.stat()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 289
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
        self.enterRule(localctx, 56, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(RogueLangParser.FOR)
            self.state = 292
            self.match(RogueLangParser.ID)
            self.state = 293
            self.match(RogueLangParser.IN)
            self.state = 294
            self.match(RogueLangParser.ID)
            self.state = 295
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
        self.enterRule(localctx, 58, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(RogueLangParser.WHILE)
            self.state = 298
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 299
            self.expr(0)
            self.state = 300
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 301
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
        self.enterRule(localctx, 60, self.RULE_returnStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(RogueLangParser.RETURN)
            self.state = 304
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
        self.enterRule(localctx, 62, self.RULE_whiteNoiseStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(RogueLangParser.T__7)
            self.state = 307
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 308
            self.match(RogueLangParser.ID)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 309
                self.match(RogueLangParser.COMMA)
                self.state = 310
                self.range_()


            self.state = 313
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 314
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
        self.enterRule(localctx, 64, self.RULE_random)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(RogueLangParser.T__8)
                self.state = 318
                self.match(RogueLangParser.IN)
                self.state = 319
                self.range_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(RogueLangParser.T__8)
                self.state = 321
                self.match(RogueLangParser.IN)
                self.state = 322
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
        self.enterRule(localctx, 66, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.expr(0)
            self.state = 326
            self.match(RogueLangParser.DOT)
            self.state = 327
            self.match(RogueLangParser.DOT)
            self.state = 328
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
            self.state = 330
            self.match(RogueLangParser.ID)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 331
                self.match(RogueLangParser.COMMA)
                self.state = 332
                self.match(RogueLangParser.ID)
                self.state = 337
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
            self.state = 338
            self.expr(0)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 339
                self.match(RogueLangParser.COMMA)
                self.state = 340
                self.expr(0)
                self.state = 345
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
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 347
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 348
                self.match(RogueLangParser.ID)
                self.state = 350 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 349
                        self.structFieldAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 352 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                pass

            elif la_ == 3:
                self.state = 354
                self.match(RogueLangParser.ID)
                self.state = 356 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 355
                        self.listAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 358 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass

            elif la_ == 4:
                self.state = 360
                self.listLength()
                pass

            elif la_ == 5:
                self.state = 361
                self.random()
                pass

            elif la_ == 6:
                self.state = 362
                self.match(RogueLangParser.NOT)
                self.state = 363
                self.expr(10)
                pass

            elif la_ == 7:
                self.state = 364
                self.match(RogueLangParser.SQRT)
                self.state = 365
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 366
                self.expr(0)
                self.state = 367
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 8:
                self.state = 369
                self.match(RogueLangParser.POW)
                self.state = 370
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 371
                self.expr(0)
                self.state = 372
                self.match(RogueLangParser.COMMA)
                self.state = 373
                self.expr(0)
                self.state = 374
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 9:
                self.state = 376
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 377
                self.expr(0)
                self.state = 378
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 10:
                self.state = 380
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 11:
                self.state = 381
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 12:
                self.state = 382
                self.match(RogueLangParser.FLOAT)
                pass

            elif la_ == 13:
                self.state = 383
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 14:
                self.state = 384
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 15:
                self.state = 385
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 400
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 388
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 389
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8615100416) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 390
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 391
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 392
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 393
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 394
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 395
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 396
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 397
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 398
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==34 or _la==35):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 399
                        self.expr(12)
                        pass

             
                self.state = 404
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
         




