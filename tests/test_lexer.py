#   test_lexer.py
from _pytest.mark.expression import TokenType

from grammar_files.generated.DungeonLexer import DungeonLexer
from antlr4 import CommonTokenStream, InputStream
#File tests if strings get tokenized correctly

#Helper function
def get_tokens_from_string(str):
    lexer = DungeonLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    stream.fill()
    tokens = stream.tokens
    return tokens

#<--------------------Keywords-------------------->

#Testing 'if'
def test_lexer_IF():
    code = 'if'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.IF
    assert tokens[1].type == -1

#Testing 'elif'
def test_lexer_ELIF():
    code = 'elif'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.ELIF
    assert tokens[1].type == -1

#Testing 'else'
def test_lexer_ELSE():
    code = 'else'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.ELSE
    assert tokens[1].type == -1

#Testing 'return'
def test_lexer_RETURN():
    code = 'return'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.RETURN
    assert tokens[1].type == -1

#Testing 'print'
def test_lexer_PRINT():
    code = 'print'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.PRINT
    assert tokens[1].type == -1

#Testing 'for'
def test_lexer_FOR():
    code = 'for'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.FOR
    assert tokens[1].type == -1

#Testing 'in'
def test_lexer_IN():
    code = 'in'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.IN
    assert tokens[1].type == -1

#Testing 'while'
def test_lexer_while():
    code = 'while'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.WHILE
    assert tokens[1].type == -1


#Testing 'def'
def test_lexer_DEF():
    code = 'def'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.DEF
    assert tokens[1].type == -1


#Testing 'layer'
def test_lexer_LAYER():
    code = 'layer'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.LAYER
    assert tokens[1].type == -1


#Testing 'procedure'
def test_lexer_PROCEDURE():
    code = 'procedure'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.PROCEDURE
    assert tokens[1].type == -1


#Testing 'seed'
def test_lexer_SEED():
    code = 'seed'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.SEED
    assert tokens[1].type == -1


#Testing 'random'
def test_lexer_RANDOM():
    code = 'random'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.RANDOM
    assert tokens[1].type == -1

#<--------------------Operators-------------------->

#Testing +
def test_lexer_PLUS():
    code = '+'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.PLUS
    assert tokens[1].type == -1

#Testing -
def test_lexer_MINUS():
    code = '-'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.MINUS
    assert tokens[1].type == -1

#Testing *
def test_lexer_MULT():
    code = '*'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.MULT
    assert tokens[1].type == -1

#Testing /
def test_lexer_DIV():
    code = '/'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.DIV
    assert tokens[1].type == -1

#Testing >
def test_lexer_GREATER_THAN():
    code = '>'
    tokens = get_tokens_from_string(code)
    assert tokens[0].type == DungeonLexer.GT
    assert tokens[1].type == -1

#Testing >=
def test_lexer_GREATER_THAN_EQUALS():
    code = '>='
    tokens = get_tokens_from_string(code)
    assert tokens[0].type == DungeonLexer.GTE
    assert tokens[1].type == -1

#Testing <
def test_lexer_LESS_THAN():
    code = '<'
    tokens = get_tokens_from_string(code)
    assert tokens[0].type == DungeonLexer.LT
    assert tokens[1].type == -1

#Testing <=
def test_lexer_LESS_THAN_EQUALS():
    code = '<='
    tokens = get_tokens_from_string(code)
    assert tokens[0].type == DungeonLexer.LTE
    assert tokens[1].type == -1

#Testing ==
def test_lexer_EQUALS():
    code = '=='
    tokens = get_tokens_from_string(code)
    assert tokens[0].type == DungeonLexer.EQ
    assert tokens[1].type == -1

#Testing !=
def test_lexer_NOT_EQUALS():
    code = '!='
    tokens = get_tokens_from_string(code)
    assert tokens[0].type == DungeonLexer.NEQ
    assert tokens[1].type == -1

#Testing +=
def test_lexer_PLUS_EQUALS():
    code = '+='
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.PEQ
    assert tokens[1].type == -1

#Testing -=
def test_lexer_MINUS_EQUALS():
    code = '-='
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.MEQ
    assert tokens[1].type == -1

#Testing %
def test_lexer_MOD():
    code = '%'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.MOD
    assert tokens[1].type == -1

#Tesing 'and'
def test_lexer_AND():
    code = 'and'
    tokens = get_tokens_from_string(code)
    assert tokens[0].type == DungeonLexer.AND
    assert tokens[1].type == -1

#Tesing 'or'
def test_lexer_OR():
    code = 'or'
    tokens = get_tokens_from_string(code)
    assert tokens[0].type == DungeonLexer.OR
    assert tokens[1].type == -1

#Tesing 'NOT'
def test_lexer_NOT():
    code = 'not'
    tokens = get_tokens_from_string(code)
    assert tokens[0].type == DungeonLexer.NOT
    assert tokens[1].type == -1

#Testing bool True
def test_lexer_TRUE():
    code = 'True'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.TRUE
    assert tokens[1].type == -1

#Testing bool False
def test_lexer_FALSE():
    code = 'False'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.FALSE
    assert tokens[1].type == -1

#Testing square root
def test_lexer_SQUARE_ROOT():
    code = 'sqrt'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.SQRT
    assert tokens[1].type == -1

#Testing power of
def test_lexer_POWER_OF():
    code = 'pow'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.POW
    assert tokens[1].type == -1

#<--------------------Datatypes-------------------->
#Testing ints
def test_lexer_INT():
    code = '1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.INT
    assert tokens[1].type == -1

#Testing floats
def test_lexer_FLOAT():
    code = '1.1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.FLOAT
    assert tokens[1].type == -1

#Testing strings
def test_lexer_STRING():
    code = '"hello"'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.STRING
    assert tokens[1].type == -1

#Testing IDs
def test_lexer_ID():
    code = 'my_var1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.ID
    assert tokens[1].type == -1

#Testing multiple tokens on the same line
def test_lexer_multiple_tokens():
    code = 'my_var1 1 "hello"'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.ID
    assert tokens[1].type == DungeonLexer.INT
    assert tokens[2].type == DungeonLexer.STRING
    assert tokens[3].type == -1

#<--------------------Common symbols-------------------->
#Testing (
def test_lexer_OPEN_PARENTHESIS():
    code = '('
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.OPEN_PARENTH
    assert tokens[1].type == -1

#Testing )
def test_lexer_CLOSED_PARENTHESIS():
    code = ')'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.CLOSED_PARENTH
    assert tokens[1].type == -1

#Testing [
def test_lexer_OPEN_BRACKET():
    code = '['
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.OPEN_BRACK
    assert tokens[1].type == -1

#Testing ]
def test_lexer_CLOSED_BRACKET():
    code = ']'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.CLOSED_BRACK
    assert tokens[1].type == -1

#Testing {
def test_lexer_OPEN_CURLY_BRACKET():
    code = '{'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.OPEN_CURL
    assert tokens[1].type == -1

#Testing }
def test_lexer_CLOSED_CURLY_BRACKET():
    code = '}'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.CLOSED_CURL
    assert tokens[1].type == -1

#Testing ,
def test_lexer_COMMA():
    code = ','
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.COMMA
    assert tokens[1].type == -1

#Testing .
def test_lexer_DOT():
    code = '.'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.DOT
    assert tokens[1].type == -1

#Testing :
def test_lexer_COLON():
    code = ':'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.COLON
    assert tokens[1].type == -1

#Testing =
def test_lexer_EQUALS_SIGN():
    code = '='
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.EQUAL_SIGN
    assert tokens[1].type == -1

#<--------------------White spaces-------------------->

#Testing if whitespaces are recognized
def test_lexer_whitespace():
    code = '  1  1  \n  1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.INT
    assert tokens[1].type == DungeonLexer.INT
    assert tokens[2].type == DungeonLexer.INT
    assert tokens[3].type == -1