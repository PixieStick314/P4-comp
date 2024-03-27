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
		T__24=25, IF=26, ELIF=27, ELSE=28, RETURN=29, PLUS=30, MINUS=31, MULT=32, 
		DIV=33, GT=34, GTE=35, LT=36, LTE=37, EQ=38, NEQ=39, MOD=40, AND=41, OR=42, 
		NOT=43, TRUE=44, FALSE=45, COMMENT_SINGLELINE=46, NUMBER=47, STRING=48, 
		ID=49, WS=50;
	public static final int
		RULE_prog = 0, RULE_stat = 1, RULE_printStat = 2, RULE_varDecl = 3, RULE_dataType = 4, 
		RULE_baseType = 5, RULE_ifStat = 6, RULE_ifExpr = 7, RULE_ifBlock = 8, 
		RULE_elifExpr = 9, RULE_elifBlock = 10, RULE_elseBlock = 11, RULE_forLoop = 12, 
		RULE_whileLoop = 13, RULE_functionDecl = 14, RULE_functionCall = 15, RULE_arrayInit = 16, 
		RULE_bsp = 17, RULE_params = 18, RULE_param = 19, RULE_args = 20, RULE_randomNumber = 21, 
		RULE_randomChoice = 22, RULE_enumDecl = 23, RULE_enumBody = 24, RULE_enumValue = 25, 
		RULE_bspDimension = 26, RULE_bspParameters = 27, RULE_dimensionList = 28, 
		RULE_minSize = 29, RULE_expr = 30, RULE_openParenth = 31, RULE_closedParenth = 32, 
		RULE_openBrack = 33, RULE_closedBrack = 34, RULE_openCurlBrack = 35, RULE_closedCurlBrack = 36, 
		RULE_comma = 37;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stat", "printStat", "varDecl", "dataType", "baseType", "ifStat", 
			"ifExpr", "ifBlock", "elifExpr", "elifBlock", "elseBlock", "forLoop", 
			"whileLoop", "functionDecl", "functionCall", "arrayInit", "bsp", "params", 
			"param", "args", "randomNumber", "randomChoice", "enumDecl", "enumBody", 
			"enumValue", "bspDimension", "bspParameters", "dimensionList", "minSize", 
			"expr", "openParenth", "closedParenth", "openBrack", "closedBrack", "openCurlBrack", 
			"closedCurlBrack", "comma"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'print'", "'='", "'string'", "'bool'", "'number'", "'for'", "'in'", 
			"'while'", "'def'", "'BSP'", "'randomNumber'", "'randomChoice'", "'enum'", 
			"'.'", "'2D'", "'3D'", "'D'", "'.add'", "'('", "')'", "'['", "']'", "'{'", 
			"'}'", "','", "'if'", "'elif'", "'else'", "'return'", "'+'", "'-'", "'*'", 
			"'/'", "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", "'%'", "'and'", 
			"'or'", "'not'", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, "IF", "ELIF", "ELSE", "RETURN", "PLUS", "MINUS", "MULT", 
			"DIV", "GT", "GTE", "LT", "LTE", "EQ", "NEQ", "MOD", "AND", "OR", "NOT", 
			"TRUE", "FALSE", "COMMENT_SINGLELINE", "NUMBER", "STRING", "ID", "WS"
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
			setState(77); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(76);
				stat();
				}
				}
				setState(79); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735145679682L) != 0) );
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
			setState(91);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(81);
				printStat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(82);
				varDecl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(83);
				ifStat();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(84);
				forLoop();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(85);
				whileLoop();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(86);
				functionDecl();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(87);
				functionCall();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(88);
				arrayInit();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(89);
				enumDecl();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(90);
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
			setState(93);
			match(T__0);
			setState(94);
			openParenth();
			setState(95);
			expr(0);
			setState(96);
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
			setState(98);
			match(ID);
			setState(103);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(99);
				match(T__1);
				setState(100);
				expr(0);
				}
				break;
			case 2:
				{
				setState(101);
				arrayInit();
				}
				break;
			case 3:
				{
				setState(102);
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
			setState(105);
			baseType();
			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(106);
				openBrack();
				setState(107);
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
			setState(111);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 615726511554616L) != 0)) ) {
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
		public List<OpenParenthContext> openParenth() {
			return getRuleContexts(OpenParenthContext.class);
		}
		public OpenParenthContext openParenth(int i) {
			return getRuleContext(OpenParenthContext.class,i);
		}
		public IfExprContext ifExpr() {
			return getRuleContext(IfExprContext.class,0);
		}
		public List<ClosedParenthContext> closedParenth() {
			return getRuleContexts(ClosedParenthContext.class);
		}
		public ClosedParenthContext closedParenth(int i) {
			return getRuleContext(ClosedParenthContext.class,i);
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
		public List<TerminalNode> ELIF() { return getTokens(RogueLangParser.ELIF); }
		public TerminalNode ELIF(int i) {
			return getToken(RogueLangParser.ELIF, i);
		}
		public List<ElifExprContext> elifExpr() {
			return getRuleContexts(ElifExprContext.class);
		}
		public ElifExprContext elifExpr(int i) {
			return getRuleContext(ElifExprContext.class,i);
		}
		public List<ElifBlockContext> elifBlock() {
			return getRuleContexts(ElifBlockContext.class);
		}
		public ElifBlockContext elifBlock(int i) {
			return getRuleContext(ElifBlockContext.class,i);
		}
		public List<ClosedBrackContext> closedBrack() {
			return getRuleContexts(ClosedBrackContext.class);
		}
		public ClosedBrackContext closedBrack(int i) {
			return getRuleContext(ClosedBrackContext.class,i);
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
			setState(113);
			match(IF);
			setState(114);
			openParenth();
			setState(115);
			ifExpr();
			setState(116);
			closedParenth();
			setState(117);
			openCurlBrack();
			setState(118);
			ifBlock();
			setState(119);
			closedCurlBrack();
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELIF) {
				{
				{
				setState(120);
				match(ELIF);
				setState(121);
				openParenth();
				setState(122);
				elifExpr();
				setState(123);
				closedParenth();
				setState(124);
				openCurlBrack();
				setState(125);
				elifBlock();
				setState(126);
				closedBrack();
				}
				}
				setState(132);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(133);
				match(ELSE);
				setState(134);
				openCurlBrack();
				setState(135);
				elseBlock();
				setState(136);
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
		enterRule(_localctx, 14, RULE_ifExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
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
		enterRule(_localctx, 16, RULE_ifBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735145679682L) != 0)) {
				{
				{
				setState(142);
				stat();
				}
				}
				setState(147);
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
		enterRule(_localctx, 18, RULE_elifExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
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
		enterRule(_localctx, 20, RULE_elifBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735145679682L) != 0)) {
				{
				{
				setState(150);
				stat();
				}
				}
				setState(155);
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
		enterRule(_localctx, 22, RULE_elseBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735145679682L) != 0)) {
				{
				{
				setState(156);
				stat();
				}
				}
				setState(161);
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
		enterRule(_localctx, 24, RULE_forLoop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			match(T__5);
			setState(163);
			varDecl();
			setState(164);
			match(T__6);
			setState(165);
			expr(0);
			setState(166);
			openCurlBrack();
			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735145679682L) != 0)) {
				{
				{
				setState(167);
				stat();
				}
				}
				setState(172);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(173);
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
		enterRule(_localctx, 26, RULE_whileLoop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(T__7);
			setState(176);
			openParenth();
			setState(177);
			expr(0);
			setState(178);
			closedParenth();
			setState(179);
			openCurlBrack();
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735145679682L) != 0)) {
				{
				{
				setState(180);
				stat();
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
		enterRule(_localctx, 28, RULE_functionDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			match(T__8);
			setState(189);
			match(ID);
			setState(190);
			openParenth();
			setState(192);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(191);
				params();
				}
			}

			setState(194);
			closedParenth();
			setState(195);
			openCurlBrack();
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735145679682L) != 0)) {
				{
				{
				setState(196);
				stat();
				}
				}
				setState(201);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(202);
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
		enterRule(_localctx, 30, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			match(ID);
			setState(205);
			openParenth();
			setState(207);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735070173184L) != 0)) {
				{
				setState(206);
				args();
				}
			}

			setState(210);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==RETURN) {
				{
				setState(209);
				match(RETURN);
				}
			}

			setState(212);
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
		enterRule(_localctx, 32, RULE_arrayInit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			openCurlBrack();
			setState(215);
			expr(0);
			setState(221);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__24) {
				{
				{
				setState(216);
				comma();
				setState(217);
				expr(0);
				}
				}
				setState(223);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(224);
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
		enterRule(_localctx, 34, RULE_bsp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			match(T__9);
			setState(227);
			bspDimension();
			setState(228);
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
		enterRule(_localctx, 36, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(230);
			param();
			setState(236);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__24) {
				{
				{
				setState(231);
				comma();
				setState(232);
				param();
				}
				}
				setState(238);
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
		enterRule(_localctx, 38, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
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
		enterRule(_localctx, 40, RULE_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			expr(0);
			setState(247);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__24) {
				{
				{
				setState(242);
				comma();
				setState(243);
				expr(0);
				}
				}
				setState(249);
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
		enterRule(_localctx, 42, RULE_randomNumber);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			match(T__10);
			setState(251);
			openParenth();
			setState(252);
			match(NUMBER);
			setState(253);
			comma();
			setState(254);
			match(NUMBER);
			setState(255);
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
		enterRule(_localctx, 44, RULE_randomChoice);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(T__11);
			setState(258);
			openParenth();
			setState(259);
			expr(0);
			setState(263); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(260);
				comma();
				setState(261);
				expr(0);
				}
				}
				setState(265); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__24 );
			setState(267);
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
		enterRule(_localctx, 46, RULE_enumDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(269);
			match(T__12);
			setState(270);
			match(ID);
			setState(271);
			openCurlBrack();
			setState(272);
			enumBody();
			setState(273);
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
		enterRule(_localctx, 48, RULE_enumBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(275);
			match(ID);
			setState(281);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__24) {
				{
				{
				setState(276);
				comma();
				setState(277);
				match(ID);
				}
				}
				setState(283);
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
		enterRule(_localctx, 50, RULE_enumValue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			match(ID);
			setState(285);
			match(T__13);
			setState(286);
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
		enterRule(_localctx, 52, RULE_bspDimension);
		try {
			setState(292);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__14:
				enterOuterAlt(_localctx, 1);
				{
				setState(288);
				match(T__14);
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 2);
				{
				setState(289);
				match(T__15);
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 3);
				{
				setState(290);
				match(NUMBER);
				setState(291);
				match(T__16);
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
		enterRule(_localctx, 54, RULE_bspParameters);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(294);
			openParenth();
			setState(295);
			dimensionList();
			setState(296);
			comma();
			setState(297);
			minSize();
			setState(298);
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
		enterRule(_localctx, 56, RULE_dimensionList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			match(NUMBER);
			setState(306);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(301);
					comma();
					setState(302);
					match(NUMBER);
					}
					} 
				}
				setState(308);
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
		enterRule(_localctx, 58, RULE_minSize);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(309);
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
		int _startState = 60;
		enterRecursionRule(_localctx, 60, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(326);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				{
				setState(312);
				match(NOT);
				setState(313);
				expr(10);
				}
				break;
			case 2:
				{
				setState(314);
				openParenth();
				setState(315);
				expr(0);
				setState(316);
				closedParenth();
				}
				break;
			case 3:
				{
				setState(318);
				match(ID);
				}
				break;
			case 4:
				{
				setState(319);
				match(STRING);
				}
				break;
			case 5:
				{
				setState(320);
				match(NUMBER);
				}
				break;
			case 6:
				{
				setState(321);
				match(TRUE);
				}
				break;
			case 7:
				{
				setState(322);
				match(FALSE);
				}
				break;
			case 8:
				{
				setState(323);
				randomNumber();
				}
				break;
			case 9:
				{
				setState(324);
				randomChoice();
				}
				break;
			case 10:
				{
				setState(325);
				enumValue();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(360);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(358);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(328);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(329);
						openBrack();
						setState(330);
						expr(0);
						setState(331);
						closedBrack();
						setState(332);
						match(T__1);
						setState(333);
						expr(17);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(335);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(336);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1112396529664L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(337);
						expr(15);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(338);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(339);
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
						setState(340);
						expr(14);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(341);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(342);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1082331758592L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(343);
						expr(13);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(344);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(345);
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
						setState(346);
						expr(12);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(347);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(348);
						openBrack();
						setState(349);
						expr(0);
						setState(350);
						closedBrack();
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(352);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(353);
						match(T__17);
						setState(354);
						openParenth();
						setState(355);
						expr(0);
						setState(356);
						closedParenth();
						}
						break;
					}
					} 
				}
				setState(362);
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
		enterRule(_localctx, 62, RULE_openParenth);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(363);
			match(T__18);
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
		enterRule(_localctx, 64, RULE_closedParenth);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(365);
			match(T__19);
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
		enterRule(_localctx, 66, RULE_openBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(367);
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
	public static class ClosedBrackContext extends ParserRuleContext {
		public ClosedBrackContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_closedBrack; }
	}

	public final ClosedBrackContext closedBrack() throws RecognitionException {
		ClosedBrackContext _localctx = new ClosedBrackContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_closedBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(369);
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
	public static class OpenCurlBrackContext extends ParserRuleContext {
		public OpenCurlBrackContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_openCurlBrack; }
	}

	public final OpenCurlBrackContext openCurlBrack() throws RecognitionException {
		OpenCurlBrackContext _localctx = new OpenCurlBrackContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_openCurlBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(371);
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
	public static class ClosedCurlBrackContext extends ParserRuleContext {
		public ClosedCurlBrackContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_closedCurlBrack; }
	}

	public final ClosedCurlBrackContext closedCurlBrack() throws RecognitionException {
		ClosedCurlBrackContext _localctx = new ClosedCurlBrackContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_closedCurlBrack);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(373);
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
	public static class CommaContext extends ParserRuleContext {
		public CommaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comma; }
	}

	public final CommaContext comma() throws RecognitionException {
		CommaContext _localctx = new CommaContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_comma);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(375);
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
		"\u0004\u00012\u017a\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0001\u0000\u0004\u0000N\b\u0000"+
		"\u000b\u0000\f\u0000O\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001\\\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0003\u0003h\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u0004n\b\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0005\u0006\u0081\b\u0006\n\u0006\f\u0006\u0084\t\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u008b"+
		"\b\u0006\u0001\u0007\u0001\u0007\u0001\b\u0005\b\u0090\b\b\n\b\f\b\u0093"+
		"\t\b\u0001\t\u0001\t\u0001\n\u0005\n\u0098\b\n\n\n\f\n\u009b\t\n\u0001"+
		"\u000b\u0005\u000b\u009e\b\u000b\n\u000b\f\u000b\u00a1\t\u000b\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0005\f\u00a9\b\f\n\f\f\f\u00ac"+
		"\t\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005"+
		"\r\u00b6\b\r\n\r\f\r\u00b9\t\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0003\u000e\u00c1\b\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0005\u000e\u00c6\b\u000e\n\u000e\f\u000e\u00c9\t\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00d0"+
		"\b\u000f\u0001\u000f\u0003\u000f\u00d3\b\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010"+
		"\u00dc\b\u0010\n\u0010\f\u0010\u00df\t\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0005\u0012\u00eb\b\u0012\n\u0012\f\u0012\u00ee\t\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0005\u0014\u00f6\b\u0014\n\u0014\f\u0014\u00f9\t\u0014\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0004"+
		"\u0016\u0108\b\u0016\u000b\u0016\f\u0016\u0109\u0001\u0016\u0001\u0016"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0005\u0018\u0118\b\u0018"+
		"\n\u0018\f\u0018\u011b\t\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u0125"+
		"\b\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0005\u001c\u0131"+
		"\b\u001c\n\u001c\f\u001c\u0134\t\u001c\u0001\u001d\u0001\u001d\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0003\u001e\u0147\b\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0005\u001e\u0167\b\u001e"+
		"\n\u001e\f\u001e\u016a\t\u001e\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001"+
		"!\u0001!\u0001\"\u0001\"\u0001#\u0001#\u0001$\u0001$\u0001%\u0001%\u0001"+
		"%\u0000\u0001<&\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJ\u0000\u0005\u0003"+
		"\u0000\u0003\u0005,-11\u0002\u0000 !((\u0001\u0000\u001e\u001f\u0001\u0000"+
		"\"\'\u0001\u0000)*\u0184\u0000M\u0001\u0000\u0000\u0000\u0002[\u0001\u0000"+
		"\u0000\u0000\u0004]\u0001\u0000\u0000\u0000\u0006b\u0001\u0000\u0000\u0000"+
		"\bi\u0001\u0000\u0000\u0000\no\u0001\u0000\u0000\u0000\fq\u0001\u0000"+
		"\u0000\u0000\u000e\u008c\u0001\u0000\u0000\u0000\u0010\u0091\u0001\u0000"+
		"\u0000\u0000\u0012\u0094\u0001\u0000\u0000\u0000\u0014\u0099\u0001\u0000"+
		"\u0000\u0000\u0016\u009f\u0001\u0000\u0000\u0000\u0018\u00a2\u0001\u0000"+
		"\u0000\u0000\u001a\u00af\u0001\u0000\u0000\u0000\u001c\u00bc\u0001\u0000"+
		"\u0000\u0000\u001e\u00cc\u0001\u0000\u0000\u0000 \u00d6\u0001\u0000\u0000"+
		"\u0000\"\u00e2\u0001\u0000\u0000\u0000$\u00e6\u0001\u0000\u0000\u0000"+
		"&\u00ef\u0001\u0000\u0000\u0000(\u00f1\u0001\u0000\u0000\u0000*\u00fa"+
		"\u0001\u0000\u0000\u0000,\u0101\u0001\u0000\u0000\u0000.\u010d\u0001\u0000"+
		"\u0000\u00000\u0113\u0001\u0000\u0000\u00002\u011c\u0001\u0000\u0000\u0000"+
		"4\u0124\u0001\u0000\u0000\u00006\u0126\u0001\u0000\u0000\u00008\u012c"+
		"\u0001\u0000\u0000\u0000:\u0135\u0001\u0000\u0000\u0000<\u0146\u0001\u0000"+
		"\u0000\u0000>\u016b\u0001\u0000\u0000\u0000@\u016d\u0001\u0000\u0000\u0000"+
		"B\u016f\u0001\u0000\u0000\u0000D\u0171\u0001\u0000\u0000\u0000F\u0173"+
		"\u0001\u0000\u0000\u0000H\u0175\u0001\u0000\u0000\u0000J\u0177\u0001\u0000"+
		"\u0000\u0000LN\u0003\u0002\u0001\u0000ML\u0001\u0000\u0000\u0000NO\u0001"+
		"\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000"+
		"P\u0001\u0001\u0000\u0000\u0000Q\\\u0003\u0004\u0002\u0000R\\\u0003\u0006"+
		"\u0003\u0000S\\\u0003\f\u0006\u0000T\\\u0003\u0018\f\u0000U\\\u0003\u001a"+
		"\r\u0000V\\\u0003\u001c\u000e\u0000W\\\u0003\u001e\u000f\u0000X\\\u0003"+
		" \u0010\u0000Y\\\u0003.\u0017\u0000Z\\\u0003<\u001e\u0000[Q\u0001\u0000"+
		"\u0000\u0000[R\u0001\u0000\u0000\u0000[S\u0001\u0000\u0000\u0000[T\u0001"+
		"\u0000\u0000\u0000[U\u0001\u0000\u0000\u0000[V\u0001\u0000\u0000\u0000"+
		"[W\u0001\u0000\u0000\u0000[X\u0001\u0000\u0000\u0000[Y\u0001\u0000\u0000"+
		"\u0000[Z\u0001\u0000\u0000\u0000\\\u0003\u0001\u0000\u0000\u0000]^\u0005"+
		"\u0001\u0000\u0000^_\u0003>\u001f\u0000_`\u0003<\u001e\u0000`a\u0003@"+
		" \u0000a\u0005\u0001\u0000\u0000\u0000bg\u00051\u0000\u0000cd\u0005\u0002"+
		"\u0000\u0000dh\u0003<\u001e\u0000eh\u0003 \u0010\u0000fh\u0003(\u0014"+
		"\u0000gc\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000gf\u0001\u0000"+
		"\u0000\u0000gh\u0001\u0000\u0000\u0000h\u0007\u0001\u0000\u0000\u0000"+
		"im\u0003\n\u0005\u0000jk\u0003B!\u0000kl\u0003D\"\u0000ln\u0001\u0000"+
		"\u0000\u0000mj\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000n\t\u0001"+
		"\u0000\u0000\u0000op\u0007\u0000\u0000\u0000p\u000b\u0001\u0000\u0000"+
		"\u0000qr\u0005\u001a\u0000\u0000rs\u0003>\u001f\u0000st\u0003\u000e\u0007"+
		"\u0000tu\u0003@ \u0000uv\u0003F#\u0000vw\u0003\u0010\b\u0000w\u0082\u0003"+
		"H$\u0000xy\u0005\u001b\u0000\u0000yz\u0003>\u001f\u0000z{\u0003\u0012"+
		"\t\u0000{|\u0003@ \u0000|}\u0003F#\u0000}~\u0003\u0014\n\u0000~\u007f"+
		"\u0003D\"\u0000\u007f\u0081\u0001\u0000\u0000\u0000\u0080x\u0001\u0000"+
		"\u0000\u0000\u0081\u0084\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000"+
		"\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u008a\u0001\u0000"+
		"\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u0086\u0005\u001c"+
		"\u0000\u0000\u0086\u0087\u0003F#\u0000\u0087\u0088\u0003\u0016\u000b\u0000"+
		"\u0088\u0089\u0003H$\u0000\u0089\u008b\u0001\u0000\u0000\u0000\u008a\u0085"+
		"\u0001\u0000\u0000\u0000\u008a\u008b\u0001\u0000\u0000\u0000\u008b\r\u0001"+
		"\u0000\u0000\u0000\u008c\u008d\u0003<\u001e\u0000\u008d\u000f\u0001\u0000"+
		"\u0000\u0000\u008e\u0090\u0003\u0002\u0001\u0000\u008f\u008e\u0001\u0000"+
		"\u0000\u0000\u0090\u0093\u0001\u0000\u0000\u0000\u0091\u008f\u0001\u0000"+
		"\u0000\u0000\u0091\u0092\u0001\u0000\u0000\u0000\u0092\u0011\u0001\u0000"+
		"\u0000\u0000\u0093\u0091\u0001\u0000\u0000\u0000\u0094\u0095\u0003<\u001e"+
		"\u0000\u0095\u0013\u0001\u0000\u0000\u0000\u0096\u0098\u0003\u0002\u0001"+
		"\u0000\u0097\u0096\u0001\u0000\u0000\u0000\u0098\u009b\u0001\u0000\u0000"+
		"\u0000\u0099\u0097\u0001\u0000\u0000\u0000\u0099\u009a\u0001\u0000\u0000"+
		"\u0000\u009a\u0015\u0001\u0000\u0000\u0000\u009b\u0099\u0001\u0000\u0000"+
		"\u0000\u009c\u009e\u0003\u0002\u0001\u0000\u009d\u009c\u0001\u0000\u0000"+
		"\u0000\u009e\u00a1\u0001\u0000\u0000\u0000\u009f\u009d\u0001\u0000\u0000"+
		"\u0000\u009f\u00a0\u0001\u0000\u0000\u0000\u00a0\u0017\u0001\u0000\u0000"+
		"\u0000\u00a1\u009f\u0001\u0000\u0000\u0000\u00a2\u00a3\u0005\u0006\u0000"+
		"\u0000\u00a3\u00a4\u0003\u0006\u0003\u0000\u00a4\u00a5\u0005\u0007\u0000"+
		"\u0000\u00a5\u00a6\u0003<\u001e\u0000\u00a6\u00aa\u0003F#\u0000\u00a7"+
		"\u00a9\u0003\u0002\u0001\u0000\u00a8\u00a7\u0001\u0000\u0000\u0000\u00a9"+
		"\u00ac\u0001\u0000\u0000\u0000\u00aa\u00a8\u0001\u0000\u0000\u0000\u00aa"+
		"\u00ab\u0001\u0000\u0000\u0000\u00ab\u00ad\u0001\u0000\u0000\u0000\u00ac"+
		"\u00aa\u0001\u0000\u0000\u0000\u00ad\u00ae\u0003H$\u0000\u00ae\u0019\u0001"+
		"\u0000\u0000\u0000\u00af\u00b0\u0005\b\u0000\u0000\u00b0\u00b1\u0003>"+
		"\u001f\u0000\u00b1\u00b2\u0003<\u001e\u0000\u00b2\u00b3\u0003@ \u0000"+
		"\u00b3\u00b7\u0003F#\u0000\u00b4\u00b6\u0003\u0002\u0001\u0000\u00b5\u00b4"+
		"\u0001\u0000\u0000\u0000\u00b6\u00b9\u0001\u0000\u0000\u0000\u00b7\u00b5"+
		"\u0001\u0000\u0000\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8\u00ba"+
		"\u0001\u0000\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00ba\u00bb"+
		"\u0003H$\u0000\u00bb\u001b\u0001\u0000\u0000\u0000\u00bc\u00bd\u0005\t"+
		"\u0000\u0000\u00bd\u00be\u00051\u0000\u0000\u00be\u00c0\u0003>\u001f\u0000"+
		"\u00bf\u00c1\u0003$\u0012\u0000\u00c0\u00bf\u0001\u0000\u0000\u0000\u00c0"+
		"\u00c1\u0001\u0000\u0000\u0000\u00c1\u00c2\u0001\u0000\u0000\u0000\u00c2"+
		"\u00c3\u0003@ \u0000\u00c3\u00c7\u0003F#\u0000\u00c4\u00c6\u0003\u0002"+
		"\u0001\u0000\u00c5\u00c4\u0001\u0000\u0000\u0000\u00c6\u00c9\u0001\u0000"+
		"\u0000\u0000\u00c7\u00c5\u0001\u0000\u0000\u0000\u00c7\u00c8\u0001\u0000"+
		"\u0000\u0000\u00c8\u00ca\u0001\u0000\u0000\u0000\u00c9\u00c7\u0001\u0000"+
		"\u0000\u0000\u00ca\u00cb\u0003H$\u0000\u00cb\u001d\u0001\u0000\u0000\u0000"+
		"\u00cc\u00cd\u00051\u0000\u0000\u00cd\u00cf\u0003>\u001f\u0000\u00ce\u00d0"+
		"\u0003(\u0014\u0000\u00cf\u00ce\u0001\u0000\u0000\u0000\u00cf\u00d0\u0001"+
		"\u0000\u0000\u0000\u00d0\u00d2\u0001\u0000\u0000\u0000\u00d1\u00d3\u0005"+
		"\u001d\u0000\u0000\u00d2\u00d1\u0001\u0000\u0000\u0000\u00d2\u00d3\u0001"+
		"\u0000\u0000\u0000\u00d3\u00d4\u0001\u0000\u0000\u0000\u00d4\u00d5\u0003"+
		"@ \u0000\u00d5\u001f\u0001\u0000\u0000\u0000\u00d6\u00d7\u0003F#\u0000"+
		"\u00d7\u00dd\u0003<\u001e\u0000\u00d8\u00d9\u0003J%\u0000\u00d9\u00da"+
		"\u0003<\u001e\u0000\u00da\u00dc\u0001\u0000\u0000\u0000\u00db\u00d8\u0001"+
		"\u0000\u0000\u0000\u00dc\u00df\u0001\u0000\u0000\u0000\u00dd\u00db\u0001"+
		"\u0000\u0000\u0000\u00dd\u00de\u0001\u0000\u0000\u0000\u00de\u00e0\u0001"+
		"\u0000\u0000\u0000\u00df\u00dd\u0001\u0000\u0000\u0000\u00e0\u00e1\u0003"+
		"H$\u0000\u00e1!\u0001\u0000\u0000\u0000\u00e2\u00e3\u0005\n\u0000\u0000"+
		"\u00e3\u00e4\u00034\u001a\u0000\u00e4\u00e5\u00036\u001b\u0000\u00e5#"+
		"\u0001\u0000\u0000\u0000\u00e6\u00ec\u0003&\u0013\u0000\u00e7\u00e8\u0003"+
		"J%\u0000\u00e8\u00e9\u0003&\u0013\u0000\u00e9\u00eb\u0001\u0000\u0000"+
		"\u0000\u00ea\u00e7\u0001\u0000\u0000\u0000\u00eb\u00ee\u0001\u0000\u0000"+
		"\u0000\u00ec\u00ea\u0001\u0000\u0000\u0000\u00ec\u00ed\u0001\u0000\u0000"+
		"\u0000\u00ed%\u0001\u0000\u0000\u0000\u00ee\u00ec\u0001\u0000\u0000\u0000"+
		"\u00ef\u00f0\u00051\u0000\u0000\u00f0\'\u0001\u0000\u0000\u0000\u00f1"+
		"\u00f7\u0003<\u001e\u0000\u00f2\u00f3\u0003J%\u0000\u00f3\u00f4\u0003"+
		"<\u001e\u0000\u00f4\u00f6\u0001\u0000\u0000\u0000\u00f5\u00f2\u0001\u0000"+
		"\u0000\u0000\u00f6\u00f9\u0001\u0000\u0000\u0000\u00f7\u00f5\u0001\u0000"+
		"\u0000\u0000\u00f7\u00f8\u0001\u0000\u0000\u0000\u00f8)\u0001\u0000\u0000"+
		"\u0000\u00f9\u00f7\u0001\u0000\u0000\u0000\u00fa\u00fb\u0005\u000b\u0000"+
		"\u0000\u00fb\u00fc\u0003>\u001f\u0000\u00fc\u00fd\u0005/\u0000\u0000\u00fd"+
		"\u00fe\u0003J%\u0000\u00fe\u00ff\u0005/\u0000\u0000\u00ff\u0100\u0003"+
		"@ \u0000\u0100+\u0001\u0000\u0000\u0000\u0101\u0102\u0005\f\u0000\u0000"+
		"\u0102\u0103\u0003>\u001f\u0000\u0103\u0107\u0003<\u001e\u0000\u0104\u0105"+
		"\u0003J%\u0000\u0105\u0106\u0003<\u001e\u0000\u0106\u0108\u0001\u0000"+
		"\u0000\u0000\u0107\u0104\u0001\u0000\u0000\u0000\u0108\u0109\u0001\u0000"+
		"\u0000\u0000\u0109\u0107\u0001\u0000\u0000\u0000\u0109\u010a\u0001\u0000"+
		"\u0000\u0000\u010a\u010b\u0001\u0000\u0000\u0000\u010b\u010c\u0003@ \u0000"+
		"\u010c-\u0001\u0000\u0000\u0000\u010d\u010e\u0005\r\u0000\u0000\u010e"+
		"\u010f\u00051\u0000\u0000\u010f\u0110\u0003F#\u0000\u0110\u0111\u0003"+
		"0\u0018\u0000\u0111\u0112\u0003H$\u0000\u0112/\u0001\u0000\u0000\u0000"+
		"\u0113\u0119\u00051\u0000\u0000\u0114\u0115\u0003J%\u0000\u0115\u0116"+
		"\u00051\u0000\u0000\u0116\u0118\u0001\u0000\u0000\u0000\u0117\u0114\u0001"+
		"\u0000\u0000\u0000\u0118\u011b\u0001\u0000\u0000\u0000\u0119\u0117\u0001"+
		"\u0000\u0000\u0000\u0119\u011a\u0001\u0000\u0000\u0000\u011a1\u0001\u0000"+
		"\u0000\u0000\u011b\u0119\u0001\u0000\u0000\u0000\u011c\u011d\u00051\u0000"+
		"\u0000\u011d\u011e\u0005\u000e\u0000\u0000\u011e\u011f\u00051\u0000\u0000"+
		"\u011f3\u0001\u0000\u0000\u0000\u0120\u0125\u0005\u000f\u0000\u0000\u0121"+
		"\u0125\u0005\u0010\u0000\u0000\u0122\u0123\u0005/\u0000\u0000\u0123\u0125"+
		"\u0005\u0011\u0000\u0000\u0124\u0120\u0001\u0000\u0000\u0000\u0124\u0121"+
		"\u0001\u0000\u0000\u0000\u0124\u0122\u0001\u0000\u0000\u0000\u01255\u0001"+
		"\u0000\u0000\u0000\u0126\u0127\u0003>\u001f\u0000\u0127\u0128\u00038\u001c"+
		"\u0000\u0128\u0129\u0003J%\u0000\u0129\u012a\u0003:\u001d\u0000\u012a"+
		"\u012b\u0003@ \u0000\u012b7\u0001\u0000\u0000\u0000\u012c\u0132\u0005"+
		"/\u0000\u0000\u012d\u012e\u0003J%\u0000\u012e\u012f\u0005/\u0000\u0000"+
		"\u012f\u0131\u0001\u0000\u0000\u0000\u0130\u012d\u0001\u0000\u0000\u0000"+
		"\u0131\u0134\u0001\u0000\u0000\u0000\u0132\u0130\u0001\u0000\u0000\u0000"+
		"\u0132\u0133\u0001\u0000\u0000\u0000\u01339\u0001\u0000\u0000\u0000\u0134"+
		"\u0132\u0001\u0000\u0000\u0000\u0135\u0136\u0005/\u0000\u0000\u0136;\u0001"+
		"\u0000\u0000\u0000\u0137\u0138\u0006\u001e\uffff\uffff\u0000\u0138\u0139"+
		"\u0005+\u0000\u0000\u0139\u0147\u0003<\u001e\n\u013a\u013b\u0003>\u001f"+
		"\u0000\u013b\u013c\u0003<\u001e\u0000\u013c\u013d\u0003@ \u0000\u013d"+
		"\u0147\u0001\u0000\u0000\u0000\u013e\u0147\u00051\u0000\u0000\u013f\u0147"+
		"\u00050\u0000\u0000\u0140\u0147\u0005/\u0000\u0000\u0141\u0147\u0005,"+
		"\u0000\u0000\u0142\u0147\u0005-\u0000\u0000\u0143\u0147\u0003*\u0015\u0000"+
		"\u0144\u0147\u0003,\u0016\u0000\u0145\u0147\u00032\u0019\u0000\u0146\u0137"+
		"\u0001\u0000\u0000\u0000\u0146\u013a\u0001\u0000\u0000\u0000\u0146\u013e"+
		"\u0001\u0000\u0000\u0000\u0146\u013f\u0001\u0000\u0000\u0000\u0146\u0140"+
		"\u0001\u0000\u0000\u0000\u0146\u0141\u0001\u0000\u0000\u0000\u0146\u0142"+
		"\u0001\u0000\u0000\u0000\u0146\u0143\u0001\u0000\u0000\u0000\u0146\u0144"+
		"\u0001\u0000\u0000\u0000\u0146\u0145\u0001\u0000\u0000\u0000\u0147\u0168"+
		"\u0001\u0000\u0000\u0000\u0148\u0149\n\u0010\u0000\u0000\u0149\u014a\u0003"+
		"B!\u0000\u014a\u014b\u0003<\u001e\u0000\u014b\u014c\u0003D\"\u0000\u014c"+
		"\u014d\u0005\u0002\u0000\u0000\u014d\u014e\u0003<\u001e\u0011\u014e\u0167"+
		"\u0001\u0000\u0000\u0000\u014f\u0150\n\u000e\u0000\u0000\u0150\u0151\u0007"+
		"\u0001\u0000\u0000\u0151\u0167\u0003<\u001e\u000f\u0152\u0153\n\r\u0000"+
		"\u0000\u0153\u0154\u0007\u0002\u0000\u0000\u0154\u0167\u0003<\u001e\u000e"+
		"\u0155\u0156\n\f\u0000\u0000\u0156\u0157\u0007\u0003\u0000\u0000\u0157"+
		"\u0167\u0003<\u001e\r\u0158\u0159\n\u000b\u0000\u0000\u0159\u015a\u0007"+
		"\u0004\u0000\u0000\u015a\u0167\u0003<\u001e\f\u015b\u015c\n\u0011\u0000"+
		"\u0000\u015c\u015d\u0003B!\u0000\u015d\u015e\u0003<\u001e\u0000\u015e"+
		"\u015f\u0003D\"\u0000\u015f\u0167\u0001\u0000\u0000\u0000\u0160\u0161"+
		"\n\u000f\u0000\u0000\u0161\u0162\u0005\u0012\u0000\u0000\u0162\u0163\u0003"+
		">\u001f\u0000\u0163\u0164\u0003<\u001e\u0000\u0164\u0165\u0003@ \u0000"+
		"\u0165\u0167\u0001\u0000\u0000\u0000\u0166\u0148\u0001\u0000\u0000\u0000"+
		"\u0166\u014f\u0001\u0000\u0000\u0000\u0166\u0152\u0001\u0000\u0000\u0000"+
		"\u0166\u0155\u0001\u0000\u0000\u0000\u0166\u0158\u0001\u0000\u0000\u0000"+
		"\u0166\u015b\u0001\u0000\u0000\u0000\u0166\u0160\u0001\u0000\u0000\u0000"+
		"\u0167\u016a\u0001\u0000\u0000\u0000\u0168\u0166\u0001\u0000\u0000\u0000"+
		"\u0168\u0169\u0001\u0000\u0000\u0000\u0169=\u0001\u0000\u0000\u0000\u016a"+
		"\u0168\u0001\u0000\u0000\u0000\u016b\u016c\u0005\u0013\u0000\u0000\u016c"+
		"?\u0001\u0000\u0000\u0000\u016d\u016e\u0005\u0014\u0000\u0000\u016eA\u0001"+
		"\u0000\u0000\u0000\u016f\u0170\u0005\u0015\u0000\u0000\u0170C\u0001\u0000"+
		"\u0000\u0000\u0171\u0172\u0005\u0016\u0000\u0000\u0172E\u0001\u0000\u0000"+
		"\u0000\u0173\u0174\u0005\u0017\u0000\u0000\u0174G\u0001\u0000\u0000\u0000"+
		"\u0175\u0176\u0005\u0018\u0000\u0000\u0176I\u0001\u0000\u0000\u0000\u0177"+
		"\u0178\u0005\u0019\u0000\u0000\u0178K\u0001\u0000\u0000\u0000\u0019O["+
		"gm\u0082\u008a\u0091\u0099\u009f\u00aa\u00b7\u00c0\u00c7\u00cf\u00d2\u00dd"+
		"\u00ec\u00f7\u0109\u0119\u0124\u0132\u0146\u0166\u0168";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}