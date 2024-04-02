// Generated from c:/Users/Lenovo/Documents/GitHub/P4-comp/src/grammar_files/RogueLang.g4 by ANTLR 4.13.1
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
	 * Enter a parse tree produced by {@link RogueLangParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterDataType(RogueLangParser.DataTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitDataType(RogueLangParser.DataTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#baseType}.
	 * @param ctx the parse tree
	 */
	void enterBaseType(RogueLangParser.BaseTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#baseType}.
	 * @param ctx the parse tree
	 */
	void exitBaseType(RogueLangParser.BaseTypeContext ctx);
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
	 * Enter a parse tree produced by {@link RogueLangParser#ifExpr}.
	 * @param ctx the parse tree
	 */
	void enterIfExpr(RogueLangParser.IfExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#ifExpr}.
	 * @param ctx the parse tree
	 */
	void exitIfExpr(RogueLangParser.IfExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#ifBlock}.
	 * @param ctx the parse tree
	 */
	void enterIfBlock(RogueLangParser.IfBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#ifBlock}.
	 * @param ctx the parse tree
	 */
	void exitIfBlock(RogueLangParser.IfBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#elifExpr}.
	 * @param ctx the parse tree
	 */
	void enterElifExpr(RogueLangParser.ElifExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#elifExpr}.
	 * @param ctx the parse tree
	 */
	void exitElifExpr(RogueLangParser.ElifExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#elifBlock}.
	 * @param ctx the parse tree
	 */
	void enterElifBlock(RogueLangParser.ElifBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#elifBlock}.
	 * @param ctx the parse tree
	 */
	void exitElifBlock(RogueLangParser.ElifBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#elseBlock}.
	 * @param ctx the parse tree
	 */
	void enterElseBlock(RogueLangParser.ElseBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#elseBlock}.
	 * @param ctx the parse tree
	 */
	void exitElseBlock(RogueLangParser.ElseBlockContext ctx);
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
	 * Enter a parse tree produced by {@link RogueLangParser#arrayInit}.
	 * @param ctx the parse tree
	 */
	void enterArrayInit(RogueLangParser.ArrayInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#arrayInit}.
	 * @param ctx the parse tree
	 */
	void exitArrayInit(RogueLangParser.ArrayInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#bsp}.
	 * @param ctx the parse tree
	 */
	void enterBsp(RogueLangParser.BspContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#bsp}.
	 * @param ctx the parse tree
	 */
	void exitBsp(RogueLangParser.BspContext ctx);
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
	 * Enter a parse tree produced by {@link RogueLangParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(RogueLangParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(RogueLangParser.ParamContext ctx);
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
	 * Enter a parse tree produced by {@link RogueLangParser#randomNumber}.
	 * @param ctx the parse tree
	 */
	void enterRandomNumber(RogueLangParser.RandomNumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#randomNumber}.
	 * @param ctx the parse tree
	 */
	void exitRandomNumber(RogueLangParser.RandomNumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#randomChoice}.
	 * @param ctx the parse tree
	 */
	void enterRandomChoice(RogueLangParser.RandomChoiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#randomChoice}.
	 * @param ctx the parse tree
	 */
	void exitRandomChoice(RogueLangParser.RandomChoiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#enumDecl}.
	 * @param ctx the parse tree
	 */
	void enterEnumDecl(RogueLangParser.EnumDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#enumDecl}.
	 * @param ctx the parse tree
	 */
	void exitEnumDecl(RogueLangParser.EnumDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#enumBody}.
	 * @param ctx the parse tree
	 */
	void enterEnumBody(RogueLangParser.EnumBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#enumBody}.
	 * @param ctx the parse tree
	 */
	void exitEnumBody(RogueLangParser.EnumBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#enumValue}.
	 * @param ctx the parse tree
	 */
	void enterEnumValue(RogueLangParser.EnumValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#enumValue}.
	 * @param ctx the parse tree
	 */
	void exitEnumValue(RogueLangParser.EnumValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#bspDimension}.
	 * @param ctx the parse tree
	 */
	void enterBspDimension(RogueLangParser.BspDimensionContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#bspDimension}.
	 * @param ctx the parse tree
	 */
	void exitBspDimension(RogueLangParser.BspDimensionContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#bspParameters}.
	 * @param ctx the parse tree
	 */
	void enterBspParameters(RogueLangParser.BspParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#bspParameters}.
	 * @param ctx the parse tree
	 */
	void exitBspParameters(RogueLangParser.BspParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#dimensionList}.
	 * @param ctx the parse tree
	 */
	void enterDimensionList(RogueLangParser.DimensionListContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#dimensionList}.
	 * @param ctx the parse tree
	 */
	void exitDimensionList(RogueLangParser.DimensionListContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#minSize}.
	 * @param ctx the parse tree
	 */
	void enterMinSize(RogueLangParser.MinSizeContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#minSize}.
	 * @param ctx the parse tree
	 */
	void exitMinSize(RogueLangParser.MinSizeContext ctx);
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
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#openParenth}.
	 * @param ctx the parse tree
	 */
	void enterOpenParenth(RogueLangParser.OpenParenthContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#openParenth}.
	 * @param ctx the parse tree
	 */
	void exitOpenParenth(RogueLangParser.OpenParenthContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#closedParenth}.
	 * @param ctx the parse tree
	 */
	void enterClosedParenth(RogueLangParser.ClosedParenthContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#closedParenth}.
	 * @param ctx the parse tree
	 */
	void exitClosedParenth(RogueLangParser.ClosedParenthContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#openBrack}.
	 * @param ctx the parse tree
	 */
	void enterOpenBrack(RogueLangParser.OpenBrackContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#openBrack}.
	 * @param ctx the parse tree
	 */
	void exitOpenBrack(RogueLangParser.OpenBrackContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#closedBrack}.
	 * @param ctx the parse tree
	 */
	void enterClosedBrack(RogueLangParser.ClosedBrackContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#closedBrack}.
	 * @param ctx the parse tree
	 */
	void exitClosedBrack(RogueLangParser.ClosedBrackContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#openCurlBrack}.
	 * @param ctx the parse tree
	 */
	void enterOpenCurlBrack(RogueLangParser.OpenCurlBrackContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#openCurlBrack}.
	 * @param ctx the parse tree
	 */
	void exitOpenCurlBrack(RogueLangParser.OpenCurlBrackContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#closedCurlBrack}.
	 * @param ctx the parse tree
	 */
	void enterClosedCurlBrack(RogueLangParser.ClosedCurlBrackContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#closedCurlBrack}.
	 * @param ctx the parse tree
	 */
	void exitClosedCurlBrack(RogueLangParser.ClosedCurlBrackContext ctx);
	/**
	 * Enter a parse tree produced by {@link RogueLangParser#comma}.
	 * @param ctx the parse tree
	 */
	void enterComma(RogueLangParser.CommaContext ctx);
	/**
	 * Exit a parse tree produced by {@link RogueLangParser#comma}.
	 * @param ctx the parse tree
	 */
	void exitComma(RogueLangParser.CommaContext ctx);
}