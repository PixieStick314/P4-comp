from src.grammar_files.generated.RogueLangParser import RogueLangParser
from src.grammar_files.generated.RogueLangLexer import RogueLangLexer
from antlr4 import *


def setup_parser(str):
    lexer = RogueLangLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    parser = RogueLangParser(stream)
    return parser

def test_print_stat():
    test = 'print ("Hello World!");'
    parser = setup_parser(test)
    tree = parser.printStat()

    # print("\n", tree.toStringTree(tree, RogueLangParser))

    assert (tree.getRuleIndex() == RogueLangParser.RULE_printStat)
    assert tree.getChild(0).getText() == 'print'
    assert tree.getChild(1).getText() == '('
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(3).getText() == ')'
    assert tree.getChild(4).getText() == ';'

def test_int_decl():
    test = 'var variable = 3;'
    parser = setup_parser(test)
    tree = parser.varDecl()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_varDecl)
    assert tree.getChild(0).getText() == 'var'
    assert tree.getChild(1).getRuleIndex() == RogueLangParser.RULE_dataType
    # assert tree.getChild(2).getRuleIndex() == shit idk man
    assert tree.getChild(3).getText() == '='
    assert tree.getChild(4).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(5).getText() == ';'

def test_if_stat():
    test = 'if (19 == 21){print("u stupid");} else{print("no im not");};'
    parser = setup_parser(test)
    tree = parser.ifStat()

    assert (tree.getRuleIndex() == RogueLangParser.RULE_ifStat)
    assert tree.getChild(0).getText() == 'if'
    assert tree.getChild(1).getText() == '('
    assert tree.getChild(2).getRuleIndex() == RogueLangParser.RULE_expr
    assert tree.getChild(3).getText() == ')'
    assert tree.getChild(4).getText() == '{'
    assert tree.getChild(5).getRuleIndex() == RogueLangParser.RULE_stat
    assert tree.getChild(6).getText() == '}'
    assert tree.getChild(7).getText() == 'else'
    assert tree.getChild(8).getText() == '{'
    assert tree.getChild(9).getRuleIndex() == RogueLangParser.RULE_stat
    assert tree.getChild(10).getText() == '}'
    assert tree.getChild(11).getText() == ';'