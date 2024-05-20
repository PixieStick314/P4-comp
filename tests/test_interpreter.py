# test_interpreter.py
import json

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
    code = '''Map(10, 10) map {
    let x = 5
    procedure {
    x = 3
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 3}}})

def test_function_decl_and_call():
    code = '''Map(10, 10) map {
    let x = 5
    procedure {
    x = setTo3()
    }
    def setTo3() {
    return 3
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 3}}})

def test_arithmetic():
    code = '''Map(10, 10) map {
    let x = 5
    procedure {x = x - 1}
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 4}}})

def test_nested_if_stat():
    code = '''Map(10, 10) map {
    let x = 5
    procedure {
    if(x == 5){
    x = 4
    if(x == 4){
    x = 3
    }
    }
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 3}}})

def test_elif_stat():
    code = '''Map(10, 10) map {
    let x = 4
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
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 2}}})

def test_else_stat():
    code = '''Map(10, 10) map {
    let x = 4
    procedure {
    if(x == 5){
    x = 1
    }
    else{
    x = 3
    }
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 3}}})

def test_while_loop():
    code = '''Map(10, 10) map {
    let x = 5
    procedure {
    while(x > 0){
    x = x - 1
    }
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 0}}})

def test_nested_function_call():
    code = '''Map(10, 10) map {
    let x = 5
    procedure {
    x = setToX(setTo3())
    }
    def setToX(x){
    return x
    }
    def setTo3() {
    return 3
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 3}}})

def test_list():
    code = '''Map(10, 10) map {
    let x = [3, 2, 1]
    procedure {
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": [3, 2, 1]}}})

def test_list_add():
    code = '''Map(10, 10) map {
    let x = [1, 2, 3]
    procedure {
    x += 4
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": [1, 2, 3, 4]}}})

def test_list_element():
    code = '''Map(10, 10) map {
    let x = 1
    procedure {
    let y = [3, 3]
    x = y[0]
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 3}}})

def test_list_element_variable_index():
    code = '''Map(10, 10) map {
    let x = 1
    procedure {
    let y = [3, 3]
    let n = 0
    x = y[n]
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 3}}})

def test_list_pop():
    code = '''Map(10, 10) map {
    let x = [1, 2, 3, 4]
    procedure {
    pop(x)
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": [1, 2, 3]}}})

def test_for_loop():
    code = '''Map(10, 10) map {
    let x = 1
    procedure {
    let y = [3, 3]
    for i in y{
    x = x + i
    }
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 7}}})

def test_comparisons():
    code = '''Map(10, 10) map {
    let x
    procedure {
    let a = 1
    let b = 1
    x = (a > 7) or (b > 8)
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": False}}})

def test_function_as_parameter():
    code = '''Map(10, 10) map {
    let x
    procedure {
    def animalSays(say){
    return say()
    }
    x = animalSays(catSays)
    }
    }
    def catSays(){
    return "meow"
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": "meow"}}})

def test_list_length():
    code = '''Map(10, 10) map {
    let x = [1, 2, 3]
    procedure {
    x = len(x)
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 3}}})

def test_minus_equals():
    code = '''Map(10, 10) map {
    let x = [1, 2, 3]
    procedure {
    x -= 3
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": [1, 2]}}})

def test_list_pop():
    code = '''Map(10, 10) map {
    let x = [1, 2, 3]
    procedure {
    x.pop()
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": [1, 2]}}})

def test_basic_2d_array():
    code = '''
    Map(10, 10) map {
    let myArray
        procedure {
            myArray = [
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ]
        }
    }
    '''
    expected_output = {"map": {"data": {
        "myArray": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    }}}
    run_test_prog(code, expected_output)

def test_random_range():
    code = '''Map(10, 10) map {
    let x = 1
    procedure {
    x = random in 2..4
    }
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    visitor = Interpreter()
    output = visitor.visit(tree)

    print(output)

    assert json.loads(output) == {'x': 2} or {'x': 3} or {'x': 4}

def test_random_choice():
    code = '''Map(10, 10) map {
    let x = 1
    procedure {
    let y = [2, 3, 4]
    x = random in y
    }
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
    Map(10, 10) map {
        let x
        procedure {
            x = sqrt(9)
        }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 3.0}}})

def test_sqrt_op_float():
    code = '''
    Map(10, 10) map {
    let x
        procedure {
            x = sqrt(9.0)
        }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 3.0}}})

def test_sqrt_op_var():
    code = '''
    Map(10, 10) map {
        let x
        procedure {
            let y = 9 
            x = sqrt(y)
        }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 3.0}}})

#TESTING POWER OF OPERATIONS
def test_pow_op():
    code = '''
    Map(10, 10) map {
        let x
        procedure {
            x = pow(4, 2)
        }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 16}}})

def test_pow_op_neg():
    code = '''
    Map(10, 10) map {
        let x
        procedure {
            x = pow(2, -2)
        }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 0.25}}})

def test_pow_op_var():
    code = '''
    Map(10, 10) map {
        let x
        procedure {
            let y = 4
            let z = 2
            x = pow(y, z)
        }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 16}}})
def test_nested_list():
    code = '''Map(10, 10) map {
    let x
    procedure {
    x = [[1, 2] , [3, 4]]
    }
    }
    '''

    run_test_prog(code, {"map": {"data": {'x': [[1, 2], [3, 4]]}}})

def test_nested_list_access():
    code = '''Map(10, 10) map {
    let x
    procedure {
    let y = [[1, 2] , [3, 4]]
    x = y[1][1]
    }
    }
    '''

    run_test_prog(code, {"map": {"data": {'x': 4}}})

def test_nested_list_assign():
    code = '''Map(10, 10) map {
    let x
    procedure {
    x = [[1, 2] , [3, 4]]
    x[1][1] = 1
    }
    }
    '''

    run_test_prog(code, {"map": {"data": {'x': [[1, 2], [3, 1]]}}})

def test_whiteNoise():
    code = '''
    Map(10, 10) map {
        let myArray
        procedure {
            myArray = [
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ]
            myArray = WhiteNoise(myArray, 0, 1)
        }
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
    
    myArray = deserialized_output["map"]["data"]["myArray"]

    assert isinstance(myArray, list), "Expected 'myArray' to be a list"
    
    for row in myArray:
        assert isinstance(row, list), "Each row should be a list"
        
        for value in row:
            assert value in (0, 1), f"Value {value} is not 0 or 1"

def test_struct():
    code = '''Map(10, 10) map {
        let x
        procedure {
        let cat = Cat{
            says = "meow"
        }
        x = cat.says
        }
        }
        struct Cat{
            says
        }
        '''

    run_test_prog(code, {"map": {"data": {'x': "meow"}}})

def test_struct_with_list_output_get():
    code = '''Map(10, 10) map {
        let x
        procedure {
        let my_struct = Struct{
            array = [1, 2, 3]
        }
        x = my_struct.array[0]
        }
        }
        struct Struct{
            array
        }
        '''

    run_test_prog(code, {"map": {"data": {'x': 1}}})

def test_struct_with_list_output_assign():
    code = '''Map(10, 10) map {
        let x
        procedure {
        let my_struct = Struct{
            array = [1, 2, 3]
        }
        my_struct.array[0] = 4
        x = my_struct.array[0]
        }
        }
        struct Struct{
            array
        }
        '''

    run_test_prog(code, {"map": {"data": {'x': 4}}})


def test_random_seed():
    code = '''Map(10, 10) map {
    let x = 10000000
    let y = 103
    let z = 30420
    let a = 9009090
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
    code = '''Map(10, 10) map {
    let x = 10000000
    let y = 103
    let z = 30420
    let a = 9009090
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
    code = '''Map(10, 10) map {
    let x = 10000000
    let y = 103
    let z = 30420
    let a = 9009090
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
    Map(10, 10) map {
    let x
    procedure {
    let my_hash = {"a": 1, "b": 2}
    x = my_hash["a"]
    }
    }
    '''

    run_test_prog(code, {"map": {"data": {"x": 1}}})

def test_hash_table_get():
    code = '''
        Map(10, 10) map {
        let x
        procedure {
        let my_hash = {"a": 1, "b": 2}
        my_hash["a"] = 3
        x = my_hash["a"]
        }
        }
        '''

    run_test_prog(code, {"map": {"data": {"x": 3}}})

def test_nested_hash_table_get():
    code = '''
        Map(10, 10) map {
        let x
        procedure {
        let my_list = [1, 2]
        let hash_1 = {"a": my_list, "b": 3}
        let hash_2 = {"a": hash_1, "b": 4}
        x = hash_2["a"]["a"][0]
        }
        }
        '''

    run_test_prog(code, {"map": {"data": {"x": 1}}})

def test_empty_list():
    code = '''
        Map(10, 10) map {
        let x
        procedure {
        x = []
        x += 1
        }
        }
        '''

    run_test_prog(code, {"map": {"data": {"x": [1]}}})

def test_for_loop_range():
    code = '''
        Map(10, 10) map {
        let x
        procedure {
        x = []
        for i in 0..5 {
            x += i
        }
        }
        }
        '''

    run_test_prog(code, {"map": {"data": {"x": [0, 1, 2, 3, 4]}}})

def test_or():
    code = '''
    Map(10, 10) map {
    let x
    procedure {
    x = 0
    let a = 1
    let b = 2
    if (a == 1 or b == 1) {
    x = 3}
    elif (a == 2 or b == 3){
    x = 4
    }
    }
    }
    '''

    run_test_prog(code, {"map": {"data": {"x": 3}}})

def test_integration_boss_room():
    code = '''
    Map(10, 10) BossRoom {
    layer terrain
    procedure {
        for i in 0..10 {
            let row = []
            for j in 0..10 {
                if (i == 0 or i == 9) {
                    row += "#"
                }
                elif (j == 0 or j == 9) {
                    row += "#"
                }
                else {
                    row += "."
                }
            }
        terrain[i] = row
        }
    }
    }
    '''

    run_test_prog(code, {"BossRoom": {"layers": {"terrain": [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
                                 ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
                                 ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
                                 ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
                                 ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
                                 ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
                                 ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
                                 ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
                                 ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
                                 ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]}}})

def test_zero_comparison():
    code = '''
    Map(10, 10) map {
    let x
    procedure {
    x = False
    let a = 0
    let b = 0
    if (a == b) {
    x = True}
    }
    }'''

    run_test_prog(code, {"map": {"data": {"x": True}}})

def test_not():
    code = '''
    Map(10, 10) map {
    let x
    procedure {
    let a = True
    x = (not a)
    }
    }
    '''

    run_test_prog(code, {"map": {"data": {"x": False}}})

def test_assign_list_element_by_id():
    code = '''
    Map(10, 10) map {
    let x
    procedure {
    let a = [1, 2, 3]
    let i = 0
    a[i] = 4
    x = a[0]
    }
    }
    '''

    run_test_prog(code, {"map": {"data": {"x": 4}}})

def test_dict_element_by_id():
    code = '''
    Map(10, 10) map {
    let x
    procedure {
    let a = {"cat": "tabby"}
    let b = "cat"
    a[b] = "ragdoll"
    x = a["cat"]
    }
    }
    '''

    run_test_prog(code, {"map": {"data": {"x": "ragdoll"}}})

def test_layer_decl():
    code = '''
    Map(2, 2) map {
    layer x = 1
    procedure {
    }
    }'''

    run_test_prog(code, {"map": {"layers": {"x": [[1,1],[1,1]]}}})
