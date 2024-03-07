# Generated from C://Users//Muffin//Documents//GitHub//P4-comp//grammar_files//RogueLang.g4 by ANTLR 4.13.1
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
        4,1,50,300,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,4,0,46,8,0,11,0,12,0,47,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,61,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,75,8,3,1,3,1,3,1,4,1,4,1,4,3,4,82,8,4,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,92,8,6,10,6,12,6,95,9,6,1,6,1,6,1,
        6,1,6,5,6,101,8,6,10,6,12,6,104,9,6,1,6,3,6,107,8,6,1,6,1,6,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,120,8,7,10,7,12,7,123,9,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,136,8,8,10,8,12,8,
        139,9,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,150,8,9,10,9,12,
        9,153,9,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,162,8,10,1,10,1,10,
        1,10,5,10,167,8,10,10,10,12,10,170,9,10,1,10,1,10,1,10,1,11,1,11,
        1,11,3,11,178,8,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,187,8,
        12,10,12,12,12,190,9,12,1,12,1,12,1,12,1,13,1,13,1,13,5,13,198,8,
        13,10,13,12,13,201,9,13,1,14,1,14,1,14,1,15,1,15,1,15,5,15,209,8,
        15,10,15,12,15,212,9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,231,8,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,
        259,8,16,10,16,12,16,262,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,18,1,18,4,18,276,8,18,11,18,12,18,277,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,5,20,291,8,20,10,20,
        12,20,294,9,20,1,21,1,21,1,21,1,21,1,21,0,1,32,22,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,4,2,0,9,15,41,41,
        1,0,39,40,1,0,37,38,1,0,27,32,323,0,45,1,0,0,0,2,60,1,0,0,0,4,62,
        1,0,0,0,6,68,1,0,0,0,8,78,1,0,0,0,10,83,1,0,0,0,12,85,1,0,0,0,14,
        110,1,0,0,0,16,127,1,0,0,0,18,143,1,0,0,0,20,157,1,0,0,0,22,174,
        1,0,0,0,24,182,1,0,0,0,26,194,1,0,0,0,28,202,1,0,0,0,30,205,1,0,
        0,0,32,230,1,0,0,0,34,263,1,0,0,0,36,270,1,0,0,0,38,281,1,0,0,0,
        40,287,1,0,0,0,42,295,1,0,0,0,44,46,3,2,1,0,45,44,1,0,0,0,46,47,
        1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,1,1,0,0,0,49,61,3,4,2,0,50,
        61,3,6,3,0,51,61,3,12,6,0,52,61,3,14,7,0,53,61,3,16,8,0,54,61,3,
        18,9,0,55,61,3,20,10,0,56,61,3,22,11,0,57,61,3,24,12,0,58,61,3,38,
        19,0,59,61,3,32,16,0,60,49,1,0,0,0,60,50,1,0,0,0,60,51,1,0,0,0,60,
        52,1,0,0,0,60,53,1,0,0,0,60,54,1,0,0,0,60,55,1,0,0,0,60,56,1,0,0,
        0,60,57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,0,0,61,3,1,0,0,0,62,63,5,
        1,0,0,63,64,5,2,0,0,64,65,3,32,16,0,65,66,5,3,0,0,66,67,5,4,0,0,
        67,5,1,0,0,0,68,69,5,5,0,0,69,70,3,8,4,0,70,74,5,41,0,0,71,72,5,
        6,0,0,72,75,3,32,16,0,73,75,3,24,12,0,74,71,1,0,0,0,74,73,1,0,0,
        0,74,75,1,0,0,0,75,76,1,0,0,0,76,77,5,4,0,0,77,7,1,0,0,0,78,81,3,
        10,5,0,79,80,5,7,0,0,80,82,5,8,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,
        9,1,0,0,0,83,84,7,0,0,0,84,11,1,0,0,0,85,86,5,16,0,0,86,87,5,2,0,
        0,87,88,3,32,16,0,88,89,5,3,0,0,89,93,5,17,0,0,90,92,3,2,1,0,91,
        90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,
        0,95,93,1,0,0,0,96,106,5,18,0,0,97,98,5,19,0,0,98,102,5,17,0,0,99,
        101,3,2,1,0,100,99,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,
        1,0,0,0,103,105,1,0,0,0,104,102,1,0,0,0,105,107,5,18,0,0,106,97,
        1,0,0,0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,5,4,0,0,109,13,1,
        0,0,0,110,111,5,20,0,0,111,112,5,2,0,0,112,113,3,6,3,0,113,114,3,
        32,16,0,114,115,5,4,0,0,115,116,3,32,16,0,116,117,5,3,0,0,117,121,
        5,17,0,0,118,120,3,2,1,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,
        1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,125,
        5,18,0,0,125,126,5,4,0,0,126,15,1,0,0,0,127,128,5,21,0,0,128,129,
        5,2,0,0,129,130,3,6,3,0,130,131,5,22,0,0,131,132,3,32,16,0,132,133,
        5,3,0,0,133,137,5,17,0,0,134,136,3,2,1,0,135,134,1,0,0,0,136,139,
        1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,137,
        1,0,0,0,140,141,5,18,0,0,141,142,5,4,0,0,142,17,1,0,0,0,143,144,
        5,23,0,0,144,145,5,2,0,0,145,146,3,32,16,0,146,147,5,3,0,0,147,151,
        5,17,0,0,148,150,3,2,1,0,149,148,1,0,0,0,150,153,1,0,0,0,151,149,
        1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,151,1,0,0,0,154,155,
        5,18,0,0,155,156,5,4,0,0,156,19,1,0,0,0,157,158,5,24,0,0,158,159,
        5,41,0,0,159,161,5,2,0,0,160,162,3,26,13,0,161,160,1,0,0,0,161,162,
        1,0,0,0,162,163,1,0,0,0,163,164,5,3,0,0,164,168,5,17,0,0,165,167,
        3,2,1,0,166,165,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,
        1,0,0,0,169,171,1,0,0,0,170,168,1,0,0,0,171,172,5,18,0,0,172,173,
        5,4,0,0,173,21,1,0,0,0,174,175,5,41,0,0,175,177,5,2,0,0,176,178,
        3,30,15,0,177,176,1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,180,
        5,3,0,0,180,181,5,4,0,0,181,23,1,0,0,0,182,183,5,17,0,0,183,188,
        3,32,16,0,184,185,5,25,0,0,185,187,3,32,16,0,186,184,1,0,0,0,187,
        190,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,
        188,1,0,0,0,191,192,5,18,0,0,192,193,5,4,0,0,193,25,1,0,0,0,194,
        199,3,28,14,0,195,196,5,25,0,0,196,198,3,28,14,0,197,195,1,0,0,0,
        198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,27,1,0,0,0,201,
        199,1,0,0,0,202,203,3,8,4,0,203,204,5,41,0,0,204,29,1,0,0,0,205,
        210,3,32,16,0,206,207,5,25,0,0,207,209,3,32,16,0,208,206,1,0,0,0,
        209,212,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,31,1,0,0,0,212,
        210,1,0,0,0,213,214,6,16,-1,0,214,215,5,2,0,0,215,216,3,32,16,0,
        216,217,5,3,0,0,217,231,1,0,0,0,218,231,5,41,0,0,219,231,5,42,0,
        0,220,231,5,43,0,0,221,231,5,44,0,0,222,231,5,45,0,0,223,231,5,46,
        0,0,224,231,5,47,0,0,225,231,5,48,0,0,226,231,5,49,0,0,227,231,3,
        34,17,0,228,231,3,36,18,0,229,231,3,42,21,0,230,213,1,0,0,0,230,
        218,1,0,0,0,230,219,1,0,0,0,230,220,1,0,0,0,230,221,1,0,0,0,230,
        222,1,0,0,0,230,223,1,0,0,0,230,224,1,0,0,0,230,225,1,0,0,0,230,
        226,1,0,0,0,230,227,1,0,0,0,230,228,1,0,0,0,230,229,1,0,0,0,231,
        260,1,0,0,0,232,233,10,18,0,0,233,234,5,7,0,0,234,235,3,32,16,0,
        235,236,5,8,0,0,236,237,5,6,0,0,237,238,3,32,16,19,238,259,1,0,0,
        0,239,240,10,16,0,0,240,241,7,1,0,0,241,259,3,32,16,17,242,243,10,
        15,0,0,243,244,7,2,0,0,244,259,3,32,16,16,245,246,10,14,0,0,246,
        247,7,3,0,0,247,259,3,32,16,15,248,249,10,19,0,0,249,250,5,7,0,0,
        250,251,3,32,16,0,251,252,5,8,0,0,252,259,1,0,0,0,253,254,10,17,
        0,0,254,255,5,26,0,0,255,256,3,32,16,0,256,257,5,3,0,0,257,259,1,
        0,0,0,258,232,1,0,0,0,258,239,1,0,0,0,258,242,1,0,0,0,258,245,1,
        0,0,0,258,248,1,0,0,0,258,253,1,0,0,0,259,262,1,0,0,0,260,258,1,
        0,0,0,260,261,1,0,0,0,261,33,1,0,0,0,262,260,1,0,0,0,263,264,5,33,
        0,0,264,265,5,2,0,0,265,266,5,42,0,0,266,267,5,25,0,0,267,268,5,
        42,0,0,268,269,5,3,0,0,269,35,1,0,0,0,270,271,5,34,0,0,271,272,5,
        2,0,0,272,275,3,32,16,0,273,274,5,25,0,0,274,276,3,32,16,0,275,273,
        1,0,0,0,276,277,1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,279,
        1,0,0,0,279,280,5,3,0,0,280,37,1,0,0,0,281,282,5,35,0,0,282,283,
        5,41,0,0,283,284,5,17,0,0,284,285,3,40,20,0,285,286,5,18,0,0,286,
        39,1,0,0,0,287,292,5,41,0,0,288,289,5,25,0,0,289,291,5,41,0,0,290,
        288,1,0,0,0,291,294,1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,
        41,1,0,0,0,294,292,1,0,0,0,295,296,5,41,0,0,296,297,5,36,0,0,297,
        298,5,41,0,0,298,43,1,0,0,0,21,47,60,74,81,93,102,106,121,137,151,
        161,168,177,188,199,210,230,258,260,277,292
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'('", "')'", "';'", "'var'", 
                     "'='", "'['", "']'", "'int'", "'string'", "'bool'", 
                     "'double'", "'date'", "'time'", "'dateTime'", "'if'", 
                     "'{'", "'}'", "'else'", "'for'", "'foreach'", "'in'", 
                     "'while'", "'function'", "','", "'.add('", "'<'", "'<='", 
                     "'>'", "'>='", "'=='", "'!='", "'randomInt'", "'randomChoice'", 
                     "'enum'", "'.'", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PLUS", "MINUS", "MULT", "DIV", "ID", 
                      "INT", "STRING", "DOUBLE", "TRUE", "FALSE", "DATE", 
                      "TIME", "DATETIME", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_printStat = 2
    RULE_varDecl = 3
    RULE_dataType = 4
    RULE_baseType = 5
    RULE_ifStat = 6
    RULE_forLoop = 7
    RULE_foreachLoop = 8
    RULE_whileLoop = 9
    RULE_functionDecl = 10
    RULE_functionCall = 11
    RULE_arrayInit = 12
    RULE_params = 13
    RULE_param = 14
    RULE_args = 15
    RULE_expr = 16
    RULE_randomInt = 17
    RULE_randomChoice = 18
    RULE_enumDecl = 19
    RULE_enumBody = 20
    RULE_enumValue = 21

    ruleNames =  [ "prog", "stat", "printStat", "varDecl", "dataType", "baseType", 
                   "ifStat", "forLoop", "foreachLoop", "whileLoop", "functionDecl", 
                   "functionCall", "arrayInit", "params", "param", "args", 
                   "expr", "randomInt", "randomChoice", "enumDecl", "enumBody", 
                   "enumValue" ]

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
    PLUS=37
    MINUS=38
    MULT=39
    DIV=40
    ID=41
    INT=42
    STRING=43
    DOUBLE=44
    TRUE=45
    FALSE=46
    DATE=47
    TIME=48
    DATETIME=49
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
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.stat()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1123761041637414) != 0)):
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


        def foreachLoop(self):
            return self.getTypedRuleContext(RogueLangParser.ForeachLoopContext,0)


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
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.ifStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.foreachLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.whileLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 55
                self.functionDecl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 56
                self.functionCall()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 57
                self.arrayInit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 58
                self.enumDecl()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 59
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
        self.enterRule(localctx, 4, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(RogueLangParser.T__0)
            self.state = 63
            self.match(RogueLangParser.T__1)
            self.state = 64
            self.expr(0)
            self.state = 65
            self.match(RogueLangParser.T__2)
            self.state = 66
            self.match(RogueLangParser.T__3)
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
            self.state = 68
            self.match(RogueLangParser.T__4)
            self.state = 69
            self.dataType()
            self.state = 70
            self.match(RogueLangParser.ID)
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 71
                self.match(RogueLangParser.T__5)
                self.state = 72
                self.expr(0)
                pass
            elif token in [17]:
                self.state = 73
                self.arrayInit()
                pass
            elif token in [4]:
                pass
            else:
                pass
            self.state = 76
            self.match(RogueLangParser.T__3)
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
        self.enterRule(localctx, 8, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.baseType()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 79
                self.match(RogueLangParser.T__6)
                self.state = 80
                self.match(RogueLangParser.T__7)


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
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023320576) != 0)):
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
        self.enterRule(localctx, 12, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(RogueLangParser.T__15)
            self.state = 86
            self.match(RogueLangParser.T__1)
            self.state = 87
            self.expr(0)
            self.state = 88
            self.match(RogueLangParser.T__2)
            self.state = 89
            self.match(RogueLangParser.T__16)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1123761041637414) != 0):
                self.state = 90
                self.stat()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(RogueLangParser.T__17)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 97
                self.match(RogueLangParser.T__18)
                self.state = 98
                self.match(RogueLangParser.T__16)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1123761041637414) != 0):
                    self.state = 99
                    self.stat()
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 105
                self.match(RogueLangParser.T__17)


            self.state = 108
            self.match(RogueLangParser.T__3)
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


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


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
            self.state = 110
            self.match(RogueLangParser.T__19)
            self.state = 111
            self.match(RogueLangParser.T__1)
            self.state = 112
            self.varDecl()
            self.state = 113
            self.expr(0)
            self.state = 114
            self.match(RogueLangParser.T__3)
            self.state = 115
            self.expr(0)
            self.state = 116
            self.match(RogueLangParser.T__2)
            self.state = 117
            self.match(RogueLangParser.T__16)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1123761041637414) != 0):
                self.state = 118
                self.stat()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(RogueLangParser.T__17)
            self.state = 125
            self.match(RogueLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForeachLoopContext(ParserRuleContext):
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
            return RogueLangParser.RULE_foreachLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeachLoop" ):
                return visitor.visitForeachLoop(self)
            else:
                return visitor.visitChildren(self)




    def foreachLoop(self):

        localctx = RogueLangParser.ForeachLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_foreachLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(RogueLangParser.T__20)
            self.state = 128
            self.match(RogueLangParser.T__1)
            self.state = 129
            self.varDecl()
            self.state = 130
            self.match(RogueLangParser.T__21)
            self.state = 131
            self.expr(0)
            self.state = 132
            self.match(RogueLangParser.T__2)
            self.state = 133
            self.match(RogueLangParser.T__16)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1123761041637414) != 0):
                self.state = 134
                self.stat()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(RogueLangParser.T__17)
            self.state = 141
            self.match(RogueLangParser.T__3)
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
            self.state = 143
            self.match(RogueLangParser.T__22)
            self.state = 144
            self.match(RogueLangParser.T__1)
            self.state = 145
            self.expr(0)
            self.state = 146
            self.match(RogueLangParser.T__2)
            self.state = 147
            self.match(RogueLangParser.T__16)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1123761041637414) != 0):
                self.state = 148
                self.stat()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(RogueLangParser.T__17)
            self.state = 155
            self.match(RogueLangParser.T__3)
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
            self.state = 157
            self.match(RogueLangParser.T__23)
            self.state = 158
            self.match(RogueLangParser.ID)
            self.state = 159
            self.match(RogueLangParser.T__1)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023320576) != 0):
                self.state = 160
                self.params()


            self.state = 163
            self.match(RogueLangParser.T__2)
            self.state = 164
            self.match(RogueLangParser.T__16)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1123761041637414) != 0):
                self.state = 165
                self.stat()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 171
            self.match(RogueLangParser.T__17)
            self.state = 172
            self.match(RogueLangParser.T__3)
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
            self.state = 174
            self.match(RogueLangParser.ID)
            self.state = 175
            self.match(RogueLangParser.T__1)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1123726653390852) != 0):
                self.state = 176
                self.args()


            self.state = 179
            self.match(RogueLangParser.T__2)
            self.state = 180
            self.match(RogueLangParser.T__3)
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
            self.state = 182
            self.match(RogueLangParser.T__16)
            self.state = 183
            self.expr(0)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 184
                self.match(RogueLangParser.T__24)
                self.state = 185
                self.expr(0)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
            self.match(RogueLangParser.T__17)
            self.state = 192
            self.match(RogueLangParser.T__3)
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
        self.enterRule(localctx, 26, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.param()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 195
                self.match(RogueLangParser.T__24)
                self.state = 196
                self.param()
                self.state = 201
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
            self.state = 202
            self.dataType()
            self.state = 203
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
        self.enterRule(localctx, 30, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.expr(0)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 206
                self.match(RogueLangParser.T__24)
                self.state = 207
                self.expr(0)
                self.state = 212
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

        def DATE(self):
            return self.getToken(RogueLangParser.DATE, 0)

        def TIME(self):
            return self.getToken(RogueLangParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(RogueLangParser.DATETIME, 0)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 214
                self.match(RogueLangParser.T__1)
                self.state = 215
                self.expr(0)
                self.state = 216
                self.match(RogueLangParser.T__2)
                pass

            elif la_ == 2:
                self.state = 218
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 3:
                self.state = 219
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 4:
                self.state = 220
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 5:
                self.state = 221
                self.match(RogueLangParser.DOUBLE)
                pass

            elif la_ == 6:
                self.state = 222
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 7:
                self.state = 223
                self.match(RogueLangParser.FALSE)
                pass

            elif la_ == 8:
                self.state = 224
                self.match(RogueLangParser.DATE)
                pass

            elif la_ == 9:
                self.state = 225
                self.match(RogueLangParser.TIME)
                pass

            elif la_ == 10:
                self.state = 226
                self.match(RogueLangParser.DATETIME)
                pass

            elif la_ == 11:
                self.state = 227
                self.randomInt()
                pass

            elif la_ == 12:
                self.state = 228
                self.randomChoice()
                pass

            elif la_ == 13:
                self.state = 229
                self.enumValue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 258
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 232
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 233
                        self.match(RogueLangParser.T__6)
                        self.state = 234
                        self.expr(0)
                        self.state = 235
                        self.match(RogueLangParser.T__7)
                        self.state = 236
                        self.match(RogueLangParser.T__5)
                        self.state = 237
                        self.expr(19)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 239
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 240
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==39 or _la==40):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 241
                        self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 242
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 243
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==37 or _la==38):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 244
                        self.expr(16)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 245
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 246
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8455716864) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 247
                        self.expr(15)
                        pass

                    elif la_ == 5:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 248
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 249
                        self.match(RogueLangParser.T__6)
                        self.state = 250
                        self.expr(0)
                        self.state = 251
                        self.match(RogueLangParser.T__7)
                        pass

                    elif la_ == 6:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 253
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 254
                        self.match(RogueLangParser.T__25)
                        self.state = 255
                        self.expr(0)
                        self.state = 256
                        self.match(RogueLangParser.T__2)
                        pass

             
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 263
            self.match(RogueLangParser.T__32)
            self.state = 264
            self.match(RogueLangParser.T__1)
            self.state = 265
            self.match(RogueLangParser.INT)
            self.state = 266
            self.match(RogueLangParser.T__24)
            self.state = 267
            self.match(RogueLangParser.INT)
            self.state = 268
            self.match(RogueLangParser.T__2)
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
            self.state = 270
            self.match(RogueLangParser.T__33)
            self.state = 271
            self.match(RogueLangParser.T__1)
            self.state = 272
            self.expr(0)
            self.state = 275 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 273
                self.match(RogueLangParser.T__24)
                self.state = 274
                self.expr(0)
                self.state = 277 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 279
            self.match(RogueLangParser.T__2)
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
            self.state = 281
            self.match(RogueLangParser.T__34)
            self.state = 282
            self.match(RogueLangParser.ID)
            self.state = 283
            self.match(RogueLangParser.T__16)
            self.state = 284
            self.enumBody()
            self.state = 285
            self.match(RogueLangParser.T__17)
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
            self.state = 287
            self.match(RogueLangParser.ID)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 288
                self.match(RogueLangParser.T__24)
                self.state = 289
                self.match(RogueLangParser.ID)
                self.state = 294
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
            self.state = 295
            self.match(RogueLangParser.ID)
            self.state = 296
            self.match(RogueLangParser.T__35)
            self.state = 297
            self.match(RogueLangParser.ID)
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
        self._predicates[16] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 17)
         




