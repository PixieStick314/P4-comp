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
        4,1,50,303,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,4,0,46,8,0,11,0,12,0,47,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,60,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,3,3,74,8,3,1,3,1,3,1,4,1,4,1,4,3,4,81,8,4,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,5,6,91,8,6,10,6,12,6,94,9,6,1,6,1,6,1,6,1,
        6,5,6,100,8,6,10,6,12,6,103,9,6,1,6,3,6,106,8,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,119,8,7,10,7,12,7,122,9,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,135,8,8,10,8,12,8,138,
        9,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,149,8,9,10,9,12,9,152,
        9,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,161,8,10,1,10,1,10,1,10,
        5,10,166,8,10,10,10,12,10,169,9,10,1,10,1,10,1,10,1,11,1,11,1,11,
        3,11,177,8,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,186,8,12,10,
        12,12,12,189,9,12,1,12,1,12,1,12,1,12,1,12,3,12,196,8,12,1,13,1,
        13,1,13,5,13,201,8,13,10,13,12,13,204,9,13,1,14,1,14,1,14,1,15,1,
        15,1,15,5,15,212,8,15,10,15,12,15,215,9,15,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,
        16,234,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,5,16,262,8,16,10,16,12,16,265,9,16,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,4,18,279,8,18,11,18,12,
        18,280,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,5,
        20,294,8,20,10,20,12,20,297,9,20,1,21,1,21,1,21,1,21,1,21,0,1,32,
        22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        0,4,2,0,9,15,41,41,1,0,27,28,1,0,29,30,1,0,31,36,326,0,45,1,0,0,
        0,2,59,1,0,0,0,4,61,1,0,0,0,6,67,1,0,0,0,8,77,1,0,0,0,10,82,1,0,
        0,0,12,84,1,0,0,0,14,109,1,0,0,0,16,126,1,0,0,0,18,142,1,0,0,0,20,
        156,1,0,0,0,22,173,1,0,0,0,24,195,1,0,0,0,26,197,1,0,0,0,28,205,
        1,0,0,0,30,208,1,0,0,0,32,233,1,0,0,0,34,266,1,0,0,0,36,273,1,0,
        0,0,38,284,1,0,0,0,40,290,1,0,0,0,42,298,1,0,0,0,44,46,3,2,1,0,45,
        44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,1,1,0,0,
        0,49,60,3,4,2,0,50,60,3,6,3,0,51,60,3,12,6,0,52,60,3,14,7,0,53,60,
        3,16,8,0,54,60,3,18,9,0,55,60,3,20,10,0,56,60,3,22,11,0,57,60,3,
        38,19,0,58,60,3,32,16,0,59,49,1,0,0,0,59,50,1,0,0,0,59,51,1,0,0,
        0,59,52,1,0,0,0,59,53,1,0,0,0,59,54,1,0,0,0,59,55,1,0,0,0,59,56,
        1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,3,1,0,0,0,61,62,5,1,0,0,62,
        63,5,2,0,0,63,64,3,32,16,0,64,65,5,3,0,0,65,66,5,4,0,0,66,5,1,0,
        0,0,67,68,5,5,0,0,68,69,3,8,4,0,69,73,5,41,0,0,70,71,5,6,0,0,71,
        74,3,32,16,0,72,74,3,24,12,0,73,70,1,0,0,0,73,72,1,0,0,0,73,74,1,
        0,0,0,74,75,1,0,0,0,75,76,5,4,0,0,76,7,1,0,0,0,77,80,3,10,5,0,78,
        79,5,7,0,0,79,81,5,8,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,9,1,0,0,
        0,82,83,7,0,0,0,83,11,1,0,0,0,84,85,5,16,0,0,85,86,5,2,0,0,86,87,
        3,32,16,0,87,88,5,3,0,0,88,92,5,17,0,0,89,91,3,2,1,0,90,89,1,0,0,
        0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,
        1,0,0,0,95,105,5,18,0,0,96,97,5,19,0,0,97,101,5,17,0,0,98,100,3,
        2,1,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,
        0,102,104,1,0,0,0,103,101,1,0,0,0,104,106,5,18,0,0,105,96,1,0,0,
        0,105,106,1,0,0,0,106,107,1,0,0,0,107,108,5,4,0,0,108,13,1,0,0,0,
        109,110,5,20,0,0,110,111,5,2,0,0,111,112,3,6,3,0,112,113,3,32,16,
        0,113,114,5,4,0,0,114,115,3,32,16,0,115,116,5,3,0,0,116,120,5,17,
        0,0,117,119,3,2,1,0,118,117,1,0,0,0,119,122,1,0,0,0,120,118,1,0,
        0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,120,1,0,0,0,123,124,5,18,
        0,0,124,125,5,4,0,0,125,15,1,0,0,0,126,127,5,21,0,0,127,128,5,2,
        0,0,128,129,3,6,3,0,129,130,5,22,0,0,130,131,3,32,16,0,131,132,5,
        3,0,0,132,136,5,17,0,0,133,135,3,2,1,0,134,133,1,0,0,0,135,138,1,
        0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,136,1,
        0,0,0,139,140,5,18,0,0,140,141,5,4,0,0,141,17,1,0,0,0,142,143,5,
        23,0,0,143,144,5,2,0,0,144,145,3,32,16,0,145,146,5,3,0,0,146,150,
        5,17,0,0,147,149,3,2,1,0,148,147,1,0,0,0,149,152,1,0,0,0,150,148,
        1,0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,150,1,0,0,0,153,154,
        5,18,0,0,154,155,5,4,0,0,155,19,1,0,0,0,156,157,5,24,0,0,157,158,
        5,41,0,0,158,160,5,2,0,0,159,161,3,26,13,0,160,159,1,0,0,0,160,161,
        1,0,0,0,161,162,1,0,0,0,162,163,5,3,0,0,163,167,5,17,0,0,164,166,
        3,2,1,0,165,164,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,
        1,0,0,0,168,170,1,0,0,0,169,167,1,0,0,0,170,171,5,18,0,0,171,172,
        5,4,0,0,172,21,1,0,0,0,173,174,5,41,0,0,174,176,5,2,0,0,175,177,
        3,30,15,0,176,175,1,0,0,0,176,177,1,0,0,0,177,178,1,0,0,0,178,179,
        5,3,0,0,179,180,5,4,0,0,180,23,1,0,0,0,181,182,5,17,0,0,182,187,
        3,32,16,0,183,184,5,25,0,0,184,186,3,32,16,0,185,183,1,0,0,0,186,
        189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,
        187,1,0,0,0,190,191,5,18,0,0,191,192,5,4,0,0,192,196,1,0,0,0,193,
        194,5,7,0,0,194,196,5,8,0,0,195,181,1,0,0,0,195,193,1,0,0,0,196,
        25,1,0,0,0,197,202,3,28,14,0,198,199,5,25,0,0,199,201,3,28,14,0,
        200,198,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,
        203,27,1,0,0,0,204,202,1,0,0,0,205,206,3,8,4,0,206,207,5,41,0,0,
        207,29,1,0,0,0,208,213,3,32,16,0,209,210,5,25,0,0,210,212,3,32,16,
        0,211,209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,
        0,214,31,1,0,0,0,215,213,1,0,0,0,216,217,6,16,-1,0,217,218,5,2,0,
        0,218,219,3,32,16,0,219,220,5,3,0,0,220,234,1,0,0,0,221,234,5,41,
        0,0,222,234,5,42,0,0,223,234,5,43,0,0,224,234,5,44,0,0,225,234,5,
        45,0,0,226,234,5,46,0,0,227,234,5,47,0,0,228,234,5,48,0,0,229,234,
        5,49,0,0,230,234,3,34,17,0,231,234,3,36,18,0,232,234,3,42,21,0,233,
        216,1,0,0,0,233,221,1,0,0,0,233,222,1,0,0,0,233,223,1,0,0,0,233,
        224,1,0,0,0,233,225,1,0,0,0,233,226,1,0,0,0,233,227,1,0,0,0,233,
        228,1,0,0,0,233,229,1,0,0,0,233,230,1,0,0,0,233,231,1,0,0,0,233,
        232,1,0,0,0,234,263,1,0,0,0,235,236,10,18,0,0,236,237,5,7,0,0,237,
        238,3,32,16,0,238,239,5,8,0,0,239,240,5,6,0,0,240,241,3,32,16,19,
        241,262,1,0,0,0,242,243,10,16,0,0,243,244,7,1,0,0,244,262,3,32,16,
        17,245,246,10,15,0,0,246,247,7,2,0,0,247,262,3,32,16,16,248,249,
        10,14,0,0,249,250,7,3,0,0,250,262,3,32,16,15,251,252,10,19,0,0,252,
        253,5,7,0,0,253,254,3,32,16,0,254,255,5,8,0,0,255,262,1,0,0,0,256,
        257,10,17,0,0,257,258,5,26,0,0,258,259,3,32,16,0,259,260,5,3,0,0,
        260,262,1,0,0,0,261,235,1,0,0,0,261,242,1,0,0,0,261,245,1,0,0,0,
        261,248,1,0,0,0,261,251,1,0,0,0,261,256,1,0,0,0,262,265,1,0,0,0,
        263,261,1,0,0,0,263,264,1,0,0,0,264,33,1,0,0,0,265,263,1,0,0,0,266,
        267,5,37,0,0,267,268,5,2,0,0,268,269,5,42,0,0,269,270,5,25,0,0,270,
        271,5,42,0,0,271,272,5,3,0,0,272,35,1,0,0,0,273,274,5,38,0,0,274,
        275,5,2,0,0,275,278,3,32,16,0,276,277,5,25,0,0,277,279,3,32,16,0,
        278,276,1,0,0,0,279,280,1,0,0,0,280,278,1,0,0,0,280,281,1,0,0,0,
        281,282,1,0,0,0,282,283,5,3,0,0,283,37,1,0,0,0,284,285,5,39,0,0,
        285,286,5,41,0,0,286,287,5,17,0,0,287,288,3,40,20,0,288,289,5,18,
        0,0,289,39,1,0,0,0,290,295,5,41,0,0,291,292,5,25,0,0,292,294,5,41,
        0,0,293,291,1,0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,295,296,1,0,
        0,0,296,41,1,0,0,0,297,295,1,0,0,0,298,299,5,41,0,0,299,300,5,40,
        0,0,300,301,5,41,0,0,301,43,1,0,0,0,22,47,59,73,80,92,101,105,120,
        136,150,160,167,176,187,195,202,213,233,261,263,280,295
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
                     "'while'", "'function'", "','", "'.add('", "'*'", "'/'", 
                     "'+'", "'-'", "'<'", "'<='", "'>'", "'>='", "'=='", 
                     "'!='", "'randomInt'", "'randomChoice'", "'enum'", 
                     "'.'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "STRING", "DOUBLE", "TRUE", 
                      "FALSE", "DATE", "TIME", "DATETIME", "WS" ]

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
    T__36=37
    T__37=38
    T__38=39
    T__39=40
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1124662984638502) != 0)):
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
            self.state = 59
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
                self.enumDecl()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 58
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
            self.state = 61
            self.match(RogueLangParser.T__0)
            self.state = 62
            self.match(RogueLangParser.T__1)
            self.state = 63
            self.expr(0)
            self.state = 64
            self.match(RogueLangParser.T__2)
            self.state = 65
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
            self.state = 67
            self.match(RogueLangParser.T__4)
            self.state = 68
            self.dataType()
            self.state = 69
            self.match(RogueLangParser.ID)
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 70
                self.match(RogueLangParser.T__5)
                self.state = 71
                self.expr(0)
                pass
            elif token in [7, 17]:
                self.state = 72
                self.arrayInit()
                pass
            elif token in [4]:
                pass
            else:
                pass
            self.state = 75
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
            self.state = 77
            self.baseType()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 78
                self.match(RogueLangParser.T__6)
                self.state = 79
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
            self.state = 82
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
            self.state = 84
            self.match(RogueLangParser.T__15)
            self.state = 85
            self.match(RogueLangParser.T__1)
            self.state = 86
            self.expr(0)
            self.state = 87
            self.match(RogueLangParser.T__2)
            self.state = 88
            self.match(RogueLangParser.T__16)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1124662984638502) != 0):
                self.state = 89
                self.stat()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(RogueLangParser.T__17)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 96
                self.match(RogueLangParser.T__18)
                self.state = 97
                self.match(RogueLangParser.T__16)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1124662984638502) != 0):
                    self.state = 98
                    self.stat()
                    self.state = 103
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 104
                self.match(RogueLangParser.T__17)


            self.state = 107
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
            self.state = 109
            self.match(RogueLangParser.T__19)
            self.state = 110
            self.match(RogueLangParser.T__1)
            self.state = 111
            self.varDecl()
            self.state = 112
            self.expr(0)
            self.state = 113
            self.match(RogueLangParser.T__3)
            self.state = 114
            self.expr(0)
            self.state = 115
            self.match(RogueLangParser.T__2)
            self.state = 116
            self.match(RogueLangParser.T__16)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1124662984638502) != 0):
                self.state = 117
                self.stat()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(RogueLangParser.T__17)
            self.state = 124
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
            self.state = 126
            self.match(RogueLangParser.T__20)
            self.state = 127
            self.match(RogueLangParser.T__1)
            self.state = 128
            self.varDecl()
            self.state = 129
            self.match(RogueLangParser.T__21)
            self.state = 130
            self.expr(0)
            self.state = 131
            self.match(RogueLangParser.T__2)
            self.state = 132
            self.match(RogueLangParser.T__16)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1124662984638502) != 0):
                self.state = 133
                self.stat()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self.match(RogueLangParser.T__17)
            self.state = 140
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
            self.state = 142
            self.match(RogueLangParser.T__22)
            self.state = 143
            self.match(RogueLangParser.T__1)
            self.state = 144
            self.expr(0)
            self.state = 145
            self.match(RogueLangParser.T__2)
            self.state = 146
            self.match(RogueLangParser.T__16)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1124662984638502) != 0):
                self.state = 147
                self.stat()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.match(RogueLangParser.T__17)
            self.state = 154
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
            self.state = 156
            self.match(RogueLangParser.T__23)
            self.state = 157
            self.match(RogueLangParser.ID)
            self.state = 158
            self.match(RogueLangParser.T__1)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023320576) != 0):
                self.state = 159
                self.params()


            self.state = 162
            self.match(RogueLangParser.T__2)
            self.state = 163
            self.match(RogueLangParser.T__16)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1124662984638502) != 0):
                self.state = 164
                self.stat()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(RogueLangParser.T__17)
            self.state = 171
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
            self.state = 173
            self.match(RogueLangParser.ID)
            self.state = 174
            self.match(RogueLangParser.T__1)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1124113200447492) != 0):
                self.state = 175
                self.args()


            self.state = 178
            self.match(RogueLangParser.T__2)
            self.state = 179
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
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(RogueLangParser.T__16)
                self.state = 182
                self.expr(0)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 183
                    self.match(RogueLangParser.T__24)
                    self.state = 184
                    self.expr(0)
                    self.state = 189
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 190
                self.match(RogueLangParser.T__17)
                self.state = 191
                self.match(RogueLangParser.T__3)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(RogueLangParser.T__6)
                self.state = 194
                self.match(RogueLangParser.T__7)
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
            self.state = 197
            self.param()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 198
                self.match(RogueLangParser.T__24)
                self.state = 199
                self.param()
                self.state = 204
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
            self.state = 205
            self.dataType()
            self.state = 206
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
            self.state = 208
            self.expr(0)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 209
                self.match(RogueLangParser.T__24)
                self.state = 210
                self.expr(0)
                self.state = 215
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
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 217
                self.match(RogueLangParser.T__1)
                self.state = 218
                self.expr(0)
                self.state = 219
                self.match(RogueLangParser.T__2)
                pass

            elif la_ == 2:
                self.state = 221
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 3:
                self.state = 222
                self.match(RogueLangParser.INT)
                pass

            elif la_ == 4:
                self.state = 223
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 5:
                self.state = 224
                self.match(RogueLangParser.DOUBLE)
                pass

            elif la_ == 6:
                self.state = 225
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 7:
                self.state = 226
                self.match(RogueLangParser.FALSE)
                pass

            elif la_ == 8:
                self.state = 227
                self.match(RogueLangParser.DATE)
                pass

            elif la_ == 9:
                self.state = 228
                self.match(RogueLangParser.TIME)
                pass

            elif la_ == 10:
                self.state = 229
                self.match(RogueLangParser.DATETIME)
                pass

            elif la_ == 11:
                self.state = 230
                self.randomInt()
                pass

            elif la_ == 12:
                self.state = 231
                self.randomChoice()
                pass

            elif la_ == 13:
                self.state = 232
                self.enumValue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 261
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 235
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 236
                        self.match(RogueLangParser.T__6)
                        self.state = 237
                        self.expr(0)
                        self.state = 238
                        self.match(RogueLangParser.T__7)
                        self.state = 239
                        self.match(RogueLangParser.T__5)
                        self.state = 240
                        self.expr(19)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 242
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 243
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 244
                        self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 245
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 246
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==30):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 247
                        self.expr(16)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 248
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 249
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135291469824) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 250
                        self.expr(15)
                        pass

                    elif la_ == 5:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 251
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 252
                        self.match(RogueLangParser.T__6)
                        self.state = 253
                        self.expr(0)
                        self.state = 254
                        self.match(RogueLangParser.T__7)
                        pass

                    elif la_ == 6:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 256
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 257
                        self.match(RogueLangParser.T__25)
                        self.state = 258
                        self.expr(0)
                        self.state = 259
                        self.match(RogueLangParser.T__2)
                        pass

             
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.state = 266
            self.match(RogueLangParser.T__36)
            self.state = 267
            self.match(RogueLangParser.T__1)
            self.state = 268
            self.match(RogueLangParser.INT)
            self.state = 269
            self.match(RogueLangParser.T__24)
            self.state = 270
            self.match(RogueLangParser.INT)
            self.state = 271
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
            self.state = 273
            self.match(RogueLangParser.T__37)
            self.state = 274
            self.match(RogueLangParser.T__1)
            self.state = 275
            self.expr(0)
            self.state = 278 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 276
                self.match(RogueLangParser.T__24)
                self.state = 277
                self.expr(0)
                self.state = 280 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 282
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
            self.state = 284
            self.match(RogueLangParser.T__38)
            self.state = 285
            self.match(RogueLangParser.ID)
            self.state = 286
            self.match(RogueLangParser.T__16)
            self.state = 287
            self.enumBody()
            self.state = 288
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
            self.state = 290
            self.match(RogueLangParser.ID)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 291
                self.match(RogueLangParser.T__24)
                self.state = 292
                self.match(RogueLangParser.ID)
                self.state = 297
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
            self.state = 298
            self.match(RogueLangParser.ID)
            self.state = 299
            self.match(RogueLangParser.T__39)
            self.state = 300
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
         




