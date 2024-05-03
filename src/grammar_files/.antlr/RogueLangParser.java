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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, IF=7, ELIF=8, ELSE=9, 
		RETURN=10, PRINT=11, FOR=12, IN=13, WHILE=14, DEF=15, LAYER=16, PROCEDURE=17, 
		PLUS=18, MINUS=19, MULT=20, DIV=21, GT=22, GTE=23, LT=24, LTE=25, EQ=26, 
		NEQ=27, PEQ=28, MEQ=29, MOD=30, AND=31, OR=32, NOT=33, TRUE=34, FALSE=35, 
		SQRT=36, POW=37, COMMENT_SINGLELINE=38, INT=39, FLOAT=40, STRING=41, ID=42, 
		OPEN_PARENTH=43, CLOSED_PARENTH=44, OPEN_BRACK=45, CLOSED_BRACK=46, OPEN_CURL=47, 
		CLOSED_CURL=48, COMMA=49, DOT=50, EQUAL_SIGN=51, WS=52;
	public static final int
		RULE_prog = 0, RULE_object = 1, RULE_procedure = 2, RULE_field = 3, RULE_stat = 4, 
		RULE_varDeclStat = 5, RULE_varDecl = 6, RULE_assignStat = 7, RULE_assignment = 8, 
		RULE_functionDecl = 9, RULE_functionCall = 10, RULE_list = 11, RULE_listElement = 12, 
		RULE_listLength = 13, RULE_listPop = 14, RULE_plusEquals = 15, RULE_minusEquals = 16, 
		RULE_printStat = 17, RULE_ifStat = 18, RULE_elifStat = 19, RULE_elseStat = 20, 
		RULE_statBlock = 21, RULE_forLoop = 22, RULE_whileLoop = 23, RULE_returnStat = 24, 
		RULE_whiteNoiseStat = 25, RULE_random = 26, RULE_range = 27, RULE_params = 28, 
		RULE_args = 29, RULE_expr = 30;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "object", "procedure", "field", "stat", "varDeclStat", "varDecl", 
			"assignStat", "assignment", "functionDecl", "functionCall", "list", "listElement", 
			"listLength", "listPop", "plusEquals", "minusEquals", "printStat", "ifStat", 
			"elifStat", "elseStat", "statBlock", "forLoop", "whileLoop", "returnStat", 
			"whiteNoiseStat", "random", "range", "params", "args", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'field'", "'let'", "'len'", "'pop'", "'WhiteNoise'", "'random'", 
			"'if'", "'elif'", "'else'", "'return'", "'print'", "'for'", "'in'", "'while'", 
			"'def'", "'layer'", "'procedure'", "'+'", "'-'", "'*'", "'/'", "'>'", 
			"'>='", "'<'", "'<='", "'=='", "'!='", "'+='", "'-='", "'%'", "'and'", 
			"'or'", "'not'", "'True'", "'False'", "'sqrt'", "'pow'", null, null, 
			null, null, null, "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'.'", 
			"'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "IF", "ELIF", "ELSE", "RETURN", 
			"PRINT", "FOR", "IN", "WHILE", "DEF", "LAYER", "PROCEDURE", "PLUS", "MINUS", 
			"MULT", "DIV", "GT", "GTE", "LT", "LTE", "EQ", "NEQ", "PEQ", "MEQ", "MOD", 
			"AND", "OR", "NOT", "TRUE", "FALSE", "SQRT", "POW", "COMMENT_SINGLELINE", 
			"INT", "FLOAT", "STRING", "ID", "OPEN_PARENTH", "CLOSED_PARENTH", "OPEN_BRACK", 
			"CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", "COMMA", "DOT", "EQUAL_SIGN", 
			"WS"
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
			setState(62);
			object();
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 158046206614764L) != 0)) {
				{
				{
				setState(63);
				stat();
				}
				}
				setState(68);
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
			setState(69);
			match(ID);
			setState(70);
			match(OPEN_CURL);
			setState(71);
			procedure();
			setState(76);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 158046206614766L) != 0)) {
				{
				setState(74);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__0:
					{
					setState(72);
					field();
					}
					break;
				case T__1:
				case T__2:
				case T__4:
				case T__5:
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
					setState(73);
					stat();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(78);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(79);
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
			setState(81);
			match(PROCEDURE);
			setState(82);
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
			setState(84);
			match(T__0);
			setState(85);
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
			setState(101);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(87);
				printStat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(88);
				varDeclStat();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(89);
				assignStat();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(90);
				functionDecl();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(91);
				ifStat();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(92);
				forLoop();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(93);
				whileLoop();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(94);
				statBlock();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(95);
				returnStat();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(96);
				plusEquals();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(97);
				minusEquals();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(98);
				listPop();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(99);
				whiteNoiseStat();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(100);
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
			setState(103);
			match(T__1);
			setState(104);
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
			setState(106);
			match(ID);
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL_SIGN) {
				{
				setState(107);
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
		public AssignStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignStat; }
	}

	public final AssignStatContext assignStat() throws RecognitionException {
		AssignStatContext _localctx = new AssignStatContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assignStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			match(ID);
			setState(111);
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
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
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
			setState(117);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(113);
				match(EQUAL_SIGN);
				setState(114);
				expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(115);
				match(EQUAL_SIGN);
				setState(116);
				list();
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
			setState(119);
			match(DEF);
			setState(120);
			match(ID);
			setState(121);
			match(OPEN_PARENTH);
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(122);
				params();
				}
			}

			setState(125);
			match(CLOSED_PARENTH);
			setState(126);
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
			setState(128);
			match(ID);
			setState(129);
			match(OPEN_PARENTH);
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17308718202952L) != 0)) {
				{
				setState(130);
				args();
				}
			}

			setState(133);
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
			setState(135);
			match(OPEN_BRACK);
			setState(144);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17308718202952L) != 0)) {
				{
				setState(136);
				expr(0);
				setState(141);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(137);
					match(COMMA);
					setState(138);
					expr(0);
					}
					}
					setState(143);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(146);
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
		public List<TerminalNode> ID() { return getTokens(RogueLangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(RogueLangParser.ID, i);
		}
		public TerminalNode OPEN_BRACK() { return getToken(RogueLangParser.OPEN_BRACK, 0); }
		public TerminalNode INT() { return getToken(RogueLangParser.INT, 0); }
		public TerminalNode CLOSED_BRACK() { return getToken(RogueLangParser.CLOSED_BRACK, 0); }
		public ListElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listElement; }
	}

	public final ListElementContext listElement() throws RecognitionException {
		ListElementContext _localctx = new ListElementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_listElement);
		try {
			setState(156);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				match(ID);
				setState(149);
				match(OPEN_BRACK);
				setState(150);
				match(INT);
				setState(151);
				match(CLOSED_BRACK);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(152);
				match(ID);
				setState(153);
				match(OPEN_BRACK);
				setState(154);
				match(ID);
				setState(155);
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
		enterRule(_localctx, 26, RULE_listLength);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(T__2);
			setState(159);
			match(OPEN_PARENTH);
			setState(160);
			match(ID);
			setState(161);
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
		enterRule(_localctx, 28, RULE_listPop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(ID);
			setState(164);
			match(DOT);
			setState(165);
			match(T__3);
			setState(166);
			match(OPEN_PARENTH);
			setState(167);
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
		enterRule(_localctx, 30, RULE_plusEquals);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(ID);
			setState(170);
			match(PEQ);
			setState(171);
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
		enterRule(_localctx, 32, RULE_minusEquals);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			match(ID);
			setState(174);
			match(MEQ);
			setState(175);
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
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public PrintStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStat; }
	}

	public final PrintStatContext printStat() throws RecognitionException {
		PrintStatContext _localctx = new PrintStatContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_printStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			match(PRINT);
			setState(178);
			match(OPEN_PARENTH);
			setState(179);
			expr(0);
			setState(180);
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
		enterRule(_localctx, 36, RULE_ifStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(IF);
			setState(183);
			match(OPEN_PARENTH);
			setState(184);
			expr(0);
			setState(185);
			match(CLOSED_PARENTH);
			setState(186);
			statBlock();
			setState(188);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELIF) {
				{
				setState(187);
				elifStat();
				}
			}

			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(190);
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
		enterRule(_localctx, 38, RULE_elifStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			match(ELIF);
			setState(194);
			match(OPEN_PARENTH);
			setState(195);
			expr(0);
			setState(196);
			match(CLOSED_PARENTH);
			setState(197);
			statBlock();
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELIF) {
				{
				setState(198);
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
		enterRule(_localctx, 40, RULE_elseStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			match(ELSE);
			setState(202);
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
		enterRule(_localctx, 42, RULE_statBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			match(OPEN_CURL);
			setState(208);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 158046206614764L) != 0)) {
				{
				{
				setState(205);
				stat();
				}
				}
				setState(210);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(211);
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
		enterRule(_localctx, 44, RULE_forLoop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(FOR);
			setState(214);
			match(ID);
			setState(215);
			match(IN);
			setState(216);
			match(ID);
			setState(217);
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
		enterRule(_localctx, 46, RULE_whileLoop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			match(WHILE);
			setState(220);
			match(OPEN_PARENTH);
			setState(221);
			expr(0);
			setState(222);
			match(CLOSED_PARENTH);
			setState(223);
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
		enterRule(_localctx, 48, RULE_returnStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(RETURN);
			setState(226);
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
		public Token arrayParam;
		public RangeContext rangeParam;
		public TerminalNode OPEN_PARENTH() { return getToken(RogueLangParser.OPEN_PARENTH, 0); }
		public TerminalNode COMMA() { return getToken(RogueLangParser.COMMA, 0); }
		public TerminalNode CLOSED_PARENTH() { return getToken(RogueLangParser.CLOSED_PARENTH, 0); }
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
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
		enterRule(_localctx, 50, RULE_whiteNoiseStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(T__4);
			setState(229);
			match(OPEN_PARENTH);
			setState(230);
			((WhiteNoiseStatContext)_localctx).arrayParam = match(ID);
			setState(231);
			match(COMMA);
			setState(232);
			((WhiteNoiseStatContext)_localctx).rangeParam = range();
			setState(233);
			match(CLOSED_PARENTH);
			setState(235);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LAYER) {
				{
				setState(234);
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
		enterRule(_localctx, 52, RULE_random);
		try {
			setState(243);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(237);
				match(T__5);
				setState(238);
				match(IN);
				setState(239);
				range();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(240);
				match(T__5);
				setState(241);
				match(IN);
				setState(242);
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
		enterRule(_localctx, 54, RULE_range);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			expr(0);
			setState(246);
			match(DOT);
			setState(247);
			match(DOT);
			setState(248);
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
		enterRule(_localctx, 56, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			match(ID);
			setState(255);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(251);
				match(COMMA);
				setState(252);
				match(ID);
				}
				}
				setState(257);
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
		enterRule(_localctx, 58, RULE_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			expr(0);
			setState(263);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(259);
				match(COMMA);
				setState(260);
				expr(0);
				}
				}
				setState(265);
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
		public ListElementContext listElement() {
			return getRuleContext(ListElementContext.class,0);
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
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
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
		int _startState = 60;
		enterRecursionRule(_localctx, 60, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(295);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(267);
				functionCall();
				}
				break;
			case 2:
				{
				setState(268);
				listElement();
				}
				break;
			case 3:
				{
				setState(269);
				listLength();
				}
				break;
			case 4:
				{
				setState(270);
				random();
				}
				break;
			case 5:
				{
				setState(271);
				match(NOT);
				setState(272);
				expr(10);
				}
				break;
			case 6:
				{
				setState(273);
				match(SQRT);
				setState(274);
				match(OPEN_PARENTH);
				setState(275);
				expr(0);
				setState(276);
				match(CLOSED_PARENTH);
				}
				break;
			case 7:
				{
				setState(278);
				match(POW);
				setState(279);
				match(OPEN_PARENTH);
				setState(280);
				expr(0);
				setState(281);
				match(COMMA);
				setState(282);
				expr(0);
				setState(283);
				match(CLOSED_PARENTH);
				}
				break;
			case 8:
				{
				setState(285);
				match(OPEN_PARENTH);
				setState(286);
				expr(0);
				setState(287);
				match(CLOSED_PARENTH);
				}
				break;
			case 9:
				{
				setState(289);
				match(ID);
				}
				break;
			case 10:
				{
				setState(290);
				match(INT);
				}
				break;
			case 11:
				{
				setState(291);
				match(FLOAT);
				}
				break;
			case 12:
				{
				setState(292);
				match(STRING);
				}
				break;
			case 13:
				{
				setState(293);
				match(TRUE);
				}
				break;
			case 14:
				{
				setState(294);
				match(FALSE);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(311);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(309);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(297);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(298);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1076887552L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(299);
						expr(15);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(300);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(301);
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
						setState(302);
						expr(14);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(303);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(304);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 264241152L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(305);
						expr(13);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(306);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(307);
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
						setState(308);
						expr(12);
						}
						break;
					}
					} 
				}
				setState(313);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
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
		case 30:
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
		"\u0004\u00014\u013b\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0001\u0000\u0001\u0000\u0005\u0000A\b\u0000\n\u0000\f\u0000D\t\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001"+
		"K\b\u0001\n\u0001\f\u0001N\t\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0003\u0004f\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0003\u0006m\b\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bv\b\b\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0003\t|\b\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0003\n\u0084\b\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0005\u000b\u008c\b\u000b\n\u000b\f\u000b\u008f\t\u000b"+
		"\u0003\u000b\u0091\b\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u009d\b\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00bd\b\u0012\u0001\u0012"+
		"\u0003\u0012\u00c0\b\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0003\u0013\u00c8\b\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0015\u0001\u0015\u0005\u0015\u00cf\b\u0015\n\u0015"+
		"\f\u0015\u00d2\t\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0003\u0019\u00ec\b\u0019\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u00f4\b\u001a"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001c"+
		"\u0001\u001c\u0001\u001c\u0005\u001c\u00fe\b\u001c\n\u001c\f\u001c\u0101"+
		"\t\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0005\u001d\u0106\b\u001d"+
		"\n\u001d\f\u001d\u0109\t\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0003\u001e\u0128\b\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0005\u001e\u0136\b\u001e\n"+
		"\u001e\f\u001e\u0139\t\u001e\u0001\u001e\u0000\u0001<\u001f\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e"+
		" \"$&(*,.02468:<\u0000\u0004\u0002\u0000\u0014\u0015\u001e\u001e\u0001"+
		"\u0000\u0012\u0013\u0001\u0000\u0016\u001b\u0001\u0000\u001f \u014b\u0000"+
		">\u0001\u0000\u0000\u0000\u0002E\u0001\u0000\u0000\u0000\u0004Q\u0001"+
		"\u0000\u0000\u0000\u0006T\u0001\u0000\u0000\u0000\be\u0001\u0000\u0000"+
		"\u0000\ng\u0001\u0000\u0000\u0000\fj\u0001\u0000\u0000\u0000\u000en\u0001"+
		"\u0000\u0000\u0000\u0010u\u0001\u0000\u0000\u0000\u0012w\u0001\u0000\u0000"+
		"\u0000\u0014\u0080\u0001\u0000\u0000\u0000\u0016\u0087\u0001\u0000\u0000"+
		"\u0000\u0018\u009c\u0001\u0000\u0000\u0000\u001a\u009e\u0001\u0000\u0000"+
		"\u0000\u001c\u00a3\u0001\u0000\u0000\u0000\u001e\u00a9\u0001\u0000\u0000"+
		"\u0000 \u00ad\u0001\u0000\u0000\u0000\"\u00b1\u0001\u0000\u0000\u0000"+
		"$\u00b6\u0001\u0000\u0000\u0000&\u00c1\u0001\u0000\u0000\u0000(\u00c9"+
		"\u0001\u0000\u0000\u0000*\u00cc\u0001\u0000\u0000\u0000,\u00d5\u0001\u0000"+
		"\u0000\u0000.\u00db\u0001\u0000\u0000\u00000\u00e1\u0001\u0000\u0000\u0000"+
		"2\u00e4\u0001\u0000\u0000\u00004\u00f3\u0001\u0000\u0000\u00006\u00f5"+
		"\u0001\u0000\u0000\u00008\u00fa\u0001\u0000\u0000\u0000:\u0102\u0001\u0000"+
		"\u0000\u0000<\u0127\u0001\u0000\u0000\u0000>B\u0003\u0002\u0001\u0000"+
		"?A\u0003\b\u0004\u0000@?\u0001\u0000\u0000\u0000AD\u0001\u0000\u0000\u0000"+
		"B@\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000C\u0001\u0001\u0000"+
		"\u0000\u0000DB\u0001\u0000\u0000\u0000EF\u0005*\u0000\u0000FG\u0005/\u0000"+
		"\u0000GL\u0003\u0004\u0002\u0000HK\u0003\u0006\u0003\u0000IK\u0003\b\u0004"+
		"\u0000JH\u0001\u0000\u0000\u0000JI\u0001\u0000\u0000\u0000KN\u0001\u0000"+
		"\u0000\u0000LJ\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MO\u0001"+
		"\u0000\u0000\u0000NL\u0001\u0000\u0000\u0000OP\u00050\u0000\u0000P\u0003"+
		"\u0001\u0000\u0000\u0000QR\u0005\u0011\u0000\u0000RS\u0003*\u0015\u0000"+
		"S\u0005\u0001\u0000\u0000\u0000TU\u0005\u0001\u0000\u0000UV\u0003\f\u0006"+
		"\u0000V\u0007\u0001\u0000\u0000\u0000Wf\u0003\"\u0011\u0000Xf\u0003\n"+
		"\u0005\u0000Yf\u0003\u000e\u0007\u0000Zf\u0003\u0012\t\u0000[f\u0003$"+
		"\u0012\u0000\\f\u0003,\u0016\u0000]f\u0003.\u0017\u0000^f\u0003*\u0015"+
		"\u0000_f\u00030\u0018\u0000`f\u0003\u001e\u000f\u0000af\u0003 \u0010\u0000"+
		"bf\u0003\u001c\u000e\u0000cf\u00032\u0019\u0000df\u0003<\u001e\u0000e"+
		"W\u0001\u0000\u0000\u0000eX\u0001\u0000\u0000\u0000eY\u0001\u0000\u0000"+
		"\u0000eZ\u0001\u0000\u0000\u0000e[\u0001\u0000\u0000\u0000e\\\u0001\u0000"+
		"\u0000\u0000e]\u0001\u0000\u0000\u0000e^\u0001\u0000\u0000\u0000e_\u0001"+
		"\u0000\u0000\u0000e`\u0001\u0000\u0000\u0000ea\u0001\u0000\u0000\u0000"+
		"eb\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000ed\u0001\u0000\u0000"+
		"\u0000f\t\u0001\u0000\u0000\u0000gh\u0005\u0002\u0000\u0000hi\u0003\f"+
		"\u0006\u0000i\u000b\u0001\u0000\u0000\u0000jl\u0005*\u0000\u0000km\u0003"+
		"\u0010\b\u0000lk\u0001\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000m\r"+
		"\u0001\u0000\u0000\u0000no\u0005*\u0000\u0000op\u0003\u0010\b\u0000p\u000f"+
		"\u0001\u0000\u0000\u0000qr\u00053\u0000\u0000rv\u0003<\u001e\u0000st\u0005"+
		"3\u0000\u0000tv\u0003\u0016\u000b\u0000uq\u0001\u0000\u0000\u0000us\u0001"+
		"\u0000\u0000\u0000v\u0011\u0001\u0000\u0000\u0000wx\u0005\u000f\u0000"+
		"\u0000xy\u0005*\u0000\u0000y{\u0005+\u0000\u0000z|\u00038\u001c\u0000"+
		"{z\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000"+
		"\u0000}~\u0005,\u0000\u0000~\u007f\u0003*\u0015\u0000\u007f\u0013\u0001"+
		"\u0000\u0000\u0000\u0080\u0081\u0005*\u0000\u0000\u0081\u0083\u0005+\u0000"+
		"\u0000\u0082\u0084\u0003:\u001d\u0000\u0083\u0082\u0001\u0000\u0000\u0000"+
		"\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0085\u0001\u0000\u0000\u0000"+
		"\u0085\u0086\u0005,\u0000\u0000\u0086\u0015\u0001\u0000\u0000\u0000\u0087"+
		"\u0090\u0005-\u0000\u0000\u0088\u008d\u0003<\u001e\u0000\u0089\u008a\u0005"+
		"1\u0000\u0000\u008a\u008c\u0003<\u001e\u0000\u008b\u0089\u0001\u0000\u0000"+
		"\u0000\u008c\u008f\u0001\u0000\u0000\u0000\u008d\u008b\u0001\u0000\u0000"+
		"\u0000\u008d\u008e\u0001\u0000\u0000\u0000\u008e\u0091\u0001\u0000\u0000"+
		"\u0000\u008f\u008d\u0001\u0000\u0000\u0000\u0090\u0088\u0001\u0000\u0000"+
		"\u0000\u0090\u0091\u0001\u0000\u0000\u0000\u0091\u0092\u0001\u0000\u0000"+
		"\u0000\u0092\u0093\u0005.\u0000\u0000\u0093\u0017\u0001\u0000\u0000\u0000"+
		"\u0094\u0095\u0005*\u0000\u0000\u0095\u0096\u0005-\u0000\u0000\u0096\u0097"+
		"\u0005\'\u0000\u0000\u0097\u009d\u0005.\u0000\u0000\u0098\u0099\u0005"+
		"*\u0000\u0000\u0099\u009a\u0005-\u0000\u0000\u009a\u009b\u0005*\u0000"+
		"\u0000\u009b\u009d\u0005.\u0000\u0000\u009c\u0094\u0001\u0000\u0000\u0000"+
		"\u009c\u0098\u0001\u0000\u0000\u0000\u009d\u0019\u0001\u0000\u0000\u0000"+
		"\u009e\u009f\u0005\u0003\u0000\u0000\u009f\u00a0\u0005+\u0000\u0000\u00a0"+
		"\u00a1\u0005*\u0000\u0000\u00a1\u00a2\u0005,\u0000\u0000\u00a2\u001b\u0001"+
		"\u0000\u0000\u0000\u00a3\u00a4\u0005*\u0000\u0000\u00a4\u00a5\u00052\u0000"+
		"\u0000\u00a5\u00a6\u0005\u0004\u0000\u0000\u00a6\u00a7\u0005+\u0000\u0000"+
		"\u00a7\u00a8\u0005,\u0000\u0000\u00a8\u001d\u0001\u0000\u0000\u0000\u00a9"+
		"\u00aa\u0005*\u0000\u0000\u00aa\u00ab\u0005\u001c\u0000\u0000\u00ab\u00ac"+
		"\u0003<\u001e\u0000\u00ac\u001f\u0001\u0000\u0000\u0000\u00ad\u00ae\u0005"+
		"*\u0000\u0000\u00ae\u00af\u0005\u001d\u0000\u0000\u00af\u00b0\u0003<\u001e"+
		"\u0000\u00b0!\u0001\u0000\u0000\u0000\u00b1\u00b2\u0005\u000b\u0000\u0000"+
		"\u00b2\u00b3\u0005+\u0000\u0000\u00b3\u00b4\u0003<\u001e\u0000\u00b4\u00b5"+
		"\u0005,\u0000\u0000\u00b5#\u0001\u0000\u0000\u0000\u00b6\u00b7\u0005\u0007"+
		"\u0000\u0000\u00b7\u00b8\u0005+\u0000\u0000\u00b8\u00b9\u0003<\u001e\u0000"+
		"\u00b9\u00ba\u0005,\u0000\u0000\u00ba\u00bc\u0003*\u0015\u0000\u00bb\u00bd"+
		"\u0003&\u0013\u0000\u00bc\u00bb\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001"+
		"\u0000\u0000\u0000\u00bd\u00bf\u0001\u0000\u0000\u0000\u00be\u00c0\u0003"+
		"(\u0014\u0000\u00bf\u00be\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001\u0000"+
		"\u0000\u0000\u00c0%\u0001\u0000\u0000\u0000\u00c1\u00c2\u0005\b\u0000"+
		"\u0000\u00c2\u00c3\u0005+\u0000\u0000\u00c3\u00c4\u0003<\u001e\u0000\u00c4"+
		"\u00c5\u0005,\u0000\u0000\u00c5\u00c7\u0003*\u0015\u0000\u00c6\u00c8\u0003"+
		"&\u0013\u0000\u00c7\u00c6\u0001\u0000\u0000\u0000\u00c7\u00c8\u0001\u0000"+
		"\u0000\u0000\u00c8\'\u0001\u0000\u0000\u0000\u00c9\u00ca\u0005\t\u0000"+
		"\u0000\u00ca\u00cb\u0003*\u0015\u0000\u00cb)\u0001\u0000\u0000\u0000\u00cc"+
		"\u00d0\u0005/\u0000\u0000\u00cd\u00cf\u0003\b\u0004\u0000\u00ce\u00cd"+
		"\u0001\u0000\u0000\u0000\u00cf\u00d2\u0001\u0000\u0000\u0000\u00d0\u00ce"+
		"\u0001\u0000\u0000\u0000\u00d0\u00d1\u0001\u0000\u0000\u0000\u00d1\u00d3"+
		"\u0001\u0000\u0000\u0000\u00d2\u00d0\u0001\u0000\u0000\u0000\u00d3\u00d4"+
		"\u00050\u0000\u0000\u00d4+\u0001\u0000\u0000\u0000\u00d5\u00d6\u0005\f"+
		"\u0000\u0000\u00d6\u00d7\u0005*\u0000\u0000\u00d7\u00d8\u0005\r\u0000"+
		"\u0000\u00d8\u00d9\u0005*\u0000\u0000\u00d9\u00da\u0003*\u0015\u0000\u00da"+
		"-\u0001\u0000\u0000\u0000\u00db\u00dc\u0005\u000e\u0000\u0000\u00dc\u00dd"+
		"\u0005+\u0000\u0000\u00dd\u00de\u0003<\u001e\u0000\u00de\u00df\u0005,"+
		"\u0000\u0000\u00df\u00e0\u0003*\u0015\u0000\u00e0/\u0001\u0000\u0000\u0000"+
		"\u00e1\u00e2\u0005\n\u0000\u0000\u00e2\u00e3\u0003<\u001e\u0000\u00e3"+
		"1\u0001\u0000\u0000\u0000\u00e4\u00e5\u0005\u0005\u0000\u0000\u00e5\u00e6"+
		"\u0005+\u0000\u0000\u00e6\u00e7\u0005*\u0000\u0000\u00e7\u00e8\u00051"+
		"\u0000\u0000\u00e8\u00e9\u00036\u001b\u0000\u00e9\u00eb\u0005,\u0000\u0000"+
		"\u00ea\u00ec\u0005\u0010\u0000\u0000\u00eb\u00ea\u0001\u0000\u0000\u0000"+
		"\u00eb\u00ec\u0001\u0000\u0000\u0000\u00ec3\u0001\u0000\u0000\u0000\u00ed"+
		"\u00ee\u0005\u0006\u0000\u0000\u00ee\u00ef\u0005\r\u0000\u0000\u00ef\u00f4"+
		"\u00036\u001b\u0000\u00f0\u00f1\u0005\u0006\u0000\u0000\u00f1\u00f2\u0005"+
		"\r\u0000\u0000\u00f2\u00f4\u0005*\u0000\u0000\u00f3\u00ed\u0001\u0000"+
		"\u0000\u0000\u00f3\u00f0\u0001\u0000\u0000\u0000\u00f45\u0001\u0000\u0000"+
		"\u0000\u00f5\u00f6\u0003<\u001e\u0000\u00f6\u00f7\u00052\u0000\u0000\u00f7"+
		"\u00f8\u00052\u0000\u0000\u00f8\u00f9\u0003<\u001e\u0000\u00f97\u0001"+
		"\u0000\u0000\u0000\u00fa\u00ff\u0005*\u0000\u0000\u00fb\u00fc\u00051\u0000"+
		"\u0000\u00fc\u00fe\u0005*\u0000\u0000\u00fd\u00fb\u0001\u0000\u0000\u0000"+
		"\u00fe\u0101\u0001\u0000\u0000\u0000\u00ff\u00fd\u0001\u0000\u0000\u0000"+
		"\u00ff\u0100\u0001\u0000\u0000\u0000\u01009\u0001\u0000\u0000\u0000\u0101"+
		"\u00ff\u0001\u0000\u0000\u0000\u0102\u0107\u0003<\u001e\u0000\u0103\u0104"+
		"\u00051\u0000\u0000\u0104\u0106\u0003<\u001e\u0000\u0105\u0103\u0001\u0000"+
		"\u0000\u0000\u0106\u0109\u0001\u0000\u0000\u0000\u0107\u0105\u0001\u0000"+
		"\u0000\u0000\u0107\u0108\u0001\u0000\u0000\u0000\u0108;\u0001\u0000\u0000"+
		"\u0000\u0109\u0107\u0001\u0000\u0000\u0000\u010a\u010b\u0006\u001e\uffff"+
		"\uffff\u0000\u010b\u0128\u0003\u0014\n\u0000\u010c\u0128\u0003\u0018\f"+
		"\u0000\u010d\u0128\u0003\u001a\r\u0000\u010e\u0128\u00034\u001a\u0000"+
		"\u010f\u0110\u0005!\u0000\u0000\u0110\u0128\u0003<\u001e\n\u0111\u0112"+
		"\u0005$\u0000\u0000\u0112\u0113\u0005+\u0000\u0000\u0113\u0114\u0003<"+
		"\u001e\u0000\u0114\u0115\u0005,\u0000\u0000\u0115\u0128\u0001\u0000\u0000"+
		"\u0000\u0116\u0117\u0005%\u0000\u0000\u0117\u0118\u0005+\u0000\u0000\u0118"+
		"\u0119\u0003<\u001e\u0000\u0119\u011a\u00051\u0000\u0000\u011a\u011b\u0003"+
		"<\u001e\u0000\u011b\u011c\u0005,\u0000\u0000\u011c\u0128\u0001\u0000\u0000"+
		"\u0000\u011d\u011e\u0005+\u0000\u0000\u011e\u011f\u0003<\u001e\u0000\u011f"+
		"\u0120\u0005,\u0000\u0000\u0120\u0128\u0001\u0000\u0000\u0000\u0121\u0128"+
		"\u0005*\u0000\u0000\u0122\u0128\u0005\'\u0000\u0000\u0123\u0128\u0005"+
		"(\u0000\u0000\u0124\u0128\u0005)\u0000\u0000\u0125\u0128\u0005\"\u0000"+
		"\u0000\u0126\u0128\u0005#\u0000\u0000\u0127\u010a\u0001\u0000\u0000\u0000"+
		"\u0127\u010c\u0001\u0000\u0000\u0000\u0127\u010d\u0001\u0000\u0000\u0000"+
		"\u0127\u010e\u0001\u0000\u0000\u0000\u0127\u010f\u0001\u0000\u0000\u0000"+
		"\u0127\u0111\u0001\u0000\u0000\u0000\u0127\u0116\u0001\u0000\u0000\u0000"+
		"\u0127\u011d\u0001\u0000\u0000\u0000\u0127\u0121\u0001\u0000\u0000\u0000"+
		"\u0127\u0122\u0001\u0000\u0000\u0000\u0127\u0123\u0001\u0000\u0000\u0000"+
		"\u0127\u0124\u0001\u0000\u0000\u0000\u0127\u0125\u0001\u0000\u0000\u0000"+
		"\u0127\u0126\u0001\u0000\u0000\u0000\u0128\u0137\u0001\u0000\u0000\u0000"+
		"\u0129\u012a\n\u000e\u0000\u0000\u012a\u012b\u0007\u0000\u0000\u0000\u012b"+
		"\u0136\u0003<\u001e\u000f\u012c\u012d\n\r\u0000\u0000\u012d\u012e\u0007"+
		"\u0001\u0000\u0000\u012e\u0136\u0003<\u001e\u000e\u012f\u0130\n\f\u0000"+
		"\u0000\u0130\u0131\u0007\u0002\u0000\u0000\u0131\u0136\u0003<\u001e\r"+
		"\u0132\u0133\n\u000b\u0000\u0000\u0133\u0134\u0007\u0003\u0000\u0000\u0134"+
		"\u0136\u0003<\u001e\f\u0135\u0129\u0001\u0000\u0000\u0000\u0135\u012c"+
		"\u0001\u0000\u0000\u0000\u0135\u012f\u0001\u0000\u0000\u0000\u0135\u0132"+
		"\u0001\u0000\u0000\u0000\u0136\u0139\u0001\u0000\u0000\u0000\u0137\u0135"+
		"\u0001\u0000\u0000\u0000\u0137\u0138\u0001\u0000\u0000\u0000\u0138=\u0001"+
		"\u0000\u0000\u0000\u0139\u0137\u0001\u0000\u0000\u0000\u0016BJLelu{\u0083"+
		"\u008d\u0090\u009c\u00bc\u00bf\u00c7\u00d0\u00eb\u00f3\u00ff\u0107\u0127"+
		"\u0135\u0137";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}