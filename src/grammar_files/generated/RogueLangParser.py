# Generated from C://Users//Muffin//Documents//GitHub//P4-comp//src//grammar_files//RogueLang.g4 by ANTLR 4.13.1
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
        4,1,43,228,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,4,0,36,8,0,11,0,12,0,37,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,49,8,1,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,3,3,61,8,3,1,4,1,4,1,4,3,4,66,8,4,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,81,8,6,10,6,12,6,84,9,
        6,1,6,1,6,3,6,88,8,6,1,7,1,7,5,7,92,8,7,10,7,12,7,95,9,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,8,1,8,5,8,105,8,8,10,8,12,8,108,9,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,5,9,118,8,9,10,9,12,9,121,9,9,1,9,1,9,1,10,
        1,10,1,10,1,10,3,10,129,8,10,1,10,1,10,1,10,5,10,134,8,10,10,10,
        12,10,137,9,10,1,10,1,10,1,11,1,11,1,11,3,11,144,8,11,1,11,1,11,
        1,12,1,12,1,12,1,12,5,12,152,8,12,10,12,12,12,155,9,12,1,12,1,12,
        1,13,1,13,1,13,5,13,162,8,13,10,13,12,13,165,9,13,1,14,1,14,1,15,
        1,15,1,15,5,15,172,8,15,10,15,12,15,175,9,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,190,8,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,5,16,223,8,16,10,16,12,16,226,9,16,1,16,0,1,
        32,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,5,3,0,1,3,
        28,29,33,33,2,0,16,17,24,24,1,0,14,15,1,0,18,23,1,0,25,26,248,0,
        35,1,0,0,0,2,48,1,0,0,0,4,50,1,0,0,0,6,55,1,0,0,0,8,62,1,0,0,0,10,
        67,1,0,0,0,12,69,1,0,0,0,14,89,1,0,0,0,16,98,1,0,0,0,18,111,1,0,
        0,0,20,124,1,0,0,0,22,140,1,0,0,0,24,147,1,0,0,0,26,158,1,0,0,0,
        28,166,1,0,0,0,30,168,1,0,0,0,32,189,1,0,0,0,34,36,3,2,1,0,35,34,
        1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,1,1,0,0,0,39,
        49,3,4,2,0,40,49,3,6,3,0,41,49,3,12,6,0,42,49,3,16,8,0,43,49,3,18,
        9,0,44,49,3,20,10,0,45,49,3,22,11,0,46,49,3,24,12,0,47,49,3,32,16,
        0,48,39,1,0,0,0,48,40,1,0,0,0,48,41,1,0,0,0,48,42,1,0,0,0,48,43,
        1,0,0,0,48,44,1,0,0,0,48,45,1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,
        49,3,1,0,0,0,50,51,5,9,0,0,51,52,5,34,0,0,52,53,3,32,16,0,53,54,
        5,35,0,0,54,5,1,0,0,0,55,60,5,33,0,0,56,57,5,42,0,0,57,61,3,32,16,
        0,58,61,3,24,12,0,59,61,3,30,15,0,60,56,1,0,0,0,60,58,1,0,0,0,60,
        59,1,0,0,0,60,61,1,0,0,0,61,7,1,0,0,0,62,65,3,10,5,0,63,64,5,36,
        0,0,64,66,5,37,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,9,1,0,0,0,67,68,
        7,0,0,0,68,11,1,0,0,0,69,70,5,5,0,0,70,71,5,34,0,0,71,72,3,32,16,
        0,72,73,5,35,0,0,73,82,3,14,7,0,74,75,5,6,0,0,75,76,5,34,0,0,76,
        77,3,32,16,0,77,78,5,35,0,0,78,79,3,14,7,0,79,81,1,0,0,0,80,74,1,
        0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,87,1,0,0,0,84,
        82,1,0,0,0,85,86,5,7,0,0,86,88,3,14,7,0,87,85,1,0,0,0,87,88,1,0,
        0,0,88,13,1,0,0,0,89,93,5,38,0,0,90,92,3,2,1,0,91,90,1,0,0,0,92,
        95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,
        0,96,97,5,39,0,0,97,15,1,0,0,0,98,99,5,10,0,0,99,100,3,6,3,0,100,
        101,5,11,0,0,101,102,3,32,16,0,102,106,5,38,0,0,103,105,3,2,1,0,
        104,103,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,
        107,109,1,0,0,0,108,106,1,0,0,0,109,110,5,39,0,0,110,17,1,0,0,0,
        111,112,5,12,0,0,112,113,5,34,0,0,113,114,3,32,16,0,114,115,5,35,
        0,0,115,119,5,38,0,0,116,118,3,2,1,0,117,116,1,0,0,0,118,121,1,0,
        0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,119,1,0,
        0,0,122,123,5,39,0,0,123,19,1,0,0,0,124,125,5,13,0,0,125,126,5,33,
        0,0,126,128,5,34,0,0,127,129,3,26,13,0,128,127,1,0,0,0,128,129,1,
        0,0,0,129,130,1,0,0,0,130,131,5,35,0,0,131,135,5,38,0,0,132,134,
        3,2,1,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,
        1,0,0,0,136,138,1,0,0,0,137,135,1,0,0,0,138,139,5,39,0,0,139,21,
        1,0,0,0,140,141,5,33,0,0,141,143,5,34,0,0,142,144,3,30,15,0,143,
        142,1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,146,5,35,0,0,146,
        23,1,0,0,0,147,148,5,38,0,0,148,153,3,32,16,0,149,150,5,40,0,0,150,
        152,3,32,16,0,151,149,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,
        154,1,0,0,0,154,156,1,0,0,0,155,153,1,0,0,0,156,157,5,39,0,0,157,
        25,1,0,0,0,158,163,3,28,14,0,159,160,5,40,0,0,160,162,3,28,14,0,
        161,159,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,
        164,27,1,0,0,0,165,163,1,0,0,0,166,167,5,33,0,0,167,29,1,0,0,0,168,
        173,3,32,16,0,169,170,5,40,0,0,170,172,3,32,16,0,171,169,1,0,0,0,
        172,175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,31,1,0,0,0,175,
        173,1,0,0,0,176,177,6,16,-1,0,177,190,3,22,11,0,178,179,5,27,0,0,
        179,190,3,32,16,7,180,181,5,34,0,0,181,182,3,32,16,0,182,183,5,35,
        0,0,183,190,1,0,0,0,184,190,5,33,0,0,185,190,5,32,0,0,186,190,5,
        31,0,0,187,190,5,28,0,0,188,190,5,29,0,0,189,176,1,0,0,0,189,178,
        1,0,0,0,189,180,1,0,0,0,189,184,1,0,0,0,189,185,1,0,0,0,189,186,
        1,0,0,0,189,187,1,0,0,0,189,188,1,0,0,0,190,224,1,0,0,0,191,192,
        10,13,0,0,192,193,5,36,0,0,193,194,3,32,16,0,194,195,5,37,0,0,195,
        196,5,42,0,0,196,197,3,32,16,14,197,223,1,0,0,0,198,199,10,11,0,
        0,199,200,7,1,0,0,200,223,3,32,16,12,201,202,10,10,0,0,202,203,7,
        2,0,0,203,223,3,32,16,11,204,205,10,9,0,0,205,206,7,3,0,0,206,223,
        3,32,16,10,207,208,10,8,0,0,208,209,7,4,0,0,209,223,3,32,16,9,210,
        211,10,14,0,0,211,212,5,36,0,0,212,213,3,32,16,0,213,214,5,37,0,
        0,214,223,1,0,0,0,215,216,10,12,0,0,216,217,5,41,0,0,217,218,5,4,
        0,0,218,219,5,34,0,0,219,220,3,32,16,0,220,221,5,35,0,0,221,223,
        1,0,0,0,222,191,1,0,0,0,222,198,1,0,0,0,222,201,1,0,0,0,222,204,
        1,0,0,0,222,207,1,0,0,0,222,210,1,0,0,0,222,215,1,0,0,0,223,226,
        1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,33,1,0,0,0,226,224,1,
        0,0,0,18,37,48,60,65,82,87,93,106,119,128,135,143,153,163,173,189,
        222,224
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'string'", "'bool'", "'number'", "'add'", 
                     "'if'", "'elif'", "'else'", "'return'", "'print'", 
                     "'for'", "'in'", "'while'", "'def'", "'+'", "'-'", 
                     "'*'", "'/'", "'>'", "'>='", "'<'", "'<='", "'=='", 
                     "'!='", "'%'", "'and'", "'or'", "'not'", "'True'", 
                     "'False'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'.'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IF", "ELIF", "ELSE", "RETURN", "PRINT", 
                      "FOR", "IN", "WHILE", "DEF", "PLUS", "MINUS", "MULT", 
                      "DIV", "GT", "GTE", "LT", "LTE", "EQ", "NEQ", "MOD", 
                      "AND", "OR", "NOT", "TRUE", "FALSE", "COMMENT_SINGLELINE", 
                      "NUMBER", "STRING", "ID", "OPEN_PARENTH", "CLOSED_PARENTH", 
                      "OPEN_BRACK", "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", 
                      "COMMA", "DOT", "EQUAL_SIGN", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_printStat = 2
    RULE_varDecl = 3
    RULE_dataType = 4
    RULE_baseType = 5
    RULE_ifStat = 6
    RULE_statBlock = 7
    RULE_forLoop = 8
    RULE_whileLoop = 9
    RULE_functionDecl = 10
    RULE_functionCall = 11
    RULE_arrayInit = 12
    RULE_params = 13
    RULE_param = 14
    RULE_args = 15
    RULE_expr = 16

    ruleNames =  [ "prog", "stat", "printStat", "varDecl", "dataType", "baseType", 
                   "ifStat", "statBlock", "forLoop", "whileLoop", "functionDecl", 
                   "functionCall", "arrayInit", "params", "param", "args", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    IF=5
    ELIF=6
    ELSE=7
    RETURN=8
    PRINT=9
    FOR=10
    IN=11
    WHILE=12
    DEF=13
    PLUS=14
    MINUS=15
    MULT=16
    DIV=17
    GT=18
    GTE=19
    LT=20
    LTE=21
    EQ=22
    NEQ=23
    MOD=24
    AND=25
    OR=26
    NOT=27
    TRUE=28
    FALSE=29
    COMMENT_SINGLELINE=30
    NUMBER=31
    STRING=32
    ID=33
    OPEN_PARENTH=34
    CLOSED_PARENTH=35
    OPEN_BRACK=36
    CLOSED_BRACK=37
    OPEN_CURL=38
    CLOSED_CURL=39
    COMMA=40
    DOT=41
    EQUAL_SIGN=42
    WS=43

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
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.stat()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 308029699616) != 0)):
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
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.ifStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 44
                self.functionDecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 45
                self.functionCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 46
                self.arrayInit()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 47
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
        self.enterRule(localctx, 4, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(RogueLangParser.PRINT)
            self.state = 51
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 52
            self.expr(0)
            self.state = 53
            self.match(RogueLangParser.CLOSED_PARENTH)
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

        def EQUAL_SIGN(self):
            return self.getToken(RogueLangParser.EQUAL_SIGN, 0)

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
            self.state = 55
            self.match(RogueLangParser.ID)
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 56
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 57
                self.expr(0)

            elif la_ == 2:
                self.state = 58
                self.arrayInit()

            elif la_ == 3:
                self.state = 59
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


        def OPEN_BRACK(self):
            return self.getToken(RogueLangParser.OPEN_BRACK, 0)

        def CLOSED_BRACK(self):
            return self.getToken(RogueLangParser.CLOSED_BRACK, 0)

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
            self.state = 62
            self.baseType()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 63
                self.match(RogueLangParser.OPEN_BRACK)
                self.state = 64
                self.match(RogueLangParser.CLOSED_BRACK)


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
            self.state = 67
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9395240974) != 0)):
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

        def OPEN_PARENTH(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.OPEN_PARENTH)
            else:
                return self.getToken(RogueLangParser.OPEN_PARENTH, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def CLOSED_PARENTH(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.CLOSED_PARENTH)
            else:
                return self.getToken(RogueLangParser.CLOSED_PARENTH, i)

        def statBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.StatBlockContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.StatBlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.ELIF)
            else:
                return self.getToken(RogueLangParser.ELIF, i)

        def ELSE(self):
            return self.getToken(RogueLangParser.ELSE, 0)

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
            self.state = 69
            self.match(RogueLangParser.IF)
            self.state = 70
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 71
            self.expr(0)
            self.state = 72
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 73
            self.statBlock()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 74
                self.match(RogueLangParser.ELIF)
                self.state = 75
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 76
                self.expr(0)
                self.state = 77
                self.match(RogueLangParser.CLOSED_PARENTH)
                self.state = 78
                self.statBlock()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 85
                self.match(RogueLangParser.ELSE)
                self.state = 86
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
        self.enterRule(localctx, 14, self.RULE_statBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 308029699616) != 0):
                self.state = 90
                self.stat()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
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

        def varDecl(self):
            return self.getTypedRuleContext(RogueLangParser.VarDeclContext,0)


        def IN(self):
            return self.getToken(RogueLangParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


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
            self.state = 98
            self.match(RogueLangParser.FOR)
            self.state = 99
            self.varDecl()
            self.state = 100
            self.match(RogueLangParser.IN)
            self.state = 101
            self.expr(0)
            self.state = 102
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 308029699616) != 0):
                self.state = 103
                self.stat()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(RogueLangParser.CLOSED_CURL)
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
            self.state = 111
            self.match(RogueLangParser.WHILE)
            self.state = 112
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 113
            self.expr(0)
            self.state = 114
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 115
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 308029699616) != 0):
                self.state = 116
                self.stat()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(RogueLangParser.CLOSED_CURL)
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

        def OPEN_CURL(self):
            return self.getToken(RogueLangParser.OPEN_CURL, 0)

        def CLOSED_CURL(self):
            return self.getToken(RogueLangParser.CLOSED_CURL, 0)

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
            self.state = 124
            self.match(RogueLangParser.DEF)
            self.state = 125
            self.match(RogueLangParser.ID)
            self.state = 126
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 127
                self.params()


            self.state = 130
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 131
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 308029699616) != 0):
                self.state = 132
                self.stat()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.match(RogueLangParser.CLOSED_CURL)
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
            self.state = 140
            self.match(RogueLangParser.ID)
            self.state = 141
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 33151778816) != 0):
                self.state = 142
                self.args()


            self.state = 145
            self.match(RogueLangParser.CLOSED_PARENTH)
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

        def OPEN_CURL(self):
            return self.getToken(RogueLangParser.OPEN_CURL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def CLOSED_CURL(self):
            return self.getToken(RogueLangParser.CLOSED_CURL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RogueLangParser.COMMA)
            else:
                return self.getToken(RogueLangParser.COMMA, i)

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
            self.state = 147
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 148
            self.expr(0)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 149
                self.match(RogueLangParser.COMMA)
                self.state = 150
                self.expr(0)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.match(RogueLangParser.CLOSED_CURL)
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
        self.enterRule(localctx, 26, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.param()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 159
                self.match(RogueLangParser.COMMA)
                self.state = 160
                self.param()
                self.state = 165
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
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
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
        self.enterRule(localctx, 30, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.expr(0)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 169
                self.match(RogueLangParser.COMMA)
                self.state = 170
                self.expr(0)
                self.state = 175
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


        def NOT(self):
            return self.getToken(RogueLangParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RogueLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RogueLangParser.ExprContext,i)


        def OPEN_PARENTH(self):
            return self.getToken(RogueLangParser.OPEN_PARENTH, 0)

        def CLOSED_PARENTH(self):
            return self.getToken(RogueLangParser.CLOSED_PARENTH, 0)

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

        def OPEN_BRACK(self):
            return self.getToken(RogueLangParser.OPEN_BRACK, 0)

        def CLOSED_BRACK(self):
            return self.getToken(RogueLangParser.CLOSED_BRACK, 0)

        def EQUAL_SIGN(self):
            return self.getToken(RogueLangParser.EQUAL_SIGN, 0)

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

        def DOT(self):
            return self.getToken(RogueLangParser.DOT, 0)

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
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 177
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 178
                self.match(RogueLangParser.NOT)
                self.state = 179
                self.expr(7)
                pass

            elif la_ == 3:
                self.state = 180
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 181
                self.expr(0)
                self.state = 182
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 4:
                self.state = 184
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 5:
                self.state = 185
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 6:
                self.state = 186
                self.match(RogueLangParser.NUMBER)
                pass

            elif la_ == 7:
                self.state = 187
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 8:
                self.state = 188
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 222
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 191
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 192
                        self.match(RogueLangParser.OPEN_BRACK)
                        self.state = 193
                        self.expr(0)
                        self.state = 194
                        self.match(RogueLangParser.CLOSED_BRACK)
                        self.state = 195
                        self.match(RogueLangParser.EQUAL_SIGN)
                        self.state = 196
                        self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 198
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 199
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16973824) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 200
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 201
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 202
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 203
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 204
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 205
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 206
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 207
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 208
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 209
                        self.expr(9)
                        pass

                    elif la_ == 6:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 210
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 211
                        self.match(RogueLangParser.OPEN_BRACK)
                        self.state = 212
                        self.expr(0)
                        self.state = 213
                        self.match(RogueLangParser.CLOSED_BRACK)
                        pass

                    elif la_ == 7:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 215
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 216
                        self.match(RogueLangParser.DOT)
                        self.state = 217
                        self.match(RogueLangParser.T__3)
                        self.state = 218
                        self.match(RogueLangParser.OPEN_PARENTH)
                        self.state = 219
                        self.expr(0)
                        self.state = 220
                        self.match(RogueLangParser.CLOSED_PARENTH)
                        pass

             
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self._predicates[16] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 12)
         




