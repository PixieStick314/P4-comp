# test_interpreter.py
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

def run_test_prog(code, expected_output):
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)
    assert output == json.dumps(expected_output)

def test_json_dumps():
    code = '''Map {
    procedure {
    x = 3
    }
    field x = 5
    }
    '''
    run_test_prog(code, {"x": 3})

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
    run_test_prog(code, {"x": 3})

def test_arithmetic():
    code = '''Map {
    procedure {x = x - 1}
    field x = 5
    }
    '''
    run_test_prog(code, {"x": 4})

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
    run_test_prog(code, {"x": 3})

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
    run_test_prog(code, {"x": 2})

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
    run_test_prog(code, {"x": 3})

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
    run_test_prog(code, {"x": 0})

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
    run_test_prog(code, {"x": 3})

def test_list():
    code = '''Map {
    procedure {
    let y = 5
    }
    field x = [3, 2, 1]
    }
    '''
    run_test_prog(code, {"x": [3, 2, 1]})

def test_list_add():
    code = '''Map {
    procedure {
    x += 4
    }
    field x = [1, 2, 3]
    }
    '''
    run_test_prog(code, {"x": [1, 2, 3, 4]})

def test_list_element():
    code = '''Map {
    procedure {
    let y = [3, 3]
    x = y[0]
    }
    field x = 1
    }
    '''
    run_test_prog(code, {"x": 3})

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
    run_test_prog(code, {"x": 3})

def test_list_pop():
    code = '''Map {
    procedure {
    x.pop()
    }
    field x = [1, 2, 3, 4]
    }
    '''
    run_test_prog(code, {"x": [1, 2, 3]})

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
    run_test_prog(code, {"x": 7})

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
    run_test_prog(code, {"x": False})

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
    run_test_prog(code, {"x": "meow"})

def test_list_length():
    code = '''Map {
    procedure {
    x = len(x)
    }
    field x = [1, 2, 3]
    }
    '''
    run_test_prog(code, {"x": 3})

def test_minus_equals():
    code = '''Map {
    procedure {
    x -= 3
    }
    field x = [1, 2, 3]
    }
    '''
    run_test_prog(code, {"x": [1, 2]})

def test_list_pop():
    code = '''Map {
    procedure {
    x.pop()
    }
    field x = [1, 2, 3]
    }
    '''
    run_test_prog(code, {"x": [1, 2]})

def test_basic_2d_array():
    code = '''
    Map {
        procedure {
            myArray = [
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ]
        }
        field myArray
    }
    '''
    expected_output = {
        "myArray": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    }
    run_test_prog(code, expected_output)

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

    assert json.loads(output) == {'x': 2} or {'x': 3} or {'x': 4}

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

    assert json.loads(output) == {'x': 2} or {'x': 3} or {'x': 4}

def test_nested_list():
    code = '''Map {
    procedure {
    x = [[1, 2] , [3, 4]]
    }
    field x
    }
    '''

    run_test_prog(code, {'x': [[1, 2], [3, 4]]})

def test_nested_list_access():
    code = '''Map {
    procedure {
    let y = [[1, 2] , [3, 4]]
    x = y[1][1]
    }
    field x
    }
    '''

    run_test_prog(code, {'x': 4})

def test_nested_list_assign():
    code = '''Map {
    procedure {
    x = [[1, 2] , [3, 4]]
    x[1][1] = 1
    }
    field x
    }
    '''

    run_test_prog(code, {'x': [[1, 2], [3, 1]]})

def test_whiteNoise():
    code = '''
    Map {
        procedure {
            myArray = [
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ]
            WhiteNoise(myArray, 0..1)
        }
        field myArray
    }
    '''

    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    try:
        deserialized_output = json.loads(output)
    except json.JSONDecodeError:
        raise ValueError("Output could not be deserialized from JSON")

    assert "myArray" in deserialized_output, "Expected 'myArray' in the output"
    
    myArray = deserialized_output["myArray"]

    assert isinstance(myArray, list), "Expected 'myArray' to be a list"
    
    for row in myArray:
        assert isinstance(row, list), "Each row should be a list"
        
        for value in row:
            assert value in (0, 1), f"Value {value} is not 0 or 1"