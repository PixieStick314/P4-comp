// Generated from c:/Users/nedim/Documents/GitHub/P4-comp/src/grammar_files/Dungeon.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link DungeonParser}.
 */
public interface DungeonListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link DungeonParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(DungeonParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(DungeonParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#map}.
	 * @param ctx the parse tree
	 */
	void enterMap(DungeonParser.MapContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#map}.
	 * @param ctx the parse tree
	 */
	void exitMap(DungeonParser.MapContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#procedure}.
	 * @param ctx the parse tree
	 */
	void enterProcedure(DungeonParser.ProcedureContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#procedure}.
	 * @param ctx the parse tree
	 */
	void exitProcedure(DungeonParser.ProcedureContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(DungeonParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(DungeonParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#layer}.
	 * @param ctx the parse tree
	 */
	void enterLayer(DungeonParser.LayerContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#layer}.
	 * @param ctx the parse tree
	 */
	void exitLayer(DungeonParser.LayerContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#varDeclStat}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclStat(DungeonParser.VarDeclStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#varDeclStat}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclStat(DungeonParser.VarDeclStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(DungeonParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(DungeonParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#assignStat}.
	 * @param ctx the parse tree
	 */
	void enterAssignStat(DungeonParser.AssignStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#assignStat}.
	 * @param ctx the parse tree
	 */
	void exitAssignStat(DungeonParser.AssignStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(DungeonParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(DungeonParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDecl(DungeonParser.FunctionDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDecl(DungeonParser.FunctionDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(DungeonParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(DungeonParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#list}.
	 * @param ctx the parse tree
	 */
	void enterList(DungeonParser.ListContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#list}.
	 * @param ctx the parse tree
	 */
	void exitList(DungeonParser.ListContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#listElement}.
	 * @param ctx the parse tree
	 */
	void enterListElement(DungeonParser.ListElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#listElement}.
	 * @param ctx the parse tree
	 */
	void exitListElement(DungeonParser.ListElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#listLength}.
	 * @param ctx the parse tree
	 */
	void enterListLength(DungeonParser.ListLengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#listLength}.
	 * @param ctx the parse tree
	 */
	void exitListLength(DungeonParser.ListLengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#listPop}.
	 * @param ctx the parse tree
	 */
	void enterListPop(DungeonParser.ListPopContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#listPop}.
	 * @param ctx the parse tree
	 */
	void exitListPop(DungeonParser.ListPopContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#hashTable}.
	 * @param ctx the parse tree
	 */
	void enterHashTable(DungeonParser.HashTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#hashTable}.
	 * @param ctx the parse tree
	 */
	void exitHashTable(DungeonParser.HashTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#keyValuePair}.
	 * @param ctx the parse tree
	 */
	void enterKeyValuePair(DungeonParser.KeyValuePairContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#keyValuePair}.
	 * @param ctx the parse tree
	 */
	void exitKeyValuePair(DungeonParser.KeyValuePairContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#struct}.
	 * @param ctx the parse tree
	 */
	void enterStruct(DungeonParser.StructContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#struct}.
	 * @param ctx the parse tree
	 */
	void exitStruct(DungeonParser.StructContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#structDef}.
	 * @param ctx the parse tree
	 */
	void enterStructDef(DungeonParser.StructDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#structDef}.
	 * @param ctx the parse tree
	 */
	void exitStructDef(DungeonParser.StructDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#structField}.
	 * @param ctx the parse tree
	 */
	void enterStructField(DungeonParser.StructFieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#structField}.
	 * @param ctx the parse tree
	 */
	void exitStructField(DungeonParser.StructFieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#plusEquals}.
	 * @param ctx the parse tree
	 */
	void enterPlusEquals(DungeonParser.PlusEqualsContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#plusEquals}.
	 * @param ctx the parse tree
	 */
	void exitPlusEquals(DungeonParser.PlusEqualsContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#minusEquals}.
	 * @param ctx the parse tree
	 */
	void enterMinusEquals(DungeonParser.MinusEqualsContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#minusEquals}.
	 * @param ctx the parse tree
	 */
	void exitMinusEquals(DungeonParser.MinusEqualsContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#printStat}.
	 * @param ctx the parse tree
	 */
	void enterPrintStat(DungeonParser.PrintStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#printStat}.
	 * @param ctx the parse tree
	 */
	void exitPrintStat(DungeonParser.PrintStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#ifStat}.
	 * @param ctx the parse tree
	 */
	void enterIfStat(DungeonParser.IfStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#ifStat}.
	 * @param ctx the parse tree
	 */
	void exitIfStat(DungeonParser.IfStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#elifStat}.
	 * @param ctx the parse tree
	 */
	void enterElifStat(DungeonParser.ElifStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#elifStat}.
	 * @param ctx the parse tree
	 */
	void exitElifStat(DungeonParser.ElifStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#elseStat}.
	 * @param ctx the parse tree
	 */
	void enterElseStat(DungeonParser.ElseStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#elseStat}.
	 * @param ctx the parse tree
	 */
	void exitElseStat(DungeonParser.ElseStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#statBlock}.
	 * @param ctx the parse tree
	 */
	void enterStatBlock(DungeonParser.StatBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#statBlock}.
	 * @param ctx the parse tree
	 */
	void exitStatBlock(DungeonParser.StatBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#forLoop}.
	 * @param ctx the parse tree
	 */
	void enterForLoop(DungeonParser.ForLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#forLoop}.
	 * @param ctx the parse tree
	 */
	void exitForLoop(DungeonParser.ForLoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void enterWhileLoop(DungeonParser.WhileLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void exitWhileLoop(DungeonParser.WhileLoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#returnStat}.
	 * @param ctx the parse tree
	 */
	void enterReturnStat(DungeonParser.ReturnStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#returnStat}.
	 * @param ctx the parse tree
	 */
	void exitReturnStat(DungeonParser.ReturnStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#random}.
	 * @param ctx the parse tree
	 */
	void enterRandom(DungeonParser.RandomContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#random}.
	 * @param ctx the parse tree
	 */
	void exitRandom(DungeonParser.RandomContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#seed}.
	 * @param ctx the parse tree
	 */
	void enterSeed(DungeonParser.SeedContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#seed}.
	 * @param ctx the parse tree
	 */
	void exitSeed(DungeonParser.SeedContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#range}.
	 * @param ctx the parse tree
	 */
	void enterRange(DungeonParser.RangeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#range}.
	 * @param ctx the parse tree
	 */
	void exitRange(DungeonParser.RangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#params}.
	 * @param ctx the parse tree
	 */
	void enterParams(DungeonParser.ParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#params}.
	 * @param ctx the parse tree
	 */
	void exitParams(DungeonParser.ParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#args}.
	 * @param ctx the parse tree
	 */
	void enterArgs(DungeonParser.ArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#args}.
	 * @param ctx the parse tree
	 */
	void exitArgs(DungeonParser.ArgsContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#inner}.
	 * @param ctx the parse tree
	 */
	void enterInner(DungeonParser.InnerContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#inner}.
	 * @param ctx the parse tree
	 */
	void exitInner(DungeonParser.InnerContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#index}.
	 * @param ctx the parse tree
	 */
	void enterIndex(DungeonParser.IndexContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#index}.
	 * @param ctx the parse tree
	 */
	void exitIndex(DungeonParser.IndexContext ctx);
	/**
	 * Enter a parse tree produced by {@link DungeonParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(DungeonParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link DungeonParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(DungeonParser.ExprContext ctx);
}