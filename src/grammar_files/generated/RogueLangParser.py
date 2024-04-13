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
        4,1,41,203,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,5,0,43,8,0,10,0,12,0,46,9,0,1,1,1,1,1,1,1,1,1,1,5,1,53,8,1,10,
        1,12,1,56,9,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,72,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,82,8,5,3,5,
        84,8,5,1,6,1,6,1,6,1,6,3,6,90,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,106,8,8,1,8,3,8,109,8,8,1,9,1,9,1,
        9,1,9,1,9,1,9,3,9,117,8,9,1,10,1,10,1,10,1,11,1,11,5,11,124,8,11,
        10,11,12,11,127,9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,3,14,146,8,14,1,14,1,14,
        1,15,1,15,1,15,1,16,1,16,1,16,5,16,156,8,16,10,16,12,16,159,9,16,
        1,17,1,17,1,18,1,18,1,18,5,18,166,8,18,10,18,12,18,169,9,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,
        184,8,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,5,19,198,8,19,10,19,12,19,201,9,19,1,19,0,1,38,20,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,4,2,0,14,15,22,22,
        1,0,12,13,1,0,16,21,1,0,23,24,215,0,40,1,0,0,0,2,47,1,0,0,0,4,59,
        1,0,0,0,6,71,1,0,0,0,8,73,1,0,0,0,10,76,1,0,0,0,12,85,1,0,0,0,14,
        94,1,0,0,0,16,99,1,0,0,0,18,110,1,0,0,0,20,118,1,0,0,0,22,121,1,
        0,0,0,24,130,1,0,0,0,26,136,1,0,0,0,28,142,1,0,0,0,30,149,1,0,0,
        0,32,152,1,0,0,0,34,160,1,0,0,0,36,162,1,0,0,0,38,183,1,0,0,0,40,
        44,3,2,1,0,41,43,3,6,3,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,
        0,44,45,1,0,0,0,45,1,1,0,0,0,46,44,1,0,0,0,47,48,5,31,0,0,48,49,
        5,36,0,0,49,54,3,4,2,0,50,53,3,8,4,0,51,53,3,6,3,0,52,50,1,0,0,0,
        52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,57,1,
        0,0,0,56,54,1,0,0,0,57,58,5,37,0,0,58,3,1,0,0,0,59,60,5,11,0,0,60,
        61,3,22,11,0,61,5,1,0,0,0,62,72,3,14,7,0,63,72,3,10,5,0,64,72,3,
        12,6,0,65,72,3,16,8,0,66,72,3,24,12,0,67,72,3,26,13,0,68,72,3,22,
        11,0,69,72,3,30,15,0,70,72,3,38,19,0,71,62,1,0,0,0,71,63,1,0,0,0,
        71,64,1,0,0,0,71,65,1,0,0,0,71,66,1,0,0,0,71,67,1,0,0,0,71,68,1,
        0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,7,1,0,0,0,73,74,5,1,0,0,74,
        75,3,10,5,0,75,9,1,0,0,0,76,83,5,31,0,0,77,81,5,40,0,0,78,82,3,38,
        19,0,79,82,3,36,18,0,80,82,3,28,14,0,81,78,1,0,0,0,81,79,1,0,0,0,
        81,80,1,0,0,0,82,84,1,0,0,0,83,77,1,0,0,0,83,84,1,0,0,0,84,11,1,
        0,0,0,85,86,5,10,0,0,86,87,5,31,0,0,87,89,5,32,0,0,88,90,3,32,16,
        0,89,88,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,5,33,0,0,92,93,
        3,22,11,0,93,13,1,0,0,0,94,95,5,6,0,0,95,96,5,32,0,0,96,97,3,38,
        19,0,97,98,5,33,0,0,98,15,1,0,0,0,99,100,5,2,0,0,100,101,5,32,0,
        0,101,102,3,38,19,0,102,103,5,33,0,0,103,105,3,22,11,0,104,106,3,
        18,9,0,105,104,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,109,3,
        20,10,0,108,107,1,0,0,0,108,109,1,0,0,0,109,17,1,0,0,0,110,111,5,
        3,0,0,111,112,5,32,0,0,112,113,3,38,19,0,113,114,5,33,0,0,114,116,
        3,22,11,0,115,117,3,18,9,0,116,115,1,0,0,0,116,117,1,0,0,0,117,19,
        1,0,0,0,118,119,5,4,0,0,119,120,3,22,11,0,120,21,1,0,0,0,121,125,
        5,36,0,0,122,124,3,6,3,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,
        1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,125,1,0,0,0,128,129,
        5,37,0,0,129,23,1,0,0,0,130,131,5,7,0,0,131,132,3,10,5,0,132,133,
        5,8,0,0,133,134,3,38,19,0,134,135,3,22,11,0,135,25,1,0,0,0,136,137,
        5,9,0,0,137,138,5,32,0,0,138,139,3,38,19,0,139,140,5,33,0,0,140,
        141,3,22,11,0,141,27,1,0,0,0,142,143,5,31,0,0,143,145,5,32,0,0,144,
        146,3,36,18,0,145,144,1,0,0,0,145,146,1,0,0,0,146,147,1,0,0,0,147,
        148,5,33,0,0,148,29,1,0,0,0,149,150,5,5,0,0,150,151,3,38,19,0,151,
        31,1,0,0,0,152,157,3,34,17,0,153,154,5,38,0,0,154,156,3,34,17,0,
        155,153,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,
        158,33,1,0,0,0,159,157,1,0,0,0,160,161,5,31,0,0,161,35,1,0,0,0,162,
        167,3,38,19,0,163,164,5,38,0,0,164,166,3,38,19,0,165,163,1,0,0,0,
        166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,37,1,0,0,0,169,
        167,1,0,0,0,170,171,6,19,-1,0,171,184,3,28,14,0,172,173,5,25,0,0,
        173,184,3,38,19,7,174,175,5,32,0,0,175,176,3,38,19,0,176,177,5,33,
        0,0,177,184,1,0,0,0,178,184,5,31,0,0,179,184,5,29,0,0,180,184,5,
        30,0,0,181,184,5,26,0,0,182,184,5,27,0,0,183,170,1,0,0,0,183,172,
        1,0,0,0,183,174,1,0,0,0,183,178,1,0,0,0,183,179,1,0,0,0,183,180,
        1,0,0,0,183,181,1,0,0,0,183,182,1,0,0,0,184,199,1,0,0,0,185,186,
        10,11,0,0,186,187,7,0,0,0,187,198,3,38,19,12,188,189,10,10,0,0,189,
        190,7,1,0,0,190,198,3,38,19,11,191,192,10,9,0,0,192,193,7,2,0,0,
        193,198,3,38,19,10,194,195,10,8,0,0,195,196,7,3,0,0,196,198,3,38,
        19,9,197,185,1,0,0,0,197,188,1,0,0,0,197,191,1,0,0,0,197,194,1,0,
        0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,39,1,0,0,
        0,201,199,1,0,0,0,17,44,52,54,71,81,83,89,105,108,116,125,145,157,
        167,183,197,199
    ]

class RogueLangParser ( Parser ):

    grammarFileName = "RogueLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'field'", "'if'", "'elif'", "'else'", 
                     "'return'", "'print'", "'for'", "'in'", "'while'", 
                     "'def'", "'procedure'", "'+'", "'-'", "'*'", "'/'", 
                     "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", "'%'", 
                     "'and'", "'or'", "'not'", "'True'", "'False'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IF", "ELIF", "ELSE", "RETURN", 
                      "PRINT", "FOR", "IN", "WHILE", "DEF", "PROCEDURE", 
                      "PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", "LT", 
                      "LTE", "EQ", "NEQ", "MOD", "AND", "OR", "NOT", "TRUE", 
                      "FALSE", "COMMENT_SINGLELINE", "NUMBER", "STRING", 
                      "ID", "OPEN_PARENTH", "CLOSED_PARENTH", "OPEN_BRACK", 
                      "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", "COMMA", 
                      "DOT", "EQUAL_SIGN", "WS" ]

    RULE_prog = 0
    RULE_object = 1
    RULE_procedure = 2
    RULE_stat = 3
    RULE_field = 4
    RULE_varDecl = 5
    RULE_functionDecl = 6
    RULE_printStat = 7
    RULE_ifStat = 8
    RULE_elifStat = 9
    RULE_elseStat = 10
    RULE_statBlock = 11
    RULE_forLoop = 12
    RULE_whileLoop = 13
    RULE_functionCall = 14
    RULE_returnStat = 15
    RULE_params = 16
    RULE_param = 17
    RULE_args = 18
    RULE_expr = 19

    ruleNames =  [ "prog", "object", "procedure", "stat", "field", "varDecl", 
                   "functionDecl", "printStat", "ifStat", "elifStat", "elseStat", 
                   "statBlock", "forLoop", "whileLoop", "functionCall", 
                   "returnStat", "params", "param", "args", "expr" ]

    EOF = Token.EOF
    T__0=1
    IF=2
    ELIF=3
    ELSE=4
    RETURN=5
    PRINT=6
    FOR=7
    IN=8
    WHILE=9
    DEF=10
    PROCEDURE=11
    PLUS=12
    MINUS=13
    MULT=14
    DIV=15
    GT=16
    GTE=17
    LT=18
    LTE=19
    EQ=20
    NEQ=21
    MOD=22
    AND=23
    OR=24
    NOT=25
    TRUE=26
    FALSE=27
    COMMENT_SINGLELINE=28
    NUMBER=29
    STRING=30
    ID=31
    OPEN_PARENTH=32
    CLOSED_PARENTH=33
    OPEN_BRACK=34
    CLOSED_BRACK=35
    OPEN_CURL=36
    CLOSED_CURL=37
    COMMA=38
    DOT=39
    EQUAL_SIGN=40
    WS=41

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
            self.state = 40
            self.object_()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 77007423204) != 0):
                self.state = 41
                self.stat()
                self.state = 46
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
            self.state = 47
            self.match(RogueLangParser.ID)
            self.state = 48
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 49
            self.procedure()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 77007423206) != 0):
                self.state = 52
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 50
                    self.field()
                    pass
                elif token in [2, 5, 6, 7, 9, 10, 25, 26, 27, 29, 30, 31, 32, 36]:
                    self.state = 51
                    self.stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
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
            self.state = 59
            self.match(RogueLangParser.PROCEDURE)
            self.state = 60
            self.statBlock()
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
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.printStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.functionDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.ifStat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.forLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self.whileLoop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 68
                self.statBlock()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 69
                self.returnStat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 70
                self.expr(0)
                pass


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
        self.enterRule(localctx, 8, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(RogueLangParser.T__0)
            self.state = 74
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

        def EQUAL_SIGN(self):
            return self.getToken(RogueLangParser.EQUAL_SIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(RogueLangParser.ExprContext,0)


        def args(self):
            return self.getTypedRuleContext(RogueLangParser.ArgsContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(RogueLangParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return RogueLangParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = RogueLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(RogueLangParser.ID)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 77
                self.match(RogueLangParser.EQUAL_SIGN)
                self.state = 81
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 78
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 79
                    self.args()
                    pass

                elif la_ == 3:
                    self.state = 80
                    self.functionCall()
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
        self.enterRule(localctx, 12, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(RogueLangParser.DEF)
            self.state = 86
            self.match(RogueLangParser.ID)
            self.state = 87
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 88
                self.params()


            self.state = 91
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 92
            self.statBlock()
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
        self.enterRule(localctx, 14, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(RogueLangParser.PRINT)
            self.state = 95
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 96
            self.expr(0)
            self.state = 97
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
        self.enterRule(localctx, 16, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(RogueLangParser.IF)
            self.state = 100
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 101
            self.expr(0)
            self.state = 102
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 103
            self.statBlock()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 104
                self.elifStat()


            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 107
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
        self.enterRule(localctx, 18, self.RULE_elifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(RogueLangParser.ELIF)
            self.state = 111
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 112
            self.expr(0)
            self.state = 113
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 114
            self.statBlock()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 115
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
        self.enterRule(localctx, 20, self.RULE_elseStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(RogueLangParser.ELSE)
            self.state = 119
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
        self.enterRule(localctx, 22, self.RULE_statBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(RogueLangParser.OPEN_CURL)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 77007423204) != 0):
                self.state = 122
                self.stat()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
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
        self.enterRule(localctx, 24, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(RogueLangParser.FOR)
            self.state = 131
            self.varDecl()
            self.state = 132
            self.match(RogueLangParser.IN)
            self.state = 133
            self.expr(0)
            self.state = 134
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
        self.enterRule(localctx, 26, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(RogueLangParser.WHILE)
            self.state = 137
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 138
            self.expr(0)
            self.state = 139
            self.match(RogueLangParser.CLOSED_PARENTH)
            self.state = 140
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
        self.enterRule(localctx, 28, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(RogueLangParser.ID)
            self.state = 143
            self.match(RogueLangParser.OPEN_PARENTH)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8287944704) != 0):
                self.state = 144
                self.args()


            self.state = 147
            self.match(RogueLangParser.CLOSED_PARENTH)
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
        self.enterRule(localctx, 30, self.RULE_returnStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(RogueLangParser.RETURN)
            self.state = 150
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
        self.enterRule(localctx, 32, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.param()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 153
                self.match(RogueLangParser.COMMA)
                self.state = 154
                self.param()
                self.state = 159
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
        self.enterRule(localctx, 34, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
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
        self.enterRule(localctx, 36, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.expr(0)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 163
                self.match(RogueLangParser.COMMA)
                self.state = 164
                self.expr(0)
                self.state = 169
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

        def NUMBER(self):
            return self.getToken(RogueLangParser.NUMBER, 0)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 171
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 172
                self.match(RogueLangParser.NOT)
                self.state = 173
                self.expr(7)
                pass

            elif la_ == 3:
                self.state = 174
                self.match(RogueLangParser.OPEN_PARENTH)
                self.state = 175
                self.expr(0)
                self.state = 176
                self.match(RogueLangParser.CLOSED_PARENTH)
                pass

            elif la_ == 4:
                self.state = 178
                self.match(RogueLangParser.ID)
                pass

            elif la_ == 5:
                self.state = 179
                self.match(RogueLangParser.NUMBER)
                pass

            elif la_ == 6:
                self.state = 180
                self.match(RogueLangParser.STRING)
                pass

            elif la_ == 7:
                self.state = 181
                self.match(RogueLangParser.TRUE)
                pass

            elif la_ == 8:
                self.state = 182
                self.match(RogueLangParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 197
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 185
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 186
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4243456) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 187
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 188
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 189
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 190
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 191
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 192
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 193
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = RogueLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 194
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 195
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 196
                        self.expr(9)
                        pass

             
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self._predicates[19] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




