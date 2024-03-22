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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, PLUS=28, MINUS=29, MULT=30, DIV=31, GT=32, 
		GTE=33, LT=34, LTE=35, EQ=36, NEQ=37, MOD=38, TRUE=39, FALSE=40, NUMBER=41, 
		STRING=42, ID=43, WS=44;
	public static final int
		RULE_prog = 0, RULE_stat = 1, RULE_printStat = 2, RULE_varDecl = 3, RULE_dataType = 4, 
		RULE_baseType = 5, RULE_ifStat = 6, RULE_forLoop = 7, RULE_whileLoop = 8, 
		RULE_functionDecl = 9, RULE_functionCall = 10, RULE_arrayInit = 11, RULE_bsp = 12, 
		RULE_params = 13, RULE_param = 14, RULE_args = 15, RULE_randomNumber = 16, 
		RULE_randomChoice = 17, RULE_enumDecl = 18, RULE_enumBody = 19, RULE_enumValue = 20, 
		RULE_bspDimension = 21, RULE_bspParameters = 22, RULE_dimensionList = 23, 
		RULE_minSize = 24, RULE_expr = 25, RULE_openParenth = 26, RULE_closedParenth = 27, 
		RULE_openBrack = 28, RULE_closedBrack = 29, RULE_openCurlBrack = 30, RULE_closedCurlBrack = 31, 
		RULE_comma = 32;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stat", "printStat", "varDecl", "dataType", "baseType", "ifStat", 
			"forLoop", "whileLoop", "functionDecl", "functionCall", "arrayInit", 
			"bsp", "params", "param", "args", "randomNumber", "randomChoice", "enumDecl", 
			"enumBody", "enumValue", "bspDimension", "bspParameters", "dimensionList", 
			"minSize", "expr", "openParenth", "closedParenth", "openBrack", "closedBrack", 
			"openCurlBrack", "closedCurlBrack", "comma"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'print'", "'='", "'string'", "'bool'", "'number'", "'if'", "'else'", 
			"'for'", "'in'", "'while'", "'def'", "'BSP'", "'randomNumber'", "'randomChoice'", 
			"'enum'", "'.'", "'2D'", "'3D'", "'D'", "'.add'", "'('", "')'", "'['", 
			"']'", "'{'", "'}'", "','", "'+'", "'-'", "'*'", "'/'", "'>'", "'>='", 
			"'<'", "'<='", "'=='", "'!='", "'%'", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", 
			"LT", "LTE", "EQ", "NEQ", "MOD", "TRUE", "FALSE", "NUMBER", "STRING", 
			"ID", "WS"
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
			setState(67); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(66);
				stat();
				}
				}
				setState(69); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 17042465942850L) != 0) );
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
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
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
		public FunctionDeclContext functionDecl() {
			return getRuleContext(FunctionDeclContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public ArrayInitContext arrayInit() {
			return getRuleContext(ArrayInitContext.class,0);
		}
		public EnumDeclContext enumDecl() {
			return getRuleContext(EnumDeclContext.class,0);
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
		enterRule(_localctx, 2, RULE_stat);
		try {
			setState(81);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(71);
				printStat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(72);
				varDecl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(73);
				ifStat();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(74);
				forLoop();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(75);
				whileLoop();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(76);
				functionDecl();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(77);
				functionCall();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(78);
				arrayInit();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(79);
				enumDecl();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(80);
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
	public static class PrintStatContext extends ParserRuleContext {
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ClosedParenthContext closedParenth() {
			return getRuleContext(ClosedParenthContext.class,0);
		}
		public PrintStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStat; }
	}

	public final PrintStatContext printStat() throws RecognitionException {
		PrintStatContext _localctx = new PrintStatContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_printStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(T__0);
			setState(84);
			openParenth();
			setState(85);
			expr(0);
			setState(86);
			closedParenth();
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
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ArrayInitContext arrayInit() {
			return getRuleContext(ArrayInitContext.class,0);
		}
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_varDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(ID);
			setState(93);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(89);
				match(T__1);
				setState(90);
				expr(0);
				}
				break;
			case 2:
				{
				setState(91);
				arrayInit();
				}
				break;
			case 3:
				{
				setState(92);
				args();
				}
				break;
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
	public static class DataTypeContext extends ParserRuleContext {
		public BaseTypeContext baseType() {
			return getRuleContext(BaseTypeContext.class,0);
		}
		public OpenBrackContext openBrack() {
			return getRuleContext(OpenBrackContext.class,0);
		}
		public ClosedBrackContext closedBrack() {
			return getRuleContext(ClosedBrackContext.class,0);
		}
		public DataTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dataType; }
	}

	public final DataTypeContext dataType() throws RecognitionException {
		DataTypeContext _localctx = new DataTypeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_dataType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			baseType();
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__22) {
				{
				setState(96);
				openBrack();
				setState(97);
				closedBrack();
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
	public static class BaseTypeContext extends ParserRuleContext {
		public TerminalNode TRUE() { return getToken(RogueLangParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(RogueLangParser.FALSE, 0); }
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public BaseTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_baseType; }
	}

	public final BaseTypeContext baseType() throws RecognitionException {
		BaseTypeContext _localctx = new BaseTypeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_baseType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 10445360463928L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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
	public static class IfStatContext extends ParserRuleContext {
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ClosedParenthContext closedParenth() {
			return getRuleContext(ClosedParenthContext.class,0);
		}
		public List<OpenCurlBrackContext> openCurlBrack() {
			return getRuleContexts(OpenCurlBrackContext.class);
		}
		public OpenCurlBrackContext openCurlBrack(int i) {
			return getRuleContext(OpenCurlBrackContext.class,i);
		}
		public List<ClosedCurlBrackContext> closedCurlBrack() {
			return getRuleContexts(ClosedCurlBrackContext.class);
		}
		public ClosedCurlBrackContext closedCurlBrack(int i) {
			return getRuleContext(ClosedCurlBrackContext.class,i);
		}
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public IfStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStat; }
	}

	public final IfStatContext ifStat() throws RecognitionException {
		IfStatContext _localctx = new IfStatContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_ifStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(T__5);
			setState(104);
			openParenth();
			setState(105);
			expr(0);
			setState(106);
			closedParenth();
			setState(107);
			openCurlBrack();
			setState(111);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17042465942850L) != 0)) {
				{
				{
				setState(108);
				stat();
				}
				}
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(114);
			closedCurlBrack();
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(115);
				match(T__6);
				setState(116);
				openCurlBrack();
				setState(120);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17042465942850L) != 0)) {
					{
					{
					setState(117);
					stat();
					}
					}
					setState(122);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(123);
				closedCurlBrack();
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
	public static class ForLoopContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public OpenCurlBrackContext openCurlBrack() {
			return getRuleContext(OpenCurlBrackContext.class,0);
		}
		public ClosedCurlBrackContext closedCurlBrack() {
			return getRuleContext(ClosedCurlBrackContext.class,0);
		}
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ForLoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forLoop; }
	}

	public final ForLoopContext forLoop() throws RecognitionException {
		ForLoopContext _localctx = new ForLoopContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_forLoop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(T__7);
			setState(128);
			varDecl();
			setState(129);
			match(T__8);
			setState(130);
			expr(0);
			setState(131);
			openCurlBrack();
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17042465942850L) != 0)) {
				{
				{
				setState(132);
				stat();
				}
				}
				setState(137);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(138);
			closedCurlBrack();
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
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ClosedParenthContext closedParenth() {
			return getRuleContext(ClosedParenthContext.class,0);
		}
		public OpenCurlBrackContext openCurlBrack() {
			return getRuleContext(OpenCurlBrackContext.class,0);
		}
		public ClosedCurlBrackContext closedCurlBrack() {
			return getRuleContext(ClosedCurlBrackContext.class,0);
		}
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public WhileLoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileLoop; }
	}

	public final WhileLoopContext whileLoop() throws RecognitionException {
		WhileLoopContext _localctx = new WhileLoopContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_whileLoop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			match(T__9);
			setState(141);
			openParenth();
			setState(142);
			expr(0);
			setState(143);
			closedParenth();
			setState(144);
			openCurlBrack();
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17042465942850L) != 0)) {
				{
				{
				setState(145);
				stat();
				}
				}
				setState(150);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(151);
			closedCurlBrack();
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
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
		}
		public ClosedParenthContext closedParenth() {
			return getRuleContext(ClosedParenthContext.class,0);
		}
		public OpenCurlBrackContext openCurlBrack() {
			return getRuleContext(OpenCurlBrackContext.class,0);
		}
		public ClosedCurlBrackContext closedCurlBrack() {
			return getRuleContext(ClosedCurlBrackContext.class,0);
		}
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
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
			setState(153);
			match(T__10);
			setState(154);
			match(ID);
			setState(155);
			openParenth();
			setState(157);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 10445360463928L) != 0)) {
				{
				setState(156);
				params();
				}
			}

			setState(159);
			closedParenth();
			setState(160);
			openCurlBrack();
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17042465942850L) != 0)) {
				{
				{
				setState(161);
				stat();
				}
				}
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(167);
			closedCurlBrack();
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
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
		}
		public ClosedParenthContext closedParenth() {
			return getRuleContext(ClosedParenthContext.class,0);
		}
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
			setState(169);
			match(ID);
			setState(170);
			openParenth();
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17042432352256L) != 0)) {
				{
				setState(171);
				args();
				}
			}

			setState(174);
			closedParenth();
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
	public static class ArrayInitContext extends ParserRuleContext {
		public OpenCurlBrackContext openCurlBrack() {
			return getRuleContext(OpenCurlBrackContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ClosedCurlBrackContext closedCurlBrack() {
			return getRuleContext(ClosedCurlBrackContext.class,0);
		}
		public List<CommaContext> comma() {
			return getRuleContexts(CommaContext.class);
		}
		public CommaContext comma(int i) {
			return getRuleContext(CommaContext.class,i);
		}
		public ArrayInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayInit; }
	}

	public final ArrayInitContext arrayInit() throws RecognitionException {
		ArrayInitContext _localctx = new ArrayInitContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_arrayInit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			openCurlBrack();
			setState(177);
			expr(0);
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__26) {
				{
				{
				setState(178);
				comma();
				setState(179);
				expr(0);
				}
				}
				setState(185);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(186);
			closedCurlBrack();
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
	public static class BspContext extends ParserRuleContext {
		public BspDimensionContext bspDimension() {
			return getRuleContext(BspDimensionContext.class,0);
		}
		public BspParametersContext bspParameters() {
			return getRuleContext(BspParametersContext.class,0);
		}
		public BspContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bsp; }
	}

	public final BspContext bsp() throws RecognitionException {
		BspContext _localctx = new BspContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_bsp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			match(T__11);
			setState(189);
			bspDimension();
			setState(190);
			bspParameters();
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
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<CommaContext> comma() {
			return getRuleContexts(CommaContext.class);
		}
		public CommaContext comma(int i) {
			return getRuleContext(CommaContext.class,i);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			param();
			setState(198);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__26) {
				{
				{
				setState(193);
				comma();
				setState(194);
				param();
				}
				}
				setState(200);
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
	public static class ParamContext extends ParserRuleContext {
		public DataTypeContext dataType() {
			return getRuleContext(DataTypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			dataType();
			setState(202);
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
	public static class ArgsContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<CommaContext> comma() {
			return getRuleContexts(CommaContext.class);
		}
		public CommaContext comma(int i) {
			return getRuleContext(CommaContext.class,i);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			expr(0);
			setState(210);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__26) {
				{
				{
				setState(205);
				comma();
				setState(206);
				expr(0);
				}
				}
				setState(212);
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
	public static class RandomNumberContext extends ParserRuleContext {
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
		}
		public List<TerminalNode> NUMBER() { return getTokens(RogueLangParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(RogueLangParser.NUMBER, i);
		}
		public CommaContext comma() {
			return getRuleContext(CommaContext.class,0);
		}
		public ClosedParenthContext closedParenth() {
			return getRuleContext(ClosedParenthContext.class,0);
		}
		public RandomNumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_randomNumber; }
	}

	public final RandomNumberContext randomNumber() throws RecognitionException {
		RandomNumberContext _localctx = new RandomNumberContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_randomNumber);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(T__12);
			setState(214);
			openParenth();
			setState(215);
			match(NUMBER);
			setState(216);
			comma();
			setState(217);
			match(NUMBER);
			setState(218);
			closedParenth();
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
	public static class RandomChoiceContext extends ParserRuleContext {
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ClosedParenthContext closedParenth() {
			return getRuleContext(ClosedParenthContext.class,0);
		}
		public List<CommaContext> comma() {
			return getRuleContexts(CommaContext.class);
		}
		public CommaContext comma(int i) {
			return getRuleContext(CommaContext.class,i);
		}
		public RandomChoiceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_randomChoice; }
	}

	public final RandomChoiceContext randomChoice() throws RecognitionException {
		RandomChoiceContext _localctx = new RandomChoiceContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_randomChoice);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(T__13);
			setState(221);
			openParenth();
			setState(222);
			expr(0);
			setState(226); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(223);
				comma();
				setState(224);
				expr(0);
				}
				}
				setState(228); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__26 );
			setState(230);
			closedParenth();
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
	public static class EnumDeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public OpenCurlBrackContext openCurlBrack() {
			return getRuleContext(OpenCurlBrackContext.class,0);
		}
		public EnumBodyContext enumBody() {
			return getRuleContext(EnumBodyContext.class,0);
		}
		public ClosedCurlBrackContext closedCurlBrack() {
			return getRuleContext(ClosedCurlBrackContext.class,0);
		}
		public EnumDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enumDecl; }
	}

	public final EnumDeclContext enumDecl() throws RecognitionException {
		EnumDeclContext _localctx = new EnumDeclContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_enumDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(T__14);
			setState(233);
			match(ID);
			setState(234);
			openCurlBrack();
			setState(235);
			enumBody();
			setState(236);
			closedCurlBrack();
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
	public static class EnumBodyContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(RogueLangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(RogueLangParser.ID, i);
		}
		public List<CommaContext> comma() {
			return getRuleContexts(CommaContext.class);
		}
		public CommaContext comma(int i) {
			return getRuleContext(CommaContext.class,i);
		}
		public EnumBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enumBody; }
	}

	public final EnumBodyContext enumBody() throws RecognitionException {
		EnumBodyContext _localctx = new EnumBodyContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_enumBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			match(ID);
			setState(244);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__26) {
				{
				{
				setState(239);
				comma();
				setState(240);
				match(ID);
				}
				}
				setState(246);
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
	public static class EnumValueContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(RogueLangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(RogueLangParser.ID, i);
		}
		public EnumValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enumValue; }
	}

	public final EnumValueContext enumValue() throws RecognitionException {
		EnumValueContext _localctx = new EnumValueContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_enumValue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			match(ID);
			setState(248);
			match(T__15);
			setState(249);
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
	public static class BspDimensionContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(RogueLangParser.NUMBER, 0); }
		public BspDimensionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bspDimension; }
	}

	public final BspDimensionContext bspDimension() throws RecognitionException {
		BspDimensionContext _localctx = new BspDimensionContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_bspDimension);
		try {
			setState(255);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__16:
				enterOuterAlt(_localctx, 1);
				{
				setState(251);
				match(T__16);
				}
				break;
			case T__17:
				enterOuterAlt(_localctx, 2);
				{
				setState(252);
				match(T__17);
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 3);
				{
				setState(253);
				match(NUMBER);
				setState(254);
				match(T__18);
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
	public static class BspParametersContext extends ParserRuleContext {
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
		}
		public DimensionListContext dimensionList() {
			return getRuleContext(DimensionListContext.class,0);
		}
		public CommaContext comma() {
			return getRuleContext(CommaContext.class,0);
		}
		public MinSizeContext minSize() {
			return getRuleContext(MinSizeContext.class,0);
		}
		public ClosedParenthContext closedParenth() {
			return getRuleContext(ClosedParenthContext.class,0);
		}
		public BspParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bspParameters; }
	}

	public final BspParametersContext bspParameters() throws RecognitionException {
		BspParametersContext _localctx = new BspParametersContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_bspParameters);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			openParenth();
			setState(258);
			dimensionList();
			setState(259);
			comma();
			setState(260);
			minSize();
			setState(261);
			closedParenth();
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
	public static class DimensionListContext extends ParserRuleContext {
		public List<TerminalNode> NUMBER() { return getTokens(RogueLangParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(RogueLangParser.NUMBER, i);
		}
		public List<CommaContext> comma() {
			return getRuleContexts(CommaContext.class);
		}
		public CommaContext comma(int i) {
			return getRuleContext(CommaContext.class,i);
		}
		public DimensionListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dimensionList; }
	}

	public final DimensionListContext dimensionList() throws RecognitionException {
		DimensionListContext _localctx = new DimensionListContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_dimensionList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			match(NUMBER);
			setState(269);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(264);
					comma();
					setState(265);
					match(NUMBER);
					}
					} 
				}
				setState(271);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
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
	public static class MinSizeContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(RogueLangParser.NUMBER, 0); }
		public MinSizeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_minSize; }
	}

	public final MinSizeContext minSize() throws RecognitionException {
		MinSizeContext _localctx = new MinSizeContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_minSize);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			match(NUMBER);
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
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ClosedParenthContext closedParenth() {
			return getRuleContext(ClosedParenthContext.class,0);
		}
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public TerminalNode STRING() { return getToken(RogueLangParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(RogueLangParser.NUMBER, 0); }
		public TerminalNode TRUE() { return getToken(RogueLangParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(RogueLangParser.FALSE, 0); }
		public RandomNumberContext randomNumber() {
			return getRuleContext(RandomNumberContext.class,0);
		}
		public RandomChoiceContext randomChoice() {
			return getRuleContext(RandomChoiceContext.class,0);
		}
		public EnumValueContext enumValue() {
			return getRuleContext(EnumValueContext.class,0);
		}
		public OpenBrackContext openBrack() {
			return getRuleContext(OpenBrackContext.class,0);
		}
		public ClosedBrackContext closedBrack() {
			return getRuleContext(ClosedBrackContext.class,0);
		}
		public TerminalNode MULT() { return getToken(RogueLangParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(RogueLangParser.DIV, 0); }
		public TerminalNode PLUS() { return getToken(RogueLangParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(RogueLangParser.MINUS, 0); }
		public TerminalNode GT() { return getToken(RogueLangParser.GT, 0); }
		public TerminalNode GTE() { return getToken(RogueLangParser.GTE, 0); }
		public TerminalNode LT() { return getToken(RogueLangParser.LT, 0); }
		public TerminalNode LTE() { return getToken(RogueLangParser.LTE, 0); }
		public TerminalNode EQ() { return getToken(RogueLangParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(RogueLangParser.NEQ, 0); }
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
		int _startState = 50;
		enterRecursionRule(_localctx, 50, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(287);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(275);
				openParenth();
				setState(276);
				expr(0);
				setState(277);
				closedParenth();
				}
				break;
			case 2:
				{
				setState(279);
				match(ID);
				}
				break;
			case 3:
				{
				setState(280);
				match(STRING);
				}
				break;
			case 4:
				{
				setState(281);
				match(NUMBER);
				}
				break;
			case 5:
				{
				setState(282);
				match(TRUE);
				}
				break;
			case 6:
				{
				setState(283);
				match(FALSE);
				}
				break;
			case 7:
				{
				setState(284);
				randomNumber();
				}
				break;
			case 8:
				{
				setState(285);
				randomChoice();
				}
				break;
			case 9:
				{
				setState(286);
				enumValue();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(318);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(316);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(289);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(290);
						openBrack();
						setState(291);
						expr(0);
						setState(292);
						closedBrack();
						setState(293);
						match(T__1);
						setState(294);
						expr(15);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(296);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(297);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MULT || _la==DIV) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(298);
						expr(13);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(299);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(300);
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
						setState(301);
						expr(12);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(302);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(303);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 270582939648L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(304);
						expr(11);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(305);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(306);
						openBrack();
						setState(307);
						expr(0);
						setState(308);
						closedBrack();
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(310);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(311);
						match(T__19);
						setState(312);
						openParenth();
						setState(313);
						expr(0);
						setState(314);
						closedParenth();
						}
						break;
					}
					} 
				}
				setState(320);
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

	@SuppressWarnings("CheckReturnValue")
	public static class OpenParenthContext extends ParserRuleContext {
		public OpenParenthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_openParenth; }
	}

	public final OpenParenthContext openParenth() throws RecognitionException {
		OpenParenthContext _localctx = new OpenParenthContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_openParenth);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(321);
			match(T__20);
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
	public static class ClosedParenthContext extends ParserRuleContext {
		public ClosedParenthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_closedParenth; }
	}

	public final ClosedParenthContext closedParenth() throws RecognitionException {
		ClosedParenthContext _localctx = new ClosedParenthContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_closedParenth);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(323);
			match(T__21);
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
	public static class OpenBrackContext extends ParserRuleContext {
		public OpenBrackContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_openBrack; }
	}

	public final OpenBrackContext openBrack() throws RecognitionException {
		OpenBrackContext _localctx = new OpenBrackContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_openBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(325);
			match(T__22);
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
	public static class ClosedBrackContext extends ParserRuleContext {
		public ClosedBrackContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_closedBrack; }
	}

	public final ClosedBrackContext closedBrack() throws RecognitionException {
		ClosedBrackContext _localctx = new ClosedBrackContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_closedBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(327);
			match(T__23);
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
	public static class OpenCurlBrackContext extends ParserRuleContext {
		public OpenCurlBrackContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_openCurlBrack; }
	}

	public final OpenCurlBrackContext openCurlBrack() throws RecognitionException {
		OpenCurlBrackContext _localctx = new OpenCurlBrackContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_openCurlBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(329);
			match(T__24);
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
	public static class ClosedCurlBrackContext extends ParserRuleContext {
		public ClosedCurlBrackContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_closedCurlBrack; }
	}

	public final ClosedCurlBrackContext closedCurlBrack() throws RecognitionException {
		ClosedCurlBrackContext _localctx = new ClosedCurlBrackContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_closedCurlBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(331);
			match(T__25);
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
	public static class CommaContext extends ParserRuleContext {
		public CommaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comma; }
	}

	public final CommaContext comma() throws RecognitionException {
		CommaContext _localctx = new CommaContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_comma);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(333);
			match(T__26);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 25:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 14);
		case 1:
			return precpred(_ctx, 12);
		case 2:
			return precpred(_ctx, 11);
		case 3:
			return precpred(_ctx, 10);
		case 4:
			return precpred(_ctx, 15);
		case 5:
			return precpred(_ctx, 13);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001,\u0150\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0001\u0000\u0004\u0000D\b\u0000"+
		"\u000b\u0000\f\u0000E\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001R\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0003\u0003^\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u0004d\b\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006n\b\u0006"+
		"\n\u0006\f\u0006q\t\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0005\u0006w\b\u0006\n\u0006\f\u0006z\t\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006~\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0005\u0007\u0086\b\u0007\n\u0007\f\u0007\u0089"+
		"\t\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0005\b\u0093\b\b\n\b\f\b\u0096\t\b\u0001\b\u0001\b\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0003\t\u009e\b\t\u0001\t\u0001\t\u0001\t\u0005"+
		"\t\u00a3\b\t\n\t\f\t\u00a6\t\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n"+
		"\u0003\n\u00ad\b\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0005\u000b\u00b6\b\u000b\n\u000b\f\u000b\u00b9"+
		"\t\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0005\r\u00c5\b\r\n\r\f\r\u00c8\t\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0005\u000f\u00d1\b\u000f\n\u000f\f\u000f\u00d4\t\u000f\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0004"+
		"\u0011\u00e3\b\u0011\u000b\u0011\f\u0011\u00e4\u0001\u0011\u0001\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0005\u0013\u00f3\b\u0013"+
		"\n\u0013\f\u0013\u00f6\t\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u0100"+
		"\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u010c"+
		"\b\u0017\n\u0017\f\u0017\u010f\t\u0017\u0001\u0018\u0001\u0018\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0003\u0019\u0120\b\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0005\u0019"+
		"\u013d\b\u0019\n\u0019\f\u0019\u0140\t\u0019\u0001\u001a\u0001\u001a\u0001"+
		"\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001"+
		"\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001 \u0000"+
		"\u00012!\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u001e \"$&(*,.02468:<>@\u0000\u0004\u0003\u0000\u0003\u0005"+
		"\'(++\u0001\u0000\u001e\u001f\u0001\u0000\u001c\u001d\u0001\u0000 %\u015a"+
		"\u0000C\u0001\u0000\u0000\u0000\u0002Q\u0001\u0000\u0000\u0000\u0004S"+
		"\u0001\u0000\u0000\u0000\u0006X\u0001\u0000\u0000\u0000\b_\u0001\u0000"+
		"\u0000\u0000\ne\u0001\u0000\u0000\u0000\fg\u0001\u0000\u0000\u0000\u000e"+
		"\u007f\u0001\u0000\u0000\u0000\u0010\u008c\u0001\u0000\u0000\u0000\u0012"+
		"\u0099\u0001\u0000\u0000\u0000\u0014\u00a9\u0001\u0000\u0000\u0000\u0016"+
		"\u00b0\u0001\u0000\u0000\u0000\u0018\u00bc\u0001\u0000\u0000\u0000\u001a"+
		"\u00c0\u0001\u0000\u0000\u0000\u001c\u00c9\u0001\u0000\u0000\u0000\u001e"+
		"\u00cc\u0001\u0000\u0000\u0000 \u00d5\u0001\u0000\u0000\u0000\"\u00dc"+
		"\u0001\u0000\u0000\u0000$\u00e8\u0001\u0000\u0000\u0000&\u00ee\u0001\u0000"+
		"\u0000\u0000(\u00f7\u0001\u0000\u0000\u0000*\u00ff\u0001\u0000\u0000\u0000"+
		",\u0101\u0001\u0000\u0000\u0000.\u0107\u0001\u0000\u0000\u00000\u0110"+
		"\u0001\u0000\u0000\u00002\u011f\u0001\u0000\u0000\u00004\u0141\u0001\u0000"+
		"\u0000\u00006\u0143\u0001\u0000\u0000\u00008\u0145\u0001\u0000\u0000\u0000"+
		":\u0147\u0001\u0000\u0000\u0000<\u0149\u0001\u0000\u0000\u0000>\u014b"+
		"\u0001\u0000\u0000\u0000@\u014d\u0001\u0000\u0000\u0000BD\u0003\u0002"+
		"\u0001\u0000CB\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000EC\u0001"+
		"\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000F\u0001\u0001\u0000\u0000"+
		"\u0000GR\u0003\u0004\u0002\u0000HR\u0003\u0006\u0003\u0000IR\u0003\f\u0006"+
		"\u0000JR\u0003\u000e\u0007\u0000KR\u0003\u0010\b\u0000LR\u0003\u0012\t"+
		"\u0000MR\u0003\u0014\n\u0000NR\u0003\u0016\u000b\u0000OR\u0003$\u0012"+
		"\u0000PR\u00032\u0019\u0000QG\u0001\u0000\u0000\u0000QH\u0001\u0000\u0000"+
		"\u0000QI\u0001\u0000\u0000\u0000QJ\u0001\u0000\u0000\u0000QK\u0001\u0000"+
		"\u0000\u0000QL\u0001\u0000\u0000\u0000QM\u0001\u0000\u0000\u0000QN\u0001"+
		"\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000QP\u0001\u0000\u0000\u0000"+
		"R\u0003\u0001\u0000\u0000\u0000ST\u0005\u0001\u0000\u0000TU\u00034\u001a"+
		"\u0000UV\u00032\u0019\u0000VW\u00036\u001b\u0000W\u0005\u0001\u0000\u0000"+
		"\u0000X]\u0005+\u0000\u0000YZ\u0005\u0002\u0000\u0000Z^\u00032\u0019\u0000"+
		"[^\u0003\u0016\u000b\u0000\\^\u0003\u001e\u000f\u0000]Y\u0001\u0000\u0000"+
		"\u0000][\u0001\u0000\u0000\u0000]\\\u0001\u0000\u0000\u0000]^\u0001\u0000"+
		"\u0000\u0000^\u0007\u0001\u0000\u0000\u0000_c\u0003\n\u0005\u0000`a\u0003"+
		"8\u001c\u0000ab\u0003:\u001d\u0000bd\u0001\u0000\u0000\u0000c`\u0001\u0000"+
		"\u0000\u0000cd\u0001\u0000\u0000\u0000d\t\u0001\u0000\u0000\u0000ef\u0007"+
		"\u0000\u0000\u0000f\u000b\u0001\u0000\u0000\u0000gh\u0005\u0006\u0000"+
		"\u0000hi\u00034\u001a\u0000ij\u00032\u0019\u0000jk\u00036\u001b\u0000"+
		"ko\u0003<\u001e\u0000ln\u0003\u0002\u0001\u0000ml\u0001\u0000\u0000\u0000"+
		"nq\u0001\u0000\u0000\u0000om\u0001\u0000\u0000\u0000op\u0001\u0000\u0000"+
		"\u0000pr\u0001\u0000\u0000\u0000qo\u0001\u0000\u0000\u0000r}\u0003>\u001f"+
		"\u0000st\u0005\u0007\u0000\u0000tx\u0003<\u001e\u0000uw\u0003\u0002\u0001"+
		"\u0000vu\u0001\u0000\u0000\u0000wz\u0001\u0000\u0000\u0000xv\u0001\u0000"+
		"\u0000\u0000xy\u0001\u0000\u0000\u0000y{\u0001\u0000\u0000\u0000zx\u0001"+
		"\u0000\u0000\u0000{|\u0003>\u001f\u0000|~\u0001\u0000\u0000\u0000}s\u0001"+
		"\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000~\r\u0001\u0000\u0000\u0000"+
		"\u007f\u0080\u0005\b\u0000\u0000\u0080\u0081\u0003\u0006\u0003\u0000\u0081"+
		"\u0082\u0005\t\u0000\u0000\u0082\u0083\u00032\u0019\u0000\u0083\u0087"+
		"\u0003<\u001e\u0000\u0084\u0086\u0003\u0002\u0001\u0000\u0085\u0084\u0001"+
		"\u0000\u0000\u0000\u0086\u0089\u0001\u0000\u0000\u0000\u0087\u0085\u0001"+
		"\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u008a\u0001"+
		"\u0000\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a\u008b\u0003"+
		">\u001f\u0000\u008b\u000f\u0001\u0000\u0000\u0000\u008c\u008d\u0005\n"+
		"\u0000\u0000\u008d\u008e\u00034\u001a\u0000\u008e\u008f\u00032\u0019\u0000"+
		"\u008f\u0090\u00036\u001b\u0000\u0090\u0094\u0003<\u001e\u0000\u0091\u0093"+
		"\u0003\u0002\u0001\u0000\u0092\u0091\u0001\u0000\u0000\u0000\u0093\u0096"+
		"\u0001\u0000\u0000\u0000\u0094\u0092\u0001\u0000\u0000\u0000\u0094\u0095"+
		"\u0001\u0000\u0000\u0000\u0095\u0097\u0001\u0000\u0000\u0000\u0096\u0094"+
		"\u0001\u0000\u0000\u0000\u0097\u0098\u0003>\u001f\u0000\u0098\u0011\u0001"+
		"\u0000\u0000\u0000\u0099\u009a\u0005\u000b\u0000\u0000\u009a\u009b\u0005"+
		"+\u0000\u0000\u009b\u009d\u00034\u001a\u0000\u009c\u009e\u0003\u001a\r"+
		"\u0000\u009d\u009c\u0001\u0000\u0000\u0000\u009d\u009e\u0001\u0000\u0000"+
		"\u0000\u009e\u009f\u0001\u0000\u0000\u0000\u009f\u00a0\u00036\u001b\u0000"+
		"\u00a0\u00a4\u0003<\u001e\u0000\u00a1\u00a3\u0003\u0002\u0001\u0000\u00a2"+
		"\u00a1\u0001\u0000\u0000\u0000\u00a3\u00a6\u0001\u0000\u0000\u0000\u00a4"+
		"\u00a2\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5"+
		"\u00a7\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001\u0000\u0000\u0000\u00a7"+
		"\u00a8\u0003>\u001f\u0000\u00a8\u0013\u0001\u0000\u0000\u0000\u00a9\u00aa"+
		"\u0005+\u0000\u0000\u00aa\u00ac\u00034\u001a\u0000\u00ab\u00ad\u0003\u001e"+
		"\u000f\u0000\u00ac\u00ab\u0001\u0000\u0000\u0000\u00ac\u00ad\u0001\u0000"+
		"\u0000\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000\u00ae\u00af\u00036\u001b"+
		"\u0000\u00af\u0015\u0001\u0000\u0000\u0000\u00b0\u00b1\u0003<\u001e\u0000"+
		"\u00b1\u00b7\u00032\u0019\u0000\u00b2\u00b3\u0003@ \u0000\u00b3\u00b4"+
		"\u00032\u0019\u0000\u00b4\u00b6\u0001\u0000\u0000\u0000\u00b5\u00b2\u0001"+
		"\u0000\u0000\u0000\u00b6\u00b9\u0001\u0000\u0000\u0000\u00b7\u00b5\u0001"+
		"\u0000\u0000\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8\u00ba\u0001"+
		"\u0000\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00ba\u00bb\u0003"+
		">\u001f\u0000\u00bb\u0017\u0001\u0000\u0000\u0000\u00bc\u00bd\u0005\f"+
		"\u0000\u0000\u00bd\u00be\u0003*\u0015\u0000\u00be\u00bf\u0003,\u0016\u0000"+
		"\u00bf\u0019\u0001\u0000\u0000\u0000\u00c0\u00c6\u0003\u001c\u000e\u0000"+
		"\u00c1\u00c2\u0003@ \u0000\u00c2\u00c3\u0003\u001c\u000e\u0000\u00c3\u00c5"+
		"\u0001\u0000\u0000\u0000\u00c4\u00c1\u0001\u0000\u0000\u0000\u00c5\u00c8"+
		"\u0001\u0000\u0000\u0000\u00c6\u00c4\u0001\u0000\u0000\u0000\u00c6\u00c7"+
		"\u0001\u0000\u0000\u0000\u00c7\u001b\u0001\u0000\u0000\u0000\u00c8\u00c6"+
		"\u0001\u0000\u0000\u0000\u00c9\u00ca\u0003\b\u0004\u0000\u00ca\u00cb\u0005"+
		"+\u0000\u0000\u00cb\u001d\u0001\u0000\u0000\u0000\u00cc\u00d2\u00032\u0019"+
		"\u0000\u00cd\u00ce\u0003@ \u0000\u00ce\u00cf\u00032\u0019\u0000\u00cf"+
		"\u00d1\u0001\u0000\u0000\u0000\u00d0\u00cd\u0001\u0000\u0000\u0000\u00d1"+
		"\u00d4\u0001\u0000\u0000\u0000\u00d2\u00d0\u0001\u0000\u0000\u0000\u00d2"+
		"\u00d3\u0001\u0000\u0000\u0000\u00d3\u001f\u0001\u0000\u0000\u0000\u00d4"+
		"\u00d2\u0001\u0000\u0000\u0000\u00d5\u00d6\u0005\r\u0000\u0000\u00d6\u00d7"+
		"\u00034\u001a\u0000\u00d7\u00d8\u0005)\u0000\u0000\u00d8\u00d9\u0003@"+
		" \u0000\u00d9\u00da\u0005)\u0000\u0000\u00da\u00db\u00036\u001b\u0000"+
		"\u00db!\u0001\u0000\u0000\u0000\u00dc\u00dd\u0005\u000e\u0000\u0000\u00dd"+
		"\u00de\u00034\u001a\u0000\u00de\u00e2\u00032\u0019\u0000\u00df\u00e0\u0003"+
		"@ \u0000\u00e0\u00e1\u00032\u0019\u0000\u00e1\u00e3\u0001\u0000\u0000"+
		"\u0000\u00e2\u00df\u0001\u0000\u0000\u0000\u00e3\u00e4\u0001\u0000\u0000"+
		"\u0000\u00e4\u00e2\u0001\u0000\u0000\u0000\u00e4\u00e5\u0001\u0000\u0000"+
		"\u0000\u00e5\u00e6\u0001\u0000\u0000\u0000\u00e6\u00e7\u00036\u001b\u0000"+
		"\u00e7#\u0001\u0000\u0000\u0000\u00e8\u00e9\u0005\u000f\u0000\u0000\u00e9"+
		"\u00ea\u0005+\u0000\u0000\u00ea\u00eb\u0003<\u001e\u0000\u00eb\u00ec\u0003"+
		"&\u0013\u0000\u00ec\u00ed\u0003>\u001f\u0000\u00ed%\u0001\u0000\u0000"+
		"\u0000\u00ee\u00f4\u0005+\u0000\u0000\u00ef\u00f0\u0003@ \u0000\u00f0"+
		"\u00f1\u0005+\u0000\u0000\u00f1\u00f3\u0001\u0000\u0000\u0000\u00f2\u00ef"+
		"\u0001\u0000\u0000\u0000\u00f3\u00f6\u0001\u0000\u0000\u0000\u00f4\u00f2"+
		"\u0001\u0000\u0000\u0000\u00f4\u00f5\u0001\u0000\u0000\u0000\u00f5\'\u0001"+
		"\u0000\u0000\u0000\u00f6\u00f4\u0001\u0000\u0000\u0000\u00f7\u00f8\u0005"+
		"+\u0000\u0000\u00f8\u00f9\u0005\u0010\u0000\u0000\u00f9\u00fa\u0005+\u0000"+
		"\u0000\u00fa)\u0001\u0000\u0000\u0000\u00fb\u0100\u0005\u0011\u0000\u0000"+
		"\u00fc\u0100\u0005\u0012\u0000\u0000\u00fd\u00fe\u0005)\u0000\u0000\u00fe"+
		"\u0100\u0005\u0013\u0000\u0000\u00ff\u00fb\u0001\u0000\u0000\u0000\u00ff"+
		"\u00fc\u0001\u0000\u0000\u0000\u00ff\u00fd\u0001\u0000\u0000\u0000\u0100"+
		"+\u0001\u0000\u0000\u0000\u0101\u0102\u00034\u001a\u0000\u0102\u0103\u0003"+
		".\u0017\u0000\u0103\u0104\u0003@ \u0000\u0104\u0105\u00030\u0018\u0000"+
		"\u0105\u0106\u00036\u001b\u0000\u0106-\u0001\u0000\u0000\u0000\u0107\u010d"+
		"\u0005)\u0000\u0000\u0108\u0109\u0003@ \u0000\u0109\u010a\u0005)\u0000"+
		"\u0000\u010a\u010c\u0001\u0000\u0000\u0000\u010b\u0108\u0001\u0000\u0000"+
		"\u0000\u010c\u010f\u0001\u0000\u0000\u0000\u010d\u010b\u0001\u0000\u0000"+
		"\u0000\u010d\u010e\u0001\u0000\u0000\u0000\u010e/\u0001\u0000\u0000\u0000"+
		"\u010f\u010d\u0001\u0000\u0000\u0000\u0110\u0111\u0005)\u0000\u0000\u0111"+
		"1\u0001\u0000\u0000\u0000\u0112\u0113\u0006\u0019\uffff\uffff\u0000\u0113"+
		"\u0114\u00034\u001a\u0000\u0114\u0115\u00032\u0019\u0000\u0115\u0116\u0003"+
		"6\u001b\u0000\u0116\u0120\u0001\u0000\u0000\u0000\u0117\u0120\u0005+\u0000"+
		"\u0000\u0118\u0120\u0005*\u0000\u0000\u0119\u0120\u0005)\u0000\u0000\u011a"+
		"\u0120\u0005\'\u0000\u0000\u011b\u0120\u0005(\u0000\u0000\u011c\u0120"+
		"\u0003 \u0010\u0000\u011d\u0120\u0003\"\u0011\u0000\u011e\u0120\u0003"+
		"(\u0014\u0000\u011f\u0112\u0001\u0000\u0000\u0000\u011f\u0117\u0001\u0000"+
		"\u0000\u0000\u011f\u0118\u0001\u0000\u0000\u0000\u011f\u0119\u0001\u0000"+
		"\u0000\u0000\u011f\u011a\u0001\u0000\u0000\u0000\u011f\u011b\u0001\u0000"+
		"\u0000\u0000\u011f\u011c\u0001\u0000\u0000\u0000\u011f\u011d\u0001\u0000"+
		"\u0000\u0000\u011f\u011e\u0001\u0000\u0000\u0000\u0120\u013e\u0001\u0000"+
		"\u0000\u0000\u0121\u0122\n\u000e\u0000\u0000\u0122\u0123\u00038\u001c"+
		"\u0000\u0123\u0124\u00032\u0019\u0000\u0124\u0125\u0003:\u001d\u0000\u0125"+
		"\u0126\u0005\u0002\u0000\u0000\u0126\u0127\u00032\u0019\u000f\u0127\u013d"+
		"\u0001\u0000\u0000\u0000\u0128\u0129\n\f\u0000\u0000\u0129\u012a\u0007"+
		"\u0001\u0000\u0000\u012a\u013d\u00032\u0019\r\u012b\u012c\n\u000b\u0000"+
		"\u0000\u012c\u012d\u0007\u0002\u0000\u0000\u012d\u013d\u00032\u0019\f"+
		"\u012e\u012f\n\n\u0000\u0000\u012f\u0130\u0007\u0003\u0000\u0000\u0130"+
		"\u013d\u00032\u0019\u000b\u0131\u0132\n\u000f\u0000\u0000\u0132\u0133"+
		"\u00038\u001c\u0000\u0133\u0134\u00032\u0019\u0000\u0134\u0135\u0003:"+
		"\u001d\u0000\u0135\u013d\u0001\u0000\u0000\u0000\u0136\u0137\n\r\u0000"+
		"\u0000\u0137\u0138\u0005\u0014\u0000\u0000\u0138\u0139\u00034\u001a\u0000"+
		"\u0139\u013a\u00032\u0019\u0000\u013a\u013b\u00036\u001b\u0000\u013b\u013d"+
		"\u0001\u0000\u0000\u0000\u013c\u0121\u0001\u0000\u0000\u0000\u013c\u0128"+
		"\u0001\u0000\u0000\u0000\u013c\u012b\u0001\u0000\u0000\u0000\u013c\u012e"+
		"\u0001\u0000\u0000\u0000\u013c\u0131\u0001\u0000\u0000\u0000\u013c\u0136"+
		"\u0001\u0000\u0000\u0000\u013d\u0140\u0001\u0000\u0000\u0000\u013e\u013c"+
		"\u0001\u0000\u0000\u0000\u013e\u013f\u0001\u0000\u0000\u0000\u013f3\u0001"+
		"\u0000\u0000\u0000\u0140\u013e\u0001\u0000\u0000\u0000\u0141\u0142\u0005"+
		"\u0015\u0000\u0000\u01425\u0001\u0000\u0000\u0000\u0143\u0144\u0005\u0016"+
		"\u0000\u0000\u01447\u0001\u0000\u0000\u0000\u0145\u0146\u0005\u0017\u0000"+
		"\u0000\u01469\u0001\u0000\u0000\u0000\u0147\u0148\u0005\u0018\u0000\u0000"+
		"\u0148;\u0001\u0000\u0000\u0000\u0149\u014a\u0005\u0019\u0000\u0000\u014a"+
		"=\u0001\u0000\u0000\u0000\u014b\u014c\u0005\u001a\u0000\u0000\u014c?\u0001"+
		"\u0000\u0000\u0000\u014d\u014e\u0005\u001b\u0000\u0000\u014eA\u0001\u0000"+
		"\u0000\u0000\u0016EQ]cox}\u0087\u0094\u009d\u00a4\u00ac\u00b7\u00c6\u00d2"+
		"\u00e4\u00f4\u00ff\u010d\u011f\u013c\u013e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}