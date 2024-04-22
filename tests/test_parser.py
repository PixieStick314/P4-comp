#   test_parser.py
from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangLexer import RogueLangLexer
from antlr4 import *


def setup_parser(str):
    lexer = RogueLangLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    parser = RogueLangParser(stream)
    return parser


def test_ambiguity_print_stat():
    test = 'print ("Hello World!")'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == RogueLangParser.RULE_printStat


def test_ambiguity_var_decl():
    test = 'let var = 5'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == RogueLangParser.RULE_varDeclStat


def test_ambiguity_function_decl():
    test = 'def function(){print("Hello World!")}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == RogueLangParser.RULE_functionDecl


def test_ambiguity_if_stat():
    test = 'if(True) {print("Hello World!")}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == RogueLangParser.RULE_ifStat


def test_ambiguity_for_loop():
    test = 'for i in x {print(i)}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == RogueLangParser.RULE_forLoop


def test_ambiguity_while_loop():
    test = 'while (x) {print(x)}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == RogueLangParser.RULE_whileLoop


def test_ambiguity_stat_block():
    test = '{print("Hello World!")}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == RogueLangParser.RULE_statBlock


def test_ambiguity_return_stat():
    test = 'return x'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == RogueLangParser.RULE_returnStat


def test_ambiguity_expr():
    test = 'function()'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == RogueLangParser.RULE_expr


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
    test = 'let variable = 3'
    parser = setup_parser(test)
    tree = parser.varDecl()

    print(tree.toStringTree(tree, RogueLangParser))

    assert (tree.getRuleIndex() == RogueLangParser.RULE_varDecl)
    assert tree.getChild(0).getText() == 'let'
    assert tree.getChild(1).getSymbol().type == RogueLangParser.ID
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_assignment


def test_if_stat():
    test = 'if (19 == 21){print("u stupid")} else{print("no im not")}'
    parser = setup_parser(test)
    tree = parser.ifStat()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_ifStat)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.IF
    assert tree.getChild(1).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == RogueLangParser.CLOSED_PARENTH
    assert tree.getChild(4).getRuleIndex() == RogueLangParser.RULE_statBlock
    assert tree.getChild(5).getRuleIndex() == RogueLangParser.RULE_elseStat


def test_for_loop():
    code = 'for i in x {print(i)}'
    parser = setup_parser(code)
    tree = parser.forLoop()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_forLoop)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.FOR
    assert tree.getChild(1).getSymbol().type == RogueLangParser.ID
    assert tree.getChild(2).getSymbol().type == RogueLangParser.IN
    assert tree.getChild(3).getSymbol().type == RogueLangParser.ID
    assert tree.getChild(4).getRuleIndex() == RogueLangParser.RULE_statBlock


def test_while_loop():
    code = 'while (true){print("true")}'
    parser = setup_parser(code)
    tree = parser.whileLoop()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_whileLoop)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.WHILE
    assert tree.getChild(1).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == RogueLangParser.CLOSED_PARENTH
    assert tree.getChild(4).getRuleIndex() == RogueLangParser.RULE_statBlock


def test_list_pop():
    code = 'x.pop(0)'
    parser = setup_parser(code)
    tree = parser.listPop()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_listPop)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.ID
    assert tree.getChild(1).getSymbol().type == RogueLangParser.DOT
    assert tree.getChild(2).getSymbol().type == RogueLangParser.POP
    assert tree.getChild(3).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(4).getSymbol().type == RogueLangParser.NUMBER
    assert tree.getChild(5).getSymbol().type == RogueLangParser.CLOSED_PARENTH


def test_function_decl():
    code = 'def add(x, y) {return x + y}'
    parser = setup_parser(code)
    tree = parser.functionDecl()

    print(tree.toStringTree(tree, RogueLangParser))

    assert (tree.getRuleIndex() == RogueLangParser.RULE_functionDecl)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.DEF
    assert tree.getChild(1).getSymbol().type == RogueLangParser.ID
    assert tree.getChild(2).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(3).getRuleIndex() == RogueLangParser.RULE_params
    assert tree.getChild(4).getSymbol().type == RogueLangParser.CLOSED_PARENTH
    assert tree.getChild(5).getRuleIndex() == RogueLangParser.RULE_statBlock


def test_function_call():
    code = 'readFile(path)'
    parser = setup_parser(code)
    tree = parser.functionCall()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_functionCall)
    assert tree.getChild(0).getSymbol().type == RogueLangParser.ID
    assert tree.getChild(1).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_args
    assert tree.getChild(3).getSymbol().type == RogueLangParser.CLOSED_PARENTH


def test_nested_if_stat():
    test = '''
    if (19 == 21) {
        if (19 == 21) {
            print("u stupid")
            }
        }'''
    parser = setup_parser(test)
    tree = parser.ifStat()

    assert tree.getRuleIndex() == RogueLangParser.RULE_ifStat
    assert tree.getChild(0).getSymbol().type == RogueLangParser.IF
    assert tree.getChild(1).getSymbol().type == RogueLangParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == RogueLangParser.CLOSED_PARENTH
    assert tree.getChild(4).stat()[0].ifStat() is not None

def test_string():
    code = 'let cat = "meow"'
    parser = setup_parser(code)
    tree = parser.varDeclStat()

    assert tree.getChild(0).getText() == 'let'
    assert tree.getChild(1).assignment().expr().getText() == '"meow"'
