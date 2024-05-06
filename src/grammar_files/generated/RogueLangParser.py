# Generated from /home/ronaldj/code/P4-comp/src/grammar_files/RogueLang.g4 by ANTLR 4.13.1
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
        4,1,54,400,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,5,0,77,8,0,10,0,12,0,
        80,9,0,1,1,1,1,1,1,1,1,1,1,5,1,87,8,1,10,1,12,1,90,9,1,1,1,1,1,1,
        2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,116,8,4,1,5,1,5,1,5,1,6,1,6,3,6,123,8,
        6,1,7,1,7,5,7,127,8,7,10,7,12,7,130,9,7,1,7,5,7,133,8,7,10,7,12,
        7,136,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,146,8,8,1,9,1,9,1,
        9,1,9,3,9,152,8,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,160,8,10,1,10,
        1,10,1,11,1,11,1,11,1,11,5,11,168,8,11,10,11,12,11,171,9,11,3,11,
        173,8,11,1,11,1,11,1,12,1,12,3,12,179,8,12,1,13,1,13,1,13,1,13,1,
        13,1,13,3,13,187,8,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,5,16,205,8,16,10,16,12,16,
        208,9,16,1,16,1,16,1,17,1,17,1,17,1,17,4,17,216,8,17,11,17,12,17,
        217,1,17,1,17,1,18,1,18,1,19,1,19,1,19,5,19,227,8,19,10,19,12,19,
        230,9,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,
        1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,3,23,251,8,23,1,23,3,23,
        254,8,23,1,24,1,24,1,24,1,24,1,24,1,24,3,24,262,8,24,1,25,1,25,1,
        25,1,26,1,26,5,26,269,8,26,10,26,12,26,272,9,26,1,26,1,26,1,27,1,
        27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,
        29,1,30,1,30,1,30,1,30,1,30,3,30,296,8,30,1,30,1,30,3,30,300,8,30,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,
        1,32,1,32,1,32,3,32,318,8,32,1,33,1,33,1,33,1,33,1,33,1,34,1,34,
        1,34,5,34,328,8,34,10,34,12,34,331,9,34,1,35,1,35,1,35,5,35,336,
        8,35,10,35,12,35,339,9,35,1,36,1,36,1,36,1,36,4,36,345,8,36,11,36,
        12,36,346,1,36,1,36,4,36,351,8,36,11,36,12,36,352,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,381,8,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,5,36,
        395,8,36,10,36,12,36,398,9,36,1,36,0,1,72,37,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,0,4,2,0,22,23,32,32,1,0,20,21,1,0,24,29,1,0,
        33,34,423,0,74,1,0,0,0,2,81,1,0,0,0,4,93,1,0,0,0,6,96,1,0,0,0,8,
        115,1,0,0,0,10,117,1,0,0,0,12,120,1,0,0,0,14,124,1,0,0,0,16,145,
        1,0,0,0,18,147,1,0,0,0,20,156,1,0,0,0,22,163,1,0,0,0,24,178,1,0,
        0,0,26,186,1,0,0,0,28,188,1,0,0,0,30,193,1,0,0,0,32,199,1,0,0,0,
        34,211,1,0,0,0,36,221,1,0,0,0,38,223,1,0,0,0,40,231,1,0,0,0,42,235,
        1,0,0,0,44,239,1,0,0,0,46,244,1,0,0,0,48,255,1,0,0,0,50,263,1,0,
        0,0,52,266,1,0,0,0,54,275,1,0,0,0,56,281,1,0,0,0,58,287,1,0,0,0,
        60,290,1,0,0,0,62,301,1,0,0,0,64,317,1,0,0,0,66,319,1,0,0,0,68,324,
        1,0,0,0,70,332,1,0,0,0,72,380,1,0,0,0,74,78,3,2,1,0,75,77,3,8,4,
        0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,1,1,
        0,0,0,80,78,1,0,0,0,81,82,5,44,0,0,82,83,5,49,0,0,83,88,3,4,2,0,
        84,87,3,6,3,0,85,87,3,8,4,0,86,84,1,0,0,0,86,85,1,0,0,0,87,90,1,
        0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,0,91,
        92,5,50,0,0,92,3,1,0,0,0,93,94,5,19,0,0,94,95,3,52,26,0,95,5,1,0,
        0,0,96,97,5,1,0,0,97,98,3,12,6,0,98,7,1,0,0,0,99,116,3,44,22,0,100,
        116,3,10,5,0,101,116,3,14,7,0,102,116,3,18,9,0,103,116,3,46,23,0,
        104,116,3,54,27,0,105,116,3,56,28,0,106,116,3,52,26,0,107,116,3,
        58,29,0,108,116,3,40,20,0,109,116,3,42,21,0,110,116,3,30,15,0,111,
        116,3,60,30,0,112,116,3,62,31,0,113,116,3,34,17,0,114,116,3,72,36,
        0,115,99,1,0,0,0,115,100,1,0,0,0,115,101,1,0,0,0,115,102,1,0,0,0,
        115,103,1,0,0,0,115,104,1,0,0,0,115,105,1,0,0,0,115,106,1,0,0,0,
        115,107,1,0,0,0,115,108,1,0,0,0,115,109,1,0,0,0,115,110,1,0,0,0,
        115,111,1,0,0,0,115,112,1,0,0,0,115,113,1,0,0,0,115,114,1,0,0,0,
        116,9,1,0,0,0,117,118,5,2,0,0,118,119,3,12,6,0,119,11,1,0,0,0,120,
        122,5,44,0,0,121,123,3,16,8,0,122,121,1,0,0,0,122,123,1,0,0,0,123,
        13,1,0,0,0,124,128,5,44,0,0,125,127,3,38,19,0,126,125,1,0,0,0,127,
        130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,134,1,0,0,0,130,
        128,1,0,0,0,131,133,3,26,13,0,132,131,1,0,0,0,133,136,1,0,0,0,134,
        132,1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,134,1,0,0,0,137,
        138,3,16,8,0,138,15,1,0,0,0,139,140,5,53,0,0,140,146,3,32,16,0,141,
        142,5,53,0,0,142,146,3,22,11,0,143,144,5,53,0,0,144,146,3,72,36,
        0,145,139,1,0,0,0,145,141,1,0,0,0,145,143,1,0,0,0,146,17,1,0,0,0,
        147,148,5,17,0,0,148,149,5,44,0,0,149,151,5,45,0,0,150,152,3,68,
        34,0,151,150,1,0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,153,154,5,46,
        0,0,154,155,3,52,26,0,155,19,1,0,0,0,156,157,5,44,0,0,157,159,5,
        45,0,0,158,160,3,70,35,0,159,158,1,0,0,0,159,160,1,0,0,0,160,161,
        1,0,0,0,161,162,5,46,0,0,162,21,1,0,0,0,163,172,5,47,0,0,164,169,
        3,24,12,0,165,166,5,51,0,0,166,168,3,24,12,0,167,165,1,0,0,0,168,
        171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,173,1,0,0,0,171,
        169,1,0,0,0,172,164,1,0,0,0,172,173,1,0,0,0,173,174,1,0,0,0,174,
        175,5,48,0,0,175,23,1,0,0,0,176,179,3,72,36,0,177,179,3,22,11,0,
        178,176,1,0,0,0,178,177,1,0,0,0,179,25,1,0,0,0,180,181,5,47,0,0,
        181,182,5,41,0,0,182,187,5,48,0,0,183,184,5,47,0,0,184,185,5,44,
        0,0,185,187,5,48,0,0,186,180,1,0,0,0,186,183,1,0,0,0,187,27,1,0,
        0,0,188,189,5,3,0,0,189,190,5,45,0,0,190,191,5,44,0,0,191,192,5,
        46,0,0,192,29,1,0,0,0,193,194,5,44,0,0,194,195,5,52,0,0,195,196,
        5,4,0,0,196,197,5,45,0,0,197,198,5,46,0,0,198,31,1,0,0,0,199,200,
        5,44,0,0,200,206,5,49,0,0,201,202,3,36,18,0,202,203,3,16,8,0,203,
        205,1,0,0,0,204,201,1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,206,
        207,1,0,0,0,207,209,1,0,0,0,208,206,1,0,0,0,209,210,5,50,0,0,210,
        33,1,0,0,0,211,212,5,5,0,0,212,213,5,44,0,0,213,215,5,49,0,0,214,
        216,3,36,18,0,215,214,1,0,0,0,216,217,1,0,0,0,217,215,1,0,0,0,217,
        218,1,0,0,0,218,219,1,0,0,0,219,220,5,50,0,0,220,35,1,0,0,0,221,
        222,5,44,0,0,222,37,1,0,0,0,223,224,5,52,0,0,224,228,5,44,0,0,225,
        227,3,26,13,0,226,225,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,
        229,1,0,0,0,229,39,1,0,0,0,230,228,1,0,0,0,231,232,5,44,0,0,232,
        233,5,30,0,0,233,234,3,72,36,0,234,41,1,0,0,0,235,236,5,44,0,0,236,
        237,5,31,0,0,237,238,3,72,36,0,238,43,1,0,0,0,239,240,5,13,0,0,240,
        241,5,45,0,0,241,242,3,72,36,0,242,243,5,46,0,0,243,45,1,0,0,0,244,
        245,5,9,0,0,245,246,5,45,0,0,246,247,3,72,36,0,247,248,5,46,0,0,
        248,250,3,52,26,0,249,251,3,48,24,0,250,249,1,0,0,0,250,251,1,0,
        0,0,251,253,1,0,0,0,252,254,3,50,25,0,253,252,1,0,0,0,253,254,1,
        0,0,0,254,47,1,0,0,0,255,256,5,10,0,0,256,257,5,45,0,0,257,258,3,
        72,36,0,258,259,5,46,0,0,259,261,3,52,26,0,260,262,3,48,24,0,261,
        260,1,0,0,0,261,262,1,0,0,0,262,49,1,0,0,0,263,264,5,11,0,0,264,
        265,3,52,26,0,265,51,1,0,0,0,266,270,5,49,0,0,267,269,3,8,4,0,268,
        267,1,0,0,0,269,272,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,
        273,1,0,0,0,272,270,1,0,0,0,273,274,5,50,0,0,274,53,1,0,0,0,275,
        276,5,14,0,0,276,277,5,44,0,0,277,278,5,15,0,0,278,279,5,44,0,0,
        279,280,3,52,26,0,280,55,1,0,0,0,281,282,5,16,0,0,282,283,5,45,0,
        0,283,284,3,72,36,0,284,285,5,46,0,0,285,286,3,52,26,0,286,57,1,
        0,0,0,287,288,5,12,0,0,288,289,3,72,36,0,289,59,1,0,0,0,290,291,
        5,6,0,0,291,292,5,45,0,0,292,295,5,44,0,0,293,294,5,51,0,0,294,296,
        3,66,33,0,295,293,1,0,0,0,295,296,1,0,0,0,296,297,1,0,0,0,297,299,
        5,46,0,0,298,300,5,18,0,0,299,298,1,0,0,0,299,300,1,0,0,0,300,61,
        1,0,0,0,301,302,5,7,0,0,302,303,5,45,0,0,303,304,5,44,0,0,304,305,
        5,51,0,0,305,306,5,44,0,0,306,307,5,51,0,0,307,308,5,44,0,0,308,
        309,5,51,0,0,309,310,5,46,0,0,310,63,1,0,0,0,311,312,5,8,0,0,312,
        313,5,15,0,0,313,318,3,66,33,0,314,315,5,8,0,0,315,316,5,15,0,0,
        316,318,5,44,0,0,317,311,1,0,0,0,317,314,1,0,0,0,318,65,1,0,0,0,
        319,320,3,72,36,0,320,321,5,52,0,0,321,322,5,52,0,0,322,323,3,72,
        36,0,323,67,1,0,0,0,324,329,5,44,0,0,325,326,5,51,0,0,326,328,5,
        44,0,0,327,325,1,0,0,0,328,331,1,0,0,0,329,327,1,0,0,0,329,330,1,
        0,0,0,330,69,1,0,0,0,331,329,1,0,0,0,332,337,3,72,36,0,333,334,5,
        51,0,0,334,336,3,72,36,0,335,333,1,0,0,0,336,339,1,0,0,0,337,335,
        1,0,0,0,337,338,1,0,0,0,338,71,1,0,0,0,339,337,1,0,0,0,340,341,6,
        36,-1,0,341,381,3,20,10,0,342,344,5,44,0,0,343,345,3,38,19,0,344,
        343,1,0,0,0,345,346,1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,347,
        381,1,0,0,0,348,350,5,44,0,0,349,351,3,26,13,0,350,349,1,0,0,0,351,
        352,1,0,0,0,352,350,1,0,0,0,352,353,1,0,0,0,353,381,1,0,0,0,354,
        381,3,28,14,0,355,381,3,64,32,0,356,357,5,35,0,0,357,381,3,72,36,
        10,358,359,5,38,0,0,359,360,5,45,0,0,360,361,3,72,36,0,361,362,5,
        46,0,0,362,381,1,0,0,0,363,364,5,39,0,0,364,365,5,45,0,0,365,366,
        3,72,36,0,366,367,5,51,0,0,367,368,3,72,36,0,368,369,5,46,0,0,369,
        381,1,0,0,0,370,371,5,45,0,0,371,372,3,72,36,0,372,373,5,46,0,0,
        373,381,1,0,0,0,374,381,5,44,0,0,375,381,5,41,0,0,376,381,5,42,0,
        0,377,381,5,43,0,0,378,381,5,36,0,0,379,381,5,37,0,0,380,340,1,0,
        0,0,380,342,1,0,0,0,380,348,1,0,0,0,380,354,1,0,0,0,380,355,1,0,
        0,0,380,356,1,0,0,0,380,358,1,0,0,0,380,363,1,0,0,0,380,370,1,0,
        0,0,380,374,1,0,0,0,380,375,1,0,0,0,380,376,1,0,0,0,380,377,1,0,
        0,0,380,378,1,0,0,0,380,379,1,0,0,0,381,396,1,0,0,0,382,383,10,14,
        0,0,383,384,7,0,0,0,384,395,3,72,36,15,385,386,10,13,0,0,386,387,
        7,1,0,0,387,395,3,72,36,14,388,389,10,12,0,0,389,390,7,2,0,0,390,
        395,3,72,36,13,391,392,10,11,0,0,392,393,7,3,0,0,393,395,3,72,36,
        12,394,382,1,0,0,0,394,385,1,0,0,0,394,388,1,0,0,0,394,391,1,0,0,
        0,395,398,1,0,0,0,396,394,1,0,0,0,396,397,1,0,0,0,397,73,1,0,0,0,
        398,396,1,0,0,0,31,78,86,88,115,122,128,134,145,151,159,169,172,
        178,186,206,217,228,250,253,261,270,295,299,317,329,337,346,352,
        380,394,396
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'field'", "'let'", "'len'", "'pop'", 
                     "'struct'", "'WhiteNoise'", "'astar'", "'random'", 
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
                      "<INVALID>", "IF", "ELIF", "ELSE", "RETURN", "PRINT", 
                      "FOR", "IN", "WHILE", "DEF", "LAYER", "PROCEDURE", 
                      "PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", "LT", 
                      "LTE", "EQ", "NEQ", "PEQ", "MEQ", "MOD", "AND", "OR", 
                      "NOT", "TRUE", "FALSE", "SQRT", "POW", "COMMENT_SINGLELINE", 
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
    RULE_astarStat = 31
    RULE_random = 32
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
                   "whileLoop", "returnStat", "whiteNoiseStat", "astarStat", 
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
    IF=9
    ELIF=10
    ELSE=11
    RETURN=12
    PRINT=13
    FOR=14
    IN=15
    WHILE=16
    DEF=17
    LAYER=18
    PROCEDURE=19
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 632184826459116) != 0):
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 632184826459118) != 0):
                self.state = 86
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 84
                    self.field()
                    pass
                elif token in [2, 3, 5, 6, 7, 8, 9, 12, 13, 14, 16, 17, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 49]:
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


        def astarStat(self):
            return self.getTypedRuleContext(RogueLangParser.AstarStatContext,0)


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
            self.state = 115
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
                self.astarStat()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 113
                self.structDef()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 114
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
            self.state = 117
            self.match(RogueLangParser.T__1)
            self.state = 118
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
            self.state = 120
            self.match(RogueLangParser.ID)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 121
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
            self.state = 124
            self.match(RogueLangParser.ID)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 125
                self.structFieldAccess()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 131
                self.listAccess()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
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
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 140
                self.struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 142
                self.list_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 144
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
            self.state = 147
            self.match(RogueLangParser.DEF)
            self.state = 148
            self.match(RogueLangParser.ID)
            self.state = 149
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 150
                self.params()


            self.state = 153
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 154
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
            self.state = 156
            self.match(RogueLangParser.ID)
            self.state = 157
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 69234872811784) != 0):
                self.state = 158
                self.args()


            self.state = 161
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
            self.state = 163
            self.match(RogueLangParser.OPEN_BRACK)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 209972361167112) != 0):
                self.state = 164
                self.listElement()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 165
                    self.match(RogueLangParser.COMMA)
                    self.state = 166
                    self.listElement()
                    self.state = 171
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 174
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
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 8, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.expr(0)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 181
                self.match(RogueLangParser.INT)
                self.state = 182
                self.match(RogueLangParser.CLOSED_BRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 184
                self.match(RogueLangParser.ID)
                self.state = 185
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
            self.state = 188
            self.match(RogueLangParser.T__2)
            self.state = 189
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 190
            self.match(RogueLangParser.ID)
            self.state = 191
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
            self.state = 193
            self.match(RogueLangParser.ID)
            self.state = 194
            self.match(RogueLangParser.DOT)
            self.state = 195
            self.match(RogueLangParser.T__3)
            self.state = 196
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 197
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
            self.state = 199
            self.match(RogueLangParser.ID)
            self.state = 200
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 201
                self.structField()
                self.state = 202
                self.assignment()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 209
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
            self.state = 211
            self.match(RogueLangParser.T__4)
            self.state = 212
            self.match(RogueLangParser.ID)
            self.state = 213
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 215 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 214
                self.structField()
                self.state = 217 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==44):
                    break

            self.state = 219
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
            self.state = 221
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
            self.state = 223
            self.match(RogueLangParser.DOT)
            self.state = 224
            self.match(RogueLangParser.ID)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 225
                    self.listAccess() 
                self.state = 230
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
            self.state = 231
            self.match(RogueLangParser.ID)
            self.state = 232
            self.match(RogueLangParser.PEQ)
            self.state = 233
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
            self.state = 235
            self.match(RogueLangParser.ID)
            self.state = 236
            self.match(RogueLangParser.MEQ)
            self.state = 237
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
            self.state = 239
            self.match(RogueLangParser.PRINT)
            self.state = 240
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 241
            self.expr(0)
            self.state = 242
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
            self.state = 244
            self.match(RogueLangParser.IF)
            self.state = 245
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 246
            self.expr(0)
            self.state = 247
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 248
            self.statBlock()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 249
                self.elifStat()


            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 252
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
            self.state = 255
            self.match(RogueLangParser.ELIF)
            self.state = 256
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 257
            self.expr(0)
            self.state = 258
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 259
            self.statBlock()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 260
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
            self.state = 263
            self.match(RogueLangParser.ELSE)
            self.state = 264
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
            self.state = 266
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 632184826459116) != 0):
                self.state = 267
                self.stat()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 273
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
            self.state = 275
            self.match(RogueLangParser.FOR)
            self.state = 276
            self.match(RogueLangParser.ID)
            self.state = 277
            self.match(RogueLangParser.IN)
            self.state = 278
            self.match(RogueLangParser.ID)
            self.state = 279
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
            self.state = 281
            self.match(RogueLangParser.WHILE)
            self.state = 282
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 283
            self.expr(0)
            self.state = 284
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 285
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
            self.state = 287
            self.match(RogueLangParser.RETURN)
            self.state = 288
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
            self.state = 290
            self.match(RogueLangParser.T__5)
            self.state = 291
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 292
            self.match(RogueLangParser.ID)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 293
                self.match(RogueLangParser.COMMA)
                self.state = 294
                self.range_()


            self.state = 297
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 298
                self.match(RogueLangParser.LAYER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AstarStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

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

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_astarStat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAstarStat" ):
                return visitor.visitAstarStat(self)
            else:
                return visitor.visitChildren(self)




    def astarStat(self):

        localctx = RogueLangParser.AstarStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_astarStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(RogueLangParser.T__6)
            self.state = 302
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 303
            self.match(RogueLangParser.ID)
            self.state = 304
            self.match(RogueLangParser.COMMA)
            self.state = 305
            self.match(RogueLangParser.ID)
            self.state = 306
            self.match(RogueLangParser.COMMA)
            self.state = 307
            self.match(RogueLangParser.ID)
            self.state = 308
            self.match(RogueLangParser.COMMA)
            self.state = 309
            self.match(RogueLangParser.CLOSED_PARENTH)
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
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(RogueLangParser.T__7)
                self.state = 312
                self.match(RogueLangParser.IN)
                self.state = 313
                self.range_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.match(RogueLangParser.T__7)
                self.state = 315
                self.match(RogueLangParser.IN)
                self.state = 316
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
            self.state = 319
            self.expr(0)
            self.state = 320
            self.match(RogueLangParser.DOT)
            self.state = 321
            self.match(RogueLangParser.DOT)
            self.state = 322
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
            self.state = 324
            self.match(RogueLangParser.ID)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 325
                self.match(RogueLangParser.COMMA)
                self.state = 326
                self.match(RogueLangParser.ID)
                self.state = 331
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
            self.state = 332
            self.expr(0)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 333
                self.match(RogueLangParser.COMMA)
                self.state = 334
                self.expr(0)
                self.state = 339
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
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 341
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 342
                self.match(RogueLangParser.ID)
                self.state = 344 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 343
                        self.structFieldAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 346 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                pass

            elif la_ == 3:
                self.state = 348
                self.match(RogueLangParser.ID)
                self.state = 350 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 349
                        self.listAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 352 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                pass

            elif la_ == 4:
                self.state = 354
                self.listLength()
                pass

            elif la_ == 5:
                self.state = 355
                self.random()
                pass

            elif la_ == 6:
                self.state = 356
                self.match(RogueLangParser.NOT)
                self.state = 357
                self.expr(10)
                pass

            elif la_ == 7:
                self.state = 358
                self.match(RogueLangParser.SQRT)
                self.state = 359
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 360
                self.expr(0)
                self.state = 361
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 8:
                self.state = 363
                self.match(RogueLangParser.POW)
                self.state = 364
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 365
                self.expr(0)
                self.state = 366
                self.match(RogueLangParser.COMMA)
                self.state = 367
                self.expr(0)
                self.state = 368
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 9:
                self.state = 370
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 371
                self.expr(0)
                self.state = 372
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 10:
                self.state = 374
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 11:
                self.state = 375
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 12:
                self.state = 376
                self.match(RogueLangParser.FLOAT)
                pass

            elif la_ == 13:
                self.state = 377
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 14:
                self.state = 378
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 15:
                self.state = 379
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 396
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 394
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 382
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 383
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4307550208) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 384
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 385
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 386
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 387
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 388
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 389
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 390
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 391
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 392
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==33 or _la==34):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 393
                        self.expr(12)
                        pass

             
                self.state = 398
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
         




