#   test_parser.py
from grammar_files.generated.DungeonParser import DungeonParser
from grammar_files.generated.DungeonLexer import DungeonLexer
from antlr4 import *


def setup_parser(str):
    lexer = DungeonLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    parser = DungeonParser(stream)
    return parser


def test_ambiguity_print_stat():
    test = 'print ("Hello World!")'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_printStat


def test_ambiguity_var_decl():
    test = 'let var = 5'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_varDeclStat


def test_ambiguity_function_decl():
    test = 'def function(){print("Hello World!")}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_functionDecl


def test_ambiguity_if_stat():
    test = 'if(True) {print("Hello World!")}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_ifStat


def test_ambiguity_for_loop():
    test = 'for i in x {print(i)}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_forLoop


def test_ambiguity_while_loop():
    test = 'while (x) {print(x)}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_whileLoop


def test_ambiguity_stat_block():
    test = '{print("Hello World!")}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_statBlock


def test_ambiguity_return_stat():
    test = 'return x'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_returnStat


def test_ambiguity_expr():
    test = 'function()'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr


def test_print_stat():
    # string we want to test
    test = 'print ("Hello World!")'
    # parses abstract syntax tree for the specific test
    # print("\n", tree.toStringTree(tree, DungeonParser))
    # the print statement above can be used to visualize how the tree looks
    parser = setup_parser(test)
    # as we only want the relevant part of the tree, we put that into the tree variable
    tree = parser.printStat()
    # the following lines check if the tree and its nodes fit the specific rules defined in the grammar file
    assert (tree.getRuleIndex() == DungeonParser.RULE_printStat)
    assert tree.getChild(0).getSymbol().type == DungeonParser.PRINT
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH


def test_var_decl():
    test = 'let variable = 3'
    parser = setup_parser(test)
    tree = parser.varDecl()

    print(tree.toStringTree(tree, DungeonParser))

    assert (tree.getRuleIndex() == DungeonParser.RULE_varDecl)
    assert tree.getChild(0).getText() == 'let'
    assert tree.getChild(1).getSymbol().type == DungeonParser.ID
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_assignment


def test_if_stat():
    test = 'if (19 == 21){print("u stupid")} else{print("no im not")}'
    parser = setup_parser(test)
    tree = parser.ifStat()

    assert (tree.getRuleIndex() == DungeonParser.RULE_ifStat)
    assert tree.getChild(0).getSymbol().type == DungeonParser.IF
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH
    assert tree.getChild(4).getRuleIndex() == DungeonParser.RULE_statBlock
    assert tree.getChild(5).getRuleIndex() == DungeonParser.RULE_elseStat


def test_for_loop():
    code = 'for i in x {print(i)}'
    parser = setup_parser(code)
    tree = parser.forLoop()

    assert (tree.getRuleIndex() == DungeonParser.RULE_forLoop)
    assert tree.getChild(0).getSymbol().type == DungeonParser.FOR
    assert tree.getChild(1).getSymbol().type == DungeonParser.ID
    assert tree.getChild(2).getSymbol().type == DungeonParser.IN
    assert tree.getChild(3).getSymbol().type == DungeonParser.ID
    assert tree.getChild(4).getRuleIndex() == DungeonParser.RULE_statBlock


def test_while_loop():
    code = 'while (true){print("true")}'
    parser = setup_parser(code)
    tree = parser.whileLoop()

    assert (tree.getRuleIndex() == DungeonParser.RULE_whileLoop)
    assert tree.getChild(0).getSymbol().type == DungeonParser.WHILE
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH
    assert tree.getChild(4).getRuleIndex() == DungeonParser.RULE_statBlock


def test_list_pop():
    code = 'x.pop()'
    parser = setup_parser(code)
    tree = parser.listPop()

    assert (tree.getRuleIndex() == DungeonParser.RULE_listPop)
    assert tree.getChild(0).getSymbol().type == DungeonParser.ID
    assert tree.getChild(1).getSymbol().type == DungeonParser.DOT
    assert tree.getChild(2).getText() == 'pop'
    assert tree.getChild(3).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(4).getSymbol().type == DungeonParser.CLOSED_PARENTH


def test_function_decl():
    code = 'def add(x, y) {return x + y}'
    parser = setup_parser(code)
    tree = parser.functionDecl()

    print(tree.toStringTree(tree, DungeonParser))

    assert (tree.getRuleIndex() == DungeonParser.RULE_functionDecl)
    assert tree.getChild(0).getSymbol().type == DungeonParser.DEF
    assert tree.getChild(1).getSymbol().type == DungeonParser.ID
    assert tree.getChild(2).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(3).getRuleIndex() == DungeonParser.RULE_params
    assert tree.getChild(4).getSymbol().type == DungeonParser.CLOSED_PARENTH
    assert tree.getChild(5).getRuleIndex() == DungeonParser.RULE_statBlock


def test_function_call():
    code = 'readFile(path)'
    parser = setup_parser(code)
    tree = parser.functionCall()

    assert (tree.getRuleIndex() == DungeonParser.RULE_functionCall)
    assert tree.getChild(0).getSymbol().type == DungeonParser.ID
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_args
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH


def test_nested_if_stat():
    test = '''
    if (19 == 21) {
        if (19 == 21) {
            print("u stupid")
            }
        }'''
    parser = setup_parser(test)
    tree = parser.ifStat()

    assert tree.getRuleIndex() == DungeonParser.RULE_ifStat
    assert tree.getChild(0).getSymbol().type == DungeonParser.IF
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH
    assert tree.getChild(4).stat()[0].ifStat() is not None

def test_string():
    code = 'let cat = "meow"'
    parser = setup_parser(code)
    tree = parser.varDeclStat()

    assert tree.getChild(0).getText() == 'let'
    assert tree.getChild(1).assignment().expr().getText() == '"meow"'


def test_struct_assign():
    code = '= Cat {says = "meow"}'
    parser = setup_parser(code)
    tree = parser.assignment()

    assert tree.getChild(0).getSymbol().type == DungeonParser.EQUAL_SIGN
    assert tree.getChild(1).getRuleIndex() == DungeonParser.RULE_struct

def test_Sqrt_Op():
    code = 'sqrt(9)'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.SQRT
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr   
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH

def test_Sqrt_Op():
    code = 'pow(1,2)'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.POW
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(3).getSymbol().type == DungeonParser.COMMA
    assert tree.getChild(4).getRuleIndex() == DungeonParser.RULE_expr   
    assert tree.getChild(5).getSymbol().type == DungeonParser.CLOSED_PARENTH

def test_seed():
    code = 'seed(7)'
    parser = setup_parser(code)
    tree = parser.seed()

    assert tree.getChild(0).getSymbol().type == DungeonParser.SEED
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH
