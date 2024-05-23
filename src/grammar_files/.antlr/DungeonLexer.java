// Generated from c:/Users/Lenovo/Documents/GitHub/P4-comp/src/grammar_files/Dungeon.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class DungeonLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, IF=6, ELIF=7, ELSE=8, RETURN=9, 
		PRINT=10, FOR=11, IN=12, WHILE=13, DEF=14, LAYER=15, PROCEDURE=16, SEED=17, 
		RANDOM=18, PLUS=19, MINUS=20, MULT=21, DIV=22, GT=23, GTE=24, LT=25, LTE=26, 
		EQ=27, NEQ=28, PEQ=29, MEQ=30, MOD=31, AND=32, OR=33, NOT=34, TRUE=35, 
		FALSE=36, SQRT=37, POW=38, COMMENT_SINGLELINE=39, INT=40, FLOAT=41, STRING=42, 
		ID=43, OPEN_PARENTH=44, CLOSED_PARENTH=45, OPEN_BRACK=46, CLOSED_BRACK=47, 
		OPEN_CURL=48, CLOSED_CURL=49, COMMA=50, DOT=51, COLON=52, EQUAL_SIGN=53, 
		WS=54;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "IF", "ELIF", "ELSE", "RETURN", 
			"PRINT", "FOR", "IN", "WHILE", "DEF", "LAYER", "PROCEDURE", "SEED", "RANDOM", 
			"PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", "LT", "LTE", "EQ", "NEQ", 
			"PEQ", "MEQ", "MOD", "AND", "OR", "NOT", "TRUE", "FALSE", "SQRT", "POW", 
			"COMMENT_SINGLELINE", "INT", "FLOAT", "STRING", "ID", "OPEN_PARENTH", 
			"CLOSED_PARENTH", "OPEN_BRACK", "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", 
			"COMMA", "DOT", "COLON", "EQUAL_SIGN", "LETTER", "ESC", "DIGIT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Map'", "'let'", "'len'", "'pop'", "'struct'", "'if'", "'elif'", 
			"'else'", "'return'", "'print'", "'for'", "'in'", "'while'", "'def'", 
			"'layer'", "'procedure'", "'seed'", "'random'", "'+'", "'-'", "'*'", 
			"'/'", "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", "'+='", "'-='", 
			"'%'", "'and'", "'or'", "'not'", "'True'", "'False'", "'sqrt'", "'pow'", 
			null, null, null, null, null, "'('", "')'", "'['", "']'", "'{'", "'}'", 
			"','", "'.'", "':'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, "IF", "ELIF", "ELSE", "RETURN", "PRINT", 
			"FOR", "IN", "WHILE", "DEF", "LAYER", "PROCEDURE", "SEED", "RANDOM", 
			"PLUS", "MINUS", "MULT", "DIV", "GT", "GTE", "LT", "LTE", "EQ", "NEQ", 
			"PEQ", "MEQ", "MOD", "AND", "OR", "NOT", "TRUE", "FALSE", "SQRT", "POW", 
			"COMMENT_SINGLELINE", "INT", "FLOAT", "STRING", "ID", "OPEN_PARENTH", 
			"CLOSED_PARENTH", "OPEN_BRACK", "CLOSED_BRACK", "OPEN_CURL", "CLOSED_CURL", 
			"COMMA", "DOT", "COLON", "EQUAL_SIGN", "WS"
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


	public DungeonLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Dungeon.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u00006\u0165\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007"+
		"+\u0002,\u0007,\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u0007"+
		"0\u00021\u00071\u00022\u00072\u00023\u00073\u00024\u00074\u00025\u0007"+
		"5\u00026\u00076\u00027\u00077\u00028\u00078\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001c"+
		"\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e"+
		"\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001 \u0001"+
		" \u0001 \u0001!\u0001!\u0001!\u0001!\u0001\"\u0001\"\u0001\"\u0001\"\u0001"+
		"\"\u0001#\u0001#\u0001#\u0001#\u0001#\u0001#\u0001$\u0001$\u0001$\u0001"+
		"$\u0001$\u0001%\u0001%\u0001%\u0001%\u0001&\u0001&\u0001&\u0001&\u0005"+
		"&\u0115\b&\n&\f&\u0118\t&\u0001&\u0001&\u0001\'\u0003\'\u011d\b\'\u0001"+
		"\'\u0004\'\u0120\b\'\u000b\'\f\'\u0121\u0001(\u0003(\u0125\b(\u0001(\u0004"+
		"(\u0128\b(\u000b(\f(\u0129\u0001(\u0001(\u0004(\u012e\b(\u000b(\f(\u012f"+
		"\u0001)\u0001)\u0001)\u0005)\u0135\b)\n)\f)\u0138\t)\u0001)\u0001)\u0001"+
		"*\u0001*\u0001*\u0005*\u013f\b*\n*\f*\u0142\t*\u0001+\u0001+\u0001,\u0001"+
		",\u0001-\u0001-\u0001.\u0001.\u0001/\u0001/\u00010\u00010\u00011\u0001"+
		"1\u00012\u00012\u00013\u00013\u00014\u00014\u00015\u00015\u00016\u0001"+
		"6\u00016\u00017\u00017\u00018\u00048\u0160\b8\u000b8\f8\u0161\u00018\u0001"+
		"8\u0000\u00009\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015"+
		"+\u0016-\u0017/\u00181\u00193\u001a5\u001b7\u001c9\u001d;\u001e=\u001f"+
		"? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_0a1c2e3g4i5k\u0000m\u0000o\u0000q6"+
		"\u0001\u0000\u0006\u0002\u0000\n\n\r\r\u0002\u0000\"\"\\\\\u0003\u0000"+
		"AZ__az\u0005\u0000\"\"\'\'\\\\nntt\u0002\u000009__\u0003\u0000\t\n\r\r"+
		"  \u016c\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000"+
		"\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000"+
		"\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000"+
		"!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001"+
		"\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000"+
		"\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000"+
		"\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u00003"+
		"\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001\u0000"+
		"\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0000;\u0001\u0000\u0000\u0000"+
		"\u0000=\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000\u0000\u0000A"+
		"\u0001\u0000\u0000\u0000\u0000C\u0001\u0000\u0000\u0000\u0000E\u0001\u0000"+
		"\u0000\u0000\u0000G\u0001\u0000\u0000\u0000\u0000I\u0001\u0000\u0000\u0000"+
		"\u0000K\u0001\u0000\u0000\u0000\u0000M\u0001\u0000\u0000\u0000\u0000O"+
		"\u0001\u0000\u0000\u0000\u0000Q\u0001\u0000\u0000\u0000\u0000S\u0001\u0000"+
		"\u0000\u0000\u0000U\u0001\u0000\u0000\u0000\u0000W\u0001\u0000\u0000\u0000"+
		"\u0000Y\u0001\u0000\u0000\u0000\u0000[\u0001\u0000\u0000\u0000\u0000]"+
		"\u0001\u0000\u0000\u0000\u0000_\u0001\u0000\u0000\u0000\u0000a\u0001\u0000"+
		"\u0000\u0000\u0000c\u0001\u0000\u0000\u0000\u0000e\u0001\u0000\u0000\u0000"+
		"\u0000g\u0001\u0000\u0000\u0000\u0000i\u0001\u0000\u0000\u0000\u0000q"+
		"\u0001\u0000\u0000\u0000\u0001s\u0001\u0000\u0000\u0000\u0003w\u0001\u0000"+
		"\u0000\u0000\u0005{\u0001\u0000\u0000\u0000\u0007\u007f\u0001\u0000\u0000"+
		"\u0000\t\u0083\u0001\u0000\u0000\u0000\u000b\u008a\u0001\u0000\u0000\u0000"+
		"\r\u008d\u0001\u0000\u0000\u0000\u000f\u0092\u0001\u0000\u0000\u0000\u0011"+
		"\u0097\u0001\u0000\u0000\u0000\u0013\u009e\u0001\u0000\u0000\u0000\u0015"+
		"\u00a4\u0001\u0000\u0000\u0000\u0017\u00a8\u0001\u0000\u0000\u0000\u0019"+
		"\u00ab\u0001\u0000\u0000\u0000\u001b\u00b1\u0001\u0000\u0000\u0000\u001d"+
		"\u00b5\u0001\u0000\u0000\u0000\u001f\u00bb\u0001\u0000\u0000\u0000!\u00c5"+
		"\u0001\u0000\u0000\u0000#\u00ca\u0001\u0000\u0000\u0000%\u00d1\u0001\u0000"+
		"\u0000\u0000\'\u00d3\u0001\u0000\u0000\u0000)\u00d5\u0001\u0000\u0000"+
		"\u0000+\u00d7\u0001\u0000\u0000\u0000-\u00d9\u0001\u0000\u0000\u0000/"+
		"\u00db\u0001\u0000\u0000\u00001\u00de\u0001\u0000\u0000\u00003\u00e0\u0001"+
		"\u0000\u0000\u00005\u00e3\u0001\u0000\u0000\u00007\u00e6\u0001\u0000\u0000"+
		"\u00009\u00e9\u0001\u0000\u0000\u0000;\u00ec\u0001\u0000\u0000\u0000="+
		"\u00ef\u0001\u0000\u0000\u0000?\u00f1\u0001\u0000\u0000\u0000A\u00f5\u0001"+
		"\u0000\u0000\u0000C\u00f8\u0001\u0000\u0000\u0000E\u00fc\u0001\u0000\u0000"+
		"\u0000G\u0101\u0001\u0000\u0000\u0000I\u0107\u0001\u0000\u0000\u0000K"+
		"\u010c\u0001\u0000\u0000\u0000M\u0110\u0001\u0000\u0000\u0000O\u011c\u0001"+
		"\u0000\u0000\u0000Q\u0124\u0001\u0000\u0000\u0000S\u0131\u0001\u0000\u0000"+
		"\u0000U\u013b\u0001\u0000\u0000\u0000W\u0143\u0001\u0000\u0000\u0000Y"+
		"\u0145\u0001\u0000\u0000\u0000[\u0147\u0001\u0000\u0000\u0000]\u0149\u0001"+
		"\u0000\u0000\u0000_\u014b\u0001\u0000\u0000\u0000a\u014d\u0001\u0000\u0000"+
		"\u0000c\u014f\u0001\u0000\u0000\u0000e\u0151\u0001\u0000\u0000\u0000g"+
		"\u0153\u0001\u0000\u0000\u0000i\u0155\u0001\u0000\u0000\u0000k\u0157\u0001"+
		"\u0000\u0000\u0000m\u0159\u0001\u0000\u0000\u0000o\u015c\u0001\u0000\u0000"+
		"\u0000q\u015f\u0001\u0000\u0000\u0000st\u0005M\u0000\u0000tu\u0005a\u0000"+
		"\u0000uv\u0005p\u0000\u0000v\u0002\u0001\u0000\u0000\u0000wx\u0005l\u0000"+
		"\u0000xy\u0005e\u0000\u0000yz\u0005t\u0000\u0000z\u0004\u0001\u0000\u0000"+
		"\u0000{|\u0005l\u0000\u0000|}\u0005e\u0000\u0000}~\u0005n\u0000\u0000"+
		"~\u0006\u0001\u0000\u0000\u0000\u007f\u0080\u0005p\u0000\u0000\u0080\u0081"+
		"\u0005o\u0000\u0000\u0081\u0082\u0005p\u0000\u0000\u0082\b\u0001\u0000"+
		"\u0000\u0000\u0083\u0084\u0005s\u0000\u0000\u0084\u0085\u0005t\u0000\u0000"+
		"\u0085\u0086\u0005r\u0000\u0000\u0086\u0087\u0005u\u0000\u0000\u0087\u0088"+
		"\u0005c\u0000\u0000\u0088\u0089\u0005t\u0000\u0000\u0089\n\u0001\u0000"+
		"\u0000\u0000\u008a\u008b\u0005i\u0000\u0000\u008b\u008c\u0005f\u0000\u0000"+
		"\u008c\f\u0001\u0000\u0000\u0000\u008d\u008e\u0005e\u0000\u0000\u008e"+
		"\u008f\u0005l\u0000\u0000\u008f\u0090\u0005i\u0000\u0000\u0090\u0091\u0005"+
		"f\u0000\u0000\u0091\u000e\u0001\u0000\u0000\u0000\u0092\u0093\u0005e\u0000"+
		"\u0000\u0093\u0094\u0005l\u0000\u0000\u0094\u0095\u0005s\u0000\u0000\u0095"+
		"\u0096\u0005e\u0000\u0000\u0096\u0010\u0001\u0000\u0000\u0000\u0097\u0098"+
		"\u0005r\u0000\u0000\u0098\u0099\u0005e\u0000\u0000\u0099\u009a\u0005t"+
		"\u0000\u0000\u009a\u009b\u0005u\u0000\u0000\u009b\u009c\u0005r\u0000\u0000"+
		"\u009c\u009d\u0005n\u0000\u0000\u009d\u0012\u0001\u0000\u0000\u0000\u009e"+
		"\u009f\u0005p\u0000\u0000\u009f\u00a0\u0005r\u0000\u0000\u00a0\u00a1\u0005"+
		"i\u0000\u0000\u00a1\u00a2\u0005n\u0000\u0000\u00a2\u00a3\u0005t\u0000"+
		"\u0000\u00a3\u0014\u0001\u0000\u0000\u0000\u00a4\u00a5\u0005f\u0000\u0000"+
		"\u00a5\u00a6\u0005o\u0000\u0000\u00a6\u00a7\u0005r\u0000\u0000\u00a7\u0016"+
		"\u0001\u0000\u0000\u0000\u00a8\u00a9\u0005i\u0000\u0000\u00a9\u00aa\u0005"+
		"n\u0000\u0000\u00aa\u0018\u0001\u0000\u0000\u0000\u00ab\u00ac\u0005w\u0000"+
		"\u0000\u00ac\u00ad\u0005h\u0000\u0000\u00ad\u00ae\u0005i\u0000\u0000\u00ae"+
		"\u00af\u0005l\u0000\u0000\u00af\u00b0\u0005e\u0000\u0000\u00b0\u001a\u0001"+
		"\u0000\u0000\u0000\u00b1\u00b2\u0005d\u0000\u0000\u00b2\u00b3\u0005e\u0000"+
		"\u0000\u00b3\u00b4\u0005f\u0000\u0000\u00b4\u001c\u0001\u0000\u0000\u0000"+
		"\u00b5\u00b6\u0005l\u0000\u0000\u00b6\u00b7\u0005a\u0000\u0000\u00b7\u00b8"+
		"\u0005y\u0000\u0000\u00b8\u00b9\u0005e\u0000\u0000\u00b9\u00ba\u0005r"+
		"\u0000\u0000\u00ba\u001e\u0001\u0000\u0000\u0000\u00bb\u00bc\u0005p\u0000"+
		"\u0000\u00bc\u00bd\u0005r\u0000\u0000\u00bd\u00be\u0005o\u0000\u0000\u00be"+
		"\u00bf\u0005c\u0000\u0000\u00bf\u00c0\u0005e\u0000\u0000\u00c0\u00c1\u0005"+
		"d\u0000\u0000\u00c1\u00c2\u0005u\u0000\u0000\u00c2\u00c3\u0005r\u0000"+
		"\u0000\u00c3\u00c4\u0005e\u0000\u0000\u00c4 \u0001\u0000\u0000\u0000\u00c5"+
		"\u00c6\u0005s\u0000\u0000\u00c6\u00c7\u0005e\u0000\u0000\u00c7\u00c8\u0005"+
		"e\u0000\u0000\u00c8\u00c9\u0005d\u0000\u0000\u00c9\"\u0001\u0000\u0000"+
		"\u0000\u00ca\u00cb\u0005r\u0000\u0000\u00cb\u00cc\u0005a\u0000\u0000\u00cc"+
		"\u00cd\u0005n\u0000\u0000\u00cd\u00ce\u0005d\u0000\u0000\u00ce\u00cf\u0005"+
		"o\u0000\u0000\u00cf\u00d0\u0005m\u0000\u0000\u00d0$\u0001\u0000\u0000"+
		"\u0000\u00d1\u00d2\u0005+\u0000\u0000\u00d2&\u0001\u0000\u0000\u0000\u00d3"+
		"\u00d4\u0005-\u0000\u0000\u00d4(\u0001\u0000\u0000\u0000\u00d5\u00d6\u0005"+
		"*\u0000\u0000\u00d6*\u0001\u0000\u0000\u0000\u00d7\u00d8\u0005/\u0000"+
		"\u0000\u00d8,\u0001\u0000\u0000\u0000\u00d9\u00da\u0005>\u0000\u0000\u00da"+
		".\u0001\u0000\u0000\u0000\u00db\u00dc\u0005>\u0000\u0000\u00dc\u00dd\u0005"+
		"=\u0000\u0000\u00dd0\u0001\u0000\u0000\u0000\u00de\u00df\u0005<\u0000"+
		"\u0000\u00df2\u0001\u0000\u0000\u0000\u00e0\u00e1\u0005<\u0000\u0000\u00e1"+
		"\u00e2\u0005=\u0000\u0000\u00e24\u0001\u0000\u0000\u0000\u00e3\u00e4\u0005"+
		"=\u0000\u0000\u00e4\u00e5\u0005=\u0000\u0000\u00e56\u0001\u0000\u0000"+
		"\u0000\u00e6\u00e7\u0005!\u0000\u0000\u00e7\u00e8\u0005=\u0000\u0000\u00e8"+
		"8\u0001\u0000\u0000\u0000\u00e9\u00ea\u0005+\u0000\u0000\u00ea\u00eb\u0005"+
		"=\u0000\u0000\u00eb:\u0001\u0000\u0000\u0000\u00ec\u00ed\u0005-\u0000"+
		"\u0000\u00ed\u00ee\u0005=\u0000\u0000\u00ee<\u0001\u0000\u0000\u0000\u00ef"+
		"\u00f0\u0005%\u0000\u0000\u00f0>\u0001\u0000\u0000\u0000\u00f1\u00f2\u0005"+
		"a\u0000\u0000\u00f2\u00f3\u0005n\u0000\u0000\u00f3\u00f4\u0005d\u0000"+
		"\u0000\u00f4@\u0001\u0000\u0000\u0000\u00f5\u00f6\u0005o\u0000\u0000\u00f6"+
		"\u00f7\u0005r\u0000\u0000\u00f7B\u0001\u0000\u0000\u0000\u00f8\u00f9\u0005"+
		"n\u0000\u0000\u00f9\u00fa\u0005o\u0000\u0000\u00fa\u00fb\u0005t\u0000"+
		"\u0000\u00fbD\u0001\u0000\u0000\u0000\u00fc\u00fd\u0005T\u0000\u0000\u00fd"+
		"\u00fe\u0005r\u0000\u0000\u00fe\u00ff\u0005u\u0000\u0000\u00ff\u0100\u0005"+
		"e\u0000\u0000\u0100F\u0001\u0000\u0000\u0000\u0101\u0102\u0005F\u0000"+
		"\u0000\u0102\u0103\u0005a\u0000\u0000\u0103\u0104\u0005l\u0000\u0000\u0104"+
		"\u0105\u0005s\u0000\u0000\u0105\u0106\u0005e\u0000\u0000\u0106H\u0001"+
		"\u0000\u0000\u0000\u0107\u0108\u0005s\u0000\u0000\u0108\u0109\u0005q\u0000"+
		"\u0000\u0109\u010a\u0005r\u0000\u0000\u010a\u010b\u0005t\u0000\u0000\u010b"+
		"J\u0001\u0000\u0000\u0000\u010c\u010d\u0005p\u0000\u0000\u010d\u010e\u0005"+
		"o\u0000\u0000\u010e\u010f\u0005w\u0000\u0000\u010fL\u0001\u0000\u0000"+
		"\u0000\u0110\u0111\u0005/\u0000\u0000\u0111\u0112\u0005/\u0000\u0000\u0112"+
		"\u0116\u0001\u0000\u0000\u0000\u0113\u0115\b\u0000\u0000\u0000\u0114\u0113"+
		"\u0001\u0000\u0000\u0000\u0115\u0118\u0001\u0000\u0000\u0000\u0116\u0114"+
		"\u0001\u0000\u0000\u0000\u0116\u0117\u0001\u0000\u0000\u0000\u0117\u0119"+
		"\u0001\u0000\u0000\u0000\u0118\u0116\u0001\u0000\u0000\u0000\u0119\u011a"+
		"\u0006&\u0000\u0000\u011aN\u0001\u0000\u0000\u0000\u011b\u011d\u0005-"+
		"\u0000\u0000\u011c\u011b\u0001\u0000\u0000\u0000\u011c\u011d\u0001\u0000"+
		"\u0000\u0000\u011d\u011f\u0001\u0000\u0000\u0000\u011e\u0120\u0003o7\u0000"+
		"\u011f\u011e\u0001\u0000\u0000\u0000\u0120\u0121\u0001\u0000\u0000\u0000"+
		"\u0121\u011f\u0001\u0000\u0000\u0000\u0121\u0122\u0001\u0000\u0000\u0000"+
		"\u0122P\u0001\u0000\u0000\u0000\u0123\u0125\u0005-\u0000\u0000\u0124\u0123"+
		"\u0001\u0000\u0000\u0000\u0124\u0125\u0001\u0000\u0000\u0000\u0125\u0127"+
		"\u0001\u0000\u0000\u0000\u0126\u0128\u0003o7\u0000\u0127\u0126\u0001\u0000"+
		"\u0000\u0000\u0128\u0129\u0001\u0000\u0000\u0000\u0129\u0127\u0001\u0000"+
		"\u0000\u0000\u0129\u012a\u0001\u0000\u0000\u0000\u012a\u012b\u0001\u0000"+
		"\u0000\u0000\u012b\u012d\u0005.\u0000\u0000\u012c\u012e\u0003o7\u0000"+
		"\u012d\u012c\u0001\u0000\u0000\u0000\u012e\u012f\u0001\u0000\u0000\u0000"+
		"\u012f\u012d\u0001\u0000\u0000\u0000\u012f\u0130\u0001\u0000\u0000\u0000"+
		"\u0130R\u0001\u0000\u0000\u0000\u0131\u0136\u0005\"\u0000\u0000\u0132"+
		"\u0135\u0003m6\u0000\u0133\u0135\b\u0001\u0000\u0000\u0134\u0132\u0001"+
		"\u0000\u0000\u0000\u0134\u0133\u0001\u0000\u0000\u0000\u0135\u0138\u0001"+
		"\u0000\u0000\u0000\u0136\u0134\u0001\u0000\u0000\u0000\u0136\u0137\u0001"+
		"\u0000\u0000\u0000\u0137\u0139\u0001\u0000\u0000\u0000\u0138\u0136\u0001"+
		"\u0000\u0000\u0000\u0139\u013a\u0005\"\u0000\u0000\u013aT\u0001\u0000"+
		"\u0000\u0000\u013b\u0140\u0003k5\u0000\u013c\u013f\u0003k5\u0000\u013d"+
		"\u013f\u0003o7\u0000\u013e\u013c\u0001\u0000\u0000\u0000\u013e\u013d\u0001"+
		"\u0000\u0000\u0000\u013f\u0142\u0001\u0000\u0000\u0000\u0140\u013e\u0001"+
		"\u0000\u0000\u0000\u0140\u0141\u0001\u0000\u0000\u0000\u0141V\u0001\u0000"+
		"\u0000\u0000\u0142\u0140\u0001\u0000\u0000\u0000\u0143\u0144\u0005(\u0000"+
		"\u0000\u0144X\u0001\u0000\u0000\u0000\u0145\u0146\u0005)\u0000\u0000\u0146"+
		"Z\u0001\u0000\u0000\u0000\u0147\u0148\u0005[\u0000\u0000\u0148\\\u0001"+
		"\u0000\u0000\u0000\u0149\u014a\u0005]\u0000\u0000\u014a^\u0001\u0000\u0000"+
		"\u0000\u014b\u014c\u0005{\u0000\u0000\u014c`\u0001\u0000\u0000\u0000\u014d"+
		"\u014e\u0005}\u0000\u0000\u014eb\u0001\u0000\u0000\u0000\u014f\u0150\u0005"+
		",\u0000\u0000\u0150d\u0001\u0000\u0000\u0000\u0151\u0152\u0005.\u0000"+
		"\u0000\u0152f\u0001\u0000\u0000\u0000\u0153\u0154\u0005:\u0000\u0000\u0154"+
		"h\u0001\u0000\u0000\u0000\u0155\u0156\u0005=\u0000\u0000\u0156j\u0001"+
		"\u0000\u0000\u0000\u0157\u0158\u0007\u0002\u0000\u0000\u0158l\u0001\u0000"+
		"\u0000\u0000\u0159\u015a\u0005\\\u0000\u0000\u015a\u015b\u0007\u0003\u0000"+
		"\u0000\u015bn\u0001\u0000\u0000\u0000\u015c\u015d\u0007\u0004\u0000\u0000"+
		"\u015dp\u0001\u0000\u0000\u0000\u015e\u0160\u0007\u0005\u0000\u0000\u015f"+
		"\u015e\u0001\u0000\u0000\u0000\u0160\u0161\u0001\u0000\u0000\u0000\u0161"+
		"\u015f\u0001\u0000\u0000\u0000\u0161\u0162\u0001\u0000\u0000\u0000\u0162"+
		"\u0163\u0001\u0000\u0000\u0000\u0163\u0164\u00068\u0000\u0000\u0164r\u0001"+
		"\u0000\u0000\u0000\f\u0000\u0116\u011c\u0121\u0124\u0129\u012f\u0134\u0136"+
		"\u013e\u0140\u0161\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}