# test_interpreter.py
import json

from grammar_files.generated.DungeonParser import DungeonParser
from grammar_files.generated.DungeonLexer import DungeonLexer
from antlr4 import *

from modules.AST.ASTBuilder import ASTBuilder
from modules.Interpreter.Interpreter import Interpreter

def setup_parser(str):
    lexer = DungeonLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    parser = DungeonParser(stream)
    return parser

def run_test_prog(code, expected_output):
    parser = setup_parser(code)
    tree = parser.prog()
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)
    visitor = Interpreter()
    output = visitor.visit(ast)
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
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)
    visitor = Interpreter()
    output = visitor.visit(ast)

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
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)
    visitor = Interpreter()
    output = visitor.visit(ast)

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
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)
    visitor = Interpreter()
    output = visitor.visit(ast)

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
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)
    visitor = Interpreter()
    output1 = visitor.visit(ast)
    output2 = visitor.visit(ast)

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
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)
    visitor = Interpreter()
    output1 = visitor.visit(ast)
    output2 = visitor.visit(ast)

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
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)
    visitor = Interpreter()
    output1 = visitor.visit(ast)

    parser = setup_parser(code)
    tree = parser.prog()
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)
    visitor = Interpreter()
    output2 = visitor.visit(ast)

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

def test_bsp_and_departition():
    code = '''
    Map(8, 8) map {
    layer terrain = 0
    procedure {
    let tree = bsp(terrain, 2)
    terrain = departition(tree)
    }
    }'''

    run_test_prog(code, {"map": {"layers": {"terrain": [[0] * 8] * 8}}})

def test_full_map():
    code = '''
    Map (64, 64) map {
        layer terrain = 0
        procedure {
            let tree = bsp(terrain, 4)
            tree = visit_partitions(tree, create_room)
            terrain = departition(tree)
        }
    }
    
    def visit_partitions(tree, function) {
        if (tree.depth > 1) {
            visit_partitions(tree.left, function)
            visit_partitions(tree.right, function)
        }
        else{
        tree.left = function(tree.left)
        tree.right = function(tree.right)
        }
        return tree
    }
    
    def create_room(matrix) {
        let set = [True, False]
        let x = random in set
    
        if (x) {
            return room(matrix)
        }
        else {
            return no_room(matrix)
        }
    }
    
    def room(matrix) {
        let x = len(matrix[0])
        let y = len(matrix)
    
        let index_x = x - 1
        let index_y = y - 1
        for i in 0..y {
            matrix[i][0] = "*"
            matrix[i][index_x] = "*"
        }
        for i in 0..x {
            matrix[0][i] = "*"
            matrix[index_y][i] = "*"
        }
    
        index_x = x - 2
        index_y = y - 2
        for i in 1..(y - 1) {
            matrix[i][1] = "#"
            matrix[i][index_x] = "#"
        }
        for i in 1..(x - 1) {
            matrix[1][i] = "#"
            matrix[index_y][i] = "#"
        }
    
        for i in 2..index_y {
            for j in 2..index_x {
                matrix[i][j] = "."
            }
        }
    
        return matrix
    }
    
    def no_room(matrix) {
        let x = len(matrix[0])
        let y = len(matrix)
    
        for i in 0..y {
            for j in 0..x {
                matrix[i][j] = "*"
            }
        }
        return matrix
    }
    '''

    parser = setup_parser(code)
    tree = parser.prog()
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)
    visitor = Interpreter()
    output = visitor.visit(ast)

def test_nested_access_inner():
    code = '''
    Map(2, 2) map {
    let x = 0
    procedure{
    let a = [1, 2, 3]
    let b = [0, 1, 0]
    x = a[b[2]]
    }
    }
    '''
    run_test_prog(code, {"map": {"data": {"x": 1}}})

def test_full_dungeon():
    code = '''
    Map (64, 64) map {
        layer terrain = 0
        procedure {
            let tree = bsp(terrain, 4)
            tree = visit_partitions(tree, create_room)
            terrain = connect_rooms(tree)
        }
    }
    
    def visit_partitions(tree, function) {
        if (tree.depth > 1) {
            visit_partitions(tree.left, function)
            visit_partitions(tree.right, function)
        }
        else{
        tree.left = function(tree.left)
        tree.right = function(tree.right)
        }
        return tree
    }
    
    def create_room(matrix) {
        let top_left = [ random in 1..(len(matrix) / 2), random in 1..(len(matrix[0]) / 2) ]
        let bottom_right = [ random in (top_left[0] + 1)..len(matrix), random in (top_left[1] + 1)..len(matrix[0]) ]
    
        for i in 0..len(matrix) {
            for j in 0..len(matrix[0]) {
                matrix[i][j] = "*"
            }
        }
    
        for i in top_left[0]..bottom_right[0] {
            for j in top_left[1]..bottom_right[1] {
                matrix[i][j] = "."
            }
        }
        return matrix
    }
    
    def connect_rooms(tree) {
        if (tree.depth > 1) {
            tree.left = connect_rooms(tree.left)
            tree.right = connect_rooms(tree.right)
        }
        let matrix = departition(tree)
        let start = [0, 0]
        while (tree.left[start[0]][start[1]] == "*") {
            start[0] = random in 0..len(tree.left)
            start[1] = random in 0..len(tree.left[0])
        }
        let goal = [0, 0]
        while (tree.right[goal[0]][goal[1]] == "*") {
            goal[0] = random in 0..len(tree.right)
            goal[1] = random in 0..len(tree.right[0])
        }
        let grid = matrix.rows
        let path = astar(start, goal, grid)
        for point in path {
            matrix.rows[point[0]][point[1]] = "."
        }
        return matrix
    }
    '''
    parser = setup_parser(code)
    tree = parser.prog()
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)
    visitor = Interpreter()
    output = visitor.visit(ast)

def test_string_add():
    code = '''
    Map(2, 2) map {
    let x = 0
    procedure{
    x = "Hello"
    x = x + " world!"
    }
    }
    '''

    run_test_prog(code, {"map": {"data": {"x": "Hello world!"}}})

def test_div_type():
    code = '''
    Map(2, 2) map {
    let x = 4
    procedure{
    x = x / 2
    }
    }
    '''

    run_test_prog(code, {"map": {"data": {"x": 2}}})
