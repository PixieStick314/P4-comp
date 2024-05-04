// Generated from c:/Users/nedim/Documents/GitHub/P4-comp/src/grammar_files/RogueLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class RogueLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, IF=8, ELIF=9, 
		ELSE=10, RETURN=11, PRINT=12, FOR=13, IN=14, WHILE=15, DEF=16, LAYER=17, 
		PROCEDURE=18, PLUS=19, MINUS=20, MULT=21, DIV=22, GT=23, GTE=24, LT=25, 
		LTE=26, EQ=27, NEQ=28, PEQ=29, MEQ=30, MOD=31, AND=32, OR=33, NOT=34, 
		TRUE=35, FALSE=36, SQRT=37, POW=38, COMMENT_SINGLELINE=39, INT=40, FLOAT=41, 
		STRING=42, ID=43, OPEN_PARENTH=44, CLOSED_PARENTH=45, OPEN_BRACK=46, CLOSED_BRACK=47, 
		OPEN_CURL=48, CLOSED_CURL=49, COMMA=50, DOT=51, EQUAL_SIGN=52, WS=53;
	public static final int
		RULE_prog = 0, RULE_object = 1, RULE_procedure = 2, RULE_field = 3, RULE_stat = 4, 
		RULE_varDeclStat = 5, RULE_varDecl = 6, RULE_assignStat = 7, RULE_assignment = 8, 
		RULE_functionDecl = 9, RULE_functionCall = 10, RULE_list = 11, RULE_listElement = 12, 
		RULE_listAccess = 13, RULE_listLength = 14, RULE_listPop = 15, RULE_struct = 16, 
		RULE_structDef = 17, RULE_structField = 18, RULE_structFieldAccess = 19, 
		RULE_plusEquals = 20, RULE_minusEquals = 21, RULE_printStat = 22, RULE_ifStat = 23, 
		RULE_elifStat = 24, RULE_elseStat = 25, RULE_statBlock = 26, RULE_forLoop = 27, 
		RULE_whileLoop = 28, RULE_returnStat = 29, RULE_whiteNoiseStat = 30, RULE_random = 31, 
		RULE_range = 32, RULE_params = 33, RULE_args = 34, RULE_expr = 35;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "object", "procedure", "field", "stat", "varDeclStat", "varDecl", 
			"assignStat", "assignment", "functionDecl", "functionCall", "list", "listElement", 
			"listAccess", "listLength", "listPop", "struct", "structDef", "structField", 
			"structFieldAccess", "plusEquals", "minusEquals", "printStat", "ifStat", 
			"elifStat", "elseStat", "statBlock", "forLoop", "whileLoop", "returnStat", 
			"whiteNoiseStat", "random", "range", "params", "args", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'field'", "'let'", "'len'", "'pop'", "'struct'", "'WhiteNoise'", 
			"'random'", "'if'", "'elif'", "'else'", "'return'", "'print'", "'for'", 
			"'in'", "'while'", "'def'", "'layer'", "'procedure'", "'+'", "'-'", "'*'", 
			"'/'", "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", "'+='", "'-='", 
			"'%'", "'and'", "'or'", "'not'", "'True'", "'False'", "'sqrt'", "'pow'", 
			null, null, null, null, null, "'('", "')'", "'['", "']'", "'{'", "'}'", 
			"','", "'.'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "IF", "ELIF", "ELSE", 
			"RETURN", "PRINT", "FOR", "IN", "WHILE", "DEF", "LAYER", "PROCEDURE", 
			"PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", "LT", "LTE", "EQ", "NEQ", 
			"PEQ", "MEQ", "MOD", "AND", "OR", "NOT", "TRUE", "FALSE", "SQRT", "POW", 
			"COMMENT_SINGLELINE", "INT", "FLOAT", "STRING", "ID", "OPEN_PARENTH", 
			"CLOSED_PARENTH", "OPEN_BRACK", "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", 
			"COMMA", "DOT", "EQUAL_SIGN", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "RogueLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public RogueLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public ObjectContext object() {
			return getRuleContext(ObjectContext.class,0);
		}
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			object();
			setState(76);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 316092413229548L) != 0)) {
				{
				{
				setState(73);
				stat();
				}
				}
				setState(78);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ObjectContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public TerminalNode OPEN_CURL() { return getToken(RogueLangParser.OPEN_CURL, 0); }
		public ProcedureContext procedure() {
			return getRuleContext(ProcedureContext.class,0);
		}
		public TerminalNode CLOSED_CURL() { return getToken(RogueLangParser.CLOSED_CURL, 0); }
		public List<FieldContext> field() {
			return getRuleContexts(FieldContext.class);
		}
		public FieldContext field(int i) {
			return getRuleContext(FieldContext.class,i);
		}
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ObjectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_object; }
	}

	public final ObjectContext object() throws RecognitionException {
		ObjectContext _localctx = new ObjectContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_object);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(ID);
			setState(80);
			match(OPEN_CURL);
			setState(81);
			procedure();
			setState(86);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 316092413229550L) != 0)) {
				{
				setState(84);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__0:
					{
					setState(82);
					field();
					}
					break;
				case T__1:
				case T__2:
				case T__4:
				case T__5:
				case T__6:
				case IF:
				case RETURN:
				case PRINT:
				case FOR:
				case WHILE:
				case DEF:
				case NOT:
				case TRUE:
				case FALSE:
				case SQRT:
				case POW:
				case INT:
				case FLOAT:
				case STRING:
				case ID:
				case OPEN_PARENTH:
				case OPEN_CURL:
					{
					setState(83);
					stat();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(88);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(89);
			match(CLOSED_CURL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProcedureContext extends ParserRuleContext {
		public TerminalNode PROCEDURE() { return getToken(RogueLangParser.PROCEDURE, 0); }
		public StatBlockContext statBlock() {
			return getRuleContext(StatBlockContext.class,0);
		}
		public ProcedureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_procedure; }
	}

	public final ProcedureContext procedure() throws RecognitionException {
		ProcedureContext _localctx = new ProcedureContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_procedure);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(PROCEDURE);
			setState(92);
			statBlock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FieldContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public FieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field; }
	}

	public final FieldContext field() throws RecognitionException {
		FieldContext _localctx = new FieldContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_field);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(T__0);
			setState(95);
			varDecl();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatContext extends ParserRuleContext {
		public PrintStatContext printStat() {
			return getRuleContext(PrintStatContext.class,0);
		}
		public VarDeclStatContext varDeclStat() {
			return getRuleContext(VarDeclStatContext.class,0);
		}
		public AssignStatContext assignStat() {
			return getRuleContext(AssignStatContext.class,0);
		}
		public FunctionDeclContext functionDecl() {
			return getRuleContext(FunctionDeclContext.class,0);
		}
		public IfStatContext ifStat() {
			return getRuleContext(IfStatContext.class,0);
		}
		public ForLoopContext forLoop() {
			return getRuleContext(ForLoopContext.class,0);
		}
		public WhileLoopContext whileLoop() {
			return getRuleContext(WhileLoopContext.class,0);
		}
		public StatBlockContext statBlock() {
			return getRuleContext(StatBlockContext.class,0);
		}
		public ReturnStatContext returnStat() {
			return getRuleContext(ReturnStatContext.class,0);
		}
		public PlusEqualsContext plusEquals() {
			return getRuleContext(PlusEqualsContext.class,0);
		}
		public MinusEqualsContext minusEquals() {
			return getRuleContext(MinusEqualsContext.class,0);
		}
		public ListPopContext listPop() {
			return getRuleContext(ListPopContext.class,0);
		}
		public WhiteNoiseStatContext whiteNoiseStat() {
			return getRuleContext(WhiteNoiseStatContext.class,0);
		}
		public StructDefContext structDef() {
			return getRuleContext(StructDefContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_stat);
		try {
			setState(112);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(97);
				printStat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(98);
				varDeclStat();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(99);
				assignStat();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(100);
				functionDecl();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(101);
				ifStat();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(102);
				forLoop();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(103);
				whileLoop();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(104);
				statBlock();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(105);
				returnStat();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(106);
				plusEquals();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(107);
				minusEquals();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(108);
				listPop();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(109);
				whiteNoiseStat();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(110);
				structDef();
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(111);
				expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclStatContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public VarDeclStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclStat; }
	}

	public final VarDeclStatContext varDeclStat() throws RecognitionException {
		VarDeclStatContext _localctx = new VarDeclStatContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_varDeclStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(T__1);
			setState(115);
			varDecl();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_varDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(ID);
			setState(119);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL_SIGN) {
				{
				setState(118);
				assignment();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignStatContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public List<StructFieldAccessContext> structFieldAccess() {
			return getRuleContexts(StructFieldAccessContext.class);
		}
		public StructFieldAccessContext structFieldAccess(int i) {
			return getRuleContext(StructFieldAccessContext.class,i);
		}
		public List<ListAccessContext> listAccess() {
			return getRuleContexts(ListAccessContext.class);
		}
		public ListAccessContext listAccess(int i) {
			return getRuleContext(ListAccessContext.class,i);
		}
		public AssignStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignStat; }
	}

	public final AssignStatContext assignStat() throws RecognitionException {
		AssignStatContext _localctx = new AssignStatContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assignStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			match(ID);
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DOT) {
				{
				{
				setState(122);
				structFieldAccess();
				}
				}
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OPEN_BRACK) {
				{
				{
				setState(128);
				listAccess();
				}
				}
				setState(133);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(134);
			assignment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode EQUAL_SIGN() { return getToken(RogueLangParser.EQUAL_SIGN, 0); }
		public StructContext struct() {
			return getRuleContext(StructContext.class,0);
		}
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_assignment);
		try {
			setState(142);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(136);
				match(EQUAL_SIGN);
				setState(137);
				struct();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(138);
				match(EQUAL_SIGN);
				setState(139);
				list();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(140);
				match(EQUAL_SIGN);
				setState(141);
				expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDeclContext extends ParserRuleContext {
		public TerminalNode DEF() { return getToken(RogueLangParser.DEF, 0); }
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public TerminalNode OPEN_PARENTH() { return getToken(RogueLangParser.OPEN_PARENTH, 0); }
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public StatBlockContext statBlock() {
			return getRuleContext(StatBlockContext.class,0);
		}
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public FunctionDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDecl; }
	}

	public final FunctionDeclContext functionDecl() throws RecognitionException {
		FunctionDeclContext _localctx = new FunctionDeclContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_functionDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			match(DEF);
			setState(145);
			match(ID);
			setState(146);
			match(OPEN_PARENTH);
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(147);
				params();
				}
			}

			setState(150);
			match(CLOSED_PARENTH);
			setState(151);
			statBlock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public TerminalNode OPEN_PARENTH() { return getToken(RogueLangParser.OPEN_PARENTH, 0); }
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			match(ID);
			setState(154);
			match(OPEN_PARENTH);
			setState(156);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 34617436405896L) != 0)) {
				{
				setState(155);
				args();
				}
			}

			setState(158);
			match(CLOSED_PARENTH);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACK() { return getToken(RogueLangParser.OPEN_BRACK, 0); }
		public TerminalNode CLOSED_BRACK() { return getToken(RogueLangParser.CLOSED_BRACK, 0); }
		public List<ListElementContext> listElement() {
			return getRuleContexts(ListElementContext.class);
		}
		public ListElementContext listElement(int i) {
			return getRuleContext(ListElementContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(RogueLangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(RogueLangParser.COMMA, i);
		}
		public ListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list; }
	}

	public final ListContext list() throws RecognitionException {
		ListContext _localctx = new ListContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(OPEN_BRACK);
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 104986180583560L) != 0)) {
				{
				setState(161);
				listElement();
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(162);
					match(COMMA);
					setState(163);
					listElement();
					}
					}
					setState(168);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(171);
			match(CLOSED_BRACK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListElementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
		}
		public ListElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listElement; }
	}

	public final ListElementContext listElement() throws RecognitionException {
		ListElementContext _localctx = new ListElementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_listElement);
		try {
			setState(175);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
			case T__6:
			case NOT:
			case TRUE:
			case FALSE:
			case SQRT:
			case POW:
			case INT:
			case FLOAT:
			case STRING:
			case ID:
			case OPEN_PARENTH:
				enterOuterAlt(_localctx, 1);
				{
				setState(173);
				expr(0);
				}
				break;
			case OPEN_BRACK:
				enterOuterAlt(_localctx, 2);
				{
				setState(174);
				list();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListAccessContext extends ParserRuleContext {
		public TerminalNode OPEN_BRACK() { return getToken(RogueLangParser.OPEN_BRACK, 0); }
		public TerminalNode INT() { return getToken(RogueLangParser.INT, 0); }
		public TerminalNode CLOSED_BRACK() { return getToken(RogueLangParser.CLOSED_BRACK, 0); }
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public ListAccessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listAccess; }
	}

	public final ListAccessContext listAccess() throws RecognitionException {
		ListAccessContext _localctx = new ListAccessContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_listAccess);
		try {
			setState(183);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(177);
				match(OPEN_BRACK);
				setState(178);
				match(INT);
				setState(179);
				match(CLOSED_BRACK);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(180);
				match(OPEN_BRACK);
				setState(181);
				match(ID);
				setState(182);
				match(CLOSED_BRACK);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListLengthContext extends ParserRuleContext {
		public TerminalNode OPEN_PARENTH() { return getToken(RogueLangParser.OPEN_PARENTH, 0); }
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public ListLengthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listLength; }
	}

	public final ListLengthContext listLength() throws RecognitionException {
		ListLengthContext _localctx = new ListLengthContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_listLength);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			match(T__2);
			setState(186);
			match(OPEN_PARENTH);
			setState(187);
			match(ID);
			setState(188);
			match(CLOSED_PARENTH);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListPopContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public TerminalNode DOT() { return getToken(RogueLangParser.DOT, 0); }
		public TerminalNode OPEN_PARENTH() { return getToken(RogueLangParser.OPEN_PARENTH, 0); }
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public ListPopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listPop; }
	}

	public final ListPopContext listPop() throws RecognitionException {
		ListPopContext _localctx = new ListPopContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_listPop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			match(ID);
			setState(191);
			match(DOT);
			setState(192);
			match(T__3);
			setState(193);
			match(OPEN_PARENTH);
			setState(194);
			match(CLOSED_PARENTH);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public TerminalNode OPEN_CURL() { return getToken(RogueLangParser.OPEN_CURL, 0); }
		public TerminalNode CLOSED_CURL() { return getToken(RogueLangParser.CLOSED_CURL, 0); }
		public List<StructFieldContext> structField() {
			return getRuleContexts(StructFieldContext.class);
		}
		public StructFieldContext structField(int i) {
			return getRuleContext(StructFieldContext.class,i);
		}
		public List<AssignmentContext> assignment() {
			return getRuleContexts(AssignmentContext.class);
		}
		public AssignmentContext assignment(int i) {
			return getRuleContext(AssignmentContext.class,i);
		}
		public StructContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct; }
	}

	public final StructContext struct() throws RecognitionException {
		StructContext _localctx = new StructContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_struct);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			match(ID);
			setState(197);
			match(OPEN_CURL);
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(198);
				structField();
				setState(199);
				assignment();
				}
				}
				setState(205);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(206);
			match(CLOSED_CURL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructDefContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public TerminalNode OPEN_CURL() { return getToken(RogueLangParser.OPEN_CURL, 0); }
		public TerminalNode CLOSED_CURL() { return getToken(RogueLangParser.CLOSED_CURL, 0); }
		public List<StructFieldContext> structField() {
			return getRuleContexts(StructFieldContext.class);
		}
		public StructFieldContext structField(int i) {
			return getRuleContext(StructFieldContext.class,i);
		}
		public StructDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structDef; }
	}

	public final StructDefContext structDef() throws RecognitionException {
		StructDefContext _localctx = new StructDefContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_structDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			match(T__4);
			setState(209);
			match(ID);
			setState(210);
			match(OPEN_CURL);
			setState(212); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(211);
				structField();
				}
				}
				setState(214); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			setState(216);
			match(CLOSED_CURL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructFieldContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public StructFieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structField; }
	}

	public final StructFieldContext structField() throws RecognitionException {
		StructFieldContext _localctx = new StructFieldContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_structField);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructFieldAccessContext extends ParserRuleContext {
		public TerminalNode DOT() { return getToken(RogueLangParser.DOT, 0); }
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public List<ListAccessContext> listAccess() {
			return getRuleContexts(ListAccessContext.class);
		}
		public ListAccessContext listAccess(int i) {
			return getRuleContext(ListAccessContext.class,i);
		}
		public StructFieldAccessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structFieldAccess; }
	}

	public final StructFieldAccessContext structFieldAccess() throws RecognitionException {
		StructFieldAccessContext _localctx = new StructFieldAccessContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_structFieldAccess);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(DOT);
			setState(221);
			match(ID);
			setState(225);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(222);
					listAccess();
					}
					} 
				}
				setState(227);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PlusEqualsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public TerminalNode PEQ() { return getToken(RogueLangParser.PEQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public PlusEqualsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_plusEquals; }
	}

	public final PlusEqualsContext plusEquals() throws RecognitionException {
		PlusEqualsContext _localctx = new PlusEqualsContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_plusEquals);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(ID);
			setState(229);
			match(PEQ);
			setState(230);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MinusEqualsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public TerminalNode MEQ() { return getToken(RogueLangParser.MEQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public MinusEqualsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_minusEquals; }
	}

	public final MinusEqualsContext minusEquals() throws RecognitionException {
		MinusEqualsContext _localctx = new MinusEqualsContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_minusEquals);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(ID);
			setState(233);
			match(MEQ);
			setState(234);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintStatContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(RogueLangParser.PRINT, 0); }
		public TerminalNode OPEN_PARENTH() { return getToken(RogueLangParser.OPEN_PARENTH, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public List<TerminalNode> PLUS() { return getTokens(RogueLangParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(RogueLangParser.PLUS, i);
		}
		public PrintStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStat; }
	}

	public final PrintStatContext printStat() throws RecognitionException {
		PrintStatContext _localctx = new PrintStatContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_printStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			match(PRINT);
			setState(237);
			match(OPEN_PARENTH);
			setState(238);
			expr(0);
			setState(243);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS) {
				{
				{
				setState(239);
				match(PLUS);
				setState(240);
				expr(0);
				}
				}
				setState(245);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(246);
			match(CLOSED_PARENTH);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(RogueLangParser.IF, 0); }
		public TerminalNode OPEN_PARENTH() { return getToken(RogueLangParser.OPEN_PARENTH, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public StatBlockContext statBlock() {
			return getRuleContext(StatBlockContext.class,0);
		}
		public ElifStatContext elifStat() {
			return getRuleContext(ElifStatContext.class,0);
		}
		public ElseStatContext elseStat() {
			return getRuleContext(ElseStatContext.class,0);
		}
		public IfStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStat; }
	}

	public final IfStatContext ifStat() throws RecognitionException {
		IfStatContext _localctx = new IfStatContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_ifStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			match(IF);
			setState(249);
			match(OPEN_PARENTH);
			setState(250);
			expr(0);
			setState(251);
			match(CLOSED_PARENTH);
			setState(252);
			statBlock();
			setState(254);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELIF) {
				{
				setState(253);
				elifStat();
				}
			}

			setState(257);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(256);
				elseStat();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElifStatContext extends ParserRuleContext {
		public TerminalNode ELIF() { return getToken(RogueLangParser.ELIF, 0); }
		public TerminalNode OPEN_PARENTH() { return getToken(RogueLangParser.OPEN_PARENTH, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public StatBlockContext statBlock() {
			return getRuleContext(StatBlockContext.class,0);
		}
		public ElifStatContext elifStat() {
			return getRuleContext(ElifStatContext.class,0);
		}
		public ElifStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elifStat; }
	}

	public final ElifStatContext elifStat() throws RecognitionException {
		ElifStatContext _localctx = new ElifStatContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_elifStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(259);
			match(ELIF);
			setState(260);
			match(OPEN_PARENTH);
			setState(261);
			expr(0);
			setState(262);
			match(CLOSED_PARENTH);
			setState(263);
			statBlock();
			setState(265);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELIF) {
				{
				setState(264);
				elifStat();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElseStatContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(RogueLangParser.ELSE, 0); }
		public StatBlockContext statBlock() {
			return getRuleContext(StatBlockContext.class,0);
		}
		public ElseStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseStat; }
	}

	public final ElseStatContext elseStat() throws RecognitionException {
		ElseStatContext _localctx = new ElseStatContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_elseStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(ELSE);
			setState(268);
			statBlock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatBlockContext extends ParserRuleContext {
		public TerminalNode OPEN_CURL() { return getToken(RogueLangParser.OPEN_CURL, 0); }
		public TerminalNode CLOSED_CURL() { return getToken(RogueLangParser.CLOSED_CURL, 0); }
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public StatBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statBlock; }
	}

	public final StatBlockContext statBlock() throws RecognitionException {
		StatBlockContext _localctx = new StatBlockContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_statBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			match(OPEN_CURL);
			setState(274);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 316092413229548L) != 0)) {
				{
				{
				setState(271);
				stat();
				}
				}
				setState(276);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(277);
			match(CLOSED_CURL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForLoopContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(RogueLangParser.FOR, 0); }
		public List<TerminalNode> ID() { return getTokens(RogueLangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(RogueLangParser.ID, i);
		}
		public TerminalNode IN() { return getToken(RogueLangParser.IN, 0); }
		public StatBlockContext statBlock() {
			return getRuleContext(StatBlockContext.class,0);
		}
		public ForLoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forLoop; }
	}

	public final ForLoopContext forLoop() throws RecognitionException {
		ForLoopContext _localctx = new ForLoopContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_forLoop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(279);
			match(FOR);
			setState(280);
			match(ID);
			setState(281);
			match(IN);
			setState(282);
			match(ID);
			setState(283);
			statBlock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileLoopContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(RogueLangParser.WHILE, 0); }
		public TerminalNode OPEN_PARENTH() { return getToken(RogueLangParser.OPEN_PARENTH, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public StatBlockContext statBlock() {
			return getRuleContext(StatBlockContext.class,0);
		}
		public WhileLoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileLoop; }
	}

	public final WhileLoopContext whileLoop() throws RecognitionException {
		WhileLoopContext _localctx = new WhileLoopContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_whileLoop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(285);
			match(WHILE);
			setState(286);
			match(OPEN_PARENTH);
			setState(287);
			expr(0);
			setState(288);
			match(CLOSED_PARENTH);
			setState(289);
			statBlock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStatContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(RogueLangParser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ReturnStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStat; }
	}

	public final ReturnStatContext returnStat() throws RecognitionException {
		ReturnStatContext _localctx = new ReturnStatContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_returnStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(291);
			match(RETURN);
			setState(292);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhiteNoiseStatContext extends ParserRuleContext {
		public TerminalNode OPEN_PARENTH() { return getToken(RogueLangParser.OPEN_PARENTH, 0); }
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public TerminalNode COMMA() { return getToken(RogueLangParser.COMMA, 0); }
		public RangeContext range() {
			return getRuleContext(RangeContext.class,0);
		}
		public TerminalNode LAYER() { return getToken(RogueLangParser.LAYER, 0); }
		public WhiteNoiseStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whiteNoiseStat; }
	}

	public final WhiteNoiseStatContext whiteNoiseStat() throws RecognitionException {
		WhiteNoiseStatContext _localctx = new WhiteNoiseStatContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_whiteNoiseStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(294);
			match(T__5);
			setState(295);
			match(OPEN_PARENTH);
			setState(296);
			match(ID);
			setState(299);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(297);
				match(COMMA);
				setState(298);
				range();
				}
			}

			setState(301);
			match(CLOSED_PARENTH);
			setState(303);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LAYER) {
				{
				setState(302);
				match(LAYER);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RandomContext extends ParserRuleContext {
		public TerminalNode IN() { return getToken(RogueLangParser.IN, 0); }
		public RangeContext range() {
			return getRuleContext(RangeContext.class,0);
		}
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public RandomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_random; }
	}

	public final RandomContext random() throws RecognitionException {
		RandomContext _localctx = new RandomContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_random);
		try {
			setState(311);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(305);
				match(T__6);
				setState(306);
				match(IN);
				setState(307);
				range();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(308);
				match(T__6);
				setState(309);
				match(IN);
				setState(310);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RangeContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> DOT() { return getTokens(RogueLangParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(RogueLangParser.DOT, i);
		}
		public RangeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_range; }
	}

	public final RangeContext range() throws RecognitionException {
		RangeContext _localctx = new RangeContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_range);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(313);
			expr(0);
			setState(314);
			match(DOT);
			setState(315);
			match(DOT);
			setState(316);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamsContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(RogueLangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(RogueLangParser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(RogueLangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(RogueLangParser.COMMA, i);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
			match(ID);
			setState(323);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(319);
				match(COMMA);
				setState(320);
				match(ID);
				}
				}
				setState(325);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgsContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(RogueLangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(RogueLangParser.COMMA, i);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(326);
			expr(0);
			setState(331);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(327);
				match(COMMA);
				setState(328);
				expr(0);
				}
				}
				setState(333);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public Token op;
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public List<StructFieldAccessContext> structFieldAccess() {
			return getRuleContexts(StructFieldAccessContext.class);
		}
		public StructFieldAccessContext structFieldAccess(int i) {
			return getRuleContext(StructFieldAccessContext.class,i);
		}
		public List<ListAccessContext> listAccess() {
			return getRuleContexts(ListAccessContext.class);
		}
		public ListAccessContext listAccess(int i) {
			return getRuleContext(ListAccessContext.class,i);
		}
		public ListLengthContext listLength() {
			return getRuleContext(ListLengthContext.class,0);
		}
		public RandomContext random() {
			return getRuleContext(RandomContext.class,0);
		}
		public TerminalNode NOT() { return getToken(RogueLangParser.NOT, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode SQRT() { return getToken(RogueLangParser.SQRT, 0); }
		public TerminalNode OPEN_PARENTH() { return getToken(RogueLangParser.OPEN_PARENTH, 0); }
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public TerminalNode POW() { return getToken(RogueLangParser.POW, 0); }
		public TerminalNode COMMA() { return getToken(RogueLangParser.COMMA, 0); }
		public TerminalNode INT() { return getToken(RogueLangParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(RogueLangParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(RogueLangParser.STRING, 0); }
		public TerminalNode TRUE() { return getToken(RogueLangParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(RogueLangParser.FALSE, 0); }
		public TerminalNode MULT() { return getToken(RogueLangParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(RogueLangParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(RogueLangParser.MOD, 0); }
		public TerminalNode PLUS() { return getToken(RogueLangParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(RogueLangParser.MINUS, 0); }
		public TerminalNode GT() { return getToken(RogueLangParser.GT, 0); }
		public TerminalNode GTE() { return getToken(RogueLangParser.GTE, 0); }
		public TerminalNode LT() { return getToken(RogueLangParser.LT, 0); }
		public TerminalNode LTE() { return getToken(RogueLangParser.LTE, 0); }
		public TerminalNode EQ() { return getToken(RogueLangParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(RogueLangParser.NEQ, 0); }
		public TerminalNode AND() { return getToken(RogueLangParser.AND, 0); }
		public TerminalNode OR() { return getToken(RogueLangParser.OR, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 70;
		enterRecursionRule(_localctx, 70, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				{
				setState(335);
				functionCall();
				}
				break;
			case 2:
				{
				setState(336);
				match(ID);
				setState(338); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(337);
						structFieldAccess();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(340); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case 3:
				{
				setState(342);
				match(ID);
				setState(344); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(343);
						listAccess();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(346); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case 4:
				{
				setState(348);
				listLength();
				}
				break;
			case 5:
				{
				setState(349);
				random();
				}
				break;
			case 6:
				{
				setState(350);
				match(NOT);
				setState(351);
				expr(10);
				}
				break;
			case 7:
				{
				setState(352);
				match(SQRT);
				setState(353);
				match(OPEN_PARENTH);
				setState(354);
				expr(0);
				setState(355);
				match(CLOSED_PARENTH);
				}
				break;
			case 8:
				{
				setState(357);
				match(POW);
				setState(358);
				match(OPEN_PARENTH);
				setState(359);
				expr(0);
				setState(360);
				match(COMMA);
				setState(361);
				expr(0);
				setState(362);
				match(CLOSED_PARENTH);
				}
				break;
			case 9:
				{
				setState(364);
				match(OPEN_PARENTH);
				setState(365);
				expr(0);
				setState(366);
				match(CLOSED_PARENTH);
				}
				break;
			case 10:
				{
				setState(368);
				match(ID);
				}
				break;
			case 11:
				{
				setState(369);
				match(INT);
				}
				break;
			case 12:
				{
				setState(370);
				match(FLOAT);
				}
				break;
			case 13:
				{
				setState(371);
				match(STRING);
				}
				break;
			case 14:
				{
				setState(372);
				match(TRUE);
				}
				break;
			case 15:
				{
				setState(373);
				match(FALSE);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(390);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(388);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(376);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(377);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2153775104L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(378);
						expr(15);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(379);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(380);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(381);
						expr(14);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(382);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(383);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 528482304L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(384);
						expr(13);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(385);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(386);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==AND || _la==OR) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(387);
						expr(12);
						}
						break;
					}
					} 
				}
				setState(392);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 35:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 14);
		case 1:
			return precpred(_ctx, 13);
		case 2:
			return precpred(_ctx, 12);
		case 3:
			return precpred(_ctx, 11);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00015\u018a\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0001\u0000\u0001\u0000\u0005\u0000K\b\u0000\n\u0000\f\u0000"+
		"N\t\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0005\u0001U\b\u0001\n\u0001\f\u0001X\t\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004q\b\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0003\u0006x\b\u0006"+
		"\u0001\u0007\u0001\u0007\u0005\u0007|\b\u0007\n\u0007\f\u0007\u007f\t"+
		"\u0007\u0001\u0007\u0005\u0007\u0082\b\u0007\n\u0007\f\u0007\u0085\t\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0003\b\u008f\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0003\t\u0095\b\t"+
		"\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0003\n\u009d\b\n\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b"+
		"\u00a5\b\u000b\n\u000b\f\u000b\u00a8\t\u000b\u0003\u000b\u00aa\b\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0003\f\u00b0\b\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00b8\b\r\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u00ca\b\u0010\n\u0010\f\u0010"+
		"\u00cd\t\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0004\u0011\u00d5\b\u0011\u000b\u0011\f\u0011\u00d6\u0001"+
		"\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0005\u0013\u00e0\b\u0013\n\u0013\f\u0013\u00e3\t\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0005\u0016\u00f2\b\u0016\n\u0016\f\u0016\u00f5\t\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0003\u0017\u00ff\b\u0017\u0001\u0017\u0003\u0017\u0102\b\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0003\u0018\u010a\b\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a"+
		"\u0001\u001a\u0005\u001a\u0111\b\u001a\n\u001a\f\u001a\u0114\t\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0003\u001e\u012c\b\u001e\u0001"+
		"\u001e\u0001\u001e\u0003\u001e\u0130\b\u001e\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0003\u001f\u0138\b\u001f\u0001"+
		" \u0001 \u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0005!\u0142\b!\n!"+
		"\f!\u0145\t!\u0001\"\u0001\"\u0001\"\u0005\"\u014a\b\"\n\"\f\"\u014d\t"+
		"\"\u0001#\u0001#\u0001#\u0001#\u0004#\u0153\b#\u000b#\f#\u0154\u0001#"+
		"\u0001#\u0004#\u0159\b#\u000b#\f#\u015a\u0001#\u0001#\u0001#\u0001#\u0001"+
		"#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001"+
		"#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001"+
		"#\u0001#\u0003#\u0177\b#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001"+
		"#\u0001#\u0001#\u0001#\u0001#\u0001#\u0005#\u0185\b#\n#\f#\u0188\t#\u0001"+
		"#\u0000\u0001F$\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDF\u0000\u0004\u0002"+
		"\u0000\u0015\u0016\u001f\u001f\u0001\u0000\u0013\u0014\u0001\u0000\u0017"+
		"\u001c\u0001\u0000 !\u01a2\u0000H\u0001\u0000\u0000\u0000\u0002O\u0001"+
		"\u0000\u0000\u0000\u0004[\u0001\u0000\u0000\u0000\u0006^\u0001\u0000\u0000"+
		"\u0000\bp\u0001\u0000\u0000\u0000\nr\u0001\u0000\u0000\u0000\fu\u0001"+
		"\u0000\u0000\u0000\u000ey\u0001\u0000\u0000\u0000\u0010\u008e\u0001\u0000"+
		"\u0000\u0000\u0012\u0090\u0001\u0000\u0000\u0000\u0014\u0099\u0001\u0000"+
		"\u0000\u0000\u0016\u00a0\u0001\u0000\u0000\u0000\u0018\u00af\u0001\u0000"+
		"\u0000\u0000\u001a\u00b7\u0001\u0000\u0000\u0000\u001c\u00b9\u0001\u0000"+
		"\u0000\u0000\u001e\u00be\u0001\u0000\u0000\u0000 \u00c4\u0001\u0000\u0000"+
		"\u0000\"\u00d0\u0001\u0000\u0000\u0000$\u00da\u0001\u0000\u0000\u0000"+
		"&\u00dc\u0001\u0000\u0000\u0000(\u00e4\u0001\u0000\u0000\u0000*\u00e8"+
		"\u0001\u0000\u0000\u0000,\u00ec\u0001\u0000\u0000\u0000.\u00f8\u0001\u0000"+
		"\u0000\u00000\u0103\u0001\u0000\u0000\u00002\u010b\u0001\u0000\u0000\u0000"+
		"4\u010e\u0001\u0000\u0000\u00006\u0117\u0001\u0000\u0000\u00008\u011d"+
		"\u0001\u0000\u0000\u0000:\u0123\u0001\u0000\u0000\u0000<\u0126\u0001\u0000"+
		"\u0000\u0000>\u0137\u0001\u0000\u0000\u0000@\u0139\u0001\u0000\u0000\u0000"+
		"B\u013e\u0001\u0000\u0000\u0000D\u0146\u0001\u0000\u0000\u0000F\u0176"+
		"\u0001\u0000\u0000\u0000HL\u0003\u0002\u0001\u0000IK\u0003\b\u0004\u0000"+
		"JI\u0001\u0000\u0000\u0000KN\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000"+
		"\u0000LM\u0001\u0000\u0000\u0000M\u0001\u0001\u0000\u0000\u0000NL\u0001"+
		"\u0000\u0000\u0000OP\u0005+\u0000\u0000PQ\u00050\u0000\u0000QV\u0003\u0004"+
		"\u0002\u0000RU\u0003\u0006\u0003\u0000SU\u0003\b\u0004\u0000TR\u0001\u0000"+
		"\u0000\u0000TS\u0001\u0000\u0000\u0000UX\u0001\u0000\u0000\u0000VT\u0001"+
		"\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000WY\u0001\u0000\u0000\u0000"+
		"XV\u0001\u0000\u0000\u0000YZ\u00051\u0000\u0000Z\u0003\u0001\u0000\u0000"+
		"\u0000[\\\u0005\u0012\u0000\u0000\\]\u00034\u001a\u0000]\u0005\u0001\u0000"+
		"\u0000\u0000^_\u0005\u0001\u0000\u0000_`\u0003\f\u0006\u0000`\u0007\u0001"+
		"\u0000\u0000\u0000aq\u0003,\u0016\u0000bq\u0003\n\u0005\u0000cq\u0003"+
		"\u000e\u0007\u0000dq\u0003\u0012\t\u0000eq\u0003.\u0017\u0000fq\u0003"+
		"6\u001b\u0000gq\u00038\u001c\u0000hq\u00034\u001a\u0000iq\u0003:\u001d"+
		"\u0000jq\u0003(\u0014\u0000kq\u0003*\u0015\u0000lq\u0003\u001e\u000f\u0000"+
		"mq\u0003<\u001e\u0000nq\u0003\"\u0011\u0000oq\u0003F#\u0000pa\u0001\u0000"+
		"\u0000\u0000pb\u0001\u0000\u0000\u0000pc\u0001\u0000\u0000\u0000pd\u0001"+
		"\u0000\u0000\u0000pe\u0001\u0000\u0000\u0000pf\u0001\u0000\u0000\u0000"+
		"pg\u0001\u0000\u0000\u0000ph\u0001\u0000\u0000\u0000pi\u0001\u0000\u0000"+
		"\u0000pj\u0001\u0000\u0000\u0000pk\u0001\u0000\u0000\u0000pl\u0001\u0000"+
		"\u0000\u0000pm\u0001\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000po\u0001"+
		"\u0000\u0000\u0000q\t\u0001\u0000\u0000\u0000rs\u0005\u0002\u0000\u0000"+
		"st\u0003\f\u0006\u0000t\u000b\u0001\u0000\u0000\u0000uw\u0005+\u0000\u0000"+
		"vx\u0003\u0010\b\u0000wv\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000"+
		"x\r\u0001\u0000\u0000\u0000y}\u0005+\u0000\u0000z|\u0003&\u0013\u0000"+
		"{z\u0001\u0000\u0000\u0000|\u007f\u0001\u0000\u0000\u0000}{\u0001\u0000"+
		"\u0000\u0000}~\u0001\u0000\u0000\u0000~\u0083\u0001\u0000\u0000\u0000"+
		"\u007f}\u0001\u0000\u0000\u0000\u0080\u0082\u0003\u001a\r\u0000\u0081"+
		"\u0080\u0001\u0000\u0000\u0000\u0082\u0085\u0001\u0000\u0000\u0000\u0083"+
		"\u0081\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000\u0000\u0084"+
		"\u0086\u0001\u0000\u0000\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0086"+
		"\u0087\u0003\u0010\b\u0000\u0087\u000f\u0001\u0000\u0000\u0000\u0088\u0089"+
		"\u00054\u0000\u0000\u0089\u008f\u0003 \u0010\u0000\u008a\u008b\u00054"+
		"\u0000\u0000\u008b\u008f\u0003\u0016\u000b\u0000\u008c\u008d\u00054\u0000"+
		"\u0000\u008d\u008f\u0003F#\u0000\u008e\u0088\u0001\u0000\u0000\u0000\u008e"+
		"\u008a\u0001\u0000\u0000\u0000\u008e\u008c\u0001\u0000\u0000\u0000\u008f"+
		"\u0011\u0001\u0000\u0000\u0000\u0090\u0091\u0005\u0010\u0000\u0000\u0091"+
		"\u0092\u0005+\u0000\u0000\u0092\u0094\u0005,\u0000\u0000\u0093\u0095\u0003"+
		"B!\u0000\u0094\u0093\u0001\u0000\u0000\u0000\u0094\u0095\u0001\u0000\u0000"+
		"\u0000\u0095\u0096\u0001\u0000\u0000\u0000\u0096\u0097\u0005-\u0000\u0000"+
		"\u0097\u0098\u00034\u001a\u0000\u0098\u0013\u0001\u0000\u0000\u0000\u0099"+
		"\u009a\u0005+\u0000\u0000\u009a\u009c\u0005,\u0000\u0000\u009b\u009d\u0003"+
		"D\"\u0000\u009c\u009b\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000"+
		"\u0000\u0000\u009d\u009e\u0001\u0000\u0000\u0000\u009e\u009f\u0005-\u0000"+
		"\u0000\u009f\u0015\u0001\u0000\u0000\u0000\u00a0\u00a9\u0005.\u0000\u0000"+
		"\u00a1\u00a6\u0003\u0018\f\u0000\u00a2\u00a3\u00052\u0000\u0000\u00a3"+
		"\u00a5\u0003\u0018\f\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000\u00a5\u00a8"+
		"\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001\u0000\u0000\u0000\u00a6\u00a7"+
		"\u0001\u0000\u0000\u0000\u00a7\u00aa\u0001\u0000\u0000\u0000\u00a8\u00a6"+
		"\u0001\u0000\u0000\u0000\u00a9\u00a1\u0001\u0000\u0000\u0000\u00a9\u00aa"+
		"\u0001\u0000\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000\u0000\u00ab\u00ac"+
		"\u0005/\u0000\u0000\u00ac\u0017\u0001\u0000\u0000\u0000\u00ad\u00b0\u0003"+
		"F#\u0000\u00ae\u00b0\u0003\u0016\u000b\u0000\u00af\u00ad\u0001\u0000\u0000"+
		"\u0000\u00af\u00ae\u0001\u0000\u0000\u0000\u00b0\u0019\u0001\u0000\u0000"+
		"\u0000\u00b1\u00b2\u0005.\u0000\u0000\u00b2\u00b3\u0005(\u0000\u0000\u00b3"+
		"\u00b8\u0005/\u0000\u0000\u00b4\u00b5\u0005.\u0000\u0000\u00b5\u00b6\u0005"+
		"+\u0000\u0000\u00b6\u00b8\u0005/\u0000\u0000\u00b7\u00b1\u0001\u0000\u0000"+
		"\u0000\u00b7\u00b4\u0001\u0000\u0000\u0000\u00b8\u001b\u0001\u0000\u0000"+
		"\u0000\u00b9\u00ba\u0005\u0003\u0000\u0000\u00ba\u00bb\u0005,\u0000\u0000"+
		"\u00bb\u00bc\u0005+\u0000\u0000\u00bc\u00bd\u0005-\u0000\u0000\u00bd\u001d"+
		"\u0001\u0000\u0000\u0000\u00be\u00bf\u0005+\u0000\u0000\u00bf\u00c0\u0005"+
		"3\u0000\u0000\u00c0\u00c1\u0005\u0004\u0000\u0000\u00c1\u00c2\u0005,\u0000"+
		"\u0000\u00c2\u00c3\u0005-\u0000\u0000\u00c3\u001f\u0001\u0000\u0000\u0000"+
		"\u00c4\u00c5\u0005+\u0000\u0000\u00c5\u00cb\u00050\u0000\u0000\u00c6\u00c7"+
		"\u0003$\u0012\u0000\u00c7\u00c8\u0003\u0010\b\u0000\u00c8\u00ca\u0001"+
		"\u0000\u0000\u0000\u00c9\u00c6\u0001\u0000\u0000\u0000\u00ca\u00cd\u0001"+
		"\u0000\u0000\u0000\u00cb\u00c9\u0001\u0000\u0000\u0000\u00cb\u00cc\u0001"+
		"\u0000\u0000\u0000\u00cc\u00ce\u0001\u0000\u0000\u0000\u00cd\u00cb\u0001"+
		"\u0000\u0000\u0000\u00ce\u00cf\u00051\u0000\u0000\u00cf!\u0001\u0000\u0000"+
		"\u0000\u00d0\u00d1\u0005\u0005\u0000\u0000\u00d1\u00d2\u0005+\u0000\u0000"+
		"\u00d2\u00d4\u00050\u0000\u0000\u00d3\u00d5\u0003$\u0012\u0000\u00d4\u00d3"+
		"\u0001\u0000\u0000\u0000\u00d5\u00d6\u0001\u0000\u0000\u0000\u00d6\u00d4"+
		"\u0001\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7\u00d8"+
		"\u0001\u0000\u0000\u0000\u00d8\u00d9\u00051\u0000\u0000\u00d9#\u0001\u0000"+
		"\u0000\u0000\u00da\u00db\u0005+\u0000\u0000\u00db%\u0001\u0000\u0000\u0000"+
		"\u00dc\u00dd\u00053\u0000\u0000\u00dd\u00e1\u0005+\u0000\u0000\u00de\u00e0"+
		"\u0003\u001a\r\u0000\u00df\u00de\u0001\u0000\u0000\u0000\u00e0\u00e3\u0001"+
		"\u0000\u0000\u0000\u00e1\u00df\u0001\u0000\u0000\u0000\u00e1\u00e2\u0001"+
		"\u0000\u0000\u0000\u00e2\'\u0001\u0000\u0000\u0000\u00e3\u00e1\u0001\u0000"+
		"\u0000\u0000\u00e4\u00e5\u0005+\u0000\u0000\u00e5\u00e6\u0005\u001d\u0000"+
		"\u0000\u00e6\u00e7\u0003F#\u0000\u00e7)\u0001\u0000\u0000\u0000\u00e8"+
		"\u00e9\u0005+\u0000\u0000\u00e9\u00ea\u0005\u001e\u0000\u0000\u00ea\u00eb"+
		"\u0003F#\u0000\u00eb+\u0001\u0000\u0000\u0000\u00ec\u00ed\u0005\f\u0000"+
		"\u0000\u00ed\u00ee\u0005,\u0000\u0000\u00ee\u00f3\u0003F#\u0000\u00ef"+
		"\u00f0\u0005\u0013\u0000\u0000\u00f0\u00f2\u0003F#\u0000\u00f1\u00ef\u0001"+
		"\u0000\u0000\u0000\u00f2\u00f5\u0001\u0000\u0000\u0000\u00f3\u00f1\u0001"+
		"\u0000\u0000\u0000\u00f3\u00f4\u0001\u0000\u0000\u0000\u00f4\u00f6\u0001"+
		"\u0000\u0000\u0000\u00f5\u00f3\u0001\u0000\u0000\u0000\u00f6\u00f7\u0005"+
		"-\u0000\u0000\u00f7-\u0001\u0000\u0000\u0000\u00f8\u00f9\u0005\b\u0000"+
		"\u0000\u00f9\u00fa\u0005,\u0000\u0000\u00fa\u00fb\u0003F#\u0000\u00fb"+
		"\u00fc\u0005-\u0000\u0000\u00fc\u00fe\u00034\u001a\u0000\u00fd\u00ff\u0003"+
		"0\u0018\u0000\u00fe\u00fd\u0001\u0000\u0000\u0000\u00fe\u00ff\u0001\u0000"+
		"\u0000\u0000\u00ff\u0101\u0001\u0000\u0000\u0000\u0100\u0102\u00032\u0019"+
		"\u0000\u0101\u0100\u0001\u0000\u0000\u0000\u0101\u0102\u0001\u0000\u0000"+
		"\u0000\u0102/\u0001\u0000\u0000\u0000\u0103\u0104\u0005\t\u0000\u0000"+
		"\u0104\u0105\u0005,\u0000\u0000\u0105\u0106\u0003F#\u0000\u0106\u0107"+
		"\u0005-\u0000\u0000\u0107\u0109\u00034\u001a\u0000\u0108\u010a\u00030"+
		"\u0018\u0000\u0109\u0108\u0001\u0000\u0000\u0000\u0109\u010a\u0001\u0000"+
		"\u0000\u0000\u010a1\u0001\u0000\u0000\u0000\u010b\u010c\u0005\n\u0000"+
		"\u0000\u010c\u010d\u00034\u001a\u0000\u010d3\u0001\u0000\u0000\u0000\u010e"+
		"\u0112\u00050\u0000\u0000\u010f\u0111\u0003\b\u0004\u0000\u0110\u010f"+
		"\u0001\u0000\u0000\u0000\u0111\u0114\u0001\u0000\u0000\u0000\u0112\u0110"+
		"\u0001\u0000\u0000\u0000\u0112\u0113\u0001\u0000\u0000\u0000\u0113\u0115"+
		"\u0001\u0000\u0000\u0000\u0114\u0112\u0001\u0000\u0000\u0000\u0115\u0116"+
		"\u00051\u0000\u0000\u01165\u0001\u0000\u0000\u0000\u0117\u0118\u0005\r"+
		"\u0000\u0000\u0118\u0119\u0005+\u0000\u0000\u0119\u011a\u0005\u000e\u0000"+
		"\u0000\u011a\u011b\u0005+\u0000\u0000\u011b\u011c\u00034\u001a\u0000\u011c"+
		"7\u0001\u0000\u0000\u0000\u011d\u011e\u0005\u000f\u0000\u0000\u011e\u011f"+
		"\u0005,\u0000\u0000\u011f\u0120\u0003F#\u0000\u0120\u0121\u0005-\u0000"+
		"\u0000\u0121\u0122\u00034\u001a\u0000\u01229\u0001\u0000\u0000\u0000\u0123"+
		"\u0124\u0005\u000b\u0000\u0000\u0124\u0125\u0003F#\u0000\u0125;\u0001"+
		"\u0000\u0000\u0000\u0126\u0127\u0005\u0006\u0000\u0000\u0127\u0128\u0005"+
		",\u0000\u0000\u0128\u012b\u0005+\u0000\u0000\u0129\u012a\u00052\u0000"+
		"\u0000\u012a\u012c\u0003@ \u0000\u012b\u0129\u0001\u0000\u0000\u0000\u012b"+
		"\u012c\u0001\u0000\u0000\u0000\u012c\u012d\u0001\u0000\u0000\u0000\u012d"+
		"\u012f\u0005-\u0000\u0000\u012e\u0130\u0005\u0011\u0000\u0000\u012f\u012e"+
		"\u0001\u0000\u0000\u0000\u012f\u0130\u0001\u0000\u0000\u0000\u0130=\u0001"+
		"\u0000\u0000\u0000\u0131\u0132\u0005\u0007\u0000\u0000\u0132\u0133\u0005"+
		"\u000e\u0000\u0000\u0133\u0138\u0003@ \u0000\u0134\u0135\u0005\u0007\u0000"+
		"\u0000\u0135\u0136\u0005\u000e\u0000\u0000\u0136\u0138\u0005+\u0000\u0000"+
		"\u0137\u0131\u0001\u0000\u0000\u0000\u0137\u0134\u0001\u0000\u0000\u0000"+
		"\u0138?\u0001\u0000\u0000\u0000\u0139\u013a\u0003F#\u0000\u013a\u013b"+
		"\u00053\u0000\u0000\u013b\u013c\u00053\u0000\u0000\u013c\u013d\u0003F"+
		"#\u0000\u013dA\u0001\u0000\u0000\u0000\u013e\u0143\u0005+\u0000\u0000"+
		"\u013f\u0140\u00052\u0000\u0000\u0140\u0142\u0005+\u0000\u0000\u0141\u013f"+
		"\u0001\u0000\u0000\u0000\u0142\u0145\u0001\u0000\u0000\u0000\u0143\u0141"+
		"\u0001\u0000\u0000\u0000\u0143\u0144\u0001\u0000\u0000\u0000\u0144C\u0001"+
		"\u0000\u0000\u0000\u0145\u0143\u0001\u0000\u0000\u0000\u0146\u014b\u0003"+
		"F#\u0000\u0147\u0148\u00052\u0000\u0000\u0148\u014a\u0003F#\u0000\u0149"+
		"\u0147\u0001\u0000\u0000\u0000\u014a\u014d\u0001\u0000\u0000\u0000\u014b"+
		"\u0149\u0001\u0000\u0000\u0000\u014b\u014c\u0001\u0000\u0000\u0000\u014c"+
		"E\u0001\u0000\u0000\u0000\u014d\u014b\u0001\u0000\u0000\u0000\u014e\u014f"+
		"\u0006#\uffff\uffff\u0000\u014f\u0177\u0003\u0014\n\u0000\u0150\u0152"+
		"\u0005+\u0000\u0000\u0151\u0153\u0003&\u0013\u0000\u0152\u0151\u0001\u0000"+
		"\u0000\u0000\u0153\u0154\u0001\u0000\u0000\u0000\u0154\u0152\u0001\u0000"+
		"\u0000\u0000\u0154\u0155\u0001\u0000\u0000\u0000\u0155\u0177\u0001\u0000"+
		"\u0000\u0000\u0156\u0158\u0005+\u0000\u0000\u0157\u0159\u0003\u001a\r"+
		"\u0000\u0158\u0157\u0001\u0000\u0000\u0000\u0159\u015a\u0001\u0000\u0000"+
		"\u0000\u015a\u0158\u0001\u0000\u0000\u0000\u015a\u015b\u0001\u0000\u0000"+
		"\u0000\u015b\u0177\u0001\u0000\u0000\u0000\u015c\u0177\u0003\u001c\u000e"+
		"\u0000\u015d\u0177\u0003>\u001f\u0000\u015e\u015f\u0005\"\u0000\u0000"+
		"\u015f\u0177\u0003F#\n\u0160\u0161\u0005%\u0000\u0000\u0161\u0162\u0005"+
		",\u0000\u0000\u0162\u0163\u0003F#\u0000\u0163\u0164\u0005-\u0000\u0000"+
		"\u0164\u0177\u0001\u0000\u0000\u0000\u0165\u0166\u0005&\u0000\u0000\u0166"+
		"\u0167\u0005,\u0000\u0000\u0167\u0168\u0003F#\u0000\u0168\u0169\u0005"+
		"2\u0000\u0000\u0169\u016a\u0003F#\u0000\u016a\u016b\u0005-\u0000\u0000"+
		"\u016b\u0177\u0001\u0000\u0000\u0000\u016c\u016d\u0005,\u0000\u0000\u016d"+
		"\u016e\u0003F#\u0000\u016e\u016f\u0005-\u0000\u0000\u016f\u0177\u0001"+
		"\u0000\u0000\u0000\u0170\u0177\u0005+\u0000\u0000\u0171\u0177\u0005(\u0000"+
		"\u0000\u0172\u0177\u0005)\u0000\u0000\u0173\u0177\u0005*\u0000\u0000\u0174"+
		"\u0177\u0005#\u0000\u0000\u0175\u0177\u0005$\u0000\u0000\u0176\u014e\u0001"+
		"\u0000\u0000\u0000\u0176\u0150\u0001\u0000\u0000\u0000\u0176\u0156\u0001"+
		"\u0000\u0000\u0000\u0176\u015c\u0001\u0000\u0000\u0000\u0176\u015d\u0001"+
		"\u0000\u0000\u0000\u0176\u015e\u0001\u0000\u0000\u0000\u0176\u0160\u0001"+
		"\u0000\u0000\u0000\u0176\u0165\u0001\u0000\u0000\u0000\u0176\u016c\u0001"+
		"\u0000\u0000\u0000\u0176\u0170\u0001\u0000\u0000\u0000\u0176\u0171\u0001"+
		"\u0000\u0000\u0000\u0176\u0172\u0001\u0000\u0000\u0000\u0176\u0173\u0001"+
		"\u0000\u0000\u0000\u0176\u0174\u0001\u0000\u0000\u0000\u0176\u0175\u0001"+
		"\u0000\u0000\u0000\u0177\u0186\u0001\u0000\u0000\u0000\u0178\u0179\n\u000e"+
		"\u0000\u0000\u0179\u017a\u0007\u0000\u0000\u0000\u017a\u0185\u0003F#\u000f"+
		"\u017b\u017c\n\r\u0000\u0000\u017c\u017d\u0007\u0001\u0000\u0000\u017d"+
		"\u0185\u0003F#\u000e\u017e\u017f\n\f\u0000\u0000\u017f\u0180\u0007\u0002"+
		"\u0000\u0000\u0180\u0185\u0003F#\r\u0181\u0182\n\u000b\u0000\u0000\u0182"+
		"\u0183\u0007\u0003\u0000\u0000\u0183\u0185\u0003F#\f\u0184\u0178\u0001"+
		"\u0000\u0000\u0000\u0184\u017b\u0001\u0000\u0000\u0000\u0184\u017e\u0001"+
		"\u0000\u0000\u0000\u0184\u0181\u0001\u0000\u0000\u0000\u0185\u0188\u0001"+
		"\u0000\u0000\u0000\u0186\u0184\u0001\u0000\u0000\u0000\u0186\u0187\u0001"+
		"\u0000\u0000\u0000\u0187G\u0001\u0000\u0000\u0000\u0188\u0186\u0001\u0000"+
		"\u0000\u0000 LTVpw}\u0083\u008e\u0094\u009c\u00a6\u00a9\u00af\u00b7\u00cb"+
		"\u00d6\u00e1\u00f3\u00fe\u0101\u0109\u0112\u012b\u012f\u0137\u0143\u014b"+
		"\u0154\u015a\u0176\u0184\u0186";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}