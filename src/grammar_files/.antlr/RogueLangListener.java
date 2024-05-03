// Generated from c:/Users/nedim/Documents/GitHub/P4-comp/src/grammar_files/RogueLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link RogueLangParser}.
 */
public interface RogueLangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(RogueLangParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(RogueLangParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#object}.
	 * @param ctx the parse tree
	 */
	void enterObject(RogueLangParser.ObjectContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#object}.
	 * @param ctx the parse tree
	 */
	void exitObject(RogueLangParser.ObjectContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#procedure}.
	 * @param ctx the parse tree
	 */
	void enterProcedure(RogueLangParser.ProcedureContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#procedure}.
	 * @param ctx the parse tree
	 */
	void exitProcedure(RogueLangParser.ProcedureContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#field}.
	 * @param ctx the parse tree
	 */
	void enterField(RogueLangParser.FieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#field}.
	 * @param ctx the parse tree
	 */
	void exitField(RogueLangParser.FieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(RogueLangParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(RogueLangParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#varDeclStat}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclStat(RogueLangParser.VarDeclStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#varDeclStat}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclStat(RogueLangParser.VarDeclStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(RogueLangParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(RogueLangParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#assignStat}.
	 * @param ctx the parse tree
	 */
	void enterAssignStat(RogueLangParser.AssignStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#assignStat}.
	 * @param ctx the parse tree
	 */
	void exitAssignStat(RogueLangParser.AssignStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(RogueLangParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(RogueLangParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDecl(RogueLangParser.FunctionDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDecl(RogueLangParser.FunctionDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(RogueLangParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(RogueLangParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#list}.
	 * @param ctx the parse tree
	 */
	void enterList(RogueLangParser.ListContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#list}.
	 * @param ctx the parse tree
	 */
	void exitList(RogueLangParser.ListContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#listElement}.
	 * @param ctx the parse tree
	 */
	void enterListElement(RogueLangParser.ListElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#listElement}.
	 * @param ctx the parse tree
	 */
	void exitListElement(RogueLangParser.ListElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#listAccess}.
	 * @param ctx the parse tree
	 */
	void enterListAccess(RogueLangParser.ListAccessContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#listAccess}.
	 * @param ctx the parse tree
	 */
	void exitListAccess(RogueLangParser.ListAccessContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#listLength}.
	 * @param ctx the parse tree
	 */
	void enterListLength(RogueLangParser.ListLengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#listLength}.
	 * @param ctx the parse tree
	 */
	void exitListLength(RogueLangParser.ListLengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#listPop}.
	 * @param ctx the parse tree
	 */
	void enterListPop(RogueLangParser.ListPopContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#listPop}.
	 * @param ctx the parse tree
	 */
	void exitListPop(RogueLangParser.ListPopContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#struct}.
	 * @param ctx the parse tree
	 */
	void enterStruct(RogueLangParser.StructContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#struct}.
	 * @param ctx the parse tree
	 */
	void exitStruct(RogueLangParser.StructContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#structDef}.
	 * @param ctx the parse tree
	 */
	void enterStructDef(RogueLangParser.StructDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#structDef}.
	 * @param ctx the parse tree
	 */
	void exitStructDef(RogueLangParser.StructDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#structField}.
	 * @param ctx the parse tree
	 */
	void enterStructField(RogueLangParser.StructFieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#structField}.
	 * @param ctx the parse tree
	 */
	void exitStructField(RogueLangParser.StructFieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#structFieldAccess}.
	 * @param ctx the parse tree
	 */
	void enterStructFieldAccess(RogueLangParser.StructFieldAccessContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#structFieldAccess}.
	 * @param ctx the parse tree
	 */
	void exitStructFieldAccess(RogueLangParser.StructFieldAccessContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#plusEquals}.
	 * @param ctx the parse tree
	 */
	void enterPlusEquals(RogueLangParser.PlusEqualsContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#plusEquals}.
	 * @param ctx the parse tree
	 */
	void exitPlusEquals(RogueLangParser.PlusEqualsContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#minusEquals}.
	 * @param ctx the parse tree
	 */
	void enterMinusEquals(RogueLangParser.MinusEqualsContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#minusEquals}.
	 * @param ctx the parse tree
	 */
	void exitMinusEquals(RogueLangParser.MinusEqualsContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#printStat}.
	 * @param ctx the parse tree
	 */
	void enterPrintStat(RogueLangParser.PrintStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#printStat}.
	 * @param ctx the parse tree
	 */
	void exitPrintStat(RogueLangParser.PrintStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#ifStat}.
	 * @param ctx the parse tree
	 */
	void enterIfStat(RogueLangParser.IfStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#ifStat}.
	 * @param ctx the parse tree
	 */
	void exitIfStat(RogueLangParser.IfStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#elifStat}.
	 * @param ctx the parse tree
	 */
	void enterElifStat(RogueLangParser.ElifStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#elifStat}.
	 * @param ctx the parse tree
	 */
	void exitElifStat(RogueLangParser.ElifStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#elseStat}.
	 * @param ctx the parse tree
	 */
	void enterElseStat(RogueLangParser.ElseStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#elseStat}.
	 * @param ctx the parse tree
	 */
	void exitElseStat(RogueLangParser.ElseStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#statBlock}.
	 * @param ctx the parse tree
	 */
	void enterStatBlock(RogueLangParser.StatBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#statBlock}.
	 * @param ctx the parse tree
	 */
	void exitStatBlock(RogueLangParser.StatBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#forLoop}.
	 * @param ctx the parse tree
	 */
	void enterForLoop(RogueLangParser.ForLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#forLoop}.
	 * @param ctx the parse tree
	 */
	void exitForLoop(RogueLangParser.ForLoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void enterWhileLoop(RogueLangParser.WhileLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void exitWhileLoop(RogueLangParser.WhileLoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#returnStat}.
	 * @param ctx the parse tree
	 */
	void enterReturnStat(RogueLangParser.ReturnStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#returnStat}.
	 * @param ctx the parse tree
	 */
	void exitReturnStat(RogueLangParser.ReturnStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#whiteNoiseStat}.
	 * @param ctx the parse tree
	 */
	void enterWhiteNoiseStat(RogueLangParser.WhiteNoiseStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#whiteNoiseStat}.
	 * @param ctx the parse tree
	 */
	void exitWhiteNoiseStat(RogueLangParser.WhiteNoiseStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#random}.
	 * @param ctx the parse tree
	 */
	void enterRandom(RogueLangParser.RandomContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#random}.
	 * @param ctx the parse tree
	 */
	void exitRandom(RogueLangParser.RandomContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#range}.
	 * @param ctx the parse tree
	 */
	void enterRange(RogueLangParser.RangeContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#range}.
	 * @param ctx the parse tree
	 */
	void exitRange(RogueLangParser.RangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#params}.
	 * @param ctx the parse tree
	 */
	void enterParams(RogueLangParser.ParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#params}.
	 * @param ctx the parse tree
	 */
	void exitParams(RogueLangParser.ParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#args}.
	 * @param ctx the parse tree
	 */
	void enterArgs(RogueLangParser.ArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#args}.
	 * @param ctx the parse tree
	 */
	void exitArgs(RogueLangParser.ArgsContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(RogueLangParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(RogueLangParser.ExprContext ctx);
}