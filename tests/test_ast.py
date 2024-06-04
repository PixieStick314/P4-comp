from _ast import AST

from antlr4 import CommonTokenStream, InputStream

from grammar_files.generated.DungeonLexer import DungeonLexer
from grammar_files.generated.DungeonParser import DungeonParser
from modules.AST.ASTBuilder import ASTBuilder
from modules.AST.Dungeon import Dungeon


def test_ast_builder():
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
        let bottom_right = [ random in (top_left[0] + 2)..len(matrix), random in (top_left[1] + 2)..len(matrix[0]) ]
    
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
        if (tree.split_plane == "vertical") {
            goal[1] = goal[1] + len(tree.right[0])
        }
        elif (tree.split_plane == "horizontal") {
            goal[0] = goal[0] + len(tree.right)
        }
        let path = astar(start, goal, matrix)
        for point in path {
            matrix[point[1]][point[0]] = "."
        }
        return matrix
    }
    '''

    lexer = DungeonLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = DungeonParser(stream)
    parse_tree = parser.prog()
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(parse_tree)

    assert isinstance(ast, Dungeon)
