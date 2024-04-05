#   test_parser.py
from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangLexer import RogueLangLexer
from antlr4 import *


def setup_parser(str):
    lexer = RogueLangLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    parser = RogueLangParser(stream)
    return parser

def test_print_stat():
    # string we want to test
    test = 'print ("Hello World!")'
    # parses abstract syntax tree for the specific test
    # print("\n", tree.toStringTree(tree, RogueLangParser))
    # the print statement above can be used to visualize how the tree looks
    parser = setup_parser(test)
    # as we only want the relevant part of the tree, we put that into the tree variable
    tree = parser.printStat()
    # the following lines check if the tree and its nodes fit the specific rules defined in the grammar file
    assert (tree.getRuleIndex() == RogueLangParser.RULE_printStat)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.PRINT
    assert tree.getChild(1).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == RogueLangParser.CLOSED_PARENTH

def test_var_decl():
    test = 'variable = 3'
    parser = setup_parser(test)
    tree = parser.varDecl()

    print(tree.toStringTree(tree, RogueLangParser))

    assert (tree.getRuleIndex() == RogueLangParser.RULE_varDecl)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.ID
    assert tree.getChild(1).getSymbol().type == RogueLangParser.EQUAL_SIGN
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_expr

def test_if_stat():
    test = 'if (19 == 21){print("u stupid")} else{print("no im not")}'
    parser = setup_parser(test)
    tree = parser.ifStat()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_ifStat)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.IF
    assert tree.getChild(1).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_ifExpr
    assert tree.getChild(3).getSymbol().type == RogueLangParser.CLOSED_PARENTH
    assert tree.getChild(4).getSymbol().type == RogueLangParser.OPEN_CURL
    assert tree.getChild(5).getRuleIndex() == RogueLangParser.RULE_ifBlock
    assert tree.getChild(6).getSymbol().type == RogueLangParser.CLOSED_CURL
    assert tree.getChild(7).getSymbol().type == RogueLangParser.ELSE
    assert tree.getChild(8).getSymbol().type == RogueLangParser.OPEN_CURL
    assert tree.getChild(9).getRuleIndex() == RogueLangParser.RULE_elseBlock
    assert tree.getChild(10).getSymbol().type == RogueLangParser.CLOSED_CURL

def test_for_loop():
    code = 'for int i in x {print(i)}'
    parser = setup_parser(code)
    tree = parser.forLoop()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_forLoop)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.FOR
    assert tree.getChild(1).getRuleIndex() == RogueLangParser.RULE_varDecl
    assert tree.getChild(2).getSymbol().type == RogueLangParser.IN
    assert tree.getChild(3).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(4).getSymbol().type == RogueLangParser.OPEN_CURL
    assert tree.getChild(5).getRuleIndex() == RogueLangParser.RULE_stat
    assert tree.getChild(6).getSymbol().type == RogueLangParser.CLOSED_CURL

def test_while_loop():
    code = 'while (true){print("true")}'
    parser = setup_parser(code)
    tree = parser.whileLoop()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_whileLoop)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.WHILE
    assert tree.getChild(1).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == RogueLangParser.CLOSED_PARENTH
    assert tree.getChild(4).getSymbol().type == RogueLangParser.OPEN_CURL
    assert tree.getChild(5).getRuleIndex() == RogueLangParser.RULE_stat
    assert tree.getChild(6).getSymbol().type == RogueLangParser.CLOSED_CURL

def test_function_decl():
    code = 'def printText(text) {print(text)}'
    parser = setup_parser(code)
    tree = parser.functionDecl()

    print(tree.toStringTree(tree, RogueLangParser))

    assert (tree.getRuleIndex() == RogueLangParser.RULE_functionDecl)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.DEF
    assert tree.getChild(1).getSymbol().type == RogueLangParser.ID
    assert tree.getChild(2).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(3).getRuleIndex() == RogueLangParser.RULE_params
    assert tree.getChild(4).getSymbol().type == RogueLangParser.CLOSED_PARENTH
    assert tree.getChild(5).getSymbol().type == RogueLangParser.OPEN_CURL
    assert tree.getChild(6).getRuleIndex() == RogueLangParser.RULE_stat
    assert tree.getChild(7).getSymbol().type == RogueLangParser.CLOSED_CURL

def test_function_call():
    code = 'readFile(path)'
    parser = setup_parser(code)
    tree = parser.functionCall()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_functionCall)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.ID
    assert tree.getChild(1).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_args
    assert tree.getChild(3).getSymbol().type == RogueLangParser.CLOSED_PARENTH

def test_array_init():
    code = '{1, 2, 3}'
    parser = setup_parser(code)
    tree = parser.arrayInit()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_arrayInit)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.OPEN_CURL
    assert tree.getChild(1).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(2).getSymbol().type == RogueLangParser.COMMA
    assert tree.getChild(3).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(4).getSymbol().type == RogueLangParser.COMMA
    assert tree.getChild(5).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(6).getSymbol().type == RogueLangParser.CLOSED_CURL

def test_bsp():
    code = 'BSP 2D (10, 10, 2)'
    parser = setup_parser(code)
    tree = parser.bsp()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_bsp)
    assert tree.getChild(0).getText() == 'BSP'
    assert tree.getChild(1).getRuleIndex() == RogueLangParser.RULE_bspDimension
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_bspParameters

def test_randomNumber():
    code = 'randomNumber(1, 10)'
    parser = setup_parser(code)
    tree = parser.randomNumber()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_randomNumber)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.RANDOM_NUMBER
    assert tree.getChild(1).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(2).getSymbol().type == RogueLangParser.NUMBER
    assert tree.getChild(3).getSymbol().type == RogueLangParser.COMMA
    assert tree.getChild(4).getSymbol().type == RogueLangParser.NUMBER
    assert tree.getChild(5).getSymbol().type == RogueLangParser.CLOSED_PARENTH

def test_random_choice():
    code = 'randomChoice(1, 2)'
    parser = setup_parser(code)
    tree = parser.randomChoice()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_randomChoice)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.RANDOM_CHOICE
    assert tree.getChild(1).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == RogueLangParser.COMMA
    assert tree.getChild(4).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(5).getSymbol().type == RogueLangParser.CLOSED_PARENTH

def test_enum_decl():
    code = 'enum my_enum {type_1, type_2}'
    parser = setup_parser(code)
    tree = parser.enumDecl()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_enumDecl)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.ENUM
    assert tree.getChild(1).getSymbol().type == RogueLangParser.ID
    assert tree.getChild(2).getSymbol().type == RogueLangParser.OPEN_CURL
    assert tree.getChild(3).getRuleIndex() == RogueLangParser.RULE_enumBody
    assert tree.getChild(4).getSymbol().type == RogueLangParser.CLOSED_CURL

def test_enum_value():
    code = 'my_enum.type_1'
    parser = setup_parser(code)
    tree = parser.enumValue()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_enumValue)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.ID
    assert tree.getChild(1).getSymbol().type == RogueLangParser.DOT
    assert tree.getChild(2).getSymbol().type == RogueLangParser.ID
