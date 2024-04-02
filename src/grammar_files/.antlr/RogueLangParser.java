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
		T__24=25, T__25=26, T__26=27, IF=28, ELIF=29, ELSE=30, RETURN=31, PLUS=32, 
		MINUS=33, MULT=34, DIV=35, GT=36, GTE=37, LT=38, LTE=39, EQ=40, NEQ=41, 
		MOD=42, AND=43, OR=44, NOT=45, TRUE=46, FALSE=47, COMMENT_SINGLELINE=48, 
		NUMBER=49, STRING=50, ID=51, WS=52;
	public static final int
		RULE_prog = 0, RULE_stat = 1, RULE_printStat = 2, RULE_varDecl = 3, RULE_dataType = 4, 
		RULE_baseType = 5, RULE_ifStat = 6, RULE_elifBlockstat = 7, RULE_ifExpr = 8, 
		RULE_ifBlock = 9, RULE_elifExpr = 10, RULE_elifBlock = 11, RULE_elseBlock = 12, 
		RULE_forLoop = 13, RULE_whileLoop = 14, RULE_functionDecl = 15, RULE_functionCall = 16, 
		RULE_arrayInit = 17, RULE_bsp = 18, RULE_params = 19, RULE_param = 20, 
		RULE_args = 21, RULE_randomNumber = 22, RULE_randomChoice = 23, RULE_enumDecl = 24, 
		RULE_enumBody = 25, RULE_enumValue = 26, RULE_bspDimension = 27, RULE_bspParameters = 28, 
		RULE_dimensionList = 29, RULE_minSize = 30, RULE_expr = 31, RULE_openParenth = 32, 
		RULE_closedParenth = 33, RULE_openBrack = 34, RULE_closedBrack = 35, RULE_openCurlBrack = 36, 
		RULE_closedCurlBrack = 37, RULE_comma = 38;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stat", "printStat", "varDecl", "dataType", "baseType", "ifStat", 
			"elifBlockstat", "ifExpr", "ifBlock", "elifExpr", "elifBlock", "elseBlock", 
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
			null, "'print'", "'='", "'string'", "'True'", "'False'", "'bool'", "'number'", 
			"'for'", "'in'", "'while'", "'def'", "'BSP'", "'randomNumber'", "'randomChoice'", 
			"'enum'", "'.'", "'2D'", "'3D'", "'D'", "'.add'", "'('", "')'", "'['", 
			"']'", "'{'", "'}'", "','", "'if'", "'elif'", "'else'", "'return'", "'+'", 
			"'-'", "'*'", "'/'", "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", "'%'", 
			"'and'", "'or'", "'not'", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "IF", "ELIF", "ELSE", "RETURN", "PLUS", "MINUS", 
			"MULT", "DIV", "GT", "GTE", "LT", "LTE", "EQ", "NEQ", "MOD", "AND", "OR", 
			"NOT", "TRUE", "FALSE", "COMMENT_SINGLELINE", "NUMBER", "STRING", "ID", 
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
			setState(79); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(78);
				stat();
				}
				}
				setState(81); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 4186940582718722L) != 0) );
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
			setState(93);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(83);
				printStat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(84);
				varDecl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(85);
				ifStat();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(86);
				forLoop();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(87);
				whileLoop();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(88);
				functionDecl();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(89);
				functionCall();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(90);
				arrayInit();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(91);
				enumDecl();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(92);
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
			setState(95);
			match(T__0);
			setState(96);
			openParenth();
			setState(97);
			expr(0);
			setState(98);
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
			setState(100);
			match(ID);
			setState(105);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(101);
				match(T__1);
				setState(102);
				expr(0);
				}
				break;
			case 2:
				{
				setState(103);
				arrayInit();
				}
				break;
			case 3:
				{
				setState(104);
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
			setState(107);
			baseType();
			setState(111);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__22) {
				{
				setState(108);
				openBrack();
				setState(109);
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
			setState(113);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2251799813685496L) != 0)) ) {
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
		public TerminalNode IF() { return getToken(RogueLangParser.IF, 0); }
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
		}
		public IfExprContext ifExpr() {
			return getRuleContext(IfExprContext.class,0);
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
		public IfBlockContext ifBlock() {
			return getRuleContext(IfBlockContext.class,0);
		}
		public List<ClosedCurlBrackContext> closedCurlBrack() {
			return getRuleContexts(ClosedCurlBrackContext.class);
		}
		public ClosedCurlBrackContext closedCurlBrack(int i) {
			return getRuleContext(ClosedCurlBrackContext.class,i);
		}
		public List<ElifBlockstatContext> elifBlockstat() {
			return getRuleContexts(ElifBlockstatContext.class);
		}
		public ElifBlockstatContext elifBlockstat(int i) {
			return getRuleContext(ElifBlockstatContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(RogueLangParser.ELSE, 0); }
		public ElseBlockContext elseBlock() {
			return getRuleContext(ElseBlockContext.class,0);
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
			setState(115);
			match(IF);
			setState(116);
			openParenth();
			setState(117);
			ifExpr();
			setState(118);
			closedParenth();
			setState(119);
			openCurlBrack();
			setState(120);
			ifBlock();
			setState(121);
			closedCurlBrack();
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELIF) {
				{
				{
				setState(122);
				elifBlockstat();
				}
				}
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(128);
				match(ELSE);
				setState(129);
				openCurlBrack();
				setState(130);
				elseBlock();
				setState(131);
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
	public static class ElifBlockstatContext extends ParserRuleContext {
		public TerminalNode ELIF() { return getToken(RogueLangParser.ELIF, 0); }
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
		}
		public ElifExprContext elifExpr() {
			return getRuleContext(ElifExprContext.class,0);
		}
		public ClosedParenthContext closedParenth() {
			return getRuleContext(ClosedParenthContext.class,0);
		}
		public OpenCurlBrackContext openCurlBrack() {
			return getRuleContext(OpenCurlBrackContext.class,0);
		}
		public ElifBlockContext elifBlock() {
			return getRuleContext(ElifBlockContext.class,0);
		}
		public ClosedCurlBrackContext closedCurlBrack() {
			return getRuleContext(ClosedCurlBrackContext.class,0);
		}
		public ElifBlockstatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elifBlockstat; }
	}

	public final ElifBlockstatContext elifBlockstat() throws RecognitionException {
		ElifBlockstatContext _localctx = new ElifBlockstatContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_elifBlockstat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(ELIF);
			setState(136);
			openParenth();
			setState(137);
			elifExpr();
			setState(138);
			closedParenth();
			setState(139);
			openCurlBrack();
			setState(140);
			elifBlock();
			setState(141);
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
	public static class IfExprContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public IfExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifExpr; }
	}

	public final IfExprContext ifExpr() throws RecognitionException {
		IfExprContext _localctx = new IfExprContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ifExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
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
	public static class IfBlockContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public IfBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifBlock; }
	}

	public final IfBlockContext ifBlock() throws RecognitionException {
		IfBlockContext _localctx = new IfBlockContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_ifBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4186940582718722L) != 0)) {
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
	public static class ElifExprContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ElifExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elifExpr; }
	}

	public final ElifExprContext elifExpr() throws RecognitionException {
		ElifExprContext _localctx = new ElifExprContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_elifExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
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
	public static class ElifBlockContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ElifBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elifBlock; }
	}

	public final ElifBlockContext elifBlock() throws RecognitionException {
		ElifBlockContext _localctx = new ElifBlockContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_elifBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4186940582718722L) != 0)) {
				{
				{
				setState(153);
				stat();
				}
				}
				setState(158);
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
	public static class ElseBlockContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ElseBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseBlock; }
	}

	public final ElseBlockContext elseBlock() throws RecognitionException {
		ElseBlockContext _localctx = new ElseBlockContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_elseBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4186940582718722L) != 0)) {
				{
				{
				setState(159);
				stat();
				}
				}
				setState(164);
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
		enterRule(_localctx, 26, RULE_forLoop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			match(T__7);
			setState(166);
			varDecl();
			setState(167);
			match(T__8);
			setState(168);
			expr(0);
			setState(169);
			openCurlBrack();
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4186940582718722L) != 0)) {
				{
				{
				setState(170);
				stat();
				}
				}
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(176);
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
		enterRule(_localctx, 28, RULE_whileLoop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			match(T__9);
			setState(179);
			openParenth();
			setState(180);
			expr(0);
			setState(181);
			closedParenth();
			setState(182);
			openCurlBrack();
			setState(186);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4186940582718722L) != 0)) {
				{
				{
				setState(183);
				stat();
				}
				}
				setState(188);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(189);
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
		enterRule(_localctx, 30, RULE_functionDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			match(T__10);
			setState(192);
			match(ID);
			setState(193);
			openParenth();
			setState(195);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(194);
				params();
				}
			}

			setState(197);
			closedParenth();
			setState(198);
			openCurlBrack();
			setState(202);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4186940582718722L) != 0)) {
				{
				{
				setState(199);
				stat();
				}
				}
				setState(204);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(205);
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
		public TerminalNode RETURN() { return getToken(RogueLangParser.RETURN, 0); }
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			match(ID);
			setState(208);
			openParenth();
			setState(210);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4186940280692736L) != 0)) {
				{
				setState(209);
				args();
				}
			}

			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==RETURN) {
				{
				setState(212);
				match(RETURN);
				}
			}

			setState(215);
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
		enterRule(_localctx, 34, RULE_arrayInit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			openCurlBrack();
			setState(218);
			expr(0);
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__26) {
				{
				{
				setState(219);
				comma();
				setState(220);
				expr(0);
				}
				}
				setState(226);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(227);
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
		enterRule(_localctx, 36, RULE_bsp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			match(T__11);
			setState(230);
			bspDimension();
			setState(231);
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
		enterRule(_localctx, 38, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(233);
			param();
			setState(239);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__26) {
				{
				{
				setState(234);
				comma();
				setState(235);
				param();
				}
				}
				setState(241);
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
		public TerminalNode ID() { return getToken(RogueLangParser.ID, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
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
		enterRule(_localctx, 42, RULE_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			expr(0);
			setState(250);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__26) {
				{
				{
				setState(245);
				comma();
				setState(246);
				expr(0);
				}
				}
				setState(252);
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
		enterRule(_localctx, 44, RULE_randomNumber);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			match(T__12);
			setState(254);
			openParenth();
			setState(255);
			match(NUMBER);
			setState(256);
			comma();
			setState(257);
			match(NUMBER);
			setState(258);
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
		enterRule(_localctx, 46, RULE_randomChoice);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(T__13);
			setState(261);
			openParenth();
			setState(262);
			expr(0);
			setState(266); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(263);
				comma();
				setState(264);
				expr(0);
				}
				}
				setState(268); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__26 );
			setState(270);
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
		enterRule(_localctx, 48, RULE_enumDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			match(T__14);
			setState(273);
			match(ID);
			setState(274);
			openCurlBrack();
			setState(275);
			enumBody();
			setState(276);
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
		enterRule(_localctx, 50, RULE_enumBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(278);
			match(ID);
			setState(284);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__26) {
				{
				{
				setState(279);
				comma();
				setState(280);
				match(ID);
				}
				}
				setState(286);
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
		enterRule(_localctx, 52, RULE_enumValue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(287);
			match(ID);
			setState(288);
			match(T__15);
			setState(289);
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
		enterRule(_localctx, 54, RULE_bspDimension);
		try {
			setState(295);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__16:
				enterOuterAlt(_localctx, 1);
				{
				setState(291);
				match(T__16);
				}
				break;
			case T__17:
				enterOuterAlt(_localctx, 2);
				{
				setState(292);
				match(T__17);
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 3);
				{
				setState(293);
				match(NUMBER);
				setState(294);
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
		enterRule(_localctx, 56, RULE_bspParameters);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			openParenth();
			setState(298);
			dimensionList();
			setState(299);
			comma();
			setState(300);
			minSize();
			setState(301);
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
		enterRule(_localctx, 58, RULE_dimensionList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(303);
			match(NUMBER);
			setState(309);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(304);
					comma();
					setState(305);
					match(NUMBER);
					}
					} 
				}
				setState(311);
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
		enterRule(_localctx, 60, RULE_minSize);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
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
		public TerminalNode NOT() { return getToken(RogueLangParser.NOT, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public OpenParenthContext openParenth() {
			return getRuleContext(OpenParenthContext.class,0);
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
		int _startState = 62;
		enterRecursionRule(_localctx, 62, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(329);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				{
				setState(315);
				match(NOT);
				setState(316);
				expr(10);
				}
				break;
			case 2:
				{
				setState(317);
				openParenth();
				setState(318);
				expr(0);
				setState(319);
				closedParenth();
				}
				break;
			case 3:
				{
				setState(321);
				match(ID);
				}
				break;
			case 4:
				{
				setState(322);
				match(STRING);
				}
				break;
			case 5:
				{
				setState(323);
				match(NUMBER);
				}
				break;
			case 6:
				{
				setState(324);
				match(TRUE);
				}
				break;
			case 7:
				{
				setState(325);
				match(FALSE);
				}
				break;
			case 8:
				{
				setState(326);
				randomNumber();
				}
				break;
			case 9:
				{
				setState(327);
				randomChoice();
				}
				break;
			case 10:
				{
				setState(328);
				enumValue();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(363);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(361);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(331);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(332);
						openBrack();
						setState(333);
						expr(0);
						setState(334);
						closedBrack();
						setState(335);
						match(T__1);
						setState(336);
						expr(17);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(338);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(339);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4449586118656L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(340);
						expr(15);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(341);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(342);
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
						setState(343);
						expr(14);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(344);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(345);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4329327034368L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(346);
						expr(13);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(347);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(348);
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
						setState(349);
						expr(12);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(350);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(351);
						openBrack();
						setState(352);
						expr(0);
						setState(353);
						closedBrack();
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(355);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(356);
						match(T__19);
						setState(357);
						openParenth();
						setState(358);
						expr(0);
						setState(359);
						closedParenth();
						}
						break;
					}
					} 
				}
				setState(365);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
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
		enterRule(_localctx, 64, RULE_openParenth);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(366);
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
		enterRule(_localctx, 66, RULE_closedParenth);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(368);
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
		enterRule(_localctx, 68, RULE_openBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(370);
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
		enterRule(_localctx, 70, RULE_closedBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(372);
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
		enterRule(_localctx, 72, RULE_openCurlBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
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
		enterRule(_localctx, 74, RULE_closedCurlBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
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
		enterRule(_localctx, 76, RULE_comma);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(378);
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
		case 31:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 16);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 12);
		case 4:
			return precpred(_ctx, 11);
		case 5:
			return precpred(_ctx, 17);
		case 6:
			return precpred(_ctx, 15);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00014\u017d\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0001\u0000\u0004\u0000"+
		"P\b\u0000\u000b\u0000\f\u0000Q\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0003\u0001^\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0003\u0003j\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0003\u0004p\b\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0005\u0006|\b\u0006\n\u0006\f\u0006\u007f\t\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u0086\b\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0005\t\u0093\b\t\n\t"+
		"\f\t\u0096\t\t\u0001\n\u0001\n\u0001\u000b\u0005\u000b\u009b\b\u000b\n"+
		"\u000b\f\u000b\u009e\t\u000b\u0001\f\u0005\f\u00a1\b\f\n\f\f\f\u00a4\t"+
		"\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r\u00ac\b\r\n"+
		"\r\f\r\u00af\t\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u00b9\b\u000e\n\u000e\f\u000e"+
		"\u00bc\t\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0003\u000f\u00c4\b\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0005\u000f\u00c9\b\u000f\n\u000f\f\u000f\u00cc\t\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u00d3\b\u0010\u0001"+
		"\u0010\u0003\u0010\u00d6\b\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u00df\b\u0011\n"+
		"\u0011\f\u0011\u00e2\t\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0005\u0013\u00ee\b\u0013\n\u0013\f\u0013\u00f1\t\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0005\u0015"+
		"\u00f9\b\u0015\n\u0015\f\u0015\u00fc\t\u0015\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0004\u0017\u010b"+
		"\b\u0017\u000b\u0017\f\u0017\u010c\u0001\u0017\u0001\u0017\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0005\u0019\u011b\b\u0019\n\u0019"+
		"\f\u0019\u011e\t\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u0128\b\u001b"+
		"\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0005\u001d\u0134\b\u001d"+
		"\n\u001d\f\u001d\u0137\t\u001d\u0001\u001e\u0001\u001e\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0003\u001f\u014a\b\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0005\u001f\u016a\b\u001f\n"+
		"\u001f\f\u001f\u016d\t\u001f\u0001 \u0001 \u0001!\u0001!\u0001\"\u0001"+
		"\"\u0001#\u0001#\u0001$\u0001$\u0001%\u0001%\u0001&\u0001&\u0001&\u0000"+
		"\u0001>\'\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJL\u0000\u0005\u0002\u0000"+
		"\u0003\u000733\u0002\u0000\"#**\u0001\u0000 !\u0001\u0000$)\u0001\u0000"+
		"+,\u0186\u0000O\u0001\u0000\u0000\u0000\u0002]\u0001\u0000\u0000\u0000"+
		"\u0004_\u0001\u0000\u0000\u0000\u0006d\u0001\u0000\u0000\u0000\bk\u0001"+
		"\u0000\u0000\u0000\nq\u0001\u0000\u0000\u0000\fs\u0001\u0000\u0000\u0000"+
		"\u000e\u0087\u0001\u0000\u0000\u0000\u0010\u008f\u0001\u0000\u0000\u0000"+
		"\u0012\u0094\u0001\u0000\u0000\u0000\u0014\u0097\u0001\u0000\u0000\u0000"+
		"\u0016\u009c\u0001\u0000\u0000\u0000\u0018\u00a2\u0001\u0000\u0000\u0000"+
		"\u001a\u00a5\u0001\u0000\u0000\u0000\u001c\u00b2\u0001\u0000\u0000\u0000"+
		"\u001e\u00bf\u0001\u0000\u0000\u0000 \u00cf\u0001\u0000\u0000\u0000\""+
		"\u00d9\u0001\u0000\u0000\u0000$\u00e5\u0001\u0000\u0000\u0000&\u00e9\u0001"+
		"\u0000\u0000\u0000(\u00f2\u0001\u0000\u0000\u0000*\u00f4\u0001\u0000\u0000"+
		"\u0000,\u00fd\u0001\u0000\u0000\u0000.\u0104\u0001\u0000\u0000\u00000"+
		"\u0110\u0001\u0000\u0000\u00002\u0116\u0001\u0000\u0000\u00004\u011f\u0001"+
		"\u0000\u0000\u00006\u0127\u0001\u0000\u0000\u00008\u0129\u0001\u0000\u0000"+
		"\u0000:\u012f\u0001\u0000\u0000\u0000<\u0138\u0001\u0000\u0000\u0000>"+
		"\u0149\u0001\u0000\u0000\u0000@\u016e\u0001\u0000\u0000\u0000B\u0170\u0001"+
		"\u0000\u0000\u0000D\u0172\u0001\u0000\u0000\u0000F\u0174\u0001\u0000\u0000"+
		"\u0000H\u0176\u0001\u0000\u0000\u0000J\u0178\u0001\u0000\u0000\u0000L"+
		"\u017a\u0001\u0000\u0000\u0000NP\u0003\u0002\u0001\u0000ON\u0001\u0000"+
		"\u0000\u0000PQ\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000QR\u0001"+
		"\u0000\u0000\u0000R\u0001\u0001\u0000\u0000\u0000S^\u0003\u0004\u0002"+
		"\u0000T^\u0003\u0006\u0003\u0000U^\u0003\f\u0006\u0000V^\u0003\u001a\r"+
		"\u0000W^\u0003\u001c\u000e\u0000X^\u0003\u001e\u000f\u0000Y^\u0003 \u0010"+
		"\u0000Z^\u0003\"\u0011\u0000[^\u00030\u0018\u0000\\^\u0003>\u001f\u0000"+
		"]S\u0001\u0000\u0000\u0000]T\u0001\u0000\u0000\u0000]U\u0001\u0000\u0000"+
		"\u0000]V\u0001\u0000\u0000\u0000]W\u0001\u0000\u0000\u0000]X\u0001\u0000"+
		"\u0000\u0000]Y\u0001\u0000\u0000\u0000]Z\u0001\u0000\u0000\u0000][\u0001"+
		"\u0000\u0000\u0000]\\\u0001\u0000\u0000\u0000^\u0003\u0001\u0000\u0000"+
		"\u0000_`\u0005\u0001\u0000\u0000`a\u0003@ \u0000ab\u0003>\u001f\u0000"+
		"bc\u0003B!\u0000c\u0005\u0001\u0000\u0000\u0000di\u00053\u0000\u0000e"+
		"f\u0005\u0002\u0000\u0000fj\u0003>\u001f\u0000gj\u0003\"\u0011\u0000h"+
		"j\u0003*\u0015\u0000ie\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000"+
		"ih\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000j\u0007\u0001\u0000"+
		"\u0000\u0000ko\u0003\n\u0005\u0000lm\u0003D\"\u0000mn\u0003F#\u0000np"+
		"\u0001\u0000\u0000\u0000ol\u0001\u0000\u0000\u0000op\u0001\u0000\u0000"+
		"\u0000p\t\u0001\u0000\u0000\u0000qr\u0007\u0000\u0000\u0000r\u000b\u0001"+
		"\u0000\u0000\u0000st\u0005\u001c\u0000\u0000tu\u0003@ \u0000uv\u0003\u0010"+
		"\b\u0000vw\u0003B!\u0000wx\u0003H$\u0000xy\u0003\u0012\t\u0000y}\u0003"+
		"J%\u0000z|\u0003\u000e\u0007\u0000{z\u0001\u0000\u0000\u0000|\u007f\u0001"+
		"\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000"+
		"~\u0085\u0001\u0000\u0000\u0000\u007f}\u0001\u0000\u0000\u0000\u0080\u0081"+
		"\u0005\u001e\u0000\u0000\u0081\u0082\u0003H$\u0000\u0082\u0083\u0003\u0018"+
		"\f\u0000\u0083\u0084\u0003J%\u0000\u0084\u0086\u0001\u0000\u0000\u0000"+
		"\u0085\u0080\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000"+
		"\u0086\r\u0001\u0000\u0000\u0000\u0087\u0088\u0005\u001d\u0000\u0000\u0088"+
		"\u0089\u0003@ \u0000\u0089\u008a\u0003\u0014\n\u0000\u008a\u008b\u0003"+
		"B!\u0000\u008b\u008c\u0003H$\u0000\u008c\u008d\u0003\u0016\u000b\u0000"+
		"\u008d\u008e\u0003J%\u0000\u008e\u000f\u0001\u0000\u0000\u0000\u008f\u0090"+
		"\u0003>\u001f\u0000\u0090\u0011\u0001\u0000\u0000\u0000\u0091\u0093\u0003"+
		"\u0002\u0001\u0000\u0092\u0091\u0001\u0000\u0000\u0000\u0093\u0096\u0001"+
		"\u0000\u0000\u0000\u0094\u0092\u0001\u0000\u0000\u0000\u0094\u0095\u0001"+
		"\u0000\u0000\u0000\u0095\u0013\u0001\u0000\u0000\u0000\u0096\u0094\u0001"+
		"\u0000\u0000\u0000\u0097\u0098\u0003>\u001f\u0000\u0098\u0015\u0001\u0000"+
		"\u0000\u0000\u0099\u009b\u0003\u0002\u0001\u0000\u009a\u0099\u0001\u0000"+
		"\u0000\u0000\u009b\u009e\u0001\u0000\u0000\u0000\u009c\u009a\u0001\u0000"+
		"\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009d\u0017\u0001\u0000"+
		"\u0000\u0000\u009e\u009c\u0001\u0000\u0000\u0000\u009f\u00a1\u0003\u0002"+
		"\u0001\u0000\u00a0\u009f\u0001\u0000\u0000\u0000\u00a1\u00a4\u0001\u0000"+
		"\u0000\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u00a2\u00a3\u0001\u0000"+
		"\u0000\u0000\u00a3\u0019\u0001\u0000\u0000\u0000\u00a4\u00a2\u0001\u0000"+
		"\u0000\u0000\u00a5\u00a6\u0005\b\u0000\u0000\u00a6\u00a7\u0003\u0006\u0003"+
		"\u0000\u00a7\u00a8\u0005\t\u0000\u0000\u00a8\u00a9\u0003>\u001f\u0000"+
		"\u00a9\u00ad\u0003H$\u0000\u00aa\u00ac\u0003\u0002\u0001\u0000\u00ab\u00aa"+
		"\u0001\u0000\u0000\u0000\u00ac\u00af\u0001\u0000\u0000\u0000\u00ad\u00ab"+
		"\u0001\u0000\u0000\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000\u00ae\u00b0"+
		"\u0001\u0000\u0000\u0000\u00af\u00ad\u0001\u0000\u0000\u0000\u00b0\u00b1"+
		"\u0003J%\u0000\u00b1\u001b\u0001\u0000\u0000\u0000\u00b2\u00b3\u0005\n"+
		"\u0000\u0000\u00b3\u00b4\u0003@ \u0000\u00b4\u00b5\u0003>\u001f\u0000"+
		"\u00b5\u00b6\u0003B!\u0000\u00b6\u00ba\u0003H$\u0000\u00b7\u00b9\u0003"+
		"\u0002\u0001\u0000\u00b8\u00b7\u0001\u0000\u0000\u0000\u00b9\u00bc\u0001"+
		"\u0000\u0000\u0000\u00ba\u00b8\u0001\u0000\u0000\u0000\u00ba\u00bb\u0001"+
		"\u0000\u0000\u0000\u00bb\u00bd\u0001\u0000\u0000\u0000\u00bc\u00ba\u0001"+
		"\u0000\u0000\u0000\u00bd\u00be\u0003J%\u0000\u00be\u001d\u0001\u0000\u0000"+
		"\u0000\u00bf\u00c0\u0005\u000b\u0000\u0000\u00c0\u00c1\u00053\u0000\u0000"+
		"\u00c1\u00c3\u0003@ \u0000\u00c2\u00c4\u0003&\u0013\u0000\u00c3\u00c2"+
		"\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000\u0000\u0000\u00c4\u00c5"+
		"\u0001\u0000\u0000\u0000\u00c5\u00c6\u0003B!\u0000\u00c6\u00ca\u0003H"+
		"$\u0000\u00c7\u00c9\u0003\u0002\u0001\u0000\u00c8\u00c7\u0001\u0000\u0000"+
		"\u0000\u00c9\u00cc\u0001\u0000\u0000\u0000\u00ca\u00c8\u0001\u0000\u0000"+
		"\u0000\u00ca\u00cb\u0001\u0000\u0000\u0000\u00cb\u00cd\u0001\u0000\u0000"+
		"\u0000\u00cc\u00ca\u0001\u0000\u0000\u0000\u00cd\u00ce\u0003J%\u0000\u00ce"+
		"\u001f\u0001\u0000\u0000\u0000\u00cf\u00d0\u00053\u0000\u0000\u00d0\u00d2"+
		"\u0003@ \u0000\u00d1\u00d3\u0003*\u0015\u0000\u00d2\u00d1\u0001\u0000"+
		"\u0000\u0000\u00d2\u00d3\u0001\u0000\u0000\u0000\u00d3\u00d5\u0001\u0000"+
		"\u0000\u0000\u00d4\u00d6\u0005\u001f\u0000\u0000\u00d5\u00d4\u0001\u0000"+
		"\u0000\u0000\u00d5\u00d6\u0001\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000"+
		"\u0000\u0000\u00d7\u00d8\u0003B!\u0000\u00d8!\u0001\u0000\u0000\u0000"+
		"\u00d9\u00da\u0003H$\u0000\u00da\u00e0\u0003>\u001f\u0000\u00db\u00dc"+
		"\u0003L&\u0000\u00dc\u00dd\u0003>\u001f\u0000\u00dd\u00df\u0001\u0000"+
		"\u0000\u0000\u00de\u00db\u0001\u0000\u0000\u0000\u00df\u00e2\u0001\u0000"+
		"\u0000\u0000\u00e0\u00de\u0001\u0000\u0000\u0000\u00e0\u00e1\u0001\u0000"+
		"\u0000\u0000\u00e1\u00e3\u0001\u0000\u0000\u0000\u00e2\u00e0\u0001\u0000"+
		"\u0000\u0000\u00e3\u00e4\u0003J%\u0000\u00e4#\u0001\u0000\u0000\u0000"+
		"\u00e5\u00e6\u0005\f\u0000\u0000\u00e6\u00e7\u00036\u001b\u0000\u00e7"+
		"\u00e8\u00038\u001c\u0000\u00e8%\u0001\u0000\u0000\u0000\u00e9\u00ef\u0003"+
		"(\u0014\u0000\u00ea\u00eb\u0003L&\u0000\u00eb\u00ec\u0003(\u0014\u0000"+
		"\u00ec\u00ee\u0001\u0000\u0000\u0000\u00ed\u00ea\u0001\u0000\u0000\u0000"+
		"\u00ee\u00f1\u0001\u0000\u0000\u0000\u00ef\u00ed\u0001\u0000\u0000\u0000"+
		"\u00ef\u00f0\u0001\u0000\u0000\u0000\u00f0\'\u0001\u0000\u0000\u0000\u00f1"+
		"\u00ef\u0001\u0000\u0000\u0000\u00f2\u00f3\u00053\u0000\u0000\u00f3)\u0001"+
		"\u0000\u0000\u0000\u00f4\u00fa\u0003>\u001f\u0000\u00f5\u00f6\u0003L&"+
		"\u0000\u00f6\u00f7\u0003>\u001f\u0000\u00f7\u00f9\u0001\u0000\u0000\u0000"+
		"\u00f8\u00f5\u0001\u0000\u0000\u0000\u00f9\u00fc\u0001\u0000\u0000\u0000"+
		"\u00fa\u00f8\u0001\u0000\u0000\u0000\u00fa\u00fb\u0001\u0000\u0000\u0000"+
		"\u00fb+\u0001\u0000\u0000\u0000\u00fc\u00fa\u0001\u0000\u0000\u0000\u00fd"+
		"\u00fe\u0005\r\u0000\u0000\u00fe\u00ff\u0003@ \u0000\u00ff\u0100\u0005"+
		"1\u0000\u0000\u0100\u0101\u0003L&\u0000\u0101\u0102\u00051\u0000\u0000"+
		"\u0102\u0103\u0003B!\u0000\u0103-\u0001\u0000\u0000\u0000\u0104\u0105"+
		"\u0005\u000e\u0000\u0000\u0105\u0106\u0003@ \u0000\u0106\u010a\u0003>"+
		"\u001f\u0000\u0107\u0108\u0003L&\u0000\u0108\u0109\u0003>\u001f\u0000"+
		"\u0109\u010b\u0001\u0000\u0000\u0000\u010a\u0107\u0001\u0000\u0000\u0000"+
		"\u010b\u010c\u0001\u0000\u0000\u0000\u010c\u010a\u0001\u0000\u0000\u0000"+
		"\u010c\u010d\u0001\u0000\u0000\u0000\u010d\u010e\u0001\u0000\u0000\u0000"+
		"\u010e\u010f\u0003B!\u0000\u010f/\u0001\u0000\u0000\u0000\u0110\u0111"+
		"\u0005\u000f\u0000\u0000\u0111\u0112\u00053\u0000\u0000\u0112\u0113\u0003"+
		"H$\u0000\u0113\u0114\u00032\u0019\u0000\u0114\u0115\u0003J%\u0000\u0115"+
		"1\u0001\u0000\u0000\u0000\u0116\u011c\u00053\u0000\u0000\u0117\u0118\u0003"+
		"L&\u0000\u0118\u0119\u00053\u0000\u0000\u0119\u011b\u0001\u0000\u0000"+
		"\u0000\u011a\u0117\u0001\u0000\u0000\u0000\u011b\u011e\u0001\u0000\u0000"+
		"\u0000\u011c\u011a\u0001\u0000\u0000\u0000\u011c\u011d\u0001\u0000\u0000"+
		"\u0000\u011d3\u0001\u0000\u0000\u0000\u011e\u011c\u0001\u0000\u0000\u0000"+
		"\u011f\u0120\u00053\u0000\u0000\u0120\u0121\u0005\u0010\u0000\u0000\u0121"+
		"\u0122\u00053\u0000\u0000\u01225\u0001\u0000\u0000\u0000\u0123\u0128\u0005"+
		"\u0011\u0000\u0000\u0124\u0128\u0005\u0012\u0000\u0000\u0125\u0126\u0005"+
		"1\u0000\u0000\u0126\u0128\u0005\u0013\u0000\u0000\u0127\u0123\u0001\u0000"+
		"\u0000\u0000\u0127\u0124\u0001\u0000\u0000\u0000\u0127\u0125\u0001\u0000"+
		"\u0000\u0000\u01287\u0001\u0000\u0000\u0000\u0129\u012a\u0003@ \u0000"+
		"\u012a\u012b\u0003:\u001d\u0000\u012b\u012c\u0003L&\u0000\u012c\u012d"+
		"\u0003<\u001e\u0000\u012d\u012e\u0003B!\u0000\u012e9\u0001\u0000\u0000"+
		"\u0000\u012f\u0135\u00051\u0000\u0000\u0130\u0131\u0003L&\u0000\u0131"+
		"\u0132\u00051\u0000\u0000\u0132\u0134\u0001\u0000\u0000\u0000\u0133\u0130"+
		"\u0001\u0000\u0000\u0000\u0134\u0137\u0001\u0000\u0000\u0000\u0135\u0133"+
		"\u0001\u0000\u0000\u0000\u0135\u0136\u0001\u0000\u0000\u0000\u0136;\u0001"+
		"\u0000\u0000\u0000\u0137\u0135\u0001\u0000\u0000\u0000\u0138\u0139\u0005"+
		"1\u0000\u0000\u0139=\u0001\u0000\u0000\u0000\u013a\u013b\u0006\u001f\uffff"+
		"\uffff\u0000\u013b\u013c\u0005-\u0000\u0000\u013c\u014a\u0003>\u001f\n"+
		"\u013d\u013e\u0003@ \u0000\u013e\u013f\u0003>\u001f\u0000\u013f\u0140"+
		"\u0003B!\u0000\u0140\u014a\u0001\u0000\u0000\u0000\u0141\u014a\u00053"+
		"\u0000\u0000\u0142\u014a\u00052\u0000\u0000\u0143\u014a\u00051\u0000\u0000"+
		"\u0144\u014a\u0005.\u0000\u0000\u0145\u014a\u0005/\u0000\u0000\u0146\u014a"+
		"\u0003,\u0016\u0000\u0147\u014a\u0003.\u0017\u0000\u0148\u014a\u00034"+
		"\u001a\u0000\u0149\u013a\u0001\u0000\u0000\u0000\u0149\u013d\u0001\u0000"+
		"\u0000\u0000\u0149\u0141\u0001\u0000\u0000\u0000\u0149\u0142\u0001\u0000"+
		"\u0000\u0000\u0149\u0143\u0001\u0000\u0000\u0000\u0149\u0144\u0001\u0000"+
		"\u0000\u0000\u0149\u0145\u0001\u0000\u0000\u0000\u0149\u0146\u0001\u0000"+
		"\u0000\u0000\u0149\u0147\u0001\u0000\u0000\u0000\u0149\u0148\u0001\u0000"+
		"\u0000\u0000\u014a\u016b\u0001\u0000\u0000\u0000\u014b\u014c\n\u0010\u0000"+
		"\u0000\u014c\u014d\u0003D\"\u0000\u014d\u014e\u0003>\u001f\u0000\u014e"+
		"\u014f\u0003F#\u0000\u014f\u0150\u0005\u0002\u0000\u0000\u0150\u0151\u0003"+
		">\u001f\u0011\u0151\u016a\u0001\u0000\u0000\u0000\u0152\u0153\n\u000e"+
		"\u0000\u0000\u0153\u0154\u0007\u0001\u0000\u0000\u0154\u016a\u0003>\u001f"+
		"\u000f\u0155\u0156\n\r\u0000\u0000\u0156\u0157\u0007\u0002\u0000\u0000"+
		"\u0157\u016a\u0003>\u001f\u000e\u0158\u0159\n\f\u0000\u0000\u0159\u015a"+
		"\u0007\u0003\u0000\u0000\u015a\u016a\u0003>\u001f\r\u015b\u015c\n\u000b"+
		"\u0000\u0000\u015c\u015d\u0007\u0004\u0000\u0000\u015d\u016a\u0003>\u001f"+
		"\f\u015e\u015f\n\u0011\u0000\u0000\u015f\u0160\u0003D\"\u0000\u0160\u0161"+
		"\u0003>\u001f\u0000\u0161\u0162\u0003F#\u0000\u0162\u016a\u0001\u0000"+
		"\u0000\u0000\u0163\u0164\n\u000f\u0000\u0000\u0164\u0165\u0005\u0014\u0000"+
		"\u0000\u0165\u0166\u0003@ \u0000\u0166\u0167\u0003>\u001f\u0000\u0167"+
		"\u0168\u0003B!\u0000\u0168\u016a\u0001\u0000\u0000\u0000\u0169\u014b\u0001"+
		"\u0000\u0000\u0000\u0169\u0152\u0001\u0000\u0000\u0000\u0169\u0155\u0001"+
		"\u0000\u0000\u0000\u0169\u0158\u0001\u0000\u0000\u0000\u0169\u015b\u0001"+
		"\u0000\u0000\u0000\u0169\u015e\u0001\u0000\u0000\u0000\u0169\u0163\u0001"+
		"\u0000\u0000\u0000\u016a\u016d\u0001\u0000\u0000\u0000\u016b\u0169\u0001"+
		"\u0000\u0000\u0000\u016b\u016c\u0001\u0000\u0000\u0000\u016c?\u0001\u0000"+
		"\u0000\u0000\u016d\u016b\u0001\u0000\u0000\u0000\u016e\u016f\u0005\u0015"+
		"\u0000\u0000\u016fA\u0001\u0000\u0000\u0000\u0170\u0171\u0005\u0016\u0000"+
		"\u0000\u0171C\u0001\u0000\u0000\u0000\u0172\u0173\u0005\u0017\u0000\u0000"+
		"\u0173E\u0001\u0000\u0000\u0000\u0174\u0175\u0005\u0018\u0000\u0000\u0175"+
		"G\u0001\u0000\u0000\u0000\u0176\u0177\u0005\u0019\u0000\u0000\u0177I\u0001"+
		"\u0000\u0000\u0000\u0178\u0179\u0005\u001a\u0000\u0000\u0179K\u0001\u0000"+
		"\u0000\u0000\u017a\u017b\u0005\u001b\u0000\u0000\u017bM\u0001\u0000\u0000"+
		"\u0000\u0019Q]io}\u0085\u0094\u009c\u00a2\u00ad\u00ba\u00c3\u00ca\u00d2"+
		"\u00d5\u00e0\u00ef\u00fa\u010c\u011c\u0127\u0135\u0149\u0169\u016b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}