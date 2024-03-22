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
        4,1,49,316,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,4,0,56,8,0,11,0,12,0,57,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,70,8,1,1,2,1,2,1,2,1,2,5,2,76,8,2,10,2,12,2,79,9,2,3,2,81,
        8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,96,8,
        4,1,5,1,5,1,5,3,5,101,8,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,111,
        8,7,10,7,12,7,114,9,7,1,7,1,7,1,7,1,7,5,7,120,8,7,10,7,12,7,123,
        9,7,1,7,3,7,126,8,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,134,8,8,10,8,12,
        8,137,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,147,8,9,10,9,12,9,
        150,9,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,158,8,10,1,10,1,10,1,10,
        5,10,163,8,10,10,10,12,10,166,9,10,1,10,1,10,1,11,1,11,1,11,3,11,
        173,8,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,181,8,12,10,12,12,12,
        184,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,5,14,195,8,
        14,10,14,12,14,198,9,14,1,15,1,15,1,15,1,16,1,16,1,16,5,16,206,8,
        16,10,16,12,16,209,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,
        1,18,1,18,1,18,1,18,4,18,223,8,18,11,18,12,18,224,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,5,20,238,8,20,10,20,12,20,
        241,9,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,251,8,22,1,
        23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,5,24,262,8,24,10,24,12,
        24,265,9,24,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,3,26,283,8,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,5,26,311,8,26,10,26,12,
        26,314,9,26,1,26,0,1,52,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,0,4,3,0,8,14,43,44,48,48,
        1,0,40,41,1,0,38,39,1,0,32,37,335,0,55,1,0,0,0,2,69,1,0,0,0,4,71,
        1,0,0,0,6,84,1,0,0,0,8,89,1,0,0,0,10,97,1,0,0,0,12,102,1,0,0,0,14,
        104,1,0,0,0,16,127,1,0,0,0,18,140,1,0,0,0,20,153,1,0,0,0,22,169,
        1,0,0,0,24,176,1,0,0,0,26,187,1,0,0,0,28,191,1,0,0,0,30,199,1,0,
        0,0,32,202,1,0,0,0,34,210,1,0,0,0,36,217,1,0,0,0,38,228,1,0,0,0,
        40,234,1,0,0,0,42,242,1,0,0,0,44,250,1,0,0,0,46,252,1,0,0,0,48,258,
        1,0,0,0,50,266,1,0,0,0,52,282,1,0,0,0,54,56,3,2,1,0,55,54,1,0,0,
        0,56,57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,1,1,0,0,0,59,70,3,
        6,3,0,60,70,3,8,4,0,61,70,3,14,7,0,62,70,3,16,8,0,63,70,3,18,9,0,
        64,70,3,20,10,0,65,70,3,22,11,0,66,70,3,24,12,0,67,70,3,38,19,0,
        68,70,3,52,26,0,69,59,1,0,0,0,69,60,1,0,0,0,69,61,1,0,0,0,69,62,
        1,0,0,0,69,63,1,0,0,0,69,64,1,0,0,0,69,65,1,0,0,0,69,66,1,0,0,0,
        69,67,1,0,0,0,69,68,1,0,0,0,70,3,1,0,0,0,71,80,5,1,0,0,72,77,3,52,
        26,0,73,74,5,2,0,0,74,76,3,52,26,0,75,73,1,0,0,0,76,79,1,0,0,0,77,
        75,1,0,0,0,77,78,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,80,72,1,0,0,
        0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,3,0,0,83,5,1,0,0,0,84,85,5,
        4,0,0,85,86,5,5,0,0,86,87,3,52,26,0,87,88,5,6,0,0,88,7,1,0,0,0,89,
        90,3,10,5,0,90,95,5,48,0,0,91,92,5,7,0,0,92,96,3,52,26,0,93,96,3,
        24,12,0,94,96,3,32,16,0,95,91,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,
        0,95,96,1,0,0,0,96,9,1,0,0,0,97,100,3,12,6,0,98,99,5,1,0,0,99,101,
        5,3,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,11,1,0,0,0,102,103,7,
        0,0,0,103,13,1,0,0,0,104,105,5,15,0,0,105,106,5,5,0,0,106,107,3,
        52,26,0,107,108,5,6,0,0,108,112,5,16,0,0,109,111,3,2,1,0,110,109,
        1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,115,
        1,0,0,0,114,112,1,0,0,0,115,125,5,17,0,0,116,117,5,18,0,0,117,121,
        5,16,0,0,118,120,3,2,1,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,
        1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,126,
        5,17,0,0,125,116,1,0,0,0,125,126,1,0,0,0,126,15,1,0,0,0,127,128,
        5,19,0,0,128,129,3,8,4,0,129,130,5,20,0,0,130,131,3,52,26,0,131,
        135,5,16,0,0,132,134,3,2,1,0,133,132,1,0,0,0,134,137,1,0,0,0,135,
        133,1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,135,1,0,0,0,138,
        139,5,17,0,0,139,17,1,0,0,0,140,141,5,21,0,0,141,142,5,5,0,0,142,
        143,3,52,26,0,143,144,5,6,0,0,144,148,5,16,0,0,145,147,3,2,1,0,146,
        145,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,
        151,1,0,0,0,150,148,1,0,0,0,151,152,5,17,0,0,152,19,1,0,0,0,153,
        154,5,22,0,0,154,155,5,48,0,0,155,157,5,5,0,0,156,158,3,28,14,0,
        157,156,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,5,6,0,0,
        160,164,5,16,0,0,161,163,3,2,1,0,162,161,1,0,0,0,163,166,1,0,0,0,
        164,162,1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,164,1,0,0,0,
        167,168,5,17,0,0,168,21,1,0,0,0,169,170,5,48,0,0,170,172,5,5,0,0,
        171,173,3,32,16,0,172,171,1,0,0,0,172,173,1,0,0,0,173,174,1,0,0,
        0,174,175,5,6,0,0,175,23,1,0,0,0,176,177,5,16,0,0,177,182,3,52,26,
        0,178,179,5,2,0,0,179,181,3,52,26,0,180,178,1,0,0,0,181,184,1,0,
        0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,182,1,0,
        0,0,185,186,5,17,0,0,186,25,1,0,0,0,187,188,5,23,0,0,188,189,3,44,
        22,0,189,190,3,46,23,0,190,27,1,0,0,0,191,196,3,30,15,0,192,193,
        5,2,0,0,193,195,3,30,15,0,194,192,1,0,0,0,195,198,1,0,0,0,196,194,
        1,0,0,0,196,197,1,0,0,0,197,29,1,0,0,0,198,196,1,0,0,0,199,200,3,
        10,5,0,200,201,5,48,0,0,201,31,1,0,0,0,202,207,3,52,26,0,203,204,
        5,2,0,0,204,206,3,52,26,0,205,203,1,0,0,0,206,209,1,0,0,0,207,205,
        1,0,0,0,207,208,1,0,0,0,208,33,1,0,0,0,209,207,1,0,0,0,210,211,5,
        24,0,0,211,212,5,5,0,0,212,213,5,45,0,0,213,214,5,2,0,0,214,215,
        5,45,0,0,215,216,5,6,0,0,216,35,1,0,0,0,217,218,5,25,0,0,218,219,
        5,5,0,0,219,222,3,52,26,0,220,221,5,2,0,0,221,223,3,52,26,0,222,
        220,1,0,0,0,223,224,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,
        226,1,0,0,0,226,227,5,6,0,0,227,37,1,0,0,0,228,229,5,26,0,0,229,
        230,5,48,0,0,230,231,5,16,0,0,231,232,3,40,20,0,232,233,5,17,0,0,
        233,39,1,0,0,0,234,239,5,48,0,0,235,236,5,2,0,0,236,238,5,48,0,0,
        237,235,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,
        240,41,1,0,0,0,241,239,1,0,0,0,242,243,5,48,0,0,243,244,5,27,0,0,
        244,245,5,48,0,0,245,43,1,0,0,0,246,251,5,28,0,0,247,251,5,29,0,
        0,248,249,5,45,0,0,249,251,5,30,0,0,250,246,1,0,0,0,250,247,1,0,
        0,0,250,248,1,0,0,0,251,45,1,0,0,0,252,253,5,5,0,0,253,254,3,48,
        24,0,254,255,5,2,0,0,255,256,3,50,25,0,256,257,5,6,0,0,257,47,1,
        0,0,0,258,263,5,45,0,0,259,260,5,2,0,0,260,262,5,45,0,0,261,259,
        1,0,0,0,262,265,1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,264,49,1,
        0,0,0,265,263,1,0,0,0,266,267,5,45,0,0,267,51,1,0,0,0,268,269,6,
        26,-1,0,269,270,5,5,0,0,270,271,3,52,26,0,271,272,5,6,0,0,272,283,
        1,0,0,0,273,283,5,48,0,0,274,283,5,45,0,0,275,283,5,47,0,0,276,283,
        5,46,0,0,277,283,5,43,0,0,278,283,5,44,0,0,279,283,3,34,17,0,280,
        283,3,36,18,0,281,283,3,42,21,0,282,268,1,0,0,0,282,273,1,0,0,0,
        282,274,1,0,0,0,282,275,1,0,0,0,282,276,1,0,0,0,282,277,1,0,0,0,
        282,278,1,0,0,0,282,279,1,0,0,0,282,280,1,0,0,0,282,281,1,0,0,0,
        283,312,1,0,0,0,284,285,10,15,0,0,285,286,5,1,0,0,286,287,3,52,26,
        0,287,288,5,3,0,0,288,289,5,7,0,0,289,290,3,52,26,16,290,311,1,0,
        0,0,291,292,10,13,0,0,292,293,7,1,0,0,293,311,3,52,26,14,294,295,
        10,12,0,0,295,296,7,2,0,0,296,311,3,52,26,13,297,298,10,11,0,0,298,
        299,7,3,0,0,299,311,3,52,26,12,300,301,10,16,0,0,301,302,5,1,0,0,
        302,303,3,52,26,0,303,304,5,3,0,0,304,311,1,0,0,0,305,306,10,14,
        0,0,306,307,5,31,0,0,307,308,3,52,26,0,308,309,5,6,0,0,309,311,1,
        0,0,0,310,284,1,0,0,0,310,291,1,0,0,0,310,294,1,0,0,0,310,297,1,
        0,0,0,310,300,1,0,0,0,310,305,1,0,0,0,311,314,1,0,0,0,312,310,1,
        0,0,0,312,313,1,0,0,0,313,53,1,0,0,0,314,312,1,0,0,0,24,57,69,77,
        80,95,100,112,121,125,135,148,157,164,172,182,196,207,224,239,250,
        263,282,310,312
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "','", "']'", "'print'", "'('", 
                     "')'", "'='", "'int'", "'string'", "'bool'", "'double'", 
                     "'date'", "'time'", "'dateTime'", "'if'", "'{'", "'}'", 
                     "'else'", "'for'", "'in'", "'while'", "'def'", "'BSP'", 
                     "'randomInt'", "'randomChoice'", "'enum'", "'.'", "'2D'", 
                     "'3D'", "'D'", "'.add('", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PLUS", "MINUS", "MULT", 
                      "DIV", "MOD", "TRUE", "FALSE", "INT", "DOUBLE", "STRING", 
                      "ID", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_array = 2
    RULE_printStat = 3
    RULE_varDecl = 4
    RULE_dataType = 5
    RULE_baseType = 6
    RULE_ifStat = 7
    RULE_forLoop = 8
    RULE_whileLoop = 9
    RULE_functionDecl = 10
    RULE_functionCall = 11
    RULE_arrayInit = 12
    RULE_bsp = 13
    RULE_params = 14
    RULE_param = 15
    RULE_args = 16
    RULE_randomInt = 17
    RULE_randomChoice = 18
    RULE_enumDecl = 19
    RULE_enumBody = 20
    RULE_enumValue = 21
    RULE_bspDimension = 22
    RULE_bspParameters = 23
    RULE_dimensionList = 24
    RULE_minSize = 25
    RULE_expr = 26

    ruleNames =  [ "prog", "stat", "array", "printStat", "varDecl", "dataType", 
                   "baseType", "ifStat", "forLoop", "whileLoop", "functionDecl", 
                   "functionCall", "arrayInit", "bsp", "params", "param", 
                   "args", "randomInt", "randomChoice", "enumDecl", "enumBody", 
                   "enumValue", "bspDimension", "bspParameters", "dimensionList", 
                   "minSize", "expr" ]

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
    PLUS=38
    MINUS=39
    MULT=40
    DIV=41
    MOD=42
    TRUE=43
    FALSE=44
    INT=45
    DOUBLE=46
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
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.stat()
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 554153984786224) != 0)):
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
            self.state = 69
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
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 64
                self.functionDecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 65
                self.functionCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 66
                self.arrayInit()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 67
                self.enumDecl()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 68
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
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
            return RogueLangParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = RogueLangParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(RogueLangParser.T__0)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 554153910730784) != 0):
                self.state = 72
                self.expr(0)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 73
                    self.match(RogueLangParser.T__1)
                    self.state = 74
                    self.expr(0)
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 82
            self.match(RogueLangParser.T__2)
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
        self.enterRule(localctx, 6, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(RogueLangParser.T__3)
            self.state = 85
            self.match(RogueLangParser.T__4)
            self.state = 86
            self.expr(0)
            self.state = 87
            self.match(RogueLangParser.T__5)
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
        self.enterRule(localctx, 8, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.dataType()
            self.state = 90
            self.match(RogueLangParser.ID)
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 91
                self.match(RogueLangParser.T__6)
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


        def getRuleIndex(self):
            return RogueLangParser.RULE_dataType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = RogueLangParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.baseType()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 98
                self.match(RogueLangParser.T__0)
                self.state = 99
                self.match(RogueLangParser.T__2)


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
        self.enterRule(localctx, 12, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 307863255809792) != 0)):
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
        self.enterRule(localctx, 14, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(RogueLangParser.T__14)
            self.state = 105
            self.match(RogueLangParser.T__4)
            self.state = 106
            self.expr(0)
            self.state = 107
            self.match(RogueLangParser.T__5)
            self.state = 108
            self.match(RogueLangParser.T__15)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 554153984786224) != 0):
                self.state = 109
                self.stat()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(RogueLangParser.T__16)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 116
                self.match(RogueLangParser.T__17)
                self.state = 117
                self.match(RogueLangParser.T__15)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 554153984786224) != 0):
                    self.state = 118
                    self.stat()
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 124
                self.match(RogueLangParser.T__16)


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
            self.state = 127
            self.match(RogueLangParser.T__18)
            self.state = 128
            self.varDecl()
            self.state = 129
            self.match(RogueLangParser.T__19)
            self.state = 130
            self.expr(0)
            self.state = 131
            self.match(RogueLangParser.T__15)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 554153984786224) != 0):
                self.state = 132
                self.stat()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.match(RogueLangParser.T__16)
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
            self.state = 140
            self.match(RogueLangParser.T__20)
            self.state = 141
            self.match(RogueLangParser.T__4)
            self.state = 142
            self.expr(0)
            self.state = 143
            self.match(RogueLangParser.T__5)
            self.state = 144
            self.match(RogueLangParser.T__15)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 554153984786224) != 0):
                self.state = 145
                self.stat()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(RogueLangParser.T__16)
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
            self.state = 153
            self.match(RogueLangParser.T__21)
            self.state = 154
            self.match(RogueLangParser.ID)
            self.state = 155
            self.match(RogueLangParser.T__4)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 307863255809792) != 0):
                self.state = 156
                self.params()


            self.state = 159
            self.match(RogueLangParser.T__5)
            self.state = 160
            self.match(RogueLangParser.T__15)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 554153984786224) != 0):
                self.state = 161
                self.stat()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(RogueLangParser.T__16)
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
            self.state = 169
            self.match(RogueLangParser.ID)
            self.state = 170
            self.match(RogueLangParser.T__4)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 554153910730784) != 0):
                self.state = 171
                self.args()


            self.state = 174
            self.match(RogueLangParser.T__5)
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
            self.state = 176
            self.match(RogueLangParser.T__15)
            self.state = 177
            self.expr(0)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 178
                self.match(RogueLangParser.T__1)
                self.state = 179
                self.expr(0)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self.match(RogueLangParser.T__16)
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
            self.state = 187
            self.match(RogueLangParser.T__22)
            self.state = 188
            self.bspDimension()
            self.state = 189
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
            self.state = 191
            self.param()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 192
                self.match(RogueLangParser.T__1)
                self.state = 193
                self.param()
                self.state = 198
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
            self.state = 199
            self.dataType()
            self.state = 200
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
            self.state = 202
            self.expr(0)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 203
                self.match(RogueLangParser.T__1)
                self.state = 204
                self.expr(0)
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 34, self.RULE_randomInt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(RogueLangParser.T__23)
            self.state = 211
            self.match(RogueLangParser.T__4)
            self.state = 212
            self.match(RogueLangParser.INT)
            self.state = 213
            self.match(RogueLangParser.T__1)
            self.state = 214
            self.match(RogueLangParser.INT)
            self.state = 215
            self.match(RogueLangParser.T__5)
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
        self.enterRule(localctx, 36, self.RULE_randomChoice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(RogueLangParser.T__24)
            self.state = 218
            self.match(RogueLangParser.T__4)
            self.state = 219
            self.expr(0)
            self.state = 222 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 220
                self.match(RogueLangParser.T__1)
                self.state = 221
                self.expr(0)
                self.state = 224 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 226
            self.match(RogueLangParser.T__5)
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
        self.enterRule(localctx, 38, self.RULE_enumDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(RogueLangParser.T__25)
            self.state = 229
            self.match(RogueLangParser.ID)
            self.state = 230
            self.match(RogueLangParser.T__15)
            self.state = 231
            self.enumBody()
            self.state = 232
            self.match(RogueLangParser.T__16)
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
        self.enterRule(localctx, 40, self.RULE_enumBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(RogueLangParser.ID)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 235
                self.match(RogueLangParser.T__1)
                self.state = 236
                self.match(RogueLangParser.ID)
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
            self.state = 242
            self.match(RogueLangParser.ID)
            self.state = 243
            self.match(RogueLangParser.T__26)
            self.state = 244
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
        self.enterRule(localctx, 44, self.RULE_bspDimension)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(RogueLangParser.T__27)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(RogueLangParser.T__28)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(RogueLangParser.INT)
                self.state = 249
                self.match(RogueLangParser.T__29)
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
        self.enterRule(localctx, 46, self.RULE_bspParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(RogueLangParser.T__4)
            self.state = 253
            self.dimensionList()
            self.state = 254
            self.match(RogueLangParser.T__1)
            self.state = 255
            self.minSize()
            self.state = 256
            self.match(RogueLangParser.T__5)
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
        self.enterRule(localctx, 48, self.RULE_dimensionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(RogueLangParser.INT)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 259
                    self.match(RogueLangParser.T__1)
                    self.state = 260
                    self.match(RogueLangParser.INT) 
                self.state = 265
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
        self.enterRule(localctx, 50, self.RULE_minSize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(RogueLangParser.INT)
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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 269
                self.match(RogueLangParser.T__4)
                self.state = 270
                self.expr(0)
                self.state = 271
                self.match(RogueLangParser.T__5)
                pass

            elif la_ == 2:
                self.state = 273
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 3:
                self.state = 274
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 4:
                self.state = 275
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 5:
                self.state = 276
                self.match(RogueLangParser.DOUBLE)
                pass

            elif la_ == 6:
                self.state = 277
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 7:
                self.state = 278
                self.match(RogueLangParser.FALSE)
                pass

            elif la_ == 8:
                self.state = 279
                self.randomInt()
                pass

            elif la_ == 9:
                self.state = 280
                self.randomChoice()
                pass

            elif la_ == 10:
                self.state = 281
                self.enumValue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 310
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 284
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 285
                        self.match(RogueLangParser.T__0)
                        self.state = 286
                        self.expr(0)
                        self.state = 287
                        self.match(RogueLangParser.T__2)
                        self.state = 288
                        self.match(RogueLangParser.T__6)
                        self.state = 289
                        self.expr(16)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 291
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 292
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==40 or _la==41):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 293
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 294
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 295
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==38 or _la==39):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 296
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 297
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 298
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 270582939648) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 299
                        self.expr(12)
                        pass

                    elif la_ == 5:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 300
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 301
                        self.match(RogueLangParser.T__0)
                        self.state = 302
                        self.expr(0)
                        self.state = 303
                        self.match(RogueLangParser.T__2)
                        pass

                    elif la_ == 6:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 305
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 306
                        self.match(RogueLangParser.T__30)
                        self.state = 307
                        self.expr(0)
                        self.state = 308
                        self.match(RogueLangParser.T__5)
                        pass

             
                self.state = 314
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self._predicates[26] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 14)
         




