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
        4,1,54,429,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,1,0,5,
        0,81,8,0,10,0,12,0,84,9,0,1,1,1,1,1,1,1,1,1,1,5,1,91,8,1,10,1,12,
        1,94,9,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,119,8,4,1,5,1,5,1,5,1,6,
        1,6,3,6,126,8,6,1,7,1,7,5,7,130,8,7,10,7,12,7,133,9,7,1,7,3,7,136,
        8,7,1,7,5,7,139,8,7,10,7,12,7,142,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,3,8,154,8,8,1,9,1,9,1,9,1,9,3,9,160,8,9,1,9,1,9,1,
        9,1,10,1,10,1,10,3,10,168,8,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,
        176,8,11,10,11,12,11,179,9,11,3,11,181,8,11,1,11,1,11,1,12,1,12,
        3,12,187,8,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,195,8,13,1,14,1,
        14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,
        16,5,16,212,8,16,10,16,12,16,215,9,16,3,16,217,8,16,1,16,1,16,1,
        17,1,17,1,17,1,17,1,17,1,17,3,17,227,8,17,1,18,1,18,1,18,1,18,1,
        18,1,18,3,18,235,8,18,1,19,1,19,1,19,1,19,1,19,5,19,242,8,19,10,
        19,12,19,245,9,19,1,19,1,19,1,20,1,20,1,20,1,20,4,20,253,8,20,11,
        20,12,20,254,1,20,1,20,1,21,1,21,1,22,1,22,1,22,5,22,264,8,22,10,
        22,12,22,267,9,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,
        25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,3,26,288,8,26,1,
        26,3,26,291,8,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,299,8,27,1,28,
        1,28,1,28,1,29,1,29,5,29,306,8,29,10,29,12,29,309,9,29,1,29,1,29,
        1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,32,
        1,32,1,32,1,33,1,33,1,33,1,33,1,33,3,33,333,8,33,1,33,1,33,3,33,
        337,8,33,1,34,1,34,1,34,1,34,1,34,1,34,3,34,345,8,34,1,35,1,35,1,
        35,1,35,1,35,1,36,1,36,1,36,5,36,355,8,36,10,36,12,36,358,9,36,1,
        37,1,37,1,37,5,37,363,8,37,10,37,12,37,366,9,37,1,38,1,38,1,38,1,
        38,4,38,372,8,38,11,38,12,38,373,1,38,1,38,1,38,1,38,4,38,380,8,
        38,11,38,12,38,381,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,1,38,3,38,410,8,38,1,38,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,5,38,424,8,38,10,38,12,38,427,9,38,
        1,38,0,1,76,39,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,0,
        4,2,0,21,22,31,31,1,0,19,20,1,0,23,28,1,0,32,33,456,0,78,1,0,0,0,
        2,85,1,0,0,0,4,97,1,0,0,0,6,100,1,0,0,0,8,118,1,0,0,0,10,120,1,0,
        0,0,12,123,1,0,0,0,14,127,1,0,0,0,16,153,1,0,0,0,18,155,1,0,0,0,
        20,164,1,0,0,0,22,171,1,0,0,0,24,186,1,0,0,0,26,194,1,0,0,0,28,196,
        1,0,0,0,30,201,1,0,0,0,32,207,1,0,0,0,34,226,1,0,0,0,36,234,1,0,
        0,0,38,236,1,0,0,0,40,248,1,0,0,0,42,258,1,0,0,0,44,260,1,0,0,0,
        46,268,1,0,0,0,48,272,1,0,0,0,50,276,1,0,0,0,52,281,1,0,0,0,54,292,
        1,0,0,0,56,300,1,0,0,0,58,303,1,0,0,0,60,312,1,0,0,0,62,318,1,0,
        0,0,64,324,1,0,0,0,66,327,1,0,0,0,68,344,1,0,0,0,70,346,1,0,0,0,
        72,351,1,0,0,0,74,359,1,0,0,0,76,409,1,0,0,0,78,82,3,2,1,0,79,81,
        3,8,4,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,
        83,1,1,0,0,0,84,82,1,0,0,0,85,86,5,43,0,0,86,87,5,48,0,0,87,92,3,
        4,2,0,88,91,3,6,3,0,89,91,3,8,4,0,90,88,1,0,0,0,90,89,1,0,0,0,91,
        94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,
        0,95,96,5,49,0,0,96,3,1,0,0,0,97,98,5,18,0,0,98,99,3,58,29,0,99,
        5,1,0,0,0,100,101,5,1,0,0,101,102,3,12,6,0,102,7,1,0,0,0,103,119,
        3,50,25,0,104,119,3,10,5,0,105,119,3,14,7,0,106,119,3,18,9,0,107,
        119,3,52,26,0,108,119,3,60,30,0,109,119,3,62,31,0,110,119,3,58,29,
        0,111,119,3,64,32,0,112,119,3,46,23,0,113,119,3,48,24,0,114,119,
        3,30,15,0,115,119,3,66,33,0,116,119,3,40,20,0,117,119,3,76,38,0,
        118,103,1,0,0,0,118,104,1,0,0,0,118,105,1,0,0,0,118,106,1,0,0,0,
        118,107,1,0,0,0,118,108,1,0,0,0,118,109,1,0,0,0,118,110,1,0,0,0,
        118,111,1,0,0,0,118,112,1,0,0,0,118,113,1,0,0,0,118,114,1,0,0,0,
        118,115,1,0,0,0,118,116,1,0,0,0,118,117,1,0,0,0,119,9,1,0,0,0,120,
        121,5,2,0,0,121,122,3,12,6,0,122,11,1,0,0,0,123,125,5,43,0,0,124,
        126,3,16,8,0,125,124,1,0,0,0,125,126,1,0,0,0,126,13,1,0,0,0,127,
        131,5,43,0,0,128,130,3,44,22,0,129,128,1,0,0,0,130,133,1,0,0,0,131,
        129,1,0,0,0,131,132,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,134,
        136,3,36,18,0,135,134,1,0,0,0,135,136,1,0,0,0,136,140,1,0,0,0,137,
        139,3,26,13,0,138,137,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,
        141,1,0,0,0,141,143,1,0,0,0,142,140,1,0,0,0,143,144,3,16,8,0,144,
        15,1,0,0,0,145,146,5,53,0,0,146,154,3,38,19,0,147,148,5,53,0,0,148,
        154,3,32,16,0,149,150,5,53,0,0,150,154,3,22,11,0,151,152,5,53,0,
        0,152,154,3,76,38,0,153,145,1,0,0,0,153,147,1,0,0,0,153,149,1,0,
        0,0,153,151,1,0,0,0,154,17,1,0,0,0,155,156,5,16,0,0,156,157,5,43,
        0,0,157,159,5,44,0,0,158,160,3,72,36,0,159,158,1,0,0,0,159,160,1,
        0,0,0,160,161,1,0,0,0,161,162,5,45,0,0,162,163,3,58,29,0,163,19,
        1,0,0,0,164,165,5,43,0,0,165,167,5,44,0,0,166,168,3,74,37,0,167,
        166,1,0,0,0,167,168,1,0,0,0,168,169,1,0,0,0,169,170,5,45,0,0,170,
        21,1,0,0,0,171,180,5,46,0,0,172,177,3,24,12,0,173,174,5,50,0,0,174,
        176,3,24,12,0,175,173,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,
        178,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,180,172,1,0,0,0,180,
        181,1,0,0,0,181,182,1,0,0,0,182,183,5,47,0,0,183,23,1,0,0,0,184,
        187,3,76,38,0,185,187,3,22,11,0,186,184,1,0,0,0,186,185,1,0,0,0,
        187,25,1,0,0,0,188,189,5,46,0,0,189,190,5,40,0,0,190,195,5,47,0,
        0,191,192,5,46,0,0,192,193,5,43,0,0,193,195,5,47,0,0,194,188,1,0,
        0,0,194,191,1,0,0,0,195,27,1,0,0,0,196,197,5,3,0,0,197,198,5,44,
        0,0,198,199,5,43,0,0,199,200,5,45,0,0,200,29,1,0,0,0,201,202,5,43,
        0,0,202,203,5,51,0,0,203,204,5,4,0,0,204,205,5,44,0,0,205,206,5,
        45,0,0,206,31,1,0,0,0,207,216,5,48,0,0,208,213,3,34,17,0,209,210,
        5,50,0,0,210,212,3,34,17,0,211,209,1,0,0,0,212,215,1,0,0,0,213,211,
        1,0,0,0,213,214,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,216,208,
        1,0,0,0,216,217,1,0,0,0,217,218,1,0,0,0,218,219,5,49,0,0,219,33,
        1,0,0,0,220,221,5,42,0,0,221,222,5,52,0,0,222,227,3,76,38,0,223,
        224,5,43,0,0,224,225,5,52,0,0,225,227,3,76,38,0,226,220,1,0,0,0,
        226,223,1,0,0,0,227,35,1,0,0,0,228,229,5,46,0,0,229,230,5,42,0,0,
        230,235,5,47,0,0,231,232,5,46,0,0,232,233,5,43,0,0,233,235,5,47,
        0,0,234,228,1,0,0,0,234,231,1,0,0,0,235,37,1,0,0,0,236,237,5,43,
        0,0,237,243,5,48,0,0,238,239,3,42,21,0,239,240,3,16,8,0,240,242,
        1,0,0,0,241,238,1,0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,243,244,
        1,0,0,0,244,246,1,0,0,0,245,243,1,0,0,0,246,247,5,49,0,0,247,39,
        1,0,0,0,248,249,5,5,0,0,249,250,5,43,0,0,250,252,5,48,0,0,251,253,
        3,42,21,0,252,251,1,0,0,0,253,254,1,0,0,0,254,252,1,0,0,0,254,255,
        1,0,0,0,255,256,1,0,0,0,256,257,5,49,0,0,257,41,1,0,0,0,258,259,
        5,43,0,0,259,43,1,0,0,0,260,261,5,51,0,0,261,265,5,43,0,0,262,264,
        3,26,13,0,263,262,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,266,
        1,0,0,0,266,45,1,0,0,0,267,265,1,0,0,0,268,269,5,43,0,0,269,270,
        5,29,0,0,270,271,3,76,38,0,271,47,1,0,0,0,272,273,5,43,0,0,273,274,
        5,30,0,0,274,275,3,76,38,0,275,49,1,0,0,0,276,277,5,12,0,0,277,278,
        5,44,0,0,278,279,3,76,38,0,279,280,5,45,0,0,280,51,1,0,0,0,281,282,
        5,8,0,0,282,283,5,44,0,0,283,284,3,76,38,0,284,285,5,45,0,0,285,
        287,3,58,29,0,286,288,3,54,27,0,287,286,1,0,0,0,287,288,1,0,0,0,
        288,290,1,0,0,0,289,291,3,56,28,0,290,289,1,0,0,0,290,291,1,0,0,
        0,291,53,1,0,0,0,292,293,5,9,0,0,293,294,5,44,0,0,294,295,3,76,38,
        0,295,296,5,45,0,0,296,298,3,58,29,0,297,299,3,54,27,0,298,297,1,
        0,0,0,298,299,1,0,0,0,299,55,1,0,0,0,300,301,5,10,0,0,301,302,3,
        58,29,0,302,57,1,0,0,0,303,307,5,48,0,0,304,306,3,8,4,0,305,304,
        1,0,0,0,306,309,1,0,0,0,307,305,1,0,0,0,307,308,1,0,0,0,308,310,
        1,0,0,0,309,307,1,0,0,0,310,311,5,49,0,0,311,59,1,0,0,0,312,313,
        5,13,0,0,313,314,5,43,0,0,314,315,5,14,0,0,315,316,5,43,0,0,316,
        317,3,58,29,0,317,61,1,0,0,0,318,319,5,15,0,0,319,320,5,44,0,0,320,
        321,3,76,38,0,321,322,5,45,0,0,322,323,3,58,29,0,323,63,1,0,0,0,
        324,325,5,11,0,0,325,326,3,76,38,0,326,65,1,0,0,0,327,328,5,6,0,
        0,328,329,5,44,0,0,329,332,5,43,0,0,330,331,5,50,0,0,331,333,3,70,
        35,0,332,330,1,0,0,0,332,333,1,0,0,0,333,334,1,0,0,0,334,336,5,45,
        0,0,335,337,5,17,0,0,336,335,1,0,0,0,336,337,1,0,0,0,337,67,1,0,
        0,0,338,339,5,7,0,0,339,340,5,14,0,0,340,345,3,70,35,0,341,342,5,
        7,0,0,342,343,5,14,0,0,343,345,5,43,0,0,344,338,1,0,0,0,344,341,
        1,0,0,0,345,69,1,0,0,0,346,347,3,76,38,0,347,348,5,51,0,0,348,349,
        5,51,0,0,349,350,3,76,38,0,350,71,1,0,0,0,351,356,5,43,0,0,352,353,
        5,50,0,0,353,355,5,43,0,0,354,352,1,0,0,0,355,358,1,0,0,0,356,354,
        1,0,0,0,356,357,1,0,0,0,357,73,1,0,0,0,358,356,1,0,0,0,359,364,3,
        76,38,0,360,361,5,50,0,0,361,363,3,76,38,0,362,360,1,0,0,0,363,366,
        1,0,0,0,364,362,1,0,0,0,364,365,1,0,0,0,365,75,1,0,0,0,366,364,1,
        0,0,0,367,368,6,38,-1,0,368,410,3,20,10,0,369,371,5,43,0,0,370,372,
        3,44,22,0,371,370,1,0,0,0,372,373,1,0,0,0,373,371,1,0,0,0,373,374,
        1,0,0,0,374,410,1,0,0,0,375,376,5,43,0,0,376,410,3,36,18,0,377,379,
        5,43,0,0,378,380,3,26,13,0,379,378,1,0,0,0,380,381,1,0,0,0,381,379,
        1,0,0,0,381,382,1,0,0,0,382,410,1,0,0,0,383,410,3,28,14,0,384,410,
        3,68,34,0,385,386,5,34,0,0,386,410,3,76,38,10,387,388,5,37,0,0,388,
        389,5,44,0,0,389,390,3,76,38,0,390,391,5,45,0,0,391,410,1,0,0,0,
        392,393,5,38,0,0,393,394,5,44,0,0,394,395,3,76,38,0,395,396,5,50,
        0,0,396,397,3,76,38,0,397,398,5,45,0,0,398,410,1,0,0,0,399,400,5,
        44,0,0,400,401,3,76,38,0,401,402,5,45,0,0,402,410,1,0,0,0,403,410,
        5,43,0,0,404,410,5,40,0,0,405,410,5,41,0,0,406,410,5,42,0,0,407,
        410,5,35,0,0,408,410,5,36,0,0,409,367,1,0,0,0,409,369,1,0,0,0,409,
        375,1,0,0,0,409,377,1,0,0,0,409,383,1,0,0,0,409,384,1,0,0,0,409,
        385,1,0,0,0,409,387,1,0,0,0,409,392,1,0,0,0,409,399,1,0,0,0,409,
        403,1,0,0,0,409,404,1,0,0,0,409,405,1,0,0,0,409,406,1,0,0,0,409,
        407,1,0,0,0,409,408,1,0,0,0,410,425,1,0,0,0,411,412,10,14,0,0,412,
        413,7,0,0,0,413,424,3,76,38,15,414,415,10,13,0,0,415,416,7,1,0,0,
        416,424,3,76,38,14,417,418,10,12,0,0,418,419,7,2,0,0,419,424,3,76,
        38,13,420,421,10,11,0,0,421,422,7,3,0,0,422,424,3,76,38,12,423,411,
        1,0,0,0,423,414,1,0,0,0,423,417,1,0,0,0,423,420,1,0,0,0,424,427,
        1,0,0,0,425,423,1,0,0,0,425,426,1,0,0,0,426,77,1,0,0,0,427,425,1,
        0,0,0,36,82,90,92,118,125,131,135,140,153,159,167,177,180,186,194,
        213,216,226,234,243,254,265,287,290,298,307,332,336,344,356,364,
        373,381,409,423,425
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
                     "'['", "']'", "'{'", "'}'", "','", "'.'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IF", "ELIF", "ELSE", "RETURN", "PRINT", "FOR", "IN", 
                      "WHILE", "DEF", "LAYER", "PROCEDURE", "PLUS", "MINUS", 
                      "MULT", "DIV", "GT", "GTE", "LT", "LTE", "EQ", "NEQ", 
                      "PEQ", "MEQ", "MOD", "AND", "OR", "NOT", "TRUE", "FALSE", 
                      "SQRT", "POW", "COMMENT_SINGLELINE", "INT", "FLOAT", 
                      "STRING", "ID", "OPEN_PARENTH", "CLOSED_PARENTH", 
                      "OPEN_BRACK", "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", 
                      "COMMA", "DOT", "COLON", "EQUAL_SIGN", "WS" ]

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
    RULE_hashTable = 16
    RULE_keyValuePair = 17
    RULE_hashKey = 18
    RULE_struct = 19
    RULE_structDef = 20
    RULE_structField = 21
    RULE_structFieldAccess = 22
    RULE_plusEquals = 23
    RULE_minusEquals = 24
    RULE_printStat = 25
    RULE_ifStat = 26
    RULE_elifStat = 27
    RULE_elseStat = 28
    RULE_statBlock = 29
    RULE_forLoop = 30
    RULE_whileLoop = 31
    RULE_returnStat = 32
    RULE_whiteNoiseStat = 33
    RULE_random = 34
    RULE_range = 35
    RULE_params = 36
    RULE_args = 37
    RULE_expr = 38

    ruleNames =  [ "prog", "object", "procedure", "field", "stat", "varDeclStat", 
                   "varDecl", "assignStat", "assignment", "functionDecl", 
                   "functionCall", "list", "listElement", "listAccess", 
                   "listLength", "listPop", "hashTable", "keyValuePair", 
                   "hashKey", "struct", "structDef", "structField", "structFieldAccess", 
                   "plusEquals", "minusEquals", "printStat", "ifStat", "elifStat", 
                   "elseStat", "statBlock", "forLoop", "whileLoop", "returnStat", 
                   "whiteNoiseStat", "random", "range", "params", "args", 
                   "expr" ]

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
    COLON=52
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
            self.state = 78
            self.object_()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 316092413229548) != 0):
                self.state = 79
                self.stat()
                self.state = 84
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
            self.state = 85
            self.match(RogueLangParser.ID)
            self.state = 86
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 87
            self.procedure()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 316092413229550) != 0):
                self.state = 90
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 88
                    self.field()
                    pass
                elif token in [2, 3, 5, 6, 7, 8, 11, 12, 13, 15, 16, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 48]:
                    self.state = 89
                    self.stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
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
            self.state = 97
            self.match(RogueLangParser.PROCEDURE)
            self.state = 98
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
            self.state = 100
            self.match(RogueLangParser.T__0)
            self.state = 101
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
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.varDeclStat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.assignStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.functionDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.ifStat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.forLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 109
                self.whileLoop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 110
                self.statBlock()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 111
                self.returnStat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 112
                self.plusEquals()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 113
                self.minusEquals()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 114
                self.listPop()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 115
                self.whiteNoiseStat()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 116
                self.structDef()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 117
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
            self.state = 120
            self.match(RogueLangParser.T__1)
            self.state = 121
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
            self.state = 123
            self.match(RogueLangParser.ID)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 124
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


        def hashKey(self):
            return self.getTypedRuleContext(RogueLangParser.HashKeyContext,0)


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
            self.state = 127
            self.match(RogueLangParser.ID)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 128
                self.structFieldAccess()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 134
                self.hashKey()


            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 137
                self.listAccess()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
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


        def hashTable(self):
            return self.getTypedRuleContext(RogueLangParser.HashTableContext,0)


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
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 146
                self.struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 148
                self.hashTable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 150
                self.list_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 152
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
            self.state = 155
            self.match(RogueLangParser.DEF)
            self.state = 156
            self.match(RogueLangParser.ID)
            self.state = 157
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 158
                self.params()


            self.state = 161
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 162
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
            self.state = 164
            self.match(RogueLangParser.ID)
            self.state = 165
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34617436405896) != 0):
                self.state = 166
                self.args()


            self.state = 169
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
            self.state = 171
            self.match(RogueLangParser.OPEN_BRACK)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 104986180583560) != 0):
                self.state = 172
                self.listElement()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 173
                    self.match(RogueLangParser.COMMA)
                    self.state = 174
                    self.listElement()
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 182
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
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 7, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.expr(0)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
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
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 189
                self.match(RogueLangParser.INT)
                self.state = 190
                self.match(RogueLangParser.CLOSED_BRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 192
                self.match(RogueLangParser.ID)
                self.state = 193
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
            self.state = 196
            self.match(RogueLangParser.T__2)
            self.state = 197
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 198
            self.match(RogueLangParser.ID)
            self.state = 199
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
            self.state = 201
            self.match(RogueLangParser.ID)
            self.state = 202
            self.match(RogueLangParser.DOT)
            self.state = 203
            self.match(RogueLangParser.T__3)
            self.state = 204
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 205
            self.match(RogueLangParser.CLOSED_PARENTH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HashTableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_CURL(self):
            return self.getToken(RogueLangParser.OPEN_CURL, 0)

        def CLOSED_CURL(self):
            return self.getToken(RogueLangParser.CLOSED_CURL, 0)

        def keyValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.KeyValuePairContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.KeyValuePairContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.COMMA)
            else:
                return self.getToken(RogueLangParser.COMMA, i)

        def getRuleIndex(self):
            return RogueLangParser.RULE_hashTable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHashTable" ):
                return visitor.visitHashTable(self)
            else:
                return visitor.visitChildren(self)




    def hashTable(self):

        localctx = RogueLangParser.HashTableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_hashTable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42 or _la==43:
                self.state = 208
                self.keyValuePair()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 209
                    self.match(RogueLangParser.COMMA)
                    self.state = 210
                    self.keyValuePair()
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 218
            self.match(RogueLangParser.CLOSED_CURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValuePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(RogueLangParser.STRING, 0)

        def COLON(self):
            return self.getToken(RogueLangParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_keyValuePair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyValuePair" ):
                return visitor.visitKeyValuePair(self)
            else:
                return visitor.visitChildren(self)




    def keyValuePair(self):

        localctx = RogueLangParser.KeyValuePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_keyValuePair)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(RogueLangParser.STRING)
                self.state = 221
                self.match(RogueLangParser.COLON)
                self.state = 222
                self.expr(0)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(RogueLangParser.ID)
                self.state = 224
                self.match(RogueLangParser.COLON)
                self.state = 225
                self.expr(0)
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


    class HashKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACK(self):
            return self.getToken(RogueLangParser.OPEN_BRACK, 0)

        def STRING(self):
            return self.getToken(RogueLangParser.STRING, 0)

        def CLOSED_BRACK(self):
            return self.getToken(RogueLangParser.CLOSED_BRACK, 0)

        def ID(self):
            return self.getToken(RogueLangParser.ID, 0)

        def getRuleIndex(self):
            return RogueLangParser.RULE_hashKey

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHashKey" ):
                return visitor.visitHashKey(self)
            else:
                return visitor.visitChildren(self)




    def hashKey(self):

        localctx = RogueLangParser.HashKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_hashKey)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 229
                self.match(RogueLangParser.STRING)
                self.state = 230
                self.match(RogueLangParser.CLOSED_BRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 232
                self.match(RogueLangParser.ID)
                self.state = 233
                self.match(RogueLangParser.CLOSED_BRACK)
                pass


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
        self.enterRule(localctx, 38, self.RULE_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(RogueLangParser.ID)
            self.state = 237
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 238
                self.structField()
                self.state = 239
                self.assignment()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
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
        self.enterRule(localctx, 40, self.RULE_structDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(RogueLangParser.T__4)
            self.state = 249
            self.match(RogueLangParser.ID)
            self.state = 250
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 252 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 251
                self.structField()
                self.state = 254 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==43):
                    break

            self.state = 256
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
        self.enterRule(localctx, 42, self.RULE_structField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
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
        self.enterRule(localctx, 44, self.RULE_structFieldAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(RogueLangParser.DOT)
            self.state = 261
            self.match(RogueLangParser.ID)
            self.state = 265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 262
                    self.listAccess() 
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_plusEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(RogueLangParser.ID)
            self.state = 269
            self.match(RogueLangParser.PEQ)
            self.state = 270
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
        self.enterRule(localctx, 48, self.RULE_minusEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(RogueLangParser.ID)
            self.state = 273
            self.match(RogueLangParser.MEQ)
            self.state = 274
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
        self.enterRule(localctx, 50, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(RogueLangParser.PRINT)
            self.state = 277
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 278
            self.expr(0)
            self.state = 279
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
        self.enterRule(localctx, 52, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(RogueLangParser.IF)
            self.state = 282
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 283
            self.expr(0)
            self.state = 284
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 285
            self.statBlock()
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 286
                self.elifStat()


            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 289
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
        self.enterRule(localctx, 54, self.RULE_elifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(RogueLangParser.ELIF)
            self.state = 293
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 294
            self.expr(0)
            self.state = 295
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 296
            self.statBlock()
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 297
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
        self.enterRule(localctx, 56, self.RULE_elseStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(RogueLangParser.ELSE)
            self.state = 301
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
        self.enterRule(localctx, 58, self.RULE_statBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 316092413229548) != 0):
                self.state = 304
                self.stat()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 310
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
        self.enterRule(localctx, 60, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(RogueLangParser.FOR)
            self.state = 313
            self.match(RogueLangParser.ID)
            self.state = 314
            self.match(RogueLangParser.IN)
            self.state = 315
            self.match(RogueLangParser.ID)
            self.state = 316
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
        self.enterRule(localctx, 62, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(RogueLangParser.WHILE)
            self.state = 319
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 320
            self.expr(0)
            self.state = 321
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 322
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
        self.enterRule(localctx, 64, self.RULE_returnStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(RogueLangParser.RETURN)
            self.state = 325
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
        self.enterRule(localctx, 66, self.RULE_whiteNoiseStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(RogueLangParser.T__5)
            self.state = 328
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 329
            self.match(RogueLangParser.ID)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 330
                self.match(RogueLangParser.COMMA)
                self.state = 331
                self.range_()


            self.state = 334
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 335
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
        self.enterRule(localctx, 68, self.RULE_random)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(RogueLangParser.T__6)
                self.state = 339
                self.match(RogueLangParser.IN)
                self.state = 340
                self.range_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(RogueLangParser.T__6)
                self.state = 342
                self.match(RogueLangParser.IN)
                self.state = 343
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
        self.enterRule(localctx, 70, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.expr(0)
            self.state = 347
            self.match(RogueLangParser.DOT)
            self.state = 348
            self.match(RogueLangParser.DOT)
            self.state = 349
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
        self.enterRule(localctx, 72, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(RogueLangParser.ID)
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 352
                self.match(RogueLangParser.COMMA)
                self.state = 353
                self.match(RogueLangParser.ID)
                self.state = 358
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
        self.enterRule(localctx, 74, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.expr(0)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 360
                self.match(RogueLangParser.COMMA)
                self.state = 361
                self.expr(0)
                self.state = 366
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


        def hashKey(self):
            return self.getTypedRuleContext(RogueLangParser.HashKeyContext,0)


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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 368
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 369
                self.match(RogueLangParser.ID)
                self.state = 371 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 370
                        self.structFieldAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 373 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                pass

            elif la_ == 3:
                self.state = 375
                self.match(RogueLangParser.ID)
                self.state = 376
                self.hashKey()
                pass

            elif la_ == 4:
                self.state = 377
                self.match(RogueLangParser.ID)
                self.state = 379 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 378
                        self.listAccess()

                    else:
                        raise NoViableAltException(self)
                    self.state = 381 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                pass

            elif la_ == 5:
                self.state = 383
                self.listLength()
                pass

            elif la_ == 6:
                self.state = 384
                self.random()
                pass

            elif la_ == 7:
                self.state = 385
                self.match(RogueLangParser.NOT)
                self.state = 386
                self.expr(10)
                pass

            elif la_ == 8:
                self.state = 387
                self.match(RogueLangParser.SQRT)
                self.state = 388
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 389
                self.expr(0)
                self.state = 390
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 9:
                self.state = 392
                self.match(RogueLangParser.POW)
                self.state = 393
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 394
                self.expr(0)
                self.state = 395
                self.match(RogueLangParser.COMMA)
                self.state = 396
                self.expr(0)
                self.state = 397
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 10:
                self.state = 399
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 400
                self.expr(0)
                self.state = 401
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 11:
                self.state = 403
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 12:
                self.state = 404
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 13:
                self.state = 405
                self.match(RogueLangParser.FLOAT)
                pass

            elif la_ == 14:
                self.state = 406
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 15:
                self.state = 407
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 16:
                self.state = 408
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 423
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 411
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 412
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2153775104) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 413
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 414
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 415
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 416
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 417
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 418
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 419
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 420
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 421
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 422
                        self.expr(12)
                        pass

             
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self._predicates[38] = self.expr_sempred
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
         




