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
		T__24=25, T__25=26, IF=27, ELIF=28, ELSE=29, PLUS=30, MINUS=31, MULT=32, 
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
			null, "'print'", "'='", "'string'", "'bool'", "'number'", "';'", "'for'", 
			"'in'", "'while'", "'def'", "'BSP'", "'randomNumber'", "'randomChoice'", 
			"'enum'", "'.'", "'2D'", "'3D'", "'D'", "'.add'", "'('", "')'", "'['", 
			"']'", "'{'", "'}'", "','", "'if'", "'elif'", "'else'", "'+'", "'-'", 
			"'*'", "'/'", "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", "'%'", "'and'", 
			"'or'", "'not'", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "IF", "ELIF", "ELSE", "PLUS", "MINUS", "MULT", "DIV", 
			"GT", "GTE", "LT", "LTE", "EQ", "NEQ", "MOD", "AND", "OR", "NOT", "TRUE", 
			"FALSE", "COMMENT_SINGLELINE", "NUMBER", "STRING", "ID", "WS"
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
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735221716610L) != 0) );
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
			if (_la==T__21) {
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

			setState(140);
			match(T__5);
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
			setState(142);
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
			setState(147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735221716610L) != 0)) {
				{
				{
				setState(144);
				stat();
				}
				}
				setState(149);
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
			setState(150);
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
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735221716610L) != 0)) {
				{
				{
				setState(152);
				stat();
				}
				}
				setState(157);
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
			setState(161);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735221716610L) != 0)) {
				{
				{
				setState(158);
				stat();
				}
				}
				setState(163);
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
			setState(164);
			match(T__6);
			setState(165);
			varDecl();
			setState(166);
			match(T__7);
			setState(167);
			expr(0);
			setState(168);
			openCurlBrack();
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735221716610L) != 0)) {
				{
				{
				setState(169);
				stat();
				}
				}
				setState(174);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(175);
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
			setState(177);
			match(T__8);
			setState(178);
			openParenth();
			setState(179);
			expr(0);
			setState(180);
			closedParenth();
			setState(181);
			openCurlBrack();
			setState(185);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735221716610L) != 0)) {
				{
				{
				setState(182);
				stat();
				}
				}
				setState(187);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(188);
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
			setState(190);
			match(T__9);
			setState(191);
			match(ID);
			setState(192);
			openParenth();
			setState(194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(193);
				params();
				}
			}

			setState(196);
			closedParenth();
			setState(197);
			openCurlBrack();
			setState(201);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735221716610L) != 0)) {
				{
				{
				setState(198);
				stat();
				}
				}
				setState(203);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(204);
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
		enterRule(_localctx, 30, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			match(ID);
			setState(207);
			openParenth();
			setState(209);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1046735070703616L) != 0)) {
				{
				setState(208);
				args();
				}
			}

			setState(211);
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
			setState(213);
			openCurlBrack();
			setState(214);
			expr(0);
			setState(220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__25) {
				{
				{
				setState(215);
				comma();
				setState(216);
				expr(0);
				}
				}
				setState(222);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(223);
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
			setState(225);
			match(T__10);
			setState(226);
			bspDimension();
			setState(227);
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
			setState(229);
			param();
			setState(235);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__25) {
				{
				{
				setState(230);
				comma();
				setState(231);
				param();
				}
				}
				setState(237);
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
			setState(238);
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
			setState(240);
			expr(0);
			setState(246);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__25) {
				{
				{
				setState(241);
				comma();
				setState(242);
				expr(0);
				}
				}
				setState(248);
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
			setState(249);
			match(T__11);
			setState(250);
			openParenth();
			setState(251);
			match(NUMBER);
			setState(252);
			comma();
			setState(253);
			match(NUMBER);
			setState(254);
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
			setState(256);
			match(T__12);
			setState(257);
			openParenth();
			setState(258);
			expr(0);
			setState(262); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(259);
				comma();
				setState(260);
				expr(0);
				}
				}
				setState(264); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__25 );
			setState(266);
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
			setState(268);
			match(T__13);
			setState(269);
			match(ID);
			setState(270);
			openCurlBrack();
			setState(271);
			enumBody();
			setState(272);
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
			setState(274);
			match(ID);
			setState(280);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__25) {
				{
				{
				setState(275);
				comma();
				setState(276);
				match(ID);
				}
				}
				setState(282);
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
			setState(283);
			match(ID);
			setState(284);
			match(T__14);
			setState(285);
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
			setState(291);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				enterOuterAlt(_localctx, 1);
				{
				setState(287);
				match(T__15);
				}
				break;
			case T__16:
				enterOuterAlt(_localctx, 2);
				{
				setState(288);
				match(T__16);
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 3);
				{
				setState(289);
				match(NUMBER);
				setState(290);
				match(T__17);
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
			setState(293);
			openParenth();
			setState(294);
			dimensionList();
			setState(295);
			comma();
			setState(296);
			minSize();
			setState(297);
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
			setState(299);
			match(NUMBER);
			setState(305);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(300);
					comma();
					setState(301);
					match(NUMBER);
					}
					} 
				}
				setState(307);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
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
			setState(308);
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
			setState(325);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(311);
				match(NOT);
				setState(312);
				expr(10);
				}
				break;
			case 2:
				{
				setState(313);
				openParenth();
				setState(314);
				expr(0);
				setState(315);
				closedParenth();
				}
				break;
			case 3:
				{
				setState(317);
				match(ID);
				}
				break;
			case 4:
				{
				setState(318);
				match(STRING);
				}
				break;
			case 5:
				{
				setState(319);
				match(NUMBER);
				}
				break;
			case 6:
				{
				setState(320);
				match(TRUE);
				}
				break;
			case 7:
				{
				setState(321);
				match(FALSE);
				}
				break;
			case 8:
				{
				setState(322);
				randomNumber();
				}
				break;
			case 9:
				{
				setState(323);
				randomChoice();
				}
				break;
			case 10:
				{
				setState(324);
				enumValue();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(359);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(357);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(327);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(328);
						openBrack();
						setState(329);
						expr(0);
						setState(330);
						closedBrack();
						setState(331);
						match(T__1);
						setState(332);
						expr(17);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(334);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(335);
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
						setState(336);
						expr(15);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(337);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(338);
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
						setState(339);
						expr(14);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(340);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(341);
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
						setState(342);
						expr(13);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(343);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(344);
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
						setState(345);
						expr(12);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(346);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(347);
						openBrack();
						setState(348);
						expr(0);
						setState(349);
						closedBrack();
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(351);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(352);
						match(T__18);
						setState(353);
						openParenth();
						setState(354);
						expr(0);
						setState(355);
						closedParenth();
						}
						break;
					}
					} 
				}
				setState(361);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
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
			setState(362);
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
			setState(364);
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
			setState(366);
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
			setState(368);
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
			setState(370);
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
			setState(372);
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
			setState(374);
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
		"\u0004\u00012\u0179\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"\b\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0005"+
		"\b\u0092\b\b\n\b\f\b\u0095\t\b\u0001\t\u0001\t\u0001\n\u0005\n\u009a\b"+
		"\n\n\n\f\n\u009d\t\n\u0001\u000b\u0005\u000b\u00a0\b\u000b\n\u000b\f\u000b"+
		"\u00a3\t\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0005\f"+
		"\u00ab\b\f\n\f\f\f\u00ae\t\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0005\r\u00b8\b\r\n\r\f\r\u00bb\t\r\u0001\r\u0001\r"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00c3\b\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u00c8\b\u000e\n\u000e"+
		"\f\u000e\u00cb\t\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0003\u000f\u00d2\b\u000f\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u00db\b\u0010"+
		"\n\u0010\f\u0010\u00de\t\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0005\u0012\u00ea\b\u0012\n\u0012\f\u0012\u00ed\t\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0005\u0014"+
		"\u00f5\b\u0014\n\u0014\f\u0014\u00f8\t\u0014\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0004\u0016\u0107"+
		"\b\u0016\u000b\u0016\f\u0016\u0108\u0001\u0016\u0001\u0016\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0005\u0018\u0117\b\u0018\n\u0018"+
		"\f\u0018\u011a\t\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u0124\b\u001a"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0005\u001c\u0130\b\u001c"+
		"\n\u001c\f\u001c\u0133\t\u001c\u0001\u001d\u0001\u001d\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0003\u001e\u0146\b\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0005\u001e\u0166\b\u001e\n"+
		"\u001e\f\u001e\u0169\t\u001e\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001"+
		"!\u0001!\u0001\"\u0001\"\u0001#\u0001#\u0001$\u0001$\u0001%\u0001%\u0001"+
		"%\u0000\u0001<&\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJ\u0000\u0005\u0003"+
		"\u0000\u0003\u0005,-11\u0002\u0000 !((\u0001\u0000\u001e\u001f\u0001\u0000"+
		"\"\'\u0001\u0000)*\u0182\u0000M\u0001\u0000\u0000\u0000\u0002[\u0001\u0000"+
		"\u0000\u0000\u0004]\u0001\u0000\u0000\u0000\u0006b\u0001\u0000\u0000\u0000"+
		"\bi\u0001\u0000\u0000\u0000\no\u0001\u0000\u0000\u0000\fq\u0001\u0000"+
		"\u0000\u0000\u000e\u008e\u0001\u0000\u0000\u0000\u0010\u0093\u0001\u0000"+
		"\u0000\u0000\u0012\u0096\u0001\u0000\u0000\u0000\u0014\u009b\u0001\u0000"+
		"\u0000\u0000\u0016\u00a1\u0001\u0000\u0000\u0000\u0018\u00a4\u0001\u0000"+
		"\u0000\u0000\u001a\u00b1\u0001\u0000\u0000\u0000\u001c\u00be\u0001\u0000"+
		"\u0000\u0000\u001e\u00ce\u0001\u0000\u0000\u0000 \u00d5\u0001\u0000\u0000"+
		"\u0000\"\u00e1\u0001\u0000\u0000\u0000$\u00e5\u0001\u0000\u0000\u0000"+
		"&\u00ee\u0001\u0000\u0000\u0000(\u00f0\u0001\u0000\u0000\u0000*\u00f9"+
		"\u0001\u0000\u0000\u0000,\u0100\u0001\u0000\u0000\u0000.\u010c\u0001\u0000"+
		"\u0000\u00000\u0112\u0001\u0000\u0000\u00002\u011b\u0001\u0000\u0000\u0000"+
		"4\u0123\u0001\u0000\u0000\u00006\u0125\u0001\u0000\u0000\u00008\u012b"+
		"\u0001\u0000\u0000\u0000:\u0134\u0001\u0000\u0000\u0000<\u0145\u0001\u0000"+
		"\u0000\u0000>\u016a\u0001\u0000\u0000\u0000@\u016c\u0001\u0000\u0000\u0000"+
		"B\u016e\u0001\u0000\u0000\u0000D\u0170\u0001\u0000\u0000\u0000F\u0172"+
		"\u0001\u0000\u0000\u0000H\u0174\u0001\u0000\u0000\u0000J\u0176\u0001\u0000"+
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
		"\u0000qr\u0005\u001b\u0000\u0000rs\u0003>\u001f\u0000st\u0003\u000e\u0007"+
		"\u0000tu\u0003@ \u0000uv\u0003F#\u0000vw\u0003\u0010\b\u0000w\u0082\u0003"+
		"H$\u0000xy\u0005\u001c\u0000\u0000yz\u0003>\u001f\u0000z{\u0003\u0012"+
		"\t\u0000{|\u0003@ \u0000|}\u0003F#\u0000}~\u0003\u0014\n\u0000~\u007f"+
		"\u0003D\"\u0000\u007f\u0081\u0001\u0000\u0000\u0000\u0080x\u0001\u0000"+
		"\u0000\u0000\u0081\u0084\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000"+
		"\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u008a\u0001\u0000"+
		"\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u0086\u0005\u001d"+
		"\u0000\u0000\u0086\u0087\u0003F#\u0000\u0087\u0088\u0003\u0016\u000b\u0000"+
		"\u0088\u0089\u0003H$\u0000\u0089\u008b\u0001\u0000\u0000\u0000\u008a\u0085"+
		"\u0001\u0000\u0000\u0000\u008a\u008b\u0001\u0000\u0000\u0000\u008b\u008c"+
		"\u0001\u0000\u0000\u0000\u008c\u008d\u0005\u0006\u0000\u0000\u008d\r\u0001"+
		"\u0000\u0000\u0000\u008e\u008f\u0003<\u001e\u0000\u008f\u000f\u0001\u0000"+
		"\u0000\u0000\u0090\u0092\u0003\u0002\u0001\u0000\u0091\u0090\u0001\u0000"+
		"\u0000\u0000\u0092\u0095\u0001\u0000\u0000\u0000\u0093\u0091\u0001\u0000"+
		"\u0000\u0000\u0093\u0094\u0001\u0000\u0000\u0000\u0094\u0011\u0001\u0000"+
		"\u0000\u0000\u0095\u0093\u0001\u0000\u0000\u0000\u0096\u0097\u0003<\u001e"+
		"\u0000\u0097\u0013\u0001\u0000\u0000\u0000\u0098\u009a\u0003\u0002\u0001"+
		"\u0000\u0099\u0098\u0001\u0000\u0000\u0000\u009a\u009d\u0001\u0000\u0000"+
		"\u0000\u009b\u0099\u0001\u0000\u0000\u0000\u009b\u009c\u0001\u0000\u0000"+
		"\u0000\u009c\u0015\u0001\u0000\u0000\u0000\u009d\u009b\u0001\u0000\u0000"+
		"\u0000\u009e\u00a0\u0003\u0002\u0001\u0000\u009f\u009e\u0001\u0000\u0000"+
		"\u0000\u00a0\u00a3\u0001\u0000\u0000\u0000\u00a1\u009f\u0001\u0000\u0000"+
		"\u0000\u00a1\u00a2\u0001\u0000\u0000\u0000\u00a2\u0017\u0001\u0000\u0000"+
		"\u0000\u00a3\u00a1\u0001\u0000\u0000\u0000\u00a4\u00a5\u0005\u0007\u0000"+
		"\u0000\u00a5\u00a6\u0003\u0006\u0003\u0000\u00a6\u00a7\u0005\b\u0000\u0000"+
		"\u00a7\u00a8\u0003<\u001e\u0000\u00a8\u00ac\u0003F#\u0000\u00a9\u00ab"+
		"\u0003\u0002\u0001\u0000\u00aa\u00a9\u0001\u0000\u0000\u0000\u00ab\u00ae"+
		"\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000\u00ac\u00ad"+
		"\u0001\u0000\u0000\u0000\u00ad\u00af\u0001\u0000\u0000\u0000\u00ae\u00ac"+
		"\u0001\u0000\u0000\u0000\u00af\u00b0\u0003H$\u0000\u00b0\u0019\u0001\u0000"+
		"\u0000\u0000\u00b1\u00b2\u0005\t\u0000\u0000\u00b2\u00b3\u0003>\u001f"+
		"\u0000\u00b3\u00b4\u0003<\u001e\u0000\u00b4\u00b5\u0003@ \u0000\u00b5"+
		"\u00b9\u0003F#\u0000\u00b6\u00b8\u0003\u0002\u0001\u0000\u00b7\u00b6\u0001"+
		"\u0000\u0000\u0000\u00b8\u00bb\u0001\u0000\u0000\u0000\u00b9\u00b7\u0001"+
		"\u0000\u0000\u0000\u00b9\u00ba\u0001\u0000\u0000\u0000\u00ba\u00bc\u0001"+
		"\u0000\u0000\u0000\u00bb\u00b9\u0001\u0000\u0000\u0000\u00bc\u00bd\u0003"+
		"H$\u0000\u00bd\u001b\u0001\u0000\u0000\u0000\u00be\u00bf\u0005\n\u0000"+
		"\u0000\u00bf\u00c0\u00051\u0000\u0000\u00c0\u00c2\u0003>\u001f\u0000\u00c1"+
		"\u00c3\u0003$\u0012\u0000\u00c2\u00c1\u0001\u0000\u0000\u0000\u00c2\u00c3"+
		"\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000\u0000\u0000\u00c4\u00c5"+
		"\u0003@ \u0000\u00c5\u00c9\u0003F#\u0000\u00c6\u00c8\u0003\u0002\u0001"+
		"\u0000\u00c7\u00c6\u0001\u0000\u0000\u0000\u00c8\u00cb\u0001\u0000\u0000"+
		"\u0000\u00c9\u00c7\u0001\u0000\u0000\u0000\u00c9\u00ca\u0001\u0000\u0000"+
		"\u0000\u00ca\u00cc\u0001\u0000\u0000\u0000\u00cb\u00c9\u0001\u0000\u0000"+
		"\u0000\u00cc\u00cd\u0003H$\u0000\u00cd\u001d\u0001\u0000\u0000\u0000\u00ce"+
		"\u00cf\u00051\u0000\u0000\u00cf\u00d1\u0003>\u001f\u0000\u00d0\u00d2\u0003"+
		"(\u0014\u0000\u00d1\u00d0\u0001\u0000\u0000\u0000\u00d1\u00d2\u0001\u0000"+
		"\u0000\u0000\u00d2\u00d3\u0001\u0000\u0000\u0000\u00d3\u00d4\u0003@ \u0000"+
		"\u00d4\u001f\u0001\u0000\u0000\u0000\u00d5\u00d6\u0003F#\u0000\u00d6\u00dc"+
		"\u0003<\u001e\u0000\u00d7\u00d8\u0003J%\u0000\u00d8\u00d9\u0003<\u001e"+
		"\u0000\u00d9\u00db\u0001\u0000\u0000\u0000\u00da\u00d7\u0001\u0000\u0000"+
		"\u0000\u00db\u00de\u0001\u0000\u0000\u0000\u00dc\u00da\u0001\u0000\u0000"+
		"\u0000\u00dc\u00dd\u0001\u0000\u0000\u0000\u00dd\u00df\u0001\u0000\u0000"+
		"\u0000\u00de\u00dc\u0001\u0000\u0000\u0000\u00df\u00e0\u0003H$\u0000\u00e0"+
		"!\u0001\u0000\u0000\u0000\u00e1\u00e2\u0005\u000b\u0000\u0000\u00e2\u00e3"+
		"\u00034\u001a\u0000\u00e3\u00e4\u00036\u001b\u0000\u00e4#\u0001\u0000"+
		"\u0000\u0000\u00e5\u00eb\u0003&\u0013\u0000\u00e6\u00e7\u0003J%\u0000"+
		"\u00e7\u00e8\u0003&\u0013\u0000\u00e8\u00ea\u0001\u0000\u0000\u0000\u00e9"+
		"\u00e6\u0001\u0000\u0000\u0000\u00ea\u00ed\u0001\u0000\u0000\u0000\u00eb"+
		"\u00e9\u0001\u0000\u0000\u0000\u00eb\u00ec\u0001\u0000\u0000\u0000\u00ec"+
		"%\u0001\u0000\u0000\u0000\u00ed\u00eb\u0001\u0000\u0000\u0000\u00ee\u00ef"+
		"\u00051\u0000\u0000\u00ef\'\u0001\u0000\u0000\u0000\u00f0\u00f6\u0003"+
		"<\u001e\u0000\u00f1\u00f2\u0003J%\u0000\u00f2\u00f3\u0003<\u001e\u0000"+
		"\u00f3\u00f5\u0001\u0000\u0000\u0000\u00f4\u00f1\u0001\u0000\u0000\u0000"+
		"\u00f5\u00f8\u0001\u0000\u0000\u0000\u00f6\u00f4\u0001\u0000\u0000\u0000"+
		"\u00f6\u00f7\u0001\u0000\u0000\u0000\u00f7)\u0001\u0000\u0000\u0000\u00f8"+
		"\u00f6\u0001\u0000\u0000\u0000\u00f9\u00fa\u0005\f\u0000\u0000\u00fa\u00fb"+
		"\u0003>\u001f\u0000\u00fb\u00fc\u0005/\u0000\u0000\u00fc\u00fd\u0003J"+
		"%\u0000\u00fd\u00fe\u0005/\u0000\u0000\u00fe\u00ff\u0003@ \u0000\u00ff"+
		"+\u0001\u0000\u0000\u0000\u0100\u0101\u0005\r\u0000\u0000\u0101\u0102"+
		"\u0003>\u001f\u0000\u0102\u0106\u0003<\u001e\u0000\u0103\u0104\u0003J"+
		"%\u0000\u0104\u0105\u0003<\u001e\u0000\u0105\u0107\u0001\u0000\u0000\u0000"+
		"\u0106\u0103\u0001\u0000\u0000\u0000\u0107\u0108\u0001\u0000\u0000\u0000"+
		"\u0108\u0106\u0001\u0000\u0000\u0000\u0108\u0109\u0001\u0000\u0000\u0000"+
		"\u0109\u010a\u0001\u0000\u0000\u0000\u010a\u010b\u0003@ \u0000\u010b-"+
		"\u0001\u0000\u0000\u0000\u010c\u010d\u0005\u000e\u0000\u0000\u010d\u010e"+
		"\u00051\u0000\u0000\u010e\u010f\u0003F#\u0000\u010f\u0110\u00030\u0018"+
		"\u0000\u0110\u0111\u0003H$\u0000\u0111/\u0001\u0000\u0000\u0000\u0112"+
		"\u0118\u00051\u0000\u0000\u0113\u0114\u0003J%\u0000\u0114\u0115\u0005"+
		"1\u0000\u0000\u0115\u0117\u0001\u0000\u0000\u0000\u0116\u0113\u0001\u0000"+
		"\u0000\u0000\u0117\u011a\u0001\u0000\u0000\u0000\u0118\u0116\u0001\u0000"+
		"\u0000\u0000\u0118\u0119\u0001\u0000\u0000\u0000\u01191\u0001\u0000\u0000"+
		"\u0000\u011a\u0118\u0001\u0000\u0000\u0000\u011b\u011c\u00051\u0000\u0000"+
		"\u011c\u011d\u0005\u000f\u0000\u0000\u011d\u011e\u00051\u0000\u0000\u011e"+
		"3\u0001\u0000\u0000\u0000\u011f\u0124\u0005\u0010\u0000\u0000\u0120\u0124"+
		"\u0005\u0011\u0000\u0000\u0121\u0122\u0005/\u0000\u0000\u0122\u0124\u0005"+
		"\u0012\u0000\u0000\u0123\u011f\u0001\u0000\u0000\u0000\u0123\u0120\u0001"+
		"\u0000\u0000\u0000\u0123\u0121\u0001\u0000\u0000\u0000\u01245\u0001\u0000"+
		"\u0000\u0000\u0125\u0126\u0003>\u001f\u0000\u0126\u0127\u00038\u001c\u0000"+
		"\u0127\u0128\u0003J%\u0000\u0128\u0129\u0003:\u001d\u0000\u0129\u012a"+
		"\u0003@ \u0000\u012a7\u0001\u0000\u0000\u0000\u012b\u0131\u0005/\u0000"+
		"\u0000\u012c\u012d\u0003J%\u0000\u012d\u012e\u0005/\u0000\u0000\u012e"+
		"\u0130\u0001\u0000\u0000\u0000\u012f\u012c\u0001\u0000\u0000\u0000\u0130"+
		"\u0133\u0001\u0000\u0000\u0000\u0131\u012f\u0001\u0000\u0000\u0000\u0131"+
		"\u0132\u0001\u0000\u0000\u0000\u01329\u0001\u0000\u0000\u0000\u0133\u0131"+
		"\u0001\u0000\u0000\u0000\u0134\u0135\u0005/\u0000\u0000\u0135;\u0001\u0000"+
		"\u0000\u0000\u0136\u0137\u0006\u001e\uffff\uffff\u0000\u0137\u0138\u0005"+
		"+\u0000\u0000\u0138\u0146\u0003<\u001e\n\u0139\u013a\u0003>\u001f\u0000"+
		"\u013a\u013b\u0003<\u001e\u0000\u013b\u013c\u0003@ \u0000\u013c\u0146"+
		"\u0001\u0000\u0000\u0000\u013d\u0146\u00051\u0000\u0000\u013e\u0146\u0005"+
		"0\u0000\u0000\u013f\u0146\u0005/\u0000\u0000\u0140\u0146\u0005,\u0000"+
		"\u0000\u0141\u0146\u0005-\u0000\u0000\u0142\u0146\u0003*\u0015\u0000\u0143"+
		"\u0146\u0003,\u0016\u0000\u0144\u0146\u00032\u0019\u0000\u0145\u0136\u0001"+
		"\u0000\u0000\u0000\u0145\u0139\u0001\u0000\u0000\u0000\u0145\u013d\u0001"+
		"\u0000\u0000\u0000\u0145\u013e\u0001\u0000\u0000\u0000\u0145\u013f\u0001"+
		"\u0000\u0000\u0000\u0145\u0140\u0001\u0000\u0000\u0000\u0145\u0141\u0001"+
		"\u0000\u0000\u0000\u0145\u0142\u0001\u0000\u0000\u0000\u0145\u0143\u0001"+
		"\u0000\u0000\u0000\u0145\u0144\u0001\u0000\u0000\u0000\u0146\u0167\u0001"+
		"\u0000\u0000\u0000\u0147\u0148\n\u0010\u0000\u0000\u0148\u0149\u0003B"+
		"!\u0000\u0149\u014a\u0003<\u001e\u0000\u014a\u014b\u0003D\"\u0000\u014b"+
		"\u014c\u0005\u0002\u0000\u0000\u014c\u014d\u0003<\u001e\u0011\u014d\u0166"+
		"\u0001\u0000\u0000\u0000\u014e\u014f\n\u000e\u0000\u0000\u014f\u0150\u0007"+
		"\u0001\u0000\u0000\u0150\u0166\u0003<\u001e\u000f\u0151\u0152\n\r\u0000"+
		"\u0000\u0152\u0153\u0007\u0002\u0000\u0000\u0153\u0166\u0003<\u001e\u000e"+
		"\u0154\u0155\n\f\u0000\u0000\u0155\u0156\u0007\u0003\u0000\u0000\u0156"+
		"\u0166\u0003<\u001e\r\u0157\u0158\n\u000b\u0000\u0000\u0158\u0159\u0007"+
		"\u0004\u0000\u0000\u0159\u0166\u0003<\u001e\f\u015a\u015b\n\u0011\u0000"+
		"\u0000\u015b\u015c\u0003B!\u0000\u015c\u015d\u0003<\u001e\u0000\u015d"+
		"\u015e\u0003D\"\u0000\u015e\u0166\u0001\u0000\u0000\u0000\u015f\u0160"+
		"\n\u000f\u0000\u0000\u0160\u0161\u0005\u0013\u0000\u0000\u0161\u0162\u0003"+
		">\u001f\u0000\u0162\u0163\u0003<\u001e\u0000\u0163\u0164\u0003@ \u0000"+
		"\u0164\u0166\u0001\u0000\u0000\u0000\u0165\u0147\u0001\u0000\u0000\u0000"+
		"\u0165\u014e\u0001\u0000\u0000\u0000\u0165\u0151\u0001\u0000\u0000\u0000"+
		"\u0165\u0154\u0001\u0000\u0000\u0000\u0165\u0157\u0001\u0000\u0000\u0000"+
		"\u0165\u015a\u0001\u0000\u0000\u0000\u0165\u015f\u0001\u0000\u0000\u0000"+
		"\u0166\u0169\u0001\u0000\u0000\u0000\u0167\u0165\u0001\u0000\u0000\u0000"+
		"\u0167\u0168\u0001\u0000\u0000\u0000\u0168=\u0001\u0000\u0000\u0000\u0169"+
		"\u0167\u0001\u0000\u0000\u0000\u016a\u016b\u0005\u0014\u0000\u0000\u016b"+
		"?\u0001\u0000\u0000\u0000\u016c\u016d\u0005\u0015\u0000\u0000\u016dA\u0001"+
		"\u0000\u0000\u0000\u016e\u016f\u0005\u0016\u0000\u0000\u016fC\u0001\u0000"+
		"\u0000\u0000\u0170\u0171\u0005\u0017\u0000\u0000\u0171E\u0001\u0000\u0000"+
		"\u0000\u0172\u0173\u0005\u0018\u0000\u0000\u0173G\u0001\u0000\u0000\u0000"+
		"\u0174\u0175\u0005\u0019\u0000\u0000\u0175I\u0001\u0000\u0000\u0000\u0176"+
		"\u0177\u0005\u001a\u0000\u0000\u0177K\u0001\u0000\u0000\u0000\u0018O["+
		"gm\u0082\u008a\u0093\u009b\u00a1\u00ac\u00b9\u00c2\u00c9\u00d1\u00dc\u00eb"+
		"\u00f6\u0108\u0118\u0123\u0131\u0145\u0165\u0167";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}