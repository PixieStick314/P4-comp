# test_interpreter.py
import json
import pytest
from grammar_files.generated.DungeonParser import DungeonParser
from grammar_files.generated.DungeonLexer import DungeonLexer
from antlr4 import *

from modules.Interpreter.Interpreter import Interpreter

def setup_parser(str):
    lexer = DungeonLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    parser = DungeonParser(stream)
    return parser

def run_test_prog(code, expected_output):
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)
    assert output == json.dumps(expected_output)

def test_json_dumps():
    code = '''output map {
    procedure {
    x = 3
    }
    output x = 5
    }
    '''
    run_test_prog(code, {"x": 3})

def test_function_decl_and_call():
    code = '''output map {
    procedure {
    x = setTo3()
    }
    output x = 5
    def setTo3() {
    return 3
    }
    }
    '''
    run_test_prog(code, {"x": 3})

def test_arithmetic():
    code = '''output map {
    procedure {x = x - 1}
    output x = 5
    }
    '''
    run_test_prog(code, {"x": 4})

def test_nested_if_stat():
    code = '''output map {
    procedure {
    if(x == 5){
    x = 4
    if(x == 4){
    x = 3
    }
    }
    }
    output x = 5
    }
    '''
    run_test_prog(code, {"x": 3})

def test_elif_stat():
    code = '''output map {
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
    output x = 4
    }
    '''
    run_test_prog(code, {"x": 2})

def test_else_stat():
    code = '''output map {
    procedure {
    if(x == 5){
    x = 1
    }
    else{
    x = 3
    }
    }
    output x = 4
    }
    '''
    run_test_prog(code, {"x": 3})

def test_while_loop():
    code = '''output map {
    procedure {
    while(x > 0){
    x = x - 1
    }
    }
    output x = 5
    }
    '''
    run_test_prog(code, {"x": 0})

def test_nested_function_call():
    code = '''output map {
    procedure {
    x = setToX(setTo3())
    }
    output x = 5
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
    code = '''output map {
    procedure {
    let y = 5
    }
    output x = [3, 2, 1]
    }
    '''
    run_test_prog(code, {"x": [3, 2, 1]})

def test_list_add():
    code = '''output map {
    procedure {
    x += 4
    }
    output x = [1, 2, 3]
    }
    '''
    run_test_prog(code, {"x": [1, 2, 3, 4]})

def test_list_element():
    code = '''output map {
    procedure {
    let y = [3, 3]
    x = y[0]
    }
    output x = 1
    }
    '''
    run_test_prog(code, {"x": 3})

def test_list_element_variable_index():
    code = '''output map {
    procedure {
    let y = [3, 3]
    let n = 0
    x = y[n]
    }
    output x = 1
    }
    '''
    run_test_prog(code, {"x": 3})

def test_list_pop():
    code = '''output map {
    procedure {
    x.pop()
    }
    output x = [1, 2, 3, 4]
    }
    '''
    run_test_prog(code, {"x": [1, 2, 3]})

def test_for_loop():
    code = '''output map {
    procedure {
    let y = [3, 3]
    for i in y{
    x = x + i
    }
    }
    output x = 1
    }
    '''
    run_test_prog(code, {"x": 7})

def test_comparisons():
    code = '''output map {
    procedure {
    x = 1
    let y = 1
    x = (x > 7) or (y > 8)
    }
    output x = True
    }
    '''
    run_test_prog(code, {"x": False})

def test_function_as_parameter():
    code = '''output map {
    procedure {
    def animalSays(say){
    return say()
    }
    x = animalSays(catSays)
    }
    output x
    }
    def catSays(){
    return "meow"
    }
    '''
    run_test_prog(code, {"x": "meow"})

def test_list_length():
    code = '''output map {
    procedure {
    x = len(x)
    }
    output x = [1, 2, 3]
    }
    '''
    run_test_prog(code, {"x": 3})

def test_minus_equals():
    code = '''output map {
    procedure {
    x -= 3
    }
    output x = [1, 2, 3]
    }
    '''
    run_test_prog(code, {"x": [1, 2]})

def test_list_pop():
    code = '''output map {
    procedure {
    x.pop()
    }
    output x = [1, 2, 3]
    }
    '''
    run_test_prog(code, {"x": [1, 2]})

def test_basic_2d_array():
    code = '''
    output map {
        procedure {
            myArray = [
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ]
        }
        output myArray
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
    code = '''output map {
    procedure {
    x = random in 2..4
    }
    output x = 1
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    print(output)

    assert json.loads(output) == {'x': 2} or {'x': 3} or {'x': 4}

def test_random_choice():
    code = '''output map {
    procedure {
    let y = [2, 3, 4]
    x = random in y
    }
    output x = 1
    }
    '''

    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    print(output)

    assert json.loads(output) == {'x': 2} or {'x': 3} or {'x': 4}

def test_sqrt_op():
    code = '''
    output map {
        procedure {
            x = sqrt(9)
        }
        output x
    }
    '''
    run_test_prog(code, {"x": 3.0})

def test_sqrt_op_float():
    code = '''
    output map {
        procedure {
            x = sqrt(9.0)
        }
        output x
    }
    '''
    run_test_prog(code, {"x": 3.0})

def test_sqrt_op_var():
    code = '''
    output map {
        procedure {
            let y = 9 
            x = sqrt(y)
        }
        output x
    }
    '''
    run_test_prog(code, {"x": 3.0})

#TESTING POWER OF OPERATIONS
def test_pow_op():
    code = '''
    output map {
        procedure {
            x = pow(4, 2)
        }
        output x
    }
    '''
    run_test_prog(code, {"x": 16})

def test_pow_op_neg():
    code = '''
    output map {
        procedure {
            x = pow(2, -2)
        }
        output x
    }
    '''
    run_test_prog(code, {"x": 0.25})

def test_pow_op_var():
    code = '''
    output map {
        procedure {
            let y = 4
            let z = 2
            x = pow(y, z)
        }
        output x
    }
    '''
    run_test_prog(code, {"x": 16})
def test_nested_list():
    code = '''output map {
    procedure {
    x = [[1, 2] , [3, 4]]
    }
    output x
    }
    '''

    run_test_prog(code, {'x': [[1, 2], [3, 4]]})

def test_nested_list_access():
    code = '''output map {
    procedure {
    let y = [[1, 2] , [3, 4]]
    x = y[1][1]
    }
    output x
    }
    '''

    run_test_prog(code, {'x': 4})

def test_nested_list_assign():
    code = '''output map {
    procedure {
    x = [[1, 2] , [3, 4]]
    x[1][1] = 1
    }
    output x
    }
    '''

    run_test_prog(code, {'x': [[1, 2], [3, 1]]})

def test_whiteNoise():
    code = '''
    output map {
        procedure {
            myArray = [
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ]
            WhiteNoise(myArray, 0..1)
        }
        output myArray
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

def test_struct():
    code = '''output map {
        procedure {
        let cat = Cat{
            says = "meow"
        }
        x = cat.says
        }
        output x
        }
        struct Cat{
            says
        }
        '''

    run_test_prog(code, {'x': "meow"})

def test_struct_with_list_output_get():
    code = '''output map {
        procedure {
        let my_struct = Struct{
            array = [1, 2, 3]
        }
        x = my_struct.array[0]
        }
        output x
        }
        struct Struct{
            array
        }
        '''

    run_test_prog(code, {'x': 1})

def test_struct_with_list_output_assign():
    code = '''output map {
        procedure {
        let my_struct = Struct{
            array = [1, 2, 3]
        }
        my_struct.array[0] = 4
        x = my_struct.array[0]
        }
        output x
        }
        struct Struct{
            array
        }
        '''

    run_test_prog(code, {'x': 4})


def test_random_seed():
    code = '''output map {
    output x = 10000000
    output y = 103
    output z = 30420
    output a = 9009090
    procedure {
    let b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    seed(2000)
    x = random in 2..1000
    seed(1750)
    y = random in 2..1000
    seed(1500)
    z = random in 2..1000
    seed(1500)
    a = random in b
    }
    }
    '''

    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output1 = visitor.visit(tree)
    output2 = visitor.visit(tree)

    print(output1)
    print(output2)

    assert output1 == output2

def test_random_single_seed():
    code = '''output map {
    output x = 10000000
    output y = 103
    output z = 30420
    output a = 9009090
    procedure {
    let b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    seed(2000)
    x = random in 2..1000
    y = random in 2..1000
    z = random in 2..1000
    a = random in b
    }
    }
    '''

    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output1 = visitor.visit(tree)
    output2 = visitor.visit(tree)

    print(output1)
    print(output2)

    assert output1 == output2

def test_random_without_seed():
    code = '''output map {
    output x = 10000000
    output y = 103
    output z = 30420
    output a = 9009090
    procedure {
    let b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = random in 2..1000
    y = random in 2..1000
    z = random in 2..1000
    a = random in b
    }
    }
    '''

    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output1 = visitor.visit(tree)

    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output2 = visitor.visit(tree)

    print(output1)
    print(output2)

    assert output1 != output2

def test_hash_table_assign():
    code = '''
    output map {
    procedure {
    let my_hash = {"a": 1, "b": 2}
    x = my_hash["a"]
    }
    output x
    }
    '''

    run_test_prog(code, {"x": 1})

def test_hash_table_get():
    code = '''
        output map {
        procedure {
        let my_hash = {"a": 1, "b": 2}
        my_hash["a"] = 3
        x = my_hash["a"]
        }
        output x
        }
        '''

    run_test_prog(code, {"x": 3})

def test_nested_hash_table_get():
    code = '''
        output map {
        procedure {
        let my_list = [1, 2]
        let hash_1 = {"a": my_list, "b": 3}
        let hash_2 = {"a": hash_1, "b": 4}
        x = hash_2["a"]["a"][0]
        }
        output x
        }
        '''

    run_test_prog(code, {"x": 1})

def test_random_seed_bool():
    code = '''output map {
    output x = 10000000
    output y = 103
    output z = 30420
    output a = 9009090
    procedure {
    let b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    seed(True)
    x = random in 2..1000
    y = random in 2..1000
    z = random in 2..1000
    a = random in b
    }
    }
    '''

    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output1 = visitor.visit(tree)
    output2 = visitor.visit(tree)

    print(output1)
    print(output2)

    assert output1 == output2

def test_random_seed_string():
    code = '''output map {
    output x = 10000000
    output y = 103
    output z = 30420
    output a = 9009090
    procedure {
    let b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    seed("abcde")
    x = random in 2..1000
    y = random in 2..1000
    z = random in 2..1000
    a = random in b
    }
    }
    '''

    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output1 = visitor.visit(tree)
    output2 = visitor.visit(tree)

    print(output1)
    print(output2)

    assert output1 == output2

def test_call_int_as_func():
    code = '''output map{
    output x = 3
    procedure{
    x()
    }
    }
    '''
    
    pytest.raises(Exception)


def test_array_in_hash_in_struct():
    code = '''output map {
        procedure {
        let array_outside = [1,2,3]
        let hash_outside = {"a": array_outside}
        let my_struct = Struct{
            array = [1, 2, 3]
            hash = {"a": 1, "b": 2, "c": 3}
            array2 = [hash_outside]
        }
        my_struct.array[0] = 4
        x = my_struct.array[0]
        y = my_struct.hash["a"]
        z = my_struct.array2[0]["a"][0]
        }
        output x
        output y
        output z
        }
        struct Struct{
            array
            hash
            array2
        }
        '''

    run_test_prog(code, {'x': 4, 'y': 1, 'z': 1})
