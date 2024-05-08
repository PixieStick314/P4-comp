#   test_parser.py
from grammar_files.generated.DungeonParser import DungeonParser
from grammar_files.generated.DungeonLexer import DungeonLexer
from antlr4 import *

#Helper function
def setup_parser(str):
    lexer = DungeonLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    parser = DungeonParser(stream)
    return parser

#<----------Ambiguity testing for assignStat---------->
#Assign stat has 4 different types of assignments, each is tested below:

#Ambiguity testing for struct assignment
def test_ambiguity_assign_stat_struct():
    test = 'my_struct = Cat{says = "meow"}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_assignStat

#Ambiguity testing for hash table assignment
def test_ambiguity_assign_stat_hash_table():
    test = 'my_hash = {"a": 1, "b": 2}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_assignStat

#Ambiguity testing for list assignment
def test_ambiguity_assign_stat_list():
    test = 'my_list = [1, 2]'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_assignStat

#Ambiguity testing for expr assignment
def test_ambiguity_assign_stat_expr():
    test = 'my_expr = 1+2'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_assignStat
#<END----------Ambiguity testing for assignStat ----------END>

#Ambiguity testing for function declaration
def test_ambiguity_function_decl():
    test = 'def function(){print("Hello World!")}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_functionDecl

#Ambiguity testing for if statement
def test_ambiguity_if_stat():
    test = 'if(True) {print("Hello World!")}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_ifStat

#Ambiguity testing for for loop
def test_ambiguity_for_loop():
    test = 'for i in x {print(i)}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_forLoop

#Ambiguity testing for while loop
def test_ambiguity_while_loop():
    test = 'while (x) {print(x)}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_whileLoop

#Ambiguity testing for stat block
def test_ambiguity_stat_block():
    test = '{print("Hello World!")}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_statBlock

#Ambiguity testing for return statement
def test_ambiguity_return_stat():
    test = 'return x'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_returnStat

#Ambiguity testing for plus equals
def test_ambiguity_plus_equals():
    test = 'my_plus_equals += 10'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_plusEquals

#Ambiguity testing for minus equals
def test_ambiguity_minus_equals():
    test = 'my_minus_equals -= 10'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_minusEquals

#Ambiguity testing for list pop
def test_ambiguity_list_pop():
    test = 'my_array.pop()'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_listPop

#Ambiguity testing for white noise stat
def test_ambiguity_white_noise_stat():
    test = 'WhiteNoise my_ID, 10..20 layer'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_whiteNoiseStat

#Ambiguity testing for struct def
def test_ambiguity_struct_def():
    test = 'struct my_struct {my_id}'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_structDef

#Ambiguity testing for seed
def test_ambiguity_seed():
    test = 'seed (10)'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_seed

#Ambiguity testing for expr
def test_ambiguity_expr():
    test = 'function()'
    parser = setup_parser(test)
    tree = parser.stat()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr

#<----------Stat testing---------->
#Testing print stat
def test_print_stat():
    test = 'print ("Hello World!")'
    parser = setup_parser(test)
    tree = parser.printStat()
    
    assert (tree.getRuleIndex() == DungeonParser.RULE_printStat)
    assert tree.getChild(0).getSymbol().type == DungeonParser.PRINT
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH

#Testing variable declaration
def test_var_decl():
    test = 'let variable = 3'
    parser = setup_parser(test)
    tree = parser.varDecl()

    assert (tree.getRuleIndex() == DungeonParser.RULE_varDecl)
    assert tree.getChild(0).getText() == 'let'
    assert tree.getChild(1).getSymbol().type == DungeonParser.ID
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_assignment

#<---------- Stat testing for assignStat---------->
#Assign stat has 4 different types of assignments, each is tested below:

#Stat testing for struct assignment
def test_assign_stat_struct():
    test = 'my_struct = Cat{says = "meow"}'
    parser = setup_parser(test)
    tree = parser.assignStat()

    assert tree.getChild(0).getSymbol().type == DungeonParser.ID
    assert tree.getChild(1).getRuleIndex() == DungeonParser.RULE_assignment
    assert tree.getChild(1).getChild(1).getRuleIndex() == DungeonParser.RULE_struct

#Stat testing for hash table assignment
def test_assign_stat_hash_table():
    test = 'my_hash = {"a": 1, "b": 2}'
    parser = setup_parser(test)
    tree = parser.assignStat()

    assert tree.getChild(0).getSymbol().type == DungeonParser.ID
    assert tree.getChild(1).getRuleIndex() == DungeonParser.RULE_assignment
    assert tree.getChild(1).getChild(1).getRuleIndex() == DungeonParser.RULE_hashTable

#Stat testing for list assignment
def test_assign_stat_list():
    test = 'my_list = [1, 2]'
    parser = setup_parser(test)
    tree = parser.assignStat()

    assert tree.getChild(0).getSymbol().type == DungeonParser.ID
    assert tree.getChild(1).getRuleIndex() == DungeonParser.RULE_assignment
    assert tree.getChild(1).getChild(1).getRuleIndex() == DungeonParser.RULE_list

#Stat testing for expr assignment
def test_assign_stat_expr():
    test = 'my_expr = 1+2'
    parser = setup_parser(test)
    tree = parser.assignStat()

    assert tree.getChild(0).getSymbol().type == DungeonParser.ID
    assert tree.getChild(1).getRuleIndex() == DungeonParser.RULE_assignment
    assert tree.getChild(1).getChild(1).getRuleIndex() == DungeonParser.RULE_expr
#<END----------Stat testing for assignStat ----------END>

#Testing function declaration
def test_function_decl():
    code = 'def add(x, y) {return x + y}'
    parser = setup_parser(code)
    tree = parser.functionDecl()

    assert (tree.getRuleIndex() == DungeonParser.RULE_functionDecl)
    assert tree.getChild(0).getSymbol().type == DungeonParser.DEF
    assert tree.getChild(1).getSymbol().type == DungeonParser.ID
    assert tree.getChild(2).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(3).getRuleIndex() == DungeonParser.RULE_params
    assert tree.getChild(4).getSymbol().type == DungeonParser.CLOSED_PARENTH
    assert tree.getChild(5).getRuleIndex() == DungeonParser.RULE_statBlock

#Testing if stat
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

#Testing nested if stat
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


#Testing for loop
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

#Testing nested for loop
def test_nested_for_loop():
    code = '''
    for i in x {
        for k in y {
            print(k)
        }
    }'''
    parser = setup_parser(code)
    tree = parser.forLoop()

    assert (tree.getRuleIndex() == DungeonParser.RULE_forLoop)
    assert tree.getChild(0).getSymbol().type == DungeonParser.FOR
    assert tree.getChild(1).getSymbol().type == DungeonParser.ID
    assert tree.getChild(2).getSymbol().type == DungeonParser.IN
    assert tree.getChild(3).getSymbol().type == DungeonParser.ID
    assert tree.getChild(4).stat()[0].forLoop() is not None

#Testing while loop
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

#Testing nested while loop
def test_nested_while_loop():
    code = '''
    while (true) {
        while (true) {
            print("hi")
        }
    }'''
    parser = setup_parser(code)
    tree = parser.whileLoop()

    assert (tree.getRuleIndex() == DungeonParser.RULE_whileLoop)
    assert tree.getChild(0).getSymbol().type == DungeonParser.WHILE
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH
    assert tree.getChild(4).stat()[0].whileLoop() is not None

#Testing statblock
def test_stat_block():
    code = '''{print("HI") if(true) {print("HI")} while(true) {print("HI")}}'''
    parser = setup_parser(code)
    tree = parser.statBlock()

    assert tree.getChild(0).getSymbol().type == DungeonParser.OPEN_CURL
    assert tree.getChild(1).getRuleIndex() == DungeonParser.RULE_stat
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_stat
    assert tree.getChild(3).getRuleIndex() == DungeonParser.RULE_stat
    assert tree.getChild(4).getSymbol().type == DungeonParser.CLOSED_CURL

#Testing return
def test_return_stat():
    test = 'return x'
    parser = setup_parser(test)
    tree = parser.returnStat()

    assert tree.getChild(0).getSymbol().type == DungeonParser.RETURN
    assert tree.getChild(1).getRuleIndex() == DungeonParser.RULE_expr

#Testing plus equals
def test_plus_equals():
    test = 'my_ID += 10'
    parser = setup_parser(test)
    tree = parser.plusEquals()

    assert tree.getChild(0).getSymbol().type == DungeonParser.ID
    assert tree.getChild(1).getSymbol().type == DungeonParser.PEQ
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Testing minus equals
def test_minus_equals():
    test = 'my_ID -= 10'
    parser = setup_parser(test)
    tree = parser.minusEquals()

    assert tree.getChild(0).getSymbol().type == DungeonParser.ID
    assert tree.getChild(1).getSymbol().type == DungeonParser.MEQ
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Testing list pop
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

#Testing white noise
def test_white_noise():
    code = 'WhiteNoise (my_ID, 10..20) layer'
    parser = setup_parser(code)
    tree = parser.whiteNoiseStat()

    assert (tree.getRuleIndex() == DungeonParser.RULE_whiteNoiseStat)
    assert tree.getChild(0).getText() == 'WhiteNoise'
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getSymbol().type == DungeonParser.ID
    assert tree.getChild(3).getSymbol().type == DungeonParser.COMMA
    assert tree.getChild(4).getRuleIndex() == DungeonParser.RULE_range
    assert tree.getChild(5).getSymbol().type == DungeonParser.CLOSED_PARENTH
    assert tree.getChild(6).getSymbol().type == DungeonParser.LAYER

#Testing struct definition
def test_struct_def():
    code = 'struct my_ID {my_ID1 my_ID2}'
    parser = setup_parser(code)
    tree = parser.structDef()

    assert (tree.getRuleIndex() == DungeonParser.RULE_structDef)
    assert tree.getChild(0).getText() == 'struct'
    assert tree.getChild(1).getSymbol().type == DungeonParser.ID
    assert tree.getChild(2).getSymbol().type == DungeonParser.OPEN_CURL
    assert tree.getChild(3).getRuleIndex() == DungeonParser.RULE_structField
    assert tree.getChild(4).getRuleIndex() == DungeonParser.RULE_structField
    assert tree.getChild(5).getSymbol().type == DungeonParser.CLOSED_CURL

#Testing seed
def test_seed():
    code = 'seed(7)'
    parser = setup_parser(code)
    tree = parser.seed()

    assert tree.getChild(0).getSymbol().type == DungeonParser.SEED
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH

#Function calls
def test_functionCall():
    code = 'my_ID(10, 20)'
    parser = setup_parser(code)
    tree = parser.functionCall()

    assert tree.getChild(0).getSymbol().type == DungeonParser.ID
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_args
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH  

#<----------Testing expr---------->
#Function calls
def test_functionCall_as_expr():
    code = 'my_ID(10, 20)'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getChild(0).getSymbol().type == DungeonParser.ID 
    assert tree.getChild(0).getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(0).getChild(2).getRuleIndex() == DungeonParser.RULE_args
    assert tree.getChild(0).getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH 

#<----------ID inner---------->
#ID inner with string
def test_inner_string():
    code = 'my_ID.my_ID1["Hello"]'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.ID 
    assert tree.getChild(1).getChild(0).getSymbol().type == DungeonParser.DOT
    assert tree.getChild(1).getChild(1).getRuleIndex() == DungeonParser.RULE_structField
    assert tree.getChild(1).getChild(2).getChild(0).getChild(1).getSymbol().type == DungeonParser.STRING

#ID inner with ID
def test_inner_ID():
    code = 'my_ID.my_ID1[my_ID2]'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.ID 
    assert tree.getChild(1).getChild(0).getSymbol().type == DungeonParser.DOT
    assert tree.getChild(1).getChild(1).getRuleIndex() == DungeonParser.RULE_structField
    assert tree.getChild(1).getChild(2).getChild(0).getChild(1).getSymbol().type == DungeonParser.ID

#ID inner with int
def test_inner_INT():
    code = 'my_ID.my_ID1[10]'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.ID 
    assert tree.getChild(1).getChild(0).getSymbol().type == DungeonParser.DOT
    assert tree.getChild(1).getChild(1).getRuleIndex() == DungeonParser.RULE_structField
    assert tree.getChild(1).getChild(2).getChild(0).getChild(1).getSymbol().type == DungeonParser.INT
#<END----------ID inner----------END>

#listLength
def test_list_length():
    code = 'len(my_ID)'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getChild(0).getText() == 'len'
    assert tree.getChild(0).getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(0).getChild(2).getSymbol().type == DungeonParser.ID
    assert tree.getChild(0).getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH

#random with range
def test_random_with_range():
    code = 'random in 10..20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getChild(0).getSymbol().type == DungeonParser.RANDOM
    assert tree.getChild(0).getChild(1).getSymbol().type == DungeonParser.IN
    assert tree.getChild(0).getChild(2).getRuleIndex() == DungeonParser.RULE_range

#random with ID
def test_random_with_ID():
    code = 'random in my_ID'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getChild(0).getSymbol().type == DungeonParser.RANDOM
    assert tree.getChild(0).getChild(1).getSymbol().type == DungeonParser.IN
    assert tree.getChild(0).getChild(2).getSymbol().type == DungeonParser.ID

#Multiplication
def test_multiplication():
    code = '10 * 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.MULT
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Division
def test_division():
    code = '10 / 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.DIV
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Modular
def test_modular():
    code = '10 % 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.MOD
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Addition
def test_addition():
    code = '10 + 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.PLUS
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Subtraction
def test_subtraction():
    code = '10 - 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.MINUS
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Greater than
def test_greater_than():
    code = '10 > 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.GT
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Greater than equals
def test_greater_than_equals():
    code = '10 >= 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.GTE
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Less than
def test_less_than():
    code = '10 < 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.LT
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Less than equals
def test_less_than_equals():
    code = '10 <= 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.LTE
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Equal
def test_equals():
    code = '10 == 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.EQ
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Not equal
def test_not_equals():
    code = '10 != 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.NEQ
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#And
def test_and():
    code = '10 and 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.AND
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Or
def test_or():
    code = '10 or 20'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(1).getSymbol().type == DungeonParser.OR
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr

#Not
def test_not():
    code = 'not 10'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.NOT
    assert tree.getChild(1).getRuleIndex() == DungeonParser.RULE_expr

#Square root
def test_square_root():
    code = 'sqrt(9)'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.SQRT
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr   
    assert tree.getChild(3).getSymbol().type == DungeonParser.CLOSED_PARENTH

#Power of
def test_power_of():
    code = 'pow(1,2)'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.POW
    assert tree.getChild(1).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(2).getRuleIndex() == DungeonParser.RULE_expr 
    assert tree.getChild(3).getSymbol().type == DungeonParser.COMMA
    assert tree.getChild(4).getRuleIndex() == DungeonParser.RULE_expr   
    assert tree.getChild(5).getSymbol().type == DungeonParser.CLOSED_PARENTH  

#Expr in parenth
def test_expr_in_parenth():
    code = '(1+2+3+4+5)'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.OPEN_PARENTH
    assert tree.getChild(1).getRuleIndex() == DungeonParser.RULE_expr    
    assert tree.getChild(2).getSymbol().type == DungeonParser.CLOSED_PARENTH  

#Id as expr
def test_ID_as_expr():
    code = 'my_ID'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.ID

#Int as expr
def test_INT_as_expr():
    code = '10'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.INT

#Float as expr
def test_float_as_expr():
    code = '2.2'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.FLOAT    

#String as expr
def test_string_as_expr():
    code = '"Hello world"'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.STRING

#Bool true as expr
def test_True_as_expr():
    code = 'True'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.TRUE

#Bool false as expr
def test_False_as_expr():
    code = 'False'
    parser = setup_parser(code)
    tree = parser.expr()

    assert tree.getChild(0).getSymbol().type == DungeonParser.FALSE