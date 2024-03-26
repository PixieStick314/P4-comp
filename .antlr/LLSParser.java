// Generated from c:/Users/nedim/Documents/GitHub/P4-comp/LLS.g4 by ANTLR 4.13.1
package src.antlr;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class LLSParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, AND=28, OR=29, NOT=30, XOR=31, GREATER_THAN=32, 
		LESS_THAN=33, EQUAL=34, NOT_EQUAL=35, GREATER_THAN_OR_EQUAL=36, LESS_THAN_OR_EQUAL=37, 
		OP_ADD=38, OP_SUB=39, OP_MUL=40, OP_DIV=41, OP_MOD=42, OP_INC=43, OP_DEC=44, 
		ADD_ASSIGN=45, SUB_ASSIGN=46, MUL_ASSIGN=47, DIV_ASSIGN=48, MOD_ASSIGN=49, 
		PRIMITIVE_TYPES=50, BOOL=51, LIST_TYPES=52, STRINGVALUE=53, IDENTIFIER=54, 
		INT=55, NUMBER=56, DIGIT=57, LETTER=58, SL_COMMENT=59, ML_COMMENT=60, 
		WS=61;
	public static final int
		RULE_prog = 0, RULE_node = 1, RULE_memeberBlocks = 2, RULE_stmt = 3, RULE_ifStmt = 4, 
		RULE_ifelsecodeblock = 5, RULE_returnstmt = 6, RULE_foreachStmt = 7, RULE_whileStmt = 8, 
		RULE_matchStmt = 9, RULE_casesStmt = 10, RULE_defaultStmt = 11, RULE_dcl = 12, 
		RULE_functionDcl = 13, RULE_parameter = 14, RULE_varDcl = 15, RULE_functionCall = 16, 
		RULE_assignment = 17, RULE_boolExpr = 18, RULE_boolExprFactor = 19, RULE_singleBoolExpr = 20, 
		RULE_comparisonExpr = 21, RULE_comparisonFactor = 22, RULE_arithmetic = 23, 
		RULE_arithAssignment = 24, RULE_arithExpr = 25, RULE_compound = 26, RULE_logical = 27, 
		RULE_comparison = 28, RULE_listReference = 29, RULE_classReference = 30, 
		RULE_classDcl = 31, RULE_classMemberDcl = 32, RULE_classType = 33, RULE_type = 34, 
		RULE_listType = 35, RULE_value = 36, RULE_valueList = 37;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "node", "memeberBlocks", "stmt", "ifStmt", "ifelsecodeblock", 
			"returnstmt", "foreachStmt", "whileStmt", "matchStmt", "casesStmt", "defaultStmt", 
			"dcl", "functionDcl", "parameter", "varDcl", "functionCall", "assignment", 
			"boolExpr", "boolExprFactor", "singleBoolExpr", "comparisonExpr", "comparisonFactor", 
			"arithmetic", "arithAssignment", "arithExpr", "compound", "logical", 
			"comparison", "listReference", "classReference", "classDcl", "classMemberDcl", 
			"classType", "type", "listType", "value", "valueList"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'if'", "'('", "')'", "'{'", "'}'", "'else'", "'return'", 
			"'foreach'", "'in'", "'while'", "'match'", "'when'", "','", "'do'", "':'", 
			"'otherwise '", "'function'", "'returns'", "'let'", "'be'", "'='", "'['", 
			"']'", "'.'", "'class'", "'is'", null, null, null, null, "'>'", "'<'", 
			"'=='", "'!='", "'>='", "'<='", "'+'", "'-'", "'*'", "'/'", "'%'", "'++'", 
			"'--'", "'+='", "'-='", "'*='", "'/='", "'%='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "AND", "OR", "NOT", "XOR", "GREATER_THAN", "LESS_THAN", 
			"EQUAL", "NOT_EQUAL", "GREATER_THAN_OR_EQUAL", "LESS_THAN_OR_EQUAL", 
			"OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", "OP_MOD", "OP_INC", "OP_DEC", 
			"ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
			"PRIMITIVE_TYPES", "BOOL", "LIST_TYPES", "STRINGVALUE", "IDENTIFIER", 
			"INT", "NUMBER", "DIGIT", "LETTER", "SL_COMMENT", "ML_COMMENT", "WS"
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
	public String getGrammarFileName() { return "LLS.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LLSParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(LLSParser.EOF, 0); }
		public List<NodeContext> node() {
			return getRuleContexts(NodeContext.class);
		}
		public NodeContext node(int i) {
			return getRuleContext(NodeContext.class,i);
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
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137386726746495756L) != 0)) {
				{
				{
				setState(76);
				node();
				}
				}
				setState(81);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(82);
			match(EOF);
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
	public static class NodeContext extends ParserRuleContext {
		public NodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_node; }
	 
		public NodeContext() { }
		public void copyFrom(NodeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NodeStatementContext extends NodeContext {
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public NodeStatementContext(NodeContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NodeDeclorationContext extends NodeContext {
		public DclContext dcl() {
			return getRuleContext(DclContext.class,0);
		}
		public NodeDeclorationContext(NodeContext ctx) { copyFrom(ctx); }
	}

	public final NodeContext node() throws RecognitionException {
		NodeContext _localctx = new NodeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_node);
		try {
			setState(86);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case T__2:
			case T__7:
			case T__8:
			case T__10:
			case T__11:
			case T__22:
			case OP_SUB:
			case OP_INC:
			case OP_DEC:
			case BOOL:
			case STRINGVALUE:
			case IDENTIFIER:
			case INT:
			case NUMBER:
				_localctx = new NodeStatementContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				stmt();
				}
				break;
			case T__17:
			case T__19:
			case T__25:
				_localctx = new NodeDeclorationContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				dcl();
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
	public static class MemeberBlocksContext extends ParserRuleContext {
		public MemeberBlocksContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_memeberBlocks; }
	 
		public MemeberBlocksContext() { }
		public void copyFrom(MemeberBlocksContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DeclorationContext extends MemeberBlocksContext {
		public VarDclContext varDcl() {
			return getRuleContext(VarDclContext.class,0);
		}
		public DeclorationContext(MemeberBlocksContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends MemeberBlocksContext {
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public StatementContext(MemeberBlocksContext ctx) { copyFrom(ctx); }
	}

	public final MemeberBlocksContext memeberBlocks() throws RecognitionException {
		MemeberBlocksContext _localctx = new MemeberBlocksContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_memeberBlocks);
		try {
			setState(90);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case T__2:
			case T__7:
			case T__8:
			case T__10:
			case T__11:
			case T__22:
			case OP_SUB:
			case OP_INC:
			case OP_DEC:
			case BOOL:
			case STRINGVALUE:
			case IDENTIFIER:
			case INT:
			case NUMBER:
				_localctx = new StatementContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(88);
				stmt();
				}
				break;
			case T__19:
				_localctx = new DeclorationContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(89);
				varDcl();
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
	public static class StmtContext extends ParserRuleContext {
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	 
		public StmtContext() { }
		public void copyFrom(StmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ValueStmtContext extends StmtContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ValueStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GotoReturnStmtContext extends StmtContext {
		public ReturnstmtContext returnstmt() {
			return getRuleContext(ReturnstmtContext.class,0);
		}
		public GotoReturnStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GotoforeachStmtContext extends StmtContext {
		public ForeachStmtContext foreachStmt() {
			return getRuleContext(ForeachStmtContext.class,0);
		}
		public GotoforeachStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallStmtContext extends StmtContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public FunctionCallStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ArithExprStmtContext extends StmtContext {
		public ArithExprContext arithExpr() {
			return getRuleContext(ArithExprContext.class,0);
		}
		public ArithExprStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BoolExprStmtContext extends StmtContext {
		public BoolExprContext boolExpr() {
			return getRuleContext(BoolExprContext.class,0);
		}
		public BoolExprStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ListReferenceStmtContext extends StmtContext {
		public ListReferenceContext listReference() {
			return getRuleContext(ListReferenceContext.class,0);
		}
		public ListReferenceStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ClassReferenceStmtContext extends StmtContext {
		public ClassReferenceContext classReference() {
			return getRuleContext(ClassReferenceContext.class,0);
		}
		public ClassReferenceStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GotoifStmtContext extends StmtContext {
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public GotoifStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GotoWhileStmtContext extends StmtContext {
		public WhileStmtContext whileStmt() {
			return getRuleContext(WhileStmtContext.class,0);
		}
		public GotoWhileStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GotomatchStmtContext extends StmtContext {
		public MatchStmtContext matchStmt() {
			return getRuleContext(MatchStmtContext.class,0);
		}
		public GotomatchStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ArithAssignmentStmtContext extends StmtContext {
		public ArithAssignmentContext arithAssignment() {
			return getRuleContext(ArithAssignmentContext.class,0);
		}
		public ArithAssignmentStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentStmtContext extends StmtContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public AssignmentStmtContext(StmtContext ctx) { copyFrom(ctx); }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_stmt);
		try {
			setState(123);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				_localctx = new GotoifStmtContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(92);
				ifStmt();
				}
				break;
			case 2:
				_localctx = new ArithAssignmentStmtContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(93);
				arithAssignment();
				setState(94);
				match(T__0);
				}
				break;
			case 3:
				_localctx = new ArithExprStmtContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(96);
				arithExpr(0);
				setState(97);
				match(T__0);
				}
				break;
			case 4:
				_localctx = new GotoforeachStmtContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(99);
				foreachStmt();
				}
				break;
			case 5:
				_localctx = new GotoWhileStmtContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(100);
				whileStmt();
				}
				break;
			case 6:
				_localctx = new BoolExprStmtContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(101);
				boolExpr();
				setState(102);
				match(T__0);
				}
				break;
			case 7:
				_localctx = new FunctionCallStmtContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(104);
				functionCall();
				setState(105);
				match(T__0);
				}
				break;
			case 8:
				_localctx = new AssignmentStmtContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(107);
				assignment();
				setState(108);
				match(T__0);
				}
				break;
			case 9:
				_localctx = new GotomatchStmtContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(110);
				matchStmt();
				}
				break;
			case 10:
				_localctx = new ValueStmtContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(111);
				value();
				setState(112);
				match(T__0);
				}
				break;
			case 11:
				_localctx = new ClassReferenceStmtContext(_localctx);
				enterOuterAlt(_localctx, 11);
				{
				setState(114);
				classReference();
				setState(115);
				match(T__0);
				}
				break;
			case 12:
				_localctx = new ListReferenceStmtContext(_localctx);
				enterOuterAlt(_localctx, 12);
				{
				setState(117);
				listReference();
				setState(118);
				match(T__0);
				}
				break;
			case 13:
				_localctx = new GotoReturnStmtContext(_localctx);
				enterOuterAlt(_localctx, 13);
				{
				setState(120);
				returnstmt();
				setState(121);
				match(T__0);
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
	public static class IfStmtContext extends ParserRuleContext {
		public BoolExprContext ifbool;
		public MemeberBlocksContext memeberBlocks;
		public List<MemeberBlocksContext> ifcode = new ArrayList<MemeberBlocksContext>();
		public BoolExprContext boolExpr;
		public List<BoolExprContext> ifelsebool = new ArrayList<BoolExprContext>();
		public IfelsecodeblockContext ifelsecodeblock;
		public List<IfelsecodeblockContext> ifelseCode = new ArrayList<IfelsecodeblockContext>();
		public List<MemeberBlocksContext> elsecode = new ArrayList<MemeberBlocksContext>();
		public List<BoolExprContext> boolExpr() {
			return getRuleContexts(BoolExprContext.class);
		}
		public BoolExprContext boolExpr(int i) {
			return getRuleContext(BoolExprContext.class,i);
		}
		public List<MemeberBlocksContext> memeberBlocks() {
			return getRuleContexts(MemeberBlocksContext.class);
		}
		public MemeberBlocksContext memeberBlocks(int i) {
			return getRuleContext(MemeberBlocksContext.class,i);
		}
		public List<IfelsecodeblockContext> ifelsecodeblock() {
			return getRuleContexts(IfelsecodeblockContext.class);
		}
		public IfelsecodeblockContext ifelsecodeblock(int i) {
			return getRuleContext(IfelsecodeblockContext.class,i);
		}
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_ifStmt);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			match(T__1);
			setState(126);
			match(T__2);
			setState(127);
			((IfStmtContext)_localctx).ifbool = boolExpr();
			setState(128);
			match(T__3);
			setState(129);
			match(T__4);
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137386726679124748L) != 0)) {
				{
				{
				setState(130);
				((IfStmtContext)_localctx).memeberBlocks = memeberBlocks();
				((IfStmtContext)_localctx).ifcode.add(((IfStmtContext)_localctx).memeberBlocks);
				}
				}
				setState(135);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(136);
			match(T__5);
			setState(148);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(137);
					match(T__6);
					setState(138);
					match(T__1);
					setState(139);
					match(T__2);
					setState(140);
					((IfStmtContext)_localctx).boolExpr = boolExpr();
					((IfStmtContext)_localctx).ifelsebool.add(((IfStmtContext)_localctx).boolExpr);
					setState(141);
					match(T__3);
					setState(142);
					match(T__4);
					setState(143);
					((IfStmtContext)_localctx).ifelsecodeblock = ifelsecodeblock();
					((IfStmtContext)_localctx).ifelseCode.add(((IfStmtContext)_localctx).ifelsecodeblock);
					setState(144);
					match(T__5);
					}
					} 
				}
				setState(150);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			setState(160);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(151);
				match(T__6);
				setState(152);
				match(T__4);
				setState(156);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137386726679124748L) != 0)) {
					{
					{
					setState(153);
					((IfStmtContext)_localctx).memeberBlocks = memeberBlocks();
					((IfStmtContext)_localctx).elsecode.add(((IfStmtContext)_localctx).memeberBlocks);
					}
					}
					setState(158);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(159);
				match(T__5);
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
	public static class IfelsecodeblockContext extends ParserRuleContext {
		public List<MemeberBlocksContext> memeberBlocks() {
			return getRuleContexts(MemeberBlocksContext.class);
		}
		public MemeberBlocksContext memeberBlocks(int i) {
			return getRuleContext(MemeberBlocksContext.class,i);
		}
		public IfelsecodeblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifelsecodeblock; }
	}

	public final IfelsecodeblockContext ifelsecodeblock() throws RecognitionException {
		IfelsecodeblockContext _localctx = new IfelsecodeblockContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_ifelsecodeblock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137386726679124748L) != 0)) {
				{
				{
				setState(162);
				memeberBlocks();
				}
				}
				setState(167);
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
	public static class ReturnstmtContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ArithExprContext arithExpr() {
			return getRuleContext(ArithExprContext.class,0);
		}
		public BoolExprContext boolExpr() {
			return getRuleContext(BoolExprContext.class,0);
		}
		public ReturnstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnstmt; }
	}

	public final ReturnstmtContext returnstmt() throws RecognitionException {
		ReturnstmtContext _localctx = new ReturnstmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_returnstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			match(T__7);
			setState(172);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(169);
				value();
				}
				break;
			case 2:
				{
				setState(170);
				arithExpr(0);
				}
				break;
			case 3:
				{
				setState(171);
				boolExpr();
				}
				break;
			}
			setState(174);
			match(T__0);
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
	public static class ForeachStmtContext extends ParserRuleContext {
		public Token item;
		public Token list;
		public List<TerminalNode> IDENTIFIER() { return getTokens(LLSParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(LLSParser.IDENTIFIER, i);
		}
		public List<MemeberBlocksContext> memeberBlocks() {
			return getRuleContexts(MemeberBlocksContext.class);
		}
		public MemeberBlocksContext memeberBlocks(int i) {
			return getRuleContext(MemeberBlocksContext.class,i);
		}
		public ForeachStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_foreachStmt; }
	}

	public final ForeachStmtContext foreachStmt() throws RecognitionException {
		ForeachStmtContext _localctx = new ForeachStmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_foreachStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(T__8);
			setState(177);
			match(T__2);
			setState(178);
			((ForeachStmtContext)_localctx).item = match(IDENTIFIER);
			setState(179);
			match(T__9);
			setState(180);
			((ForeachStmtContext)_localctx).list = match(IDENTIFIER);
			setState(181);
			match(T__3);
			setState(182);
			match(T__4);
			setState(186);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137386726679124748L) != 0)) {
				{
				{
				setState(183);
				memeberBlocks();
				}
				}
				setState(188);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(189);
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
	public static class WhileStmtContext extends ParserRuleContext {
		public BoolExprContext boolExpr() {
			return getRuleContext(BoolExprContext.class,0);
		}
		public List<MemeberBlocksContext> memeberBlocks() {
			return getRuleContexts(MemeberBlocksContext.class);
		}
		public MemeberBlocksContext memeberBlocks(int i) {
			return getRuleContext(MemeberBlocksContext.class,i);
		}
		public WhileStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStmt; }
	}

	public final WhileStmtContext whileStmt() throws RecognitionException {
		WhileStmtContext _localctx = new WhileStmtContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_whileStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			match(T__10);
			setState(192);
			match(T__2);
			setState(193);
			boolExpr();
			setState(194);
			match(T__3);
			setState(195);
			match(T__4);
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137386726679124748L) != 0)) {
				{
				{
				setState(196);
				memeberBlocks();
				}
				}
				setState(201);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(202);
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
	public static class MatchStmtContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public List<CasesStmtContext> casesStmt() {
			return getRuleContexts(CasesStmtContext.class);
		}
		public CasesStmtContext casesStmt(int i) {
			return getRuleContext(CasesStmtContext.class,i);
		}
		public DefaultStmtContext defaultStmt() {
			return getRuleContext(DefaultStmtContext.class,0);
		}
		public MatchStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_matchStmt; }
	}

	public final MatchStmtContext matchStmt() throws RecognitionException {
		MatchStmtContext _localctx = new MatchStmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_matchStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			match(T__11);
			setState(205);
			value();
			setState(206);
			match(T__4);
			setState(210);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__12) {
				{
				{
				setState(207);
				casesStmt();
				}
				}
				setState(212);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(214);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__16) {
				{
				setState(213);
				defaultStmt();
				}
			}

			setState(216);
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
	public static class CasesStmtContext extends ParserRuleContext {
		public ValueContext value;
		public List<ValueContext> opt = new ArrayList<ValueContext>();
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List<MemeberBlocksContext> memeberBlocks() {
			return getRuleContexts(MemeberBlocksContext.class);
		}
		public MemeberBlocksContext memeberBlocks(int i) {
			return getRuleContext(MemeberBlocksContext.class,i);
		}
		public CasesStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_casesStmt; }
	}

	public final CasesStmtContext casesStmt() throws RecognitionException {
		CasesStmtContext _localctx = new CasesStmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_casesStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			match(T__12);
			{
			setState(219);
			((CasesStmtContext)_localctx).value = value();
			((CasesStmtContext)_localctx).opt.add(((CasesStmtContext)_localctx).value);
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__13) {
				{
				{
				setState(220);
				match(T__13);
				setState(221);
				((CasesStmtContext)_localctx).value = value();
				((CasesStmtContext)_localctx).opt.add(((CasesStmtContext)_localctx).value);
				}
				}
				setState(226);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(227);
			match(T__14);
			setState(228);
			match(T__15);
			setState(232);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137386726679124748L) != 0)) {
				{
				{
				setState(229);
				memeberBlocks();
				}
				}
				setState(234);
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
	public static class DefaultStmtContext extends ParserRuleContext {
		public List<MemeberBlocksContext> memeberBlocks() {
			return getRuleContexts(MemeberBlocksContext.class);
		}
		public MemeberBlocksContext memeberBlocks(int i) {
			return getRuleContext(MemeberBlocksContext.class,i);
		}
		public DefaultStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defaultStmt; }
	}

	public final DefaultStmtContext defaultStmt() throws RecognitionException {
		DefaultStmtContext _localctx = new DefaultStmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_defaultStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			match(T__16);
			setState(236);
			match(T__14);
			setState(237);
			match(T__15);
			setState(241);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137386726679124748L) != 0)) {
				{
				{
				setState(238);
				memeberBlocks();
				}
				}
				setState(243);
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
	public static class DclContext extends ParserRuleContext {
		public DclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dcl; }
	 
		public DclContext() { }
		public void copyFrom(DclContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VariableDeclorationContext extends DclContext {
		public VarDclContext varDcl() {
			return getRuleContext(VarDclContext.class,0);
		}
		public VariableDeclorationContext(DclContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ClassDeclorationContext extends DclContext {
		public ClassDclContext classDcl() {
			return getRuleContext(ClassDclContext.class,0);
		}
		public ClassDeclorationContext(DclContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDeclorationContext extends DclContext {
		public FunctionDclContext functionDcl() {
			return getRuleContext(FunctionDclContext.class,0);
		}
		public FunctionDeclorationContext(DclContext ctx) { copyFrom(ctx); }
	}

	public final DclContext dcl() throws RecognitionException {
		DclContext _localctx = new DclContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_dcl);
		try {
			setState(247);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__19:
				_localctx = new VariableDeclorationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(244);
				varDcl();
				}
				break;
			case T__25:
				_localctx = new ClassDeclorationContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(245);
				classDcl();
				}
				break;
			case T__17:
				_localctx = new FunctionDeclorationContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(246);
				functionDcl();
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
	public static class FunctionDclContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(LLSParser.IDENTIFIER, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public List<MemeberBlocksContext> memeberBlocks() {
			return getRuleContexts(MemeberBlocksContext.class);
		}
		public MemeberBlocksContext memeberBlocks(int i) {
			return getRuleContext(MemeberBlocksContext.class,i);
		}
		public FunctionDclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDcl; }
	}

	public final FunctionDclContext functionDcl() throws RecognitionException {
		FunctionDclContext _localctx = new FunctionDclContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_functionDcl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			match(T__17);
			setState(250);
			match(IDENTIFIER);
			setState(251);
			match(T__2);
			setState(260);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 23643898043695104L) != 0)) {
				{
				setState(252);
				parameter();
				setState(257);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__13) {
					{
					{
					setState(253);
					match(T__13);
					setState(254);
					parameter();
					}
					}
					setState(259);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(262);
			match(T__3);
			setState(263);
			match(T__18);
			setState(264);
			type();
			setState(265);
			match(T__4);
			setState(269);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137386726679124748L) != 0)) {
				{
				{
				setState(266);
				memeberBlocks();
				}
				}
				setState(271);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(272);
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
	public static class ParameterContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(LLSParser.IDENTIFIER, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ListTypeContext listType() {
			return getRuleContext(ListTypeContext.class,0);
		}
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRIMITIVE_TYPES:
			case IDENTIFIER:
				{
				setState(274);
				type();
				}
				break;
			case LIST_TYPES:
				{
				setState(275);
				listType();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(278);
			match(IDENTIFIER);
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
	public static class VarDclContext extends ParserRuleContext {
		public VarDclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDcl; }
	 
		public VarDclContext() { }
		public void copyFrom(VarDclContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SingleVarDclContext extends VarDclContext {
		public TerminalNode IDENTIFIER() { return getToken(LLSParser.IDENTIFIER, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ArithExprContext arithExpr() {
			return getRuleContext(ArithExprContext.class,0);
		}
		public BoolExprContext boolExpr() {
			return getRuleContext(BoolExprContext.class,0);
		}
		public SingleVarDclContext(VarDclContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ValueListDclContext extends VarDclContext {
		public TerminalNode IDENTIFIER() { return getToken(LLSParser.IDENTIFIER, 0); }
		public TerminalNode LIST_TYPES() { return getToken(LLSParser.LIST_TYPES, 0); }
		public ValueListContext valueList() {
			return getRuleContext(ValueListContext.class,0);
		}
		public ValueListDclContext(VarDclContext ctx) { copyFrom(ctx); }
	}

	public final VarDclContext varDcl() throws RecognitionException {
		VarDclContext _localctx = new VarDclContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_varDcl);
		try {
			setState(298);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				_localctx = new SingleVarDclContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(280);
				match(T__19);
				setState(281);
				match(IDENTIFIER);
				setState(282);
				match(T__20);
				{
				setState(283);
				type();
				setState(287);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
				case 1:
					{
					setState(284);
					value();
					}
					break;
				case 2:
					{
					setState(285);
					arithExpr(0);
					}
					break;
				case 3:
					{
					setState(286);
					boolExpr();
					}
					break;
				}
				}
				setState(289);
				match(T__0);
				}
				break;
			case 2:
				_localctx = new ValueListDclContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(291);
				match(T__19);
				setState(292);
				match(IDENTIFIER);
				setState(293);
				match(T__20);
				setState(294);
				match(LIST_TYPES);
				setState(295);
				valueList();
				setState(296);
				match(T__0);
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
	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(LLSParser.IDENTIFIER, 0); }
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
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
			setState(300);
			match(IDENTIFIER);
			setState(301);
			match(T__2);
			setState(310);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137359788643188736L) != 0)) {
				{
				setState(302);
				value();
				setState(307);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__13) {
					{
					{
					setState(303);
					match(T__13);
					setState(304);
					value();
					}
					}
					setState(309);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(312);
			match(T__3);
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
		public Token equal;
		public Token be;
		public TerminalNode IDENTIFIER() { return getToken(LLSParser.IDENTIFIER, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ArithExprContext arithExpr() {
			return getRuleContext(ArithExprContext.class,0);
		}
		public BoolExprContext boolExpr() {
			return getRuleContext(BoolExprContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			match(IDENTIFIER);
			setState(317);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__21:
				{
				setState(315);
				((AssignmentContext)_localctx).equal = match(T__21);
				}
				break;
			case T__20:
				{
				setState(316);
				((AssignmentContext)_localctx).be = match(T__20);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(322);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				setState(319);
				value();
				}
				break;
			case 2:
				{
				setState(320);
				arithExpr(0);
				}
				break;
			case 3:
				{
				setState(321);
				boolExpr();
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
	public static class BoolExprContext extends ParserRuleContext {
		public BoolExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boolExpr; }
	 
		public BoolExprContext() { }
		public void copyFrom(BoolExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MultiBoolExprBoolContext extends BoolExprContext {
		public BoolExprFactorContext left;
		public BoolExprFactorContext boolExprFactor;
		public List<BoolExprFactorContext> right = new ArrayList<BoolExprFactorContext>();
		public List<BoolExprFactorContext> boolExprFactor() {
			return getRuleContexts(BoolExprFactorContext.class);
		}
		public BoolExprFactorContext boolExprFactor(int i) {
			return getRuleContext(BoolExprFactorContext.class,i);
		}
		public List<LogicalContext> logical() {
			return getRuleContexts(LogicalContext.class);
		}
		public LogicalContext logical(int i) {
			return getRuleContext(LogicalContext.class,i);
		}
		public MultiBoolExprBoolContext(BoolExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SingleBoolExprBoolContext extends BoolExprContext {
		public SingleBoolExprContext singleBoolExpr() {
			return getRuleContext(SingleBoolExprContext.class,0);
		}
		public SingleBoolExprBoolContext(BoolExprContext ctx) { copyFrom(ctx); }
	}

	public final BoolExprContext boolExpr() throws RecognitionException {
		BoolExprContext _localctx = new BoolExprContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_boolExpr);
		int _la;
		try {
			setState(333);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				_localctx = new SingleBoolExprBoolContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(324);
				singleBoolExpr();
				}
				break;
			case 2:
				_localctx = new MultiBoolExprBoolContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(325);
				((MultiBoolExprBoolContext)_localctx).left = boolExprFactor();
				setState(329); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(326);
					logical();
					setState(327);
					((MultiBoolExprBoolContext)_localctx).boolExprFactor = boolExprFactor();
					((MultiBoolExprBoolContext)_localctx).right.add(((MultiBoolExprBoolContext)_localctx).boolExprFactor);
					}
					}
					setState(331); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 4026531840L) != 0) );
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
	public static class BoolExprFactorContext extends ParserRuleContext {
		public BoolExprFactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boolExprFactor; }
	 
		public BoolExprFactorContext() { }
		public void copyFrom(BoolExprFactorContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BoolExprFactorBoolContext extends BoolExprFactorContext {
		public ComparisonExprContext comparisonExpr() {
			return getRuleContext(ComparisonExprContext.class,0);
		}
		public BoolExprFactorBoolContext(BoolExprFactorContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonFactorBoolExprContext extends BoolExprFactorContext {
		public ComparisonFactorContext comparisonFactor() {
			return getRuleContext(ComparisonFactorContext.class,0);
		}
		public ComparisonFactorBoolExprContext(BoolExprFactorContext ctx) { copyFrom(ctx); }
	}

	public final BoolExprFactorContext boolExprFactor() throws RecognitionException {
		BoolExprFactorContext _localctx = new BoolExprFactorContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_boolExprFactor);
		try {
			setState(337);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				_localctx = new ComparisonFactorBoolExprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(335);
				comparisonFactor();
				}
				break;
			case 2:
				_localctx = new BoolExprFactorBoolContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(336);
				comparisonExpr();
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
	public static class SingleBoolExprContext extends ParserRuleContext {
		public SingleBoolExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleBoolExpr; }
	 
		public SingleBoolExprContext() { }
		public void copyFrom(SingleBoolExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonExprSingleBoolContext extends SingleBoolExprContext {
		public ComparisonExprContext comparisonExpr() {
			return getRuleContext(ComparisonExprContext.class,0);
		}
		public ComparisonExprSingleBoolContext(SingleBoolExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonFactorsingleBoolExprContext extends SingleBoolExprContext {
		public ComparisonFactorContext comparisonFactor() {
			return getRuleContext(ComparisonFactorContext.class,0);
		}
		public ComparisonFactorsingleBoolExprContext(SingleBoolExprContext ctx) { copyFrom(ctx); }
	}

	public final SingleBoolExprContext singleBoolExpr() throws RecognitionException {
		SingleBoolExprContext _localctx = new SingleBoolExprContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_singleBoolExpr);
		try {
			setState(341);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				_localctx = new ComparisonExprSingleBoolContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(339);
				comparisonExpr();
				}
				break;
			case 2:
				_localctx = new ComparisonFactorsingleBoolExprContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(340);
				comparisonFactor();
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
	public static class ComparisonExprContext extends ParserRuleContext {
		public ComparisonFactorContext left;
		public ComparisonFactorContext right;
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public List<ComparisonFactorContext> comparisonFactor() {
			return getRuleContexts(ComparisonFactorContext.class);
		}
		public ComparisonFactorContext comparisonFactor(int i) {
			return getRuleContext(ComparisonFactorContext.class,i);
		}
		public ComparisonExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparisonExpr; }
	}

	public final ComparisonExprContext comparisonExpr() throws RecognitionException {
		ComparisonExprContext _localctx = new ComparisonExprContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_comparisonExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(343);
			((ComparisonExprContext)_localctx).left = comparisonFactor();
			setState(344);
			comparison();
			setState(345);
			((ComparisonExprContext)_localctx).right = comparisonFactor();
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
	public static class ComparisonFactorContext extends ParserRuleContext {
		public ComparisonFactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparisonFactor; }
	 
		public ComparisonFactorContext() { }
		public void copyFrom(ComparisonFactorContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BoolComparisonFactorContext extends ComparisonFactorContext {
		public TerminalNode BOOL() { return getToken(LLSParser.BOOL, 0); }
		public BoolComparisonFactorContext(ComparisonFactorContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SingleValueComparisonFactorContext extends ComparisonFactorContext {
		public TerminalNode IDENTIFIER() { return getToken(LLSParser.IDENTIFIER, 0); }
		public SingleValueComparisonFactorContext(ComparisonFactorContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParBoolExprComparisonFactorContext extends ComparisonFactorContext {
		public BoolExprContext boolExpr() {
			return getRuleContext(BoolExprContext.class,0);
		}
		public ParBoolExprComparisonFactorContext(ComparisonFactorContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumberComparisonFactorContext extends ComparisonFactorContext {
		public TerminalNode NUMBER() { return getToken(LLSParser.NUMBER, 0); }
		public NumberComparisonFactorContext(ComparisonFactorContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntComparisonFactorContext extends ComparisonFactorContext {
		public TerminalNode INT() { return getToken(LLSParser.INT, 0); }
		public IntComparisonFactorContext(ComparisonFactorContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallComparisonFactorContext extends ComparisonFactorContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public FunctionCallComparisonFactorContext(ComparisonFactorContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringComparisonFactorContext extends ComparisonFactorContext {
		public TerminalNode STRINGVALUE() { return getToken(LLSParser.STRINGVALUE, 0); }
		public StringComparisonFactorContext(ComparisonFactorContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ListReferenceComparisonFactorContext extends ComparisonFactorContext {
		public ListReferenceContext listReference() {
			return getRuleContext(ListReferenceContext.class,0);
		}
		public ListReferenceComparisonFactorContext(ComparisonFactorContext ctx) { copyFrom(ctx); }
	}

	public final ComparisonFactorContext comparisonFactor() throws RecognitionException {
		ComparisonFactorContext _localctx = new ComparisonFactorContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_comparisonFactor);
		try {
			setState(358);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				_localctx = new SingleValueComparisonFactorContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(347);
				match(IDENTIFIER);
				}
				break;
			case 2:
				_localctx = new ParBoolExprComparisonFactorContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(348);
				match(T__2);
				setState(349);
				boolExpr();
				setState(350);
				match(T__3);
				}
				break;
			case 3:
				_localctx = new ListReferenceComparisonFactorContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(352);
				listReference();
				}
				break;
			case 4:
				_localctx = new BoolComparisonFactorContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(353);
				match(BOOL);
				}
				break;
			case 5:
				_localctx = new IntComparisonFactorContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(354);
				match(INT);
				}
				break;
			case 6:
				_localctx = new NumberComparisonFactorContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(355);
				match(NUMBER);
				}
				break;
			case 7:
				_localctx = new StringComparisonFactorContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(356);
				match(STRINGVALUE);
				}
				break;
			case 8:
				_localctx = new FunctionCallComparisonFactorContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(357);
				functionCall();
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
	public static class ArithmeticContext extends ParserRuleContext {
		public Token op;
		public TerminalNode OP_ADD() { return getToken(LLSParser.OP_ADD, 0); }
		public TerminalNode OP_SUB() { return getToken(LLSParser.OP_SUB, 0); }
		public TerminalNode OP_MUL() { return getToken(LLSParser.OP_MUL, 0); }
		public TerminalNode OP_DIV() { return getToken(LLSParser.OP_DIV, 0); }
		public TerminalNode OP_MOD() { return getToken(LLSParser.OP_MOD, 0); }
		public ArithmeticContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmetic; }
	}

	public final ArithmeticContext arithmetic() throws RecognitionException {
		ArithmeticContext _localctx = new ArithmeticContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_arithmetic);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(360);
			((ArithmeticContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 8521215115264L) != 0)) ) {
				((ArithmeticContext)_localctx).op = (Token)_errHandler.recoverInline(this);
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
	public static class ArithAssignmentContext extends ParserRuleContext {
		public Token equal;
		public TerminalNode IDENTIFIER() { return getToken(LLSParser.IDENTIFIER, 0); }
		public ArithExprContext arithExpr() {
			return getRuleContext(ArithExprContext.class,0);
		}
		public CompoundContext compound() {
			return getRuleContext(CompoundContext.class,0);
		}
		public ArithAssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithAssignment; }
	}

	public final ArithAssignmentContext arithAssignment() throws RecognitionException {
		ArithAssignmentContext _localctx = new ArithAssignmentContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_arithAssignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(362);
			match(IDENTIFIER);
			setState(365);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__21:
				{
				setState(363);
				((ArithAssignmentContext)_localctx).equal = match(T__21);
				}
				break;
			case ADD_ASSIGN:
			case SUB_ASSIGN:
			case MUL_ASSIGN:
			case DIV_ASSIGN:
			case MOD_ASSIGN:
				{
				setState(364);
				compound();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(367);
			arithExpr(0);
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
	public static class ArithExprContext extends ParserRuleContext {
		public ArithExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithExpr; }
	 
		public ArithExprContext() { }
		public void copyFrom(ArithExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ValueExprContext extends ArithExprContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ValueExprContext(ArithExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnaryExprContext extends ArithExprContext {
		public Token op;
		public ValueContext right;
		public ValueContext left;
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public TerminalNode OP_INC() { return getToken(LLSParser.OP_INC, 0); }
		public TerminalNode OP_DEC() { return getToken(LLSParser.OP_DEC, 0); }
		public UnaryExprContext(ArithExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NegatinExprContext extends ArithExprContext {
		public Token op;
		public ArithExprContext arithExpr() {
			return getRuleContext(ArithExprContext.class,0);
		}
		public TerminalNode OP_SUB() { return getToken(LLSParser.OP_SUB, 0); }
		public NegatinExprContext(ArithExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParArithExprContext extends ArithExprContext {
		public ArithExprContext arithExpr() {
			return getRuleContext(ArithExprContext.class,0);
		}
		public ParArithExprContext(ArithExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddExprContext extends ArithExprContext {
		public ArithExprContext left;
		public Token op;
		public ArithExprContext right;
		public List<ArithExprContext> arithExpr() {
			return getRuleContexts(ArithExprContext.class);
		}
		public ArithExprContext arithExpr(int i) {
			return getRuleContext(ArithExprContext.class,i);
		}
		public TerminalNode OP_ADD() { return getToken(LLSParser.OP_ADD, 0); }
		public TerminalNode OP_SUB() { return getToken(LLSParser.OP_SUB, 0); }
		public AddExprContext(ArithExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MultiExprContext extends ArithExprContext {
		public ArithExprContext left;
		public Token op;
		public ArithExprContext right;
		public List<ArithExprContext> arithExpr() {
			return getRuleContexts(ArithExprContext.class);
		}
		public ArithExprContext arithExpr(int i) {
			return getRuleContext(ArithExprContext.class,i);
		}
		public TerminalNode OP_MUL() { return getToken(LLSParser.OP_MUL, 0); }
		public TerminalNode OP_DIV() { return getToken(LLSParser.OP_DIV, 0); }
		public TerminalNode OP_MOD() { return getToken(LLSParser.OP_MOD, 0); }
		public MultiExprContext(ArithExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallExprContext extends ArithExprContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public FunctionCallExprContext(ArithExprContext ctx) { copyFrom(ctx); }
	}

	public final ArithExprContext arithExpr() throws RecognitionException {
		return arithExpr(0);
	}

	private ArithExprContext arithExpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ArithExprContext _localctx = new ArithExprContext(_ctx, _parentState);
		ArithExprContext _prevctx = _localctx;
		int _startState = 50;
		enterRecursionRule(_localctx, 50, RULE_arithExpr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(385);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				{
				_localctx = new NegatinExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(370);
				((NegatinExprContext)_localctx).op = match(OP_SUB);
				setState(371);
				arithExpr(7);
				}
				break;
			case 2:
				{
				_localctx = new ValueExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(372);
				value();
				}
				break;
			case 3:
				{
				_localctx = new FunctionCallExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(373);
				functionCall();
				}
				break;
			case 4:
				{
				_localctx = new ParArithExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(374);
				match(T__2);
				setState(375);
				arithExpr(0);
				setState(376);
				match(T__3);
				}
				break;
			case 5:
				{
				_localctx = new UnaryExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(383);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case OP_INC:
				case OP_DEC:
					{
					setState(378);
					((UnaryExprContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==OP_INC || _la==OP_DEC) ) {
						((UnaryExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(379);
					((UnaryExprContext)_localctx).right = value();
					}
					break;
				case T__22:
				case BOOL:
				case STRINGVALUE:
				case IDENTIFIER:
				case INT:
				case NUMBER:
					{
					setState(380);
					((UnaryExprContext)_localctx).left = value();
					setState(381);
					((UnaryExprContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==OP_INC || _la==OP_DEC) ) {
						((UnaryExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(395);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(393);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
					case 1:
						{
						_localctx = new MultiExprContext(new ArithExprContext(_parentctx, _parentState));
						((MultiExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_arithExpr);
						setState(387);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(388);
						((MultiExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7696581394432L) != 0)) ) {
							((MultiExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(389);
						((MultiExprContext)_localctx).right = arithExpr(7);
						}
						break;
					case 2:
						{
						_localctx = new AddExprContext(new ArithExprContext(_parentctx, _parentState));
						((AddExprContext)_localctx).left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_arithExpr);
						setState(390);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(391);
						((AddExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==OP_ADD || _la==OP_SUB) ) {
							((AddExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(392);
						((AddExprContext)_localctx).right = arithExpr(6);
						}
						break;
					}
					} 
				}
				setState(397);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
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
	public static class CompoundContext extends ParserRuleContext {
		public CompoundContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compound; }
	 
		public CompoundContext() { }
		public void copyFrom(CompoundContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CompoundModContext extends CompoundContext {
		public TerminalNode MOD_ASSIGN() { return getToken(LLSParser.MOD_ASSIGN, 0); }
		public CompoundModContext(CompoundContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CompoundAddContext extends CompoundContext {
		public TerminalNode ADD_ASSIGN() { return getToken(LLSParser.ADD_ASSIGN, 0); }
		public CompoundAddContext(CompoundContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CompoundDivContext extends CompoundContext {
		public TerminalNode DIV_ASSIGN() { return getToken(LLSParser.DIV_ASSIGN, 0); }
		public CompoundDivContext(CompoundContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CompoundSubContext extends CompoundContext {
		public TerminalNode SUB_ASSIGN() { return getToken(LLSParser.SUB_ASSIGN, 0); }
		public CompoundSubContext(CompoundContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CompoundMulContext extends CompoundContext {
		public TerminalNode MUL_ASSIGN() { return getToken(LLSParser.MUL_ASSIGN, 0); }
		public CompoundMulContext(CompoundContext ctx) { copyFrom(ctx); }
	}

	public final CompoundContext compound() throws RecognitionException {
		CompoundContext _localctx = new CompoundContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_compound);
		try {
			setState(403);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD_ASSIGN:
				_localctx = new CompoundAddContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(398);
				match(ADD_ASSIGN);
				}
				break;
			case SUB_ASSIGN:
				_localctx = new CompoundSubContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(399);
				match(SUB_ASSIGN);
				}
				break;
			case MUL_ASSIGN:
				_localctx = new CompoundMulContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(400);
				match(MUL_ASSIGN);
				}
				break;
			case DIV_ASSIGN:
				_localctx = new CompoundDivContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(401);
				match(DIV_ASSIGN);
				}
				break;
			case MOD_ASSIGN:
				_localctx = new CompoundModContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(402);
				match(MOD_ASSIGN);
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
	public static class LogicalContext extends ParserRuleContext {
		public LogicalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical; }
	 
		public LogicalContext() { }
		public void copyFrom(LogicalContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LogicalNotContext extends LogicalContext {
		public TerminalNode NOT() { return getToken(LLSParser.NOT, 0); }
		public LogicalNotContext(LogicalContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LogicalAndContext extends LogicalContext {
		public TerminalNode AND() { return getToken(LLSParser.AND, 0); }
		public LogicalAndContext(LogicalContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LogicalXOrContext extends LogicalContext {
		public TerminalNode XOR() { return getToken(LLSParser.XOR, 0); }
		public LogicalXOrContext(LogicalContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LogicalOrContext extends LogicalContext {
		public TerminalNode OR() { return getToken(LLSParser.OR, 0); }
		public LogicalOrContext(LogicalContext ctx) { copyFrom(ctx); }
	}

	public final LogicalContext logical() throws RecognitionException {
		LogicalContext _localctx = new LogicalContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_logical);
		try {
			setState(409);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AND:
				_localctx = new LogicalAndContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(405);
				match(AND);
				}
				break;
			case OR:
				_localctx = new LogicalOrContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(406);
				match(OR);
				}
				break;
			case NOT:
				_localctx = new LogicalNotContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(407);
				match(NOT);
				}
				break;
			case XOR:
				_localctx = new LogicalXOrContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(408);
				match(XOR);
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
	public static class ComparisonContext extends ParserRuleContext {
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	 
		public ComparisonContext() { }
		public void copyFrom(ComparisonContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonGreaterOrEqualContext extends ComparisonContext {
		public TerminalNode GREATER_THAN_OR_EQUAL() { return getToken(LLSParser.GREATER_THAN_OR_EQUAL, 0); }
		public ComparisonGreaterOrEqualContext(ComparisonContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonNotEqualContext extends ComparisonContext {
		public TerminalNode NOT_EQUAL() { return getToken(LLSParser.NOT_EQUAL, 0); }
		public ComparisonNotEqualContext(ComparisonContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonLessContext extends ComparisonContext {
		public TerminalNode LESS_THAN() { return getToken(LLSParser.LESS_THAN, 0); }
		public ComparisonLessContext(ComparisonContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonLessOrEqualContext extends ComparisonContext {
		public TerminalNode LESS_THAN_OR_EQUAL() { return getToken(LLSParser.LESS_THAN_OR_EQUAL, 0); }
		public ComparisonLessOrEqualContext(ComparisonContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonEqualContext extends ComparisonContext {
		public TerminalNode EQUAL() { return getToken(LLSParser.EQUAL, 0); }
		public ComparisonEqualContext(ComparisonContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonGreaterContext extends ComparisonContext {
		public TerminalNode GREATER_THAN() { return getToken(LLSParser.GREATER_THAN, 0); }
		public ComparisonGreaterContext(ComparisonContext ctx) { copyFrom(ctx); }
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_comparison);
		try {
			setState(417);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GREATER_THAN:
				_localctx = new ComparisonGreaterContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(411);
				match(GREATER_THAN);
				}
				break;
			case LESS_THAN:
				_localctx = new ComparisonLessContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(412);
				match(LESS_THAN);
				}
				break;
			case EQUAL:
				_localctx = new ComparisonEqualContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(413);
				match(EQUAL);
				}
				break;
			case NOT_EQUAL:
				_localctx = new ComparisonNotEqualContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(414);
				match(NOT_EQUAL);
				}
				break;
			case GREATER_THAN_OR_EQUAL:
				_localctx = new ComparisonGreaterOrEqualContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(415);
				match(GREATER_THAN_OR_EQUAL);
				}
				break;
			case LESS_THAN_OR_EQUAL:
				_localctx = new ComparisonLessOrEqualContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(416);
				match(LESS_THAN_OR_EQUAL);
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
	public static class ListReferenceContext extends ParserRuleContext {
		public Token ID;
		public Token HolderID;
		public Token HolderInt;
		public ArithExprContext HolderExpr;
		public List<TerminalNode> IDENTIFIER() { return getTokens(LLSParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(LLSParser.IDENTIFIER, i);
		}
		public TerminalNode INT() { return getToken(LLSParser.INT, 0); }
		public ArithExprContext arithExpr() {
			return getRuleContext(ArithExprContext.class,0);
		}
		public ListReferenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listReference; }
	}

	public final ListReferenceContext listReference() throws RecognitionException {
		ListReferenceContext _localctx = new ListReferenceContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_listReference);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(419);
			((ListReferenceContext)_localctx).ID = match(IDENTIFIER);
			setState(420);
			match(T__22);
			setState(424);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,41,_ctx) ) {
			case 1:
				{
				setState(421);
				((ListReferenceContext)_localctx).HolderID = match(IDENTIFIER);
				}
				break;
			case 2:
				{
				setState(422);
				((ListReferenceContext)_localctx).HolderInt = match(INT);
				}
				break;
			case 3:
				{
				setState(423);
				((ListReferenceContext)_localctx).HolderExpr = arithExpr(0);
				}
				break;
			}
			setState(426);
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
	public static class ClassReferenceContext extends ParserRuleContext {
		public Token classref;
		public Token attribute;
		public ParameterContext parameter;
		public List<ParameterContext> par = new ArrayList<ParameterContext>();
		public List<TerminalNode> IDENTIFIER() { return getTokens(LLSParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(LLSParser.IDENTIFIER, i);
		}
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public ClassReferenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classReference; }
	}

	public final ClassReferenceContext classReference() throws RecognitionException {
		ClassReferenceContext _localctx = new ClassReferenceContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_classReference);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(428);
			((ClassReferenceContext)_localctx).classref = match(IDENTIFIER);
			setState(429);
			match(T__24);
			setState(430);
			((ClassReferenceContext)_localctx).attribute = match(IDENTIFIER);
			setState(439);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(431);
				match(T__2);
				setState(435);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 23643898043695104L) != 0)) {
					{
					{
					setState(432);
					((ClassReferenceContext)_localctx).parameter = parameter();
					((ClassReferenceContext)_localctx).par.add(((ClassReferenceContext)_localctx).parameter);
					}
					}
					setState(437);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(438);
				match(T__3);
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
	public static class ClassDclContext extends ParserRuleContext {
		public Token classname;
		public Token works;
		public List<TerminalNode> IDENTIFIER() { return getTokens(LLSParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(LLSParser.IDENTIFIER, i);
		}
		public List<ClassMemberDclContext> classMemberDcl() {
			return getRuleContexts(ClassMemberDclContext.class);
		}
		public ClassMemberDclContext classMemberDcl(int i) {
			return getRuleContext(ClassMemberDclContext.class,i);
		}
		public ClassDclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDcl; }
	}

	public final ClassDclContext classDcl() throws RecognitionException {
		ClassDclContext _localctx = new ClassDclContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_classDcl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(441);
			match(T__25);
			setState(442);
			((ClassDclContext)_localctx).classname = match(IDENTIFIER);
			setState(445);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__26) {
				{
				setState(443);
				match(T__26);
				setState(444);
				((ClassDclContext)_localctx).works = match(IDENTIFIER);
				}
			}

			setState(447);
			match(T__4);
			setState(451);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__17 || _la==T__19) {
				{
				{
				setState(448);
				classMemberDcl();
				}
				}
				setState(453);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(454);
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
	public static class ClassMemberDclContext extends ParserRuleContext {
		public ClassMemberDclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classMemberDcl; }
	 
		public ClassMemberDclContext() { }
		public void copyFrom(ClassMemberDclContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ClassVarDclContext extends ClassMemberDclContext {
		public VarDclContext varDcl() {
			return getRuleContext(VarDclContext.class,0);
		}
		public ClassVarDclContext(ClassMemberDclContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ClassfuntionDclContext extends ClassMemberDclContext {
		public FunctionDclContext functionDcl() {
			return getRuleContext(FunctionDclContext.class,0);
		}
		public ClassfuntionDclContext(ClassMemberDclContext ctx) { copyFrom(ctx); }
	}

	public final ClassMemberDclContext classMemberDcl() throws RecognitionException {
		ClassMemberDclContext _localctx = new ClassMemberDclContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_classMemberDcl);
		try {
			setState(458);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__19:
				_localctx = new ClassVarDclContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(456);
				varDcl();
				}
				break;
			case T__17:
				_localctx = new ClassfuntionDclContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(457);
				functionDcl();
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
	public static class ClassTypeContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(LLSParser.IDENTIFIER, 0); }
		public ClassTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classType; }
	}

	public final ClassTypeContext classType() throws RecognitionException {
		ClassTypeContext _localctx = new ClassTypeContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_classType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(460);
			match(IDENTIFIER);
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
	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	 
		public TypeContext() { }
		public void copyFrom(TypeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TypesPrimContext extends TypeContext {
		public TerminalNode PRIMITIVE_TYPES() { return getToken(LLSParser.PRIMITIVE_TYPES, 0); }
		public TypesPrimContext(TypeContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TypesClassTypesContext extends TypeContext {
		public ClassTypeContext classType() {
			return getRuleContext(ClassTypeContext.class,0);
		}
		public TypesClassTypesContext(TypeContext ctx) { copyFrom(ctx); }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_type);
		try {
			setState(464);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRIMITIVE_TYPES:
				_localctx = new TypesPrimContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(462);
				match(PRIMITIVE_TYPES);
				}
				break;
			case IDENTIFIER:
				_localctx = new TypesClassTypesContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(463);
				classType();
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
	public static class ListTypeContext extends ParserRuleContext {
		public ListTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listType; }
	 
		public ListTypeContext() { }
		public void copyFrom(ListTypeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TypesListContext extends ListTypeContext {
		public TerminalNode LIST_TYPES() { return getToken(LLSParser.LIST_TYPES, 0); }
		public TypesListContext(ListTypeContext ctx) { copyFrom(ctx); }
	}

	public final ListTypeContext listType() throws RecognitionException {
		ListTypeContext _localctx = new ListTypeContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_listType);
		try {
			_localctx = new TypesListContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(466);
			match(LIST_TYPES);
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
	public static class ValueContext extends ParserRuleContext {
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	 
		public ValueContext() { }
		public void copyFrom(ValueContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ValueIntContext extends ValueContext {
		public TerminalNode INT() { return getToken(LLSParser.INT, 0); }
		public ValueIntContext(ValueContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ListOfValueContext extends ValueContext {
		public ValueListContext valueList() {
			return getRuleContext(ValueListContext.class,0);
		}
		public ListOfValueContext(ValueContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ValueNumContext extends ValueContext {
		public TerminalNode NUMBER() { return getToken(LLSParser.NUMBER, 0); }
		public ValueNumContext(ValueContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ValueIDContext extends ValueContext {
		public TerminalNode IDENTIFIER() { return getToken(LLSParser.IDENTIFIER, 0); }
		public ValueIDContext(ValueContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ValueListRefContext extends ValueContext {
		public ListReferenceContext listReference() {
			return getRuleContext(ListReferenceContext.class,0);
		}
		public ValueListRefContext(ValueContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ValueStringContext extends ValueContext {
		public TerminalNode STRINGVALUE() { return getToken(LLSParser.STRINGVALUE, 0); }
		public ValueStringContext(ValueContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ValueBoolContext extends ValueContext {
		public TerminalNode BOOL() { return getToken(LLSParser.BOOL, 0); }
		public ValueBoolContext(ValueContext ctx) { copyFrom(ctx); }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_value);
		try {
			setState(475);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,48,_ctx) ) {
			case 1:
				_localctx = new ValueIntContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(468);
				match(INT);
				}
				break;
			case 2:
				_localctx = new ValueNumContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(469);
				match(NUMBER);
				}
				break;
			case 3:
				_localctx = new ValueStringContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(470);
				match(STRINGVALUE);
				}
				break;
			case 4:
				_localctx = new ValueBoolContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(471);
				match(BOOL);
				}
				break;
			case 5:
				_localctx = new ValueListRefContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(472);
				listReference();
				}
				break;
			case 6:
				_localctx = new ListOfValueContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(473);
				valueList();
				}
				break;
			case 7:
				_localctx = new ValueIDContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(474);
				match(IDENTIFIER);
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
	public static class ValueListContext extends ParserRuleContext {
		public ValueContext value;
		public List<ValueContext> following = new ArrayList<ValueContext>();
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public ValueListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valueList; }
	}

	public final ValueListContext valueList() throws RecognitionException {
		ValueListContext _localctx = new ValueListContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_valueList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(477);
			match(T__22);
			setState(486);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137359788643188736L) != 0)) {
				{
				setState(478);
				((ValueListContext)_localctx).value = value();
				((ValueListContext)_localctx).following.add(((ValueListContext)_localctx).value);
				setState(483);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__13) {
					{
					{
					setState(479);
					match(T__13);
					setState(480);
					((ValueListContext)_localctx).value = value();
					((ValueListContext)_localctx).following.add(((ValueListContext)_localctx).value);
					}
					}
					setState(485);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(488);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 25:
			return arithExpr_sempred((ArithExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean arithExpr_sempred(ArithExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001=\u01eb\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0001\u0000\u0005\u0000N\b\u0000"+
		"\n\u0000\f\u0000Q\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0003\u0001W\b\u0001\u0001\u0002\u0001\u0002\u0003\u0002[\b\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0003\u0003|\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0005\u0004\u0084\b\u0004\n\u0004\f\u0004"+
		"\u0087\t\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004"+
		"\u0093\b\u0004\n\u0004\f\u0004\u0096\t\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0005\u0004\u009b\b\u0004\n\u0004\f\u0004\u009e\t\u0004\u0001\u0004"+
		"\u0003\u0004\u00a1\b\u0004\u0001\u0005\u0005\u0005\u00a4\b\u0005\n\u0005"+
		"\f\u0005\u00a7\t\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006\u00ad\b\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0005\u0007\u00b9\b\u0007\n\u0007\f\u0007\u00bc\t\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0005\b\u00c6\b"+
		"\b\n\b\f\b\u00c9\t\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0005"+
		"\t\u00d1\b\t\n\t\f\t\u00d4\t\t\u0001\t\u0003\t\u00d7\b\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\n\u0001\n\u0005\n\u00df\b\n\n\n\f\n\u00e2\t\n"+
		"\u0001\n\u0001\n\u0001\n\u0005\n\u00e7\b\n\n\n\f\n\u00ea\t\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u00f0\b\u000b\n\u000b"+
		"\f\u000b\u00f3\t\u000b\u0001\f\u0001\f\u0001\f\u0003\f\u00f8\b\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r\u0100\b\r\n\r\f\r\u0103"+
		"\t\r\u0003\r\u0105\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r"+
		"\u010c\b\r\n\r\f\r\u010f\t\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0003"+
		"\u000e\u0115\b\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u0120"+
		"\b\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u012b\b\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u0132"+
		"\b\u0010\n\u0010\f\u0010\u0135\t\u0010\u0003\u0010\u0137\b\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u013e"+
		"\b\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u0143\b\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0004\u0012"+
		"\u014a\b\u0012\u000b\u0012\f\u0012\u014b\u0003\u0012\u014e\b\u0012\u0001"+
		"\u0013\u0001\u0013\u0003\u0013\u0152\b\u0013\u0001\u0014\u0001\u0014\u0003"+
		"\u0014\u0156\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0003\u0016\u0167"+
		"\b\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0003"+
		"\u0018\u016e\b\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0003"+
		"\u0019\u0180\b\u0019\u0003\u0019\u0182\b\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0005\u0019\u018a\b\u0019"+
		"\n\u0019\f\u0019\u018d\t\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0003\u001a\u0194\b\u001a\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0003\u001b\u019a\b\u001b\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0003\u001c\u01a2\b\u001c\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u01a9"+
		"\b\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0005\u001e\u01b2\b\u001e\n\u001e\f\u001e\u01b5\t\u001e"+
		"\u0001\u001e\u0003\u001e\u01b8\b\u001e\u0001\u001f\u0001\u001f\u0001\u001f"+
		"\u0001\u001f\u0003\u001f\u01be\b\u001f\u0001\u001f\u0001\u001f\u0005\u001f"+
		"\u01c2\b\u001f\n\u001f\f\u001f\u01c5\t\u001f\u0001\u001f\u0001\u001f\u0001"+
		" \u0001 \u0003 \u01cb\b \u0001!\u0001!\u0001\"\u0001\"\u0003\"\u01d1\b"+
		"\"\u0001#\u0001#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0003"+
		"$\u01dc\b$\u0001%\u0001%\u0001%\u0001%\u0005%\u01e2\b%\n%\f%\u01e5\t%"+
		"\u0003%\u01e7\b%\u0001%\u0001%\u0001%\u0000\u00012&\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$&(*,.02468:<>@BDFHJ\u0000\u0004\u0001\u0000&*\u0001\u0000+,\u0001\u0000"+
		"(*\u0001\u0000&\'\u021f\u0000O\u0001\u0000\u0000\u0000\u0002V\u0001\u0000"+
		"\u0000\u0000\u0004Z\u0001\u0000\u0000\u0000\u0006{\u0001\u0000\u0000\u0000"+
		"\b}\u0001\u0000\u0000\u0000\n\u00a5\u0001\u0000\u0000\u0000\f\u00a8\u0001"+
		"\u0000\u0000\u0000\u000e\u00b0\u0001\u0000\u0000\u0000\u0010\u00bf\u0001"+
		"\u0000\u0000\u0000\u0012\u00cc\u0001\u0000\u0000\u0000\u0014\u00da\u0001"+
		"\u0000\u0000\u0000\u0016\u00eb\u0001\u0000\u0000\u0000\u0018\u00f7\u0001"+
		"\u0000\u0000\u0000\u001a\u00f9\u0001\u0000\u0000\u0000\u001c\u0114\u0001"+
		"\u0000\u0000\u0000\u001e\u012a\u0001\u0000\u0000\u0000 \u012c\u0001\u0000"+
		"\u0000\u0000\"\u013a\u0001\u0000\u0000\u0000$\u014d\u0001\u0000\u0000"+
		"\u0000&\u0151\u0001\u0000\u0000\u0000(\u0155\u0001\u0000\u0000\u0000*"+
		"\u0157\u0001\u0000\u0000\u0000,\u0166\u0001\u0000\u0000\u0000.\u0168\u0001"+
		"\u0000\u0000\u00000\u016a\u0001\u0000\u0000\u00002\u0181\u0001\u0000\u0000"+
		"\u00004\u0193\u0001\u0000\u0000\u00006\u0199\u0001\u0000\u0000\u00008"+
		"\u01a1\u0001\u0000\u0000\u0000:\u01a3\u0001\u0000\u0000\u0000<\u01ac\u0001"+
		"\u0000\u0000\u0000>\u01b9\u0001\u0000\u0000\u0000@\u01ca\u0001\u0000\u0000"+
		"\u0000B\u01cc\u0001\u0000\u0000\u0000D\u01d0\u0001\u0000\u0000\u0000F"+
		"\u01d2\u0001\u0000\u0000\u0000H\u01db\u0001\u0000\u0000\u0000J\u01dd\u0001"+
		"\u0000\u0000\u0000LN\u0003\u0002\u0001\u0000ML\u0001\u0000\u0000\u0000"+
		"NQ\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000"+
		"\u0000PR\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000RS\u0005\u0000"+
		"\u0000\u0001S\u0001\u0001\u0000\u0000\u0000TW\u0003\u0006\u0003\u0000"+
		"UW\u0003\u0018\f\u0000VT\u0001\u0000\u0000\u0000VU\u0001\u0000\u0000\u0000"+
		"W\u0003\u0001\u0000\u0000\u0000X[\u0003\u0006\u0003\u0000Y[\u0003\u001e"+
		"\u000f\u0000ZX\u0001\u0000\u0000\u0000ZY\u0001\u0000\u0000\u0000[\u0005"+
		"\u0001\u0000\u0000\u0000\\|\u0003\b\u0004\u0000]^\u00030\u0018\u0000^"+
		"_\u0005\u0001\u0000\u0000_|\u0001\u0000\u0000\u0000`a\u00032\u0019\u0000"+
		"ab\u0005\u0001\u0000\u0000b|\u0001\u0000\u0000\u0000c|\u0003\u000e\u0007"+
		"\u0000d|\u0003\u0010\b\u0000ef\u0003$\u0012\u0000fg\u0005\u0001\u0000"+
		"\u0000g|\u0001\u0000\u0000\u0000hi\u0003 \u0010\u0000ij\u0005\u0001\u0000"+
		"\u0000j|\u0001\u0000\u0000\u0000kl\u0003\"\u0011\u0000lm\u0005\u0001\u0000"+
		"\u0000m|\u0001\u0000\u0000\u0000n|\u0003\u0012\t\u0000op\u0003H$\u0000"+
		"pq\u0005\u0001\u0000\u0000q|\u0001\u0000\u0000\u0000rs\u0003<\u001e\u0000"+
		"st\u0005\u0001\u0000\u0000t|\u0001\u0000\u0000\u0000uv\u0003:\u001d\u0000"+
		"vw\u0005\u0001\u0000\u0000w|\u0001\u0000\u0000\u0000xy\u0003\f\u0006\u0000"+
		"yz\u0005\u0001\u0000\u0000z|\u0001\u0000\u0000\u0000{\\\u0001\u0000\u0000"+
		"\u0000{]\u0001\u0000\u0000\u0000{`\u0001\u0000\u0000\u0000{c\u0001\u0000"+
		"\u0000\u0000{d\u0001\u0000\u0000\u0000{e\u0001\u0000\u0000\u0000{h\u0001"+
		"\u0000\u0000\u0000{k\u0001\u0000\u0000\u0000{n\u0001\u0000\u0000\u0000"+
		"{o\u0001\u0000\u0000\u0000{r\u0001\u0000\u0000\u0000{u\u0001\u0000\u0000"+
		"\u0000{x\u0001\u0000\u0000\u0000|\u0007\u0001\u0000\u0000\u0000}~\u0005"+
		"\u0002\u0000\u0000~\u007f\u0005\u0003\u0000\u0000\u007f\u0080\u0003$\u0012"+
		"\u0000\u0080\u0081\u0005\u0004\u0000\u0000\u0081\u0085\u0005\u0005\u0000"+
		"\u0000\u0082\u0084\u0003\u0004\u0002\u0000\u0083\u0082\u0001\u0000\u0000"+
		"\u0000\u0084\u0087\u0001\u0000\u0000\u0000\u0085\u0083\u0001\u0000\u0000"+
		"\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u0088\u0001\u0000\u0000"+
		"\u0000\u0087\u0085\u0001\u0000\u0000\u0000\u0088\u0094\u0005\u0006\u0000"+
		"\u0000\u0089\u008a\u0005\u0007\u0000\u0000\u008a\u008b\u0005\u0002\u0000"+
		"\u0000\u008b\u008c\u0005\u0003\u0000\u0000\u008c\u008d\u0003$\u0012\u0000"+
		"\u008d\u008e\u0005\u0004\u0000\u0000\u008e\u008f\u0005\u0005\u0000\u0000"+
		"\u008f\u0090\u0003\n\u0005\u0000\u0090\u0091\u0005\u0006\u0000\u0000\u0091"+
		"\u0093\u0001\u0000\u0000\u0000\u0092\u0089\u0001\u0000\u0000\u0000\u0093"+
		"\u0096\u0001\u0000\u0000\u0000\u0094\u0092\u0001\u0000\u0000\u0000\u0094"+
		"\u0095\u0001\u0000\u0000\u0000\u0095\u00a0\u0001\u0000\u0000\u0000\u0096"+
		"\u0094\u0001\u0000\u0000\u0000\u0097\u0098\u0005\u0007\u0000\u0000\u0098"+
		"\u009c\u0005\u0005\u0000\u0000\u0099\u009b\u0003\u0004\u0002\u0000\u009a"+
		"\u0099\u0001\u0000\u0000\u0000\u009b\u009e\u0001\u0000\u0000\u0000\u009c"+
		"\u009a\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009d"+
		"\u009f\u0001\u0000\u0000\u0000\u009e\u009c\u0001\u0000\u0000\u0000\u009f"+
		"\u00a1\u0005\u0006\u0000\u0000\u00a0\u0097\u0001\u0000\u0000\u0000\u00a0"+
		"\u00a1\u0001\u0000\u0000\u0000\u00a1\t\u0001\u0000\u0000\u0000\u00a2\u00a4"+
		"\u0003\u0004\u0002\u0000\u00a3\u00a2\u0001\u0000\u0000\u0000\u00a4\u00a7"+
		"\u0001\u0000\u0000\u0000\u00a5\u00a3\u0001\u0000\u0000\u0000\u00a5\u00a6"+
		"\u0001\u0000\u0000\u0000\u00a6\u000b\u0001\u0000\u0000\u0000\u00a7\u00a5"+
		"\u0001\u0000\u0000\u0000\u00a8\u00ac\u0005\b\u0000\u0000\u00a9\u00ad\u0003"+
		"H$\u0000\u00aa\u00ad\u00032\u0019\u0000\u00ab\u00ad\u0003$\u0012\u0000"+
		"\u00ac\u00a9\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000"+
		"\u00ac\u00ab\u0001\u0000\u0000\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000"+
		"\u00ae\u00af\u0005\u0001\u0000\u0000\u00af\r\u0001\u0000\u0000\u0000\u00b0"+
		"\u00b1\u0005\t\u0000\u0000\u00b1\u00b2\u0005\u0003\u0000\u0000\u00b2\u00b3"+
		"\u00056\u0000\u0000\u00b3\u00b4\u0005\n\u0000\u0000\u00b4\u00b5\u0005"+
		"6\u0000\u0000\u00b5\u00b6\u0005\u0004\u0000\u0000\u00b6\u00ba\u0005\u0005"+
		"\u0000\u0000\u00b7\u00b9\u0003\u0004\u0002\u0000\u00b8\u00b7\u0001\u0000"+
		"\u0000\u0000\u00b9\u00bc\u0001\u0000\u0000\u0000\u00ba\u00b8\u0001\u0000"+
		"\u0000\u0000\u00ba\u00bb\u0001\u0000\u0000\u0000\u00bb\u00bd\u0001\u0000"+
		"\u0000\u0000\u00bc\u00ba\u0001\u0000\u0000\u0000\u00bd\u00be\u0005\u0006"+
		"\u0000\u0000\u00be\u000f\u0001\u0000\u0000\u0000\u00bf\u00c0\u0005\u000b"+
		"\u0000\u0000\u00c0\u00c1\u0005\u0003\u0000\u0000\u00c1\u00c2\u0003$\u0012"+
		"\u0000\u00c2\u00c3\u0005\u0004\u0000\u0000\u00c3\u00c7\u0005\u0005\u0000"+
		"\u0000\u00c4\u00c6\u0003\u0004\u0002\u0000\u00c5\u00c4\u0001\u0000\u0000"+
		"\u0000\u00c6\u00c9\u0001\u0000\u0000\u0000\u00c7\u00c5\u0001\u0000\u0000"+
		"\u0000\u00c7\u00c8\u0001\u0000\u0000\u0000\u00c8\u00ca\u0001\u0000\u0000"+
		"\u0000\u00c9\u00c7\u0001\u0000\u0000\u0000\u00ca\u00cb\u0005\u0006\u0000"+
		"\u0000\u00cb\u0011\u0001\u0000\u0000\u0000\u00cc\u00cd\u0005\f\u0000\u0000"+
		"\u00cd\u00ce\u0003H$\u0000\u00ce\u00d2\u0005\u0005\u0000\u0000\u00cf\u00d1"+
		"\u0003\u0014\n\u0000\u00d0\u00cf\u0001\u0000\u0000\u0000\u00d1\u00d4\u0001"+
		"\u0000\u0000\u0000\u00d2\u00d0\u0001\u0000\u0000\u0000\u00d2\u00d3\u0001"+
		"\u0000\u0000\u0000\u00d3\u00d6\u0001\u0000\u0000\u0000\u00d4\u00d2\u0001"+
		"\u0000\u0000\u0000\u00d5\u00d7\u0003\u0016\u000b\u0000\u00d6\u00d5\u0001"+
		"\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7\u00d8\u0001"+
		"\u0000\u0000\u0000\u00d8\u00d9\u0005\u0006\u0000\u0000\u00d9\u0013\u0001"+
		"\u0000\u0000\u0000\u00da\u00db\u0005\r\u0000\u0000\u00db\u00e0\u0003H"+
		"$\u0000\u00dc\u00dd\u0005\u000e\u0000\u0000\u00dd\u00df\u0003H$\u0000"+
		"\u00de\u00dc\u0001\u0000\u0000\u0000\u00df\u00e2\u0001\u0000\u0000\u0000"+
		"\u00e0\u00de\u0001\u0000\u0000\u0000\u00e0\u00e1\u0001\u0000\u0000\u0000"+
		"\u00e1\u00e3\u0001\u0000\u0000\u0000\u00e2\u00e0\u0001\u0000\u0000\u0000"+
		"\u00e3\u00e4\u0005\u000f\u0000\u0000\u00e4\u00e8\u0005\u0010\u0000\u0000"+
		"\u00e5\u00e7\u0003\u0004\u0002\u0000\u00e6\u00e5\u0001\u0000\u0000\u0000"+
		"\u00e7\u00ea\u0001\u0000\u0000\u0000\u00e8\u00e6\u0001\u0000\u0000\u0000"+
		"\u00e8\u00e9\u0001\u0000\u0000\u0000\u00e9\u0015\u0001\u0000\u0000\u0000"+
		"\u00ea\u00e8\u0001\u0000\u0000\u0000\u00eb\u00ec\u0005\u0011\u0000\u0000"+
		"\u00ec\u00ed\u0005\u000f\u0000\u0000\u00ed\u00f1\u0005\u0010\u0000\u0000"+
		"\u00ee\u00f0\u0003\u0004\u0002\u0000\u00ef\u00ee\u0001\u0000\u0000\u0000"+
		"\u00f0\u00f3\u0001\u0000\u0000\u0000\u00f1\u00ef\u0001\u0000\u0000\u0000"+
		"\u00f1\u00f2\u0001\u0000\u0000\u0000\u00f2\u0017\u0001\u0000\u0000\u0000"+
		"\u00f3\u00f1\u0001\u0000\u0000\u0000\u00f4\u00f8\u0003\u001e\u000f\u0000"+
		"\u00f5\u00f8\u0003>\u001f\u0000\u00f6\u00f8\u0003\u001a\r\u0000\u00f7"+
		"\u00f4\u0001\u0000\u0000\u0000\u00f7\u00f5\u0001\u0000\u0000\u0000\u00f7"+
		"\u00f6\u0001\u0000\u0000\u0000\u00f8\u0019\u0001\u0000\u0000\u0000\u00f9"+
		"\u00fa\u0005\u0012\u0000\u0000\u00fa\u00fb\u00056\u0000\u0000\u00fb\u0104"+
		"\u0005\u0003\u0000\u0000\u00fc\u0101\u0003\u001c\u000e\u0000\u00fd\u00fe"+
		"\u0005\u000e\u0000\u0000\u00fe\u0100\u0003\u001c\u000e\u0000\u00ff\u00fd"+
		"\u0001\u0000\u0000\u0000\u0100\u0103\u0001\u0000\u0000\u0000\u0101\u00ff"+
		"\u0001\u0000\u0000\u0000\u0101\u0102\u0001\u0000\u0000\u0000\u0102\u0105"+
		"\u0001\u0000\u0000\u0000\u0103\u0101\u0001\u0000\u0000\u0000\u0104\u00fc"+
		"\u0001\u0000\u0000\u0000\u0104\u0105\u0001\u0000\u0000\u0000\u0105\u0106"+
		"\u0001\u0000\u0000\u0000\u0106\u0107\u0005\u0004\u0000\u0000\u0107\u0108"+
		"\u0005\u0013\u0000\u0000\u0108\u0109\u0003D\"\u0000\u0109\u010d\u0005"+
		"\u0005\u0000\u0000\u010a\u010c\u0003\u0004\u0002\u0000\u010b\u010a\u0001"+
		"\u0000\u0000\u0000\u010c\u010f\u0001\u0000\u0000\u0000\u010d\u010b\u0001"+
		"\u0000\u0000\u0000\u010d\u010e\u0001\u0000\u0000\u0000\u010e\u0110\u0001"+
		"\u0000\u0000\u0000\u010f\u010d\u0001\u0000\u0000\u0000\u0110\u0111\u0005"+
		"\u0006\u0000\u0000\u0111\u001b\u0001\u0000\u0000\u0000\u0112\u0115\u0003"+
		"D\"\u0000\u0113\u0115\u0003F#\u0000\u0114\u0112\u0001\u0000\u0000\u0000"+
		"\u0114\u0113\u0001\u0000\u0000\u0000\u0115\u0116\u0001\u0000\u0000\u0000"+
		"\u0116\u0117\u00056\u0000\u0000\u0117\u001d\u0001\u0000\u0000\u0000\u0118"+
		"\u0119\u0005\u0014\u0000\u0000\u0119\u011a\u00056\u0000\u0000\u011a\u011b"+
		"\u0005\u0015\u0000\u0000\u011b\u011f\u0003D\"\u0000\u011c\u0120\u0003"+
		"H$\u0000\u011d\u0120\u00032\u0019\u0000\u011e\u0120\u0003$\u0012\u0000"+
		"\u011f\u011c\u0001\u0000\u0000\u0000\u011f\u011d\u0001\u0000\u0000\u0000"+
		"\u011f\u011e\u0001\u0000\u0000\u0000\u011f\u0120\u0001\u0000\u0000\u0000"+
		"\u0120\u0121\u0001\u0000\u0000\u0000\u0121\u0122\u0005\u0001\u0000\u0000"+
		"\u0122\u012b\u0001\u0000\u0000\u0000\u0123\u0124\u0005\u0014\u0000\u0000"+
		"\u0124\u0125\u00056\u0000\u0000\u0125\u0126\u0005\u0015\u0000\u0000\u0126"+
		"\u0127\u00054\u0000\u0000\u0127\u0128\u0003J%\u0000\u0128\u0129\u0005"+
		"\u0001\u0000\u0000\u0129\u012b\u0001\u0000\u0000\u0000\u012a\u0118\u0001"+
		"\u0000\u0000\u0000\u012a\u0123\u0001\u0000\u0000\u0000\u012b\u001f\u0001"+
		"\u0000\u0000\u0000\u012c\u012d\u00056\u0000\u0000\u012d\u0136\u0005\u0003"+
		"\u0000\u0000\u012e\u0133\u0003H$\u0000\u012f\u0130\u0005\u000e\u0000\u0000"+
		"\u0130\u0132\u0003H$\u0000\u0131\u012f\u0001\u0000\u0000\u0000\u0132\u0135"+
		"\u0001\u0000\u0000\u0000\u0133\u0131\u0001\u0000\u0000\u0000\u0133\u0134"+
		"\u0001\u0000\u0000\u0000\u0134\u0137\u0001\u0000\u0000\u0000\u0135\u0133"+
		"\u0001\u0000\u0000\u0000\u0136\u012e\u0001\u0000\u0000\u0000\u0136\u0137"+
		"\u0001\u0000\u0000\u0000\u0137\u0138\u0001\u0000\u0000\u0000\u0138\u0139"+
		"\u0005\u0004\u0000\u0000\u0139!\u0001\u0000\u0000\u0000\u013a\u013d\u0005"+
		"6\u0000\u0000\u013b\u013e\u0005\u0016\u0000\u0000\u013c\u013e\u0005\u0015"+
		"\u0000\u0000\u013d\u013b\u0001\u0000\u0000\u0000\u013d\u013c\u0001\u0000"+
		"\u0000\u0000\u013e\u0142\u0001\u0000\u0000\u0000\u013f\u0143\u0003H$\u0000"+
		"\u0140\u0143\u00032\u0019\u0000\u0141\u0143\u0003$\u0012\u0000\u0142\u013f"+
		"\u0001\u0000\u0000\u0000\u0142\u0140\u0001\u0000\u0000\u0000\u0142\u0141"+
		"\u0001\u0000\u0000\u0000\u0143#\u0001\u0000\u0000\u0000\u0144\u014e\u0003"+
		"(\u0014\u0000\u0145\u0149\u0003&\u0013\u0000\u0146\u0147\u00036\u001b"+
		"\u0000\u0147\u0148\u0003&\u0013\u0000\u0148\u014a\u0001\u0000\u0000\u0000"+
		"\u0149\u0146\u0001\u0000\u0000\u0000\u014a\u014b\u0001\u0000\u0000\u0000"+
		"\u014b\u0149\u0001\u0000\u0000\u0000\u014b\u014c\u0001\u0000\u0000\u0000"+
		"\u014c\u014e\u0001\u0000\u0000\u0000\u014d\u0144\u0001\u0000\u0000\u0000"+
		"\u014d\u0145\u0001\u0000\u0000\u0000\u014e%\u0001\u0000\u0000\u0000\u014f"+
		"\u0152\u0003,\u0016\u0000\u0150\u0152\u0003*\u0015\u0000\u0151\u014f\u0001"+
		"\u0000\u0000\u0000\u0151\u0150\u0001\u0000\u0000\u0000\u0152\'\u0001\u0000"+
		"\u0000\u0000\u0153\u0156\u0003*\u0015\u0000\u0154\u0156\u0003,\u0016\u0000"+
		"\u0155\u0153\u0001\u0000\u0000\u0000\u0155\u0154\u0001\u0000\u0000\u0000"+
		"\u0156)\u0001\u0000\u0000\u0000\u0157\u0158\u0003,\u0016\u0000\u0158\u0159"+
		"\u00038\u001c\u0000\u0159\u015a\u0003,\u0016\u0000\u015a+\u0001\u0000"+
		"\u0000\u0000\u015b\u0167\u00056\u0000\u0000\u015c\u015d\u0005\u0003\u0000"+
		"\u0000\u015d\u015e\u0003$\u0012\u0000\u015e\u015f\u0005\u0004\u0000\u0000"+
		"\u015f\u0167\u0001\u0000\u0000\u0000\u0160\u0167\u0003:\u001d\u0000\u0161"+
		"\u0167\u00053\u0000\u0000\u0162\u0167\u00057\u0000\u0000\u0163\u0167\u0005"+
		"8\u0000\u0000\u0164\u0167\u00055\u0000\u0000\u0165\u0167\u0003 \u0010"+
		"\u0000\u0166\u015b\u0001\u0000\u0000\u0000\u0166\u015c\u0001\u0000\u0000"+
		"\u0000\u0166\u0160\u0001\u0000\u0000\u0000\u0166\u0161\u0001\u0000\u0000"+
		"\u0000\u0166\u0162\u0001\u0000\u0000\u0000\u0166\u0163\u0001\u0000\u0000"+
		"\u0000\u0166\u0164\u0001\u0000\u0000\u0000\u0166\u0165\u0001\u0000\u0000"+
		"\u0000\u0167-\u0001\u0000\u0000\u0000\u0168\u0169\u0007\u0000\u0000\u0000"+
		"\u0169/\u0001\u0000\u0000\u0000\u016a\u016d\u00056\u0000\u0000\u016b\u016e"+
		"\u0005\u0016\u0000\u0000\u016c\u016e\u00034\u001a\u0000\u016d\u016b\u0001"+
		"\u0000\u0000\u0000\u016d\u016c\u0001\u0000\u0000\u0000\u016e\u016f\u0001"+
		"\u0000\u0000\u0000\u016f\u0170\u00032\u0019\u0000\u01701\u0001\u0000\u0000"+
		"\u0000\u0171\u0172\u0006\u0019\uffff\uffff\u0000\u0172\u0173\u0005\'\u0000"+
		"\u0000\u0173\u0182\u00032\u0019\u0007\u0174\u0182\u0003H$\u0000\u0175"+
		"\u0182\u0003 \u0010\u0000\u0176\u0177\u0005\u0003\u0000\u0000\u0177\u0178"+
		"\u00032\u0019\u0000\u0178\u0179\u0005\u0004\u0000\u0000\u0179\u0182\u0001"+
		"\u0000\u0000\u0000\u017a\u017b\u0007\u0001\u0000\u0000\u017b\u0180\u0003"+
		"H$\u0000\u017c\u017d\u0003H$\u0000\u017d\u017e\u0007\u0001\u0000\u0000"+
		"\u017e\u0180\u0001\u0000\u0000\u0000\u017f\u017a\u0001\u0000\u0000\u0000"+
		"\u017f\u017c\u0001\u0000\u0000\u0000\u0180\u0182\u0001\u0000\u0000\u0000"+
		"\u0181\u0171\u0001\u0000\u0000\u0000\u0181\u0174\u0001\u0000\u0000\u0000"+
		"\u0181\u0175\u0001\u0000\u0000\u0000\u0181\u0176\u0001\u0000\u0000\u0000"+
		"\u0181\u017f\u0001\u0000\u0000\u0000\u0182\u018b\u0001\u0000\u0000\u0000"+
		"\u0183\u0184\n\u0006\u0000\u0000\u0184\u0185\u0007\u0002\u0000\u0000\u0185"+
		"\u018a\u00032\u0019\u0007\u0186\u0187\n\u0005\u0000\u0000\u0187\u0188"+
		"\u0007\u0003\u0000\u0000\u0188\u018a\u00032\u0019\u0006\u0189\u0183\u0001"+
		"\u0000\u0000\u0000\u0189\u0186\u0001\u0000\u0000\u0000\u018a\u018d\u0001"+
		"\u0000\u0000\u0000\u018b\u0189\u0001\u0000\u0000\u0000\u018b\u018c\u0001"+
		"\u0000\u0000\u0000\u018c3\u0001\u0000\u0000\u0000\u018d\u018b\u0001\u0000"+
		"\u0000\u0000\u018e\u0194\u0005-\u0000\u0000\u018f\u0194\u0005.\u0000\u0000"+
		"\u0190\u0194\u0005/\u0000\u0000\u0191\u0194\u00050\u0000\u0000\u0192\u0194"+
		"\u00051\u0000\u0000\u0193\u018e\u0001\u0000\u0000\u0000\u0193\u018f\u0001"+
		"\u0000\u0000\u0000\u0193\u0190\u0001\u0000\u0000\u0000\u0193\u0191\u0001"+
		"\u0000\u0000\u0000\u0193\u0192\u0001\u0000\u0000\u0000\u01945\u0001\u0000"+
		"\u0000\u0000\u0195\u019a\u0005\u001c\u0000\u0000\u0196\u019a\u0005\u001d"+
		"\u0000\u0000\u0197\u019a\u0005\u001e\u0000\u0000\u0198\u019a\u0005\u001f"+
		"\u0000\u0000\u0199\u0195\u0001\u0000\u0000\u0000\u0199\u0196\u0001\u0000"+
		"\u0000\u0000\u0199\u0197\u0001\u0000\u0000\u0000\u0199\u0198\u0001\u0000"+
		"\u0000\u0000\u019a7\u0001\u0000\u0000\u0000\u019b\u01a2\u0005 \u0000\u0000"+
		"\u019c\u01a2\u0005!\u0000\u0000\u019d\u01a2\u0005\"\u0000\u0000\u019e"+
		"\u01a2\u0005#\u0000\u0000\u019f\u01a2\u0005$\u0000\u0000\u01a0\u01a2\u0005"+
		"%\u0000\u0000\u01a1\u019b\u0001\u0000\u0000\u0000\u01a1\u019c\u0001\u0000"+
		"\u0000\u0000\u01a1\u019d\u0001\u0000\u0000\u0000\u01a1\u019e\u0001\u0000"+
		"\u0000\u0000\u01a1\u019f\u0001\u0000\u0000\u0000\u01a1\u01a0\u0001\u0000"+
		"\u0000\u0000\u01a29\u0001\u0000\u0000\u0000\u01a3\u01a4\u00056\u0000\u0000"+
		"\u01a4\u01a8\u0005\u0017\u0000\u0000\u01a5\u01a9\u00056\u0000\u0000\u01a6"+
		"\u01a9\u00057\u0000\u0000\u01a7\u01a9\u00032\u0019\u0000\u01a8\u01a5\u0001"+
		"\u0000\u0000\u0000\u01a8\u01a6\u0001\u0000\u0000\u0000\u01a8\u01a7\u0001"+
		"\u0000\u0000\u0000\u01a9\u01aa\u0001\u0000\u0000\u0000\u01aa\u01ab\u0005"+
		"\u0018\u0000\u0000\u01ab;\u0001\u0000\u0000\u0000\u01ac\u01ad\u00056\u0000"+
		"\u0000\u01ad\u01ae\u0005\u0019\u0000\u0000\u01ae\u01b7\u00056\u0000\u0000"+
		"\u01af\u01b3\u0005\u0003\u0000\u0000\u01b0\u01b2\u0003\u001c\u000e\u0000"+
		"\u01b1\u01b0\u0001\u0000\u0000\u0000\u01b2\u01b5\u0001\u0000\u0000\u0000"+
		"\u01b3\u01b1\u0001\u0000\u0000\u0000\u01b3\u01b4\u0001\u0000\u0000\u0000"+
		"\u01b4\u01b6\u0001\u0000\u0000\u0000\u01b5\u01b3\u0001\u0000\u0000\u0000"+
		"\u01b6\u01b8\u0005\u0004\u0000\u0000\u01b7\u01af\u0001\u0000\u0000\u0000"+
		"\u01b7\u01b8\u0001\u0000\u0000\u0000\u01b8=\u0001\u0000\u0000\u0000\u01b9"+
		"\u01ba\u0005\u001a\u0000\u0000\u01ba\u01bd\u00056\u0000\u0000\u01bb\u01bc"+
		"\u0005\u001b\u0000\u0000\u01bc\u01be\u00056\u0000\u0000\u01bd\u01bb\u0001"+
		"\u0000\u0000\u0000\u01bd\u01be\u0001\u0000\u0000\u0000\u01be\u01bf\u0001"+
		"\u0000\u0000\u0000\u01bf\u01c3\u0005\u0005\u0000\u0000\u01c0\u01c2\u0003"+
		"@ \u0000\u01c1\u01c0\u0001\u0000\u0000\u0000\u01c2\u01c5\u0001\u0000\u0000"+
		"\u0000\u01c3\u01c1\u0001\u0000\u0000\u0000\u01c3\u01c4\u0001\u0000\u0000"+
		"\u0000\u01c4\u01c6\u0001\u0000\u0000\u0000\u01c5\u01c3\u0001\u0000\u0000"+
		"\u0000\u01c6\u01c7\u0005\u0006\u0000\u0000\u01c7?\u0001\u0000\u0000\u0000"+
		"\u01c8\u01cb\u0003\u001e\u000f\u0000\u01c9\u01cb\u0003\u001a\r\u0000\u01ca"+
		"\u01c8\u0001\u0000\u0000\u0000\u01ca\u01c9\u0001\u0000\u0000\u0000\u01cb"+
		"A\u0001\u0000\u0000\u0000\u01cc\u01cd\u00056\u0000\u0000\u01cdC\u0001"+
		"\u0000\u0000\u0000\u01ce\u01d1\u00052\u0000\u0000\u01cf\u01d1\u0003B!"+
		"\u0000\u01d0\u01ce\u0001\u0000\u0000\u0000\u01d0\u01cf\u0001\u0000\u0000"+
		"\u0000\u01d1E\u0001\u0000\u0000\u0000\u01d2\u01d3\u00054\u0000\u0000\u01d3"+
		"G\u0001\u0000\u0000\u0000\u01d4\u01dc\u00057\u0000\u0000\u01d5\u01dc\u0005"+
		"8\u0000\u0000\u01d6\u01dc\u00055\u0000\u0000\u01d7\u01dc\u00053\u0000"+
		"\u0000\u01d8\u01dc\u0003:\u001d\u0000\u01d9\u01dc\u0003J%\u0000\u01da"+
		"\u01dc\u00056\u0000\u0000\u01db\u01d4\u0001\u0000\u0000\u0000\u01db\u01d5"+
		"\u0001\u0000\u0000\u0000\u01db\u01d6\u0001\u0000\u0000\u0000\u01db\u01d7"+
		"\u0001\u0000\u0000\u0000\u01db\u01d8\u0001\u0000\u0000\u0000\u01db\u01d9"+
		"\u0001\u0000\u0000\u0000\u01db\u01da\u0001\u0000\u0000\u0000\u01dcI\u0001"+
		"\u0000\u0000\u0000\u01dd\u01e6\u0005\u0017\u0000\u0000\u01de\u01e3\u0003"+
		"H$\u0000\u01df\u01e0\u0005\u000e\u0000\u0000\u01e0\u01e2\u0003H$\u0000"+
		"\u01e1\u01df\u0001\u0000\u0000\u0000\u01e2\u01e5\u0001\u0000\u0000\u0000"+
		"\u01e3\u01e1\u0001\u0000\u0000\u0000\u01e3\u01e4\u0001\u0000\u0000\u0000"+
		"\u01e4\u01e7\u0001\u0000\u0000\u0000\u01e5\u01e3\u0001\u0000\u0000\u0000"+
		"\u01e6\u01de\u0001\u0000\u0000\u0000\u01e6\u01e7\u0001\u0000\u0000\u0000"+
		"\u01e7\u01e8\u0001\u0000\u0000\u0000\u01e8\u01e9\u0005\u0018\u0000\u0000"+
		"\u01e9K\u0001\u0000\u0000\u00003OVZ{\u0085\u0094\u009c\u00a0\u00a5\u00ac"+
		"\u00ba\u00c7\u00d2\u00d6\u00e0\u00e8\u00f1\u00f7\u0101\u0104\u010d\u0114"+
		"\u011f\u012a\u0133\u0136\u013d\u0142\u014b\u014d\u0151\u0155\u0166\u016d"+
		"\u017f\u0181\u0189\u018b\u0193\u0199\u01a1\u01a8\u01b3\u01b7\u01bd\u01c3"+
		"\u01ca\u01d0\u01db\u01e3\u01e6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}