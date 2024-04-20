import json

from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangLexer import RogueLangLexer
from antlr4 import *

from modules.Interpreter.Interpreter import Interpreter


def setup_parser(str):
    lexer = RogueLangLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    parser = RogueLangParser(stream)
    return parser


def test_json_dumps():
    code = '''Map {
    procedure {
    x = 3
    }
    field x = 5
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 3.0})


def test_function_decl_and_call():
    code = '''Map {
    procedure {
    x = setTo3()
    }
    field x = 5
    def setTo3() {
    return 3
    }
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 3.0})


def test_arithmetic():
    code = '''Map {
    procedure {x = x - 1}
    field x = 5
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 4.0})


def test_nested_if_stat():
    code = '''Map {
    procedure {
    if(x == 5){
    x = 4
    if(x == 4){
    x = 3
    }
    }
    }
    field x = 5
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 3.0})


def test_elif_stat():
    code = '''Map {
    procedure {
    if(x == 5){
    x = 1
    }
    elif(x == 1){
    x = 3
    }
    elif(x == 4){
    x = 2
    }
    }
    field x = 4
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 2.0})


def test_else_stat():
    code = '''Map {
    procedure {
    if(x == 5){
    x = 1
    }
    else{
    x = 3
    }
    }
    field x = 4
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 3.0})


def test_while_loop():
    code = '''Map {
    procedure {
    while(x > 0){
    x = x - 1
    }
    }
    field x = 5
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 0.0})


def test_nested_function_call():
    code = '''Map {
    procedure {
    x = setToX(setTo3())
    }
    field x = 5
    def setToX(x){
    return x
    }
    def setTo3() {
    return 3
    }
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 3.0})


def test_list():
    code = '''Map {
    procedure {
    let y = 5
    }
    field x = [3, 2, 1]
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": [3.0, 2.0, 1.0]})


def test_list_add():
    code = '''Map {
    procedure {
    x += 4
    }
    field x = [1, 2, 3]
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": [1.0, 2.0, 3.0, 4.0]})


def test_list_element():
    code = '''Map {
    procedure {
    let y = [3, 3]
    x = y[0]
    }
    field x = 1
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 3.0})


def test_list_element_variable_index():
    code = '''Map {
    procedure {
    let y = [3, 3]
    let n = 0
    x = y[n]
    }
    field x = 1
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 3.0})


def test_for_loop():
    code = '''Map {
    procedure {
    let y = [3, 3]
    for i in y{
    x = x + i
    }
    }
    field x = 1
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 7.0})


def test_comparisons():
    code = '''Map {
    procedure {
    x = 1
    let y = 1
    x = (x > 7) or (y > 8)
    }
    field x = True
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": False})

def test_function_as_parameter():
    code = '''Map {
    procedure {
    def animalSays(say){
    return say()
    }
    x = animalSays(catSays)
    }
    field x
    }
    def catSays(){
    return "meow"
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": "meow"})

def test_list_length():
    code = '''Map {
    procedure {
    x = len(x)
    }
    field x = [1, 2, 3]
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": 3})

def test_minus_equals():
    code = '''Map {
    procedure {
    x -= 3
    }
    field x = [1, 2, 3]
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": [1.0, 2.0]})

def test_list_pop():
    code = '''Map {
    procedure {
    x.pop()
    }
    field x = [1, 2, 3]
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    assert output == json.dumps({"x": [1.0, 2.0]})

def test_random_range():
    code = '''Map {
    procedure {
    x = random in 2..4
    }
    field x = 1
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    print(output)

    assert json.loads(output) == {'x': 2.0} or {'x': 3.0} or {'x': 4.0}

def test_random_choice():
    code = '''Map {
    procedure {
    let y = [2, 3, 4]
    x = random in y
    }
    field x = 1
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    print(output)

    assert json.loads(output) == {'x': 2.0} or {'x': 3.0} or {'x': 4.0}
