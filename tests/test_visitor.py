from ExecutorHelper import get_visitor
from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangLexer import RogueLangLexer
from antlr4 import *

from modules.Interpreter.Visitor import Visitor


def setup_parser(str):
    lexer = RogueLangLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    parser = RogueLangParser(stream)
    return parser

def get_output(tree):
    suffix, visitor = get_visitor("python")
    output = visitor.visit(tree)
    return output

def test_print_stat():
    test = 'print ("Hello World!")'
    parser = setup_parser(test)
    tree = parser.printStat()
    output = get_output(tree)

    assert output == 'print("Hello World!")'

def test_var_decl():
    test = 'variable = 3'
    parser = setup_parser(test)
    tree = parser.varDecl()
    output = get_output(tree)

    assert output == 'variable = 3'

def test_if_stat():
    test = 'if (19 == 21){print("u stupid")} else{print("no im not")}'
    parser = setup_parser(test)
    tree = parser.ifStat()
    output = get_output(tree)

    assert output == 'if 19 == 21:\n    print("u stupid")\nelse:\n    print("no im not")'

def test_for_loop():
    code = 'for int i in x {print(i)}'
    parser = setup_parser(code)
    tree = parser.forLoop()
    output = get_output(tree)

    assert output == 'for int i in x {print(i)}'
def test_while_loop():
    code = 'while (true){print("true")}'
    parser = setup_parser(code)
    tree = parser.whileLoop()
    output = get_output(tree)

    assert output == 'while true:\n    print("true")'

def test_function_decl():
    code = 'def printText(text) {print(text)}'
    parser = setup_parser(code)
    tree = parser.functionDecl()
    output = get_output(tree)

    assert output == 'def printText(text):\n    print(text)\n'

def test_function_call():
    code = 'readFile(path)'
    parser = setup_parser(code)
    tree = parser.functionCall()
    output = get_output(tree)

    assert output == 'readFile(path)'

def test_array_init():
    code = '[1, 2, 3]'
    parser = setup_parser(code)
    tree = parser.arrayInit()
    output = get_output(tree)

    assert output == '[1, 2, 3]'

def test_jsonify():
    code = '''Map {
    procedure {
    }
    field x = 5
    }
    '''
    parser = setup_parser(code)
    tree = parser.object_()
    visitor = Visitor()
    output = visitor.visit(tree)
    print(output)
