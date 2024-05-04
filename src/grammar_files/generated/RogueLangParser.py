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
        4,1,53,394,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,1,0,5,0,75,8,0,10,0,12,0,78,9,0,1,1,
        1,1,1,1,1,1,1,1,5,1,85,8,1,10,1,12,1,88,9,1,1,1,1,1,1,2,1,2,1,2,
        1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,3,4,113,8,4,1,5,1,5,1,5,1,6,1,6,3,6,120,8,6,1,7,1,7,5,7,
        124,8,7,10,7,12,7,127,9,7,1,7,5,7,130,8,7,10,7,12,7,133,9,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,143,8,8,1,9,1,9,1,9,1,9,3,9,149,
        8,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,157,8,10,1,10,1,10,1,11,1,11,
        1,11,1,11,5,11,165,8,11,10,11,12,11,168,9,11,3,11,170,8,11,1,11,
        1,11,1,12,1,12,3,12,176,8,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,
        184,8,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,16,1,16,1,16,1,16,1,16,5,16,202,8,16,10,16,12,16,205,9,16,1,16,
        1,16,1,17,1,17,1,17,1,17,4,17,213,8,17,11,17,12,17,214,1,17,1,17,
        1,18,1,18,1,19,1,19,1,19,5,19,224,8,19,10,19,12,19,227,9,19,1,20,
        1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,5,22,
        242,8,22,10,22,12,22,245,9,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,
        1,23,3,23,255,8,23,1,23,3,23,258,8,23,1,24,1,24,1,24,1,24,1,24,1,
        24,3,24,266,8,24,1,25,1,25,1,25,1,26,1,26,5,26,273,8,26,10,26,12,
        26,276,9,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,
        28,1,28,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,3,30,300,
        8,30,1,30,1,30,3,30,304,8,30,1,31,1,31,1,31,1,31,1,31,1,31,3,31,
        312,8,31,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,5,33,322,8,33,10,
        33,12,33,325,9,33,1,34,1,34,1,34,5,34,330,8,34,10,34,12,34,333,9,
        34,1,35,1,35,1,35,1,35,4,35,339,8,35,11,35,12,35,340,1,35,1,35,4,
        35,345,8,35,11,35,12,35,346,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,3,35,375,8,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,5,35,389,8,35,10,35,12,35,
        392,9,35,1,35,0,1,70,36,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,0,
        4,2,0,21,22,31,31,1,0,19,20,1,0,23,28,1,0,32,33,418,0,72,1,0,0,0,
        2,79,1,0,0,0,4,91,1,0,0,0,6,94,1,0,0,0,8,112,1,0,0,0,10,114,1,0,
        0,0,12,117,1,0,0,0,14,121,1,0,0,0,16,142,1,0,0,0,18,144,1,0,0,0,
        20,153,1,0,0,0,22,160,1,0,0,0,24,175,1,0,0,0,26,183,1,0,0,0,28,185,
        1,0,0,0,30,190,1,0,0,0,32,196,1,0,0,0,34,208,1,0,0,0,36,218,1,0,
        0,0,38,220,1,0,0,0,40,228,1,0,0,0,42,232,1,0,0,0,44,236,1,0,0,0,
        46,248,1,0,0,0,48,259,1,0,0,0,50,267,1,0,0,0,52,270,1,0,0,0,54,279,
        1,0,0,0,56,285,1,0,0,0,58,291,1,0,0,0,60,294,1,0,0,0,62,311,1,0,
        0,0,64,313,1,0,0,0,66,318,1,0,0,0,68,326,1,0,0,0,70,374,1,0,0,0,
        72,76,3,2,1,0,73,75,3,8,4,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,
        0,0,0,76,77,1,0,0,0,77,1,1,0,0,0,78,76,1,0,0,0,79,80,5,43,0,0,80,
        81,5,48,0,0,81,86,3,4,2,0,82,85,3,6,3,0,83,85,3,8,4,0,84,82,1,0,
        0,0,84,83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,
        1,0,0,0,88,86,1,0,0,0,89,90,5,49,0,0,90,3,1,0,0,0,91,92,5,18,0,0,
        92,93,3,52,26,0,93,5,1,0,0,0,94,95,5,1,0,0,95,96,3,12,6,0,96,7,1,
        0,0,0,97,113,3,44,22,0,98,113,3,10,5,0,99,113,3,14,7,0,100,113,3,
        18,9,0,101,113,3,46,23,0,102,113,3,54,27,0,103,113,3,56,28,0,104,
        113,3,52,26,0,105,113,3,58,29,0,106,113,3,40,20,0,107,113,3,42,21,
        0,108,113,3,30,15,0,109,113,3,60,30,0,110,113,3,34,17,0,111,113,
        3,70,35,0,112,97,1,0,0,0,112,98,1,0,0,0,112,99,1,0,0,0,112,100,1,
        0,0,0,112,101,1,0,0,0,112,102,1,0,0,0,112,103,1,0,0,0,112,104,1,
        0,0,0,112,105,1,0,0,0,112,106,1,0,0,0,112,107,1,0,0,0,112,108,1,
        0,0,0,112,109,1,0,0,0,112,110,1,0,0,0,112,111,1,0,0,0,113,9,1,0,
        0,0,114,115,5,2,0,0,115,116,3,12,6,0,116,11,1,0,0,0,117,119,5,43,
        0,0,118,120,3,16,8,0,119,118,1,0,0,0,119,120,1,0,0,0,120,13,1,0,
        0,0,121,125,5,43,0,0,122,124,3,38,19,0,123,122,1,0,0,0,124,127,1,
        0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,131,1,0,0,0,127,125,1,
        0,0,0,128,130,3,26,13,0,129,128,1,0,0,0,130,133,1,0,0,0,131,129,
        1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,135,
        3,16,8,0,135,15,1,0,0,0,136,137,5,52,0,0,137,143,3,32,16,0,138,139,
        5,52,0,0,139,143,3,22,11,0,140,141,5,52,0,0,141,143,3,70,35,0,142,
        136,1,0,0,0,142,138,1,0,0,0,142,140,1,0,0,0,143,17,1,0,0,0,144,145,
        5,16,0,0,145,146,5,43,0,0,146,148,5,44,0,0,147,149,3,66,33,0,148,
        147,1,0,0,0,148,149,1,0,0,0,149,150,1,0,0,0,150,151,5,45,0,0,151,
        152,3,52,26,0,152,19,1,0,0,0,153,154,5,43,0,0,154,156,5,44,0,0,155,
        157,3,68,34,0,156,155,1,0,0,0,156,157,1,0,0,0,157,158,1,0,0,0,158,
        159,5,45,0,0,159,21,1,0,0,0,160,169,5,46,0,0,161,166,3,24,12,0,162,
        163,5,50,0,0,163,165,3,24,12,0,164,162,1,0,0,0,165,168,1,0,0,0,166,
        164,1,0,0,0,166,167,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,169,
        161,1,0,0,0,169,170,1,0,0,0,170,171,1,0,0,0,171,172,5,47,0,0,172,
        23,1,0,0,0,173,176,3,70,35,0,174,176,3,22,11,0,175,173,1,0,0,0,175,
        174,1,0,0,0,176,25,1,0,0,0,177,178,5,46,0,0,178,179,5,40,0,0,179,
        184,5,47,0,0,180,181,5,46,0,0,181,182,5,43,0,0,182,184,5,47,0,0,
        183,177,1,0,0,0,183,180,1,0,0,0,184,27,1,0,0,0,185,186,5,3,0,0,186,
        187,5,44,0,0,187,188,5,43,0,0,188,189,5,45,0,0,189,29,1,0,0,0,190,
        191,5,43,0,0,191,192,5,51,0,0,192,193,5,4,0,0,193,194,5,44,0,0,194,
        195,5,45,0,0,195,31,1,0,0,0,196,197,5,43,0,0,197,203,5,48,0,0,198,
        199,3,36,18,0,199,200,3,16,8,0,200,202,1,0,0,0,201,198,1,0,0,0,202,
        205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,206,1,0,0,0,205,
        203,1,0,0,0,206,207,5,49,0,0,207,33,1,0,0,0,208,209,5,5,0,0,209,
        210,5,43,0,0,210,212,5,48,0,0,211,213,3,36,18,0,212,211,1,0,0,0,
        213,214,1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,215,216,1,0,0,0,
        216,217,5,49,0,0,217,35,1,0,0,0,218,219,5,43,0,0,219,37,1,0,0,0,
        220,221,5,51,0,0,221,225,5,43,0,0,222,224,3,26,13,0,223,222,1,0,
        0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,39,1,0,0,
        0,227,225,1,0,0,0,228,229,5,43,0,0,229,230,5,29,0,0,230,231,3,70,
        35,0,231,41,1,0,0,0,232,233,5,43,0,0,233,234,5,30,0,0,234,235,3,
        70,35,0,235,43,1,0,0,0,236,237,5,12,0,0,237,238,5,44,0,0,238,243,
        3,70,35,0,239,240,5,19,0,0,240,242,3,70,35,0,241,239,1,0,0,0,242,
        245,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,246,1,0,0,0,245,
        243,1,0,0,0,246,247,5,45,0,0,247,45,1,0,0,0,248,249,5,8,0,0,249,
        250,5,44,0,0,250,251,3,70,35,0,251,252,5,45,0,0,252,254,3,52,26,
        0,253,255,3,48,24,0,254,253,1,0,0,0,254,255,1,0,0,0,255,257,1,0,
        0,0,256,258,3,50,25,0,257,256,1,0,0,0,257,258,1,0,0,0,258,47,1,0,
        0,0,259,260,5,9,0,0,260,261,5,44,0,0,261,262,3,70,35,0,262,263,5,
        45,0,0,263,265,3,52,26,0,264,266,3,48,24,0,265,264,1,0,0,0,265,266,
        1,0,0,0,266,49,1,0,0,0,267,268,5,10,0,0,268,269,3,52,26,0,269,51,
        1,0,0,0,270,274,5,48,0,0,271,273,3,8,4,0,272,271,1,0,0,0,273,276,
        1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,277,1,0,0,0,276,274,
        1,0,0,0,277,278,5,49,0,0,278,53,1,0,0,0,279,280,5,13,0,0,280,281,
        5,43,0,0,281,282,5,14,0,0,282,283,5,43,0,0,283,284,3,52,26,0,284,
        55,1,0,0,0,285,286,5,15,0,0,286,287,5,44,0,0,287,288,3,70,35,0,288,
        289,5,45,0,0,289,290,3,52,26,0,290,57,1,0,0,0,291,292,5,11,0,0,292,
        293,3,70,35,0,293,59,1,0,0,0,294,295,5,6,0,0,295,296,5,44,0,0,296,
        299,5,43,0,0,297,298,5,50,0,0,298,300,3,64,32,0,299,297,1,0,0,0,
        299,300,1,0,0,0,300,301,1,0,0,0,301,303,5,45,0,0,302,304,5,17,0,
        0,303,302,1,0,0,0,303,304,1,0,0,0,304,61,1,0,0,0,305,306,5,7,0,0,
        306,307,5,14,0,0,307,312,3,64,32,0,308,309,5,7,0,0,309,310,5,14,
        0,0,310,312,5,43,0,0,311,305,1,0,0,0,311,308,1,0,0,0,312,63,1,0,
        0,0,313,314,3,70,35,0,314,315,5,51,0,0,315,316,5,51,0,0,316,317,
        3,70,35,0,317,65,1,0,0,0,318,323,5,43,0,0,319,320,5,50,0,0,320,322,
        5,43,0,0,321,319,1,0,0,0,322,325,1,0,0,0,323,321,1,0,0,0,323,324,
        1,0,0,0,324,67,1,0,0,0,325,323,1,0,0,0,326,331,3,70,35,0,327,328,
        5,50,0,0,328,330,3,70,35,0,329,327,1,0,0,0,330,333,1,0,0,0,331,329,
        1,0,0,0,331,332,1,0,0,0,332,69,1,0,0,0,333,331,1,0,0,0,334,335,6,
        35,-1,0,335,375,3,20,10,0,336,338,5,43,0,0,337,339,3,38,19,0,338,
        337,1,0,0,0,339,340,1,0,0,0,340,338,1,0,0,0,340,341,1,0,0,0,341,
        375,1,0,0,0,342,344,5,43,0,0,343,345,3,26,13,0,344,343,1,0,0,0,345,
        346,1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,347,375,1,0,0,0,348,
        375,3,28,14,0,349,375,3,62,31,0,350,351,5,34,0,0,351,375,3,70,35,
        10,352,353,5,37,0,0,353,354,5,44,0,0,354,355,3,70,35,0,355,356,5,
        45,0,0,356,375,1,0,0,0,357,358,5,38,0,0,358,359,5,44,0,0,359,360,
        3,70,35,0,360,361,5,50,0,0,361,362,3,70,35,0,362,363,5,45,0,0,363,
        375,1,0,0,0,364,365,5,44,0,0,365,366,3,70,35,0,366,367,5,45,0,0,
        367,375,1,0,0,0,368,375,5,43,0,0,369,375,5,40,0,0,370,375,5,41,0,
        0,371,375,5,42,0,0,372,375,5,35,0,0,373,375,5,36,0,0,374,334,1,0,
        0,0,374,336,1,0,0,0,374,342,1,0,0,0,374,348,1,0,0,0,374,349,1,0,
        0,0,374,350,1,0,0,0,374,352,1,0,0,0,374,357,1,0,0,0,374,364,1,0,
        0,0,374,368,1,0,0,0,374,369,1,0,0,0,374,370,1,0,0,0,374,371,1,0,
        0,0,374,372,1,0,0,0,374,373,1,0,0,0,375,390,1,0,0,0,376,377,10,14,
        0,0,377,378,7,0,0,0,378,389,3,70,35,15,379,380,10,13,0,0,380,381,
        7,1,0,0,381,389,3,70,35,14,382,383,10,12,0,0,383,384,7,2,0,0,384,
        389,3,70,35,13,385,386,10,11,0,0,386,387,7,3,0,0,387,389,3,70,35,
        12,388,376,1,0,0,0,388,379,1,0,0,0,388,382,1,0,0,0,388,385,1,0,0,
        0,389,392,1,0,0,0,390,388,1,0,0,0,390,391,1,0,0,0,391,71,1,0,0,0,
        392,390,1,0,0,0,32,76,84,86,112,119,125,131,142,148,156,166,169,
        175,183,203,214,225,243,254,257,265,274,299,303,311,323,331,340,
        346,374,388,390
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'field'", "'let'", "'len'", "'pop'", 
                     "'struct'", "'WhiteNoise'", "'random'", "'if'", "'elif'", 
                     "'else'", "'return'", "'print'", "'for'", "'in'", "'while'", 
                     "'def'", "'layer'", "'procedure'", "'+'", "'-'", "'*'", 
                     "'/'", "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", 
                     "'+='", "'-='", "'%'", "'and'", "'or'", "'not'", "'True'", 
                     "'False'", "'sqrt'", "'pow'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IF", "ELIF", "ELSE", "RETURN", "PRINT", "FOR", "IN", 
                      "WHILE", "DEF", "LAYER", "PROCEDURE", "PLUS", "MINUS", 
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
    RULE_range = 32
    RULE_params = 33
    RULE_args = 34
    RULE_expr = 35

    ruleNames =  [ "prog", "object", "procedure", "field", "stat", "varDeclStat", 
                   "varDecl", "assignStat", "assignment", "functionDecl", 
                   "functionCall", "list", "listElement", "listAccess", 
                   "listLength", "listPop", "struct", "structDef", "structField", 
                   "structFieldAccess", "plusEquals", "minusEquals", "printStat", 
                   "ifStat", "elifStat", "elseStat", "statBlock", "forLoop", 
                   "whileLoop", "returnStat", "whiteNoiseStat", "random", 
                   "range", "params", "args", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    IF=8
    ELIF=9
    ELSE=10
    RETURN=11
    PRINT=12
    FOR=13
    IN=14
    WHILE=15
    DEF=16
    LAYER=17
    PROCEDURE=18
    PLUS=19
    MINUS=20
    MULT=21
    DIV=22
    GT=23
    GTE=24
    LT=25
    LTE=26
    EQ=27
    NEQ=28
    PEQ=29
    MEQ=30
    MOD=31
    AND=32
    OR=33
    NOT=34
    TRUE=35
    FALSE=36
    SQRT=37
    POW=38
    COMMENT_SINGLELINE=39
    INT=40
    FLOAT=41
    STRING=42
    ID=43
    OPEN_PARENTH=44
    CLOSED_PARENTH=45
    OPEN_BRACK=46
    CLOSED_BRACK=47
    OPEN_CURL=48
    CLOSED_CURL=49
    COMMA=50
    DOT=51
    EQUAL_SIGN=52
    WS=53

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
            self.state = 72
            self.object_()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 316092413229548) != 0):
                self.state = 73
                self.stat()
                self.state = 78
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
            self.state = 79
            self.match(RogueLangParser.ID)
            self.state = 80
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 81
            self.procedure()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 316092413229550) != 0):
                self.state = 84
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 82
                    self.field()
                    pass
                elif token in [2, 3, 5, 6, 7, 8, 11, 12, 13, 15, 16, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 48]:
                    self.state = 83
                    self.stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
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
            self.state = 91
            self.match(RogueLangParser.PROCEDURE)
            self.state = 92
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
            self.state = 94
            self.match(RogueLangParser.T__0)
            self.state = 95
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
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.varDeclStat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.assignStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 100
                self.functionDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 101
                self.ifStat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 102
                self.forLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 103
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 104
                self.statBlock()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 105
                self.returnStat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 106
                self.plusEquals()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 107
                self.minusEquals()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 108
                self.listPop()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 109
                self.whiteNoiseStat()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 110
                self.structDef()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 111
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
            self.state = 114
            self.match(RogueLangParser.T__1)
            self.state = 115
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
            self.state = 117
            self.match(RogueLangParser.ID)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 118
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
            self.state = 121
            self.match(RogueLangParser.ID)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 122
                self.structFieldAccess()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 128
                self.listAccess()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
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
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 137
                self.struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 139
                self.list_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 141
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
            self.state = 144
            self.match(RogueLangParser.DEF)
            self.state = 145
            self.match(RogueLangParser.ID)
            self.state = 146
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 147
                self.params()


            self.state = 150
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 151
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
            self.state = 153
            self.match(RogueLangParser.ID)
            self.state = 154
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34617436405896) != 0):
                self.state = 155
                self.args()


            self.state = 158
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
            self.state = 160
            self.match(RogueLangParser.OPEN_BRACK)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 104986180583560) != 0):
                self.state = 161
                self.listElement()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 162
                    self.match(RogueLangParser.COMMA)
                    self.state = 163
                    self.listElement()
                    self.state = 168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 171
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
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 7, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.expr(0)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
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
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 178
                self.match(RogueLangParser.INT)
                self.state = 179
                self.match(RogueLangParser.CLOSED_BRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 181
                self.match(RogueLangParser.ID)
                self.state = 182
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
            self.state = 185
            self.match(RogueLangParser.T__2)
            self.state = 186
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 187
            self.match(RogueLangParser.ID)
            self.state = 188
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
            self.state = 190
            self.match(RogueLangParser.ID)
            self.state = 191
            self.match(RogueLangParser.DOT)
            self.state = 192
            self.match(RogueLangParser.T__3)
            self.state = 193
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 194
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
            self.state = 196
            self.match(RogueLangParser.ID)
            self.state = 197
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 198
                self.structField()
                self.state = 199
                self.assignment()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
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
            self.state = 208
            self.match(RogueLangParser.T__4)
            self.state = 209
            self.match(RogueLangParser.ID)
            self.state = 210
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 212 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 211
                self.structField()
                self.state = 214 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==43):
                    break

            self.state = 216
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
            self.state = 218
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
            self.state = 220
            self.match(RogueLangParser.DOT)
            self.state = 221
            self.match(RogueLangParser.ID)
            self.state = 225
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 222
                    self.listAccess() 
                self.state = 227
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
            self.state = 228
            self.match(RogueLangParser.ID)
            self.state = 229
            self.match(RogueLangParser.PEQ)
            self.state = 230
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
            self.state = 232
            self.match(RogueLangParser.ID)
            self.state = 233
            self.match(RogueLangParser.MEQ)
            self.state = 234
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.PLUS)
            else:
                return self.getToken(RogueLangParser.PLUS, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(RogueLangParser.PRINT)
            self.state = 237
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 238
            self.expr(0)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 239
                self.match(RogueLangParser.PLUS)
                self.state = 240
                self.expr(0)
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
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
            self.state = 248
            self.match(RogueLangParser.IF)
            self.state = 249
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 250
            self.expr(0)
            self.state = 251
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 252
            self.statBlock()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 253
                self.elifStat()


            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 256
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
            self.state = 259
            self.match(RogueLangParser.ELIF)
            self.state = 260
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 261
            self.expr(0)
            self.state = 262
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 263
            self.statBlock()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 264
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
            self.state = 267
            self.match(RogueLangParser.ELSE)
            self.state = 268
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
            self.state = 270
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 316092413229548) != 0):
                self.state = 271
                self.stat()
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 277
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
            self.state = 279
            self.match(RogueLangParser.FOR)
            self.state = 280
            self.match(RogueLangParser.ID)
            self.state = 281
            self.match(RogueLangParser.IN)
            self.state = 282
            self.match(RogueLangParser.ID)
            self.state = 283
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
            self.state = 285
            self.match(RogueLangParser.WHILE)
            self.state = 286
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 287
            self.expr(0)
            self.state = 288
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 289
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
            self.state = 291
            self.match(RogueLangParser.RETURN)
            self.state = 292
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
            self.state = 294
            self.match(RogueLangParser.T__5)
            self.state = 295
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 296
            self.match(RogueLangParser.ID)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 297
                self.match(RogueLangParser.COMMA)
                self.state = 298
                self.range_()


            self.state = 301
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 302
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
        self.enterRule(localctx, 62, self.RULE_random)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.match(RogueLangParser.T__6)
                self.state = 306
                self.match(RogueLangParser.IN)
                self.state = 307
                self.range_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(RogueLangParser.T__6)
                self.state = 309
                self.match(RogueLangParser.IN)
                self.state = 310
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
        self.enterRule(localctx, 64, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.expr(0)
            self.state = 314
            self.match(RogueLangParser.DOT)
            self.state = 315
            self.match(RogueLangParser.DOT)
            self.state = 316
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
        self.enterRule(localctx, 66, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(RogueLangParser.ID)
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 319
                self.match(RogueLangParser.COMMA)
                self.state = 320
                self.match(RogueLangParser.ID)
                self.state = 325
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
        self.enterRule(localctx, 68, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.expr(0)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 327
                self.match(RogueLangParser.COMMA)
                self.state = 328
                self.expr(0)
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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 335
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 336
                self.match(RogueLangParser.ID)
                self.state = 338 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 337
                        self.structFieldAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 340 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                pass

            elif la_ == 3:
                self.state = 342
                self.match(RogueLangParser.ID)
                self.state = 344 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 343
                        self.listAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 346 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                pass

            elif la_ == 4:
                self.state = 348
                self.listLength()
                pass

            elif la_ == 5:
                self.state = 349
                self.random()
                pass

            elif la_ == 6:
                self.state = 350
                self.match(RogueLangParser.NOT)
                self.state = 351
                self.expr(10)
                pass

            elif la_ == 7:
                self.state = 352
                self.match(RogueLangParser.SQRT)
                self.state = 353
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 354
                self.expr(0)
                self.state = 355
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 8:
                self.state = 357
                self.match(RogueLangParser.POW)
                self.state = 358
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 359
                self.expr(0)
                self.state = 360
                self.match(RogueLangParser.COMMA)
                self.state = 361
                self.expr(0)
                self.state = 362
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 9:
                self.state = 364
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 365
                self.expr(0)
                self.state = 366
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 10:
                self.state = 368
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 11:
                self.state = 369
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 12:
                self.state = 370
                self.match(RogueLangParser.FLOAT)
                pass

            elif la_ == 13:
                self.state = 371
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 14:
                self.state = 372
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 15:
                self.state = 373
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 388
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 376
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 377
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2153775104) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 378
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 379
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 380
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 381
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 382
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 383
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 384
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 385
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 386
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 387
                        self.expr(12)
                        pass

             
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        self._predicates[35] = self.expr_sempred
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
         




