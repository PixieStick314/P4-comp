#   test_lexer.py
from _pytest.mark.expression import TokenType

from grammar_files.generated.DungeonLexer import DungeonLexer
from antlr4 import CommonTokenStream, InputStream


def get_tokens_from_string(str):
    lexer = DungeonLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    stream.fill()
    tokens = stream.tokens
    return tokens

def test_lexer_PLUS():
    code = '+'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.PLUS
    assert tokens[1].type == -1

def test_lexer_MINUS():
    code = '-'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.MINUS
    assert tokens[1].type == -1

def test_lexer_MULT():
    code = '*'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.MULT
    assert tokens[1].type == -1

def test_lexer_DIV():
    code = '/'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.DIV
    assert tokens[1].type == -1

def test_lexer_MOD():
    code = '%'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.MOD
    assert tokens[1].type == -1

def test_lexer_ID():
    code = 'my_var1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.ID
    assert tokens[1].type == -1

def test_lexer_INT():
    code = '1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.INT
    assert tokens[1].type == -1

def test_lexer_DOUBLE():
    code = '1.1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.FLOAT
    assert tokens[1].type == -1

def test_lexer_STRING():
    code = '"hello"'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.STRING
    assert tokens[1].type == -1

def test_lexer_multiple_tokens():
    code = 'my_var1 1 "hello"'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.ID
    assert tokens[1].type == DungeonLexer.INT
    assert tokens[2].type == DungeonLexer.STRING
    assert tokens[3].type == -1

def test_lexer_TRUE():
    code = 'True'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.TRUE
    assert tokens[1].type == -1

def test_lexer_FALSE():
    code = 'False'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.FALSE
    assert tokens[1].type == -1

def test_lexer_dot():
    code = '.'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.DOT
    assert tokens[1].type == -1

def test_lexer_whitespace():
    code = '  1  1  \n  1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.INT
    assert tokens[1].type == DungeonLexer.INT
    assert tokens[2].type == DungeonLexer.INT
    assert tokens[3].type == -1

def test_lexer_nested_if_stat():
    code = '''if(x == 5){
    x = 4
    if(x == 4){
    x = 3
    }
    }
    '''

    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.IF
    assert tokens[1].type == DungeonLexer.OPEN_PARENTH
    assert tokens[2].type == DungeonLexer.ID
    assert tokens[3].type == DungeonLexer.EQ
    assert tokens[4].type == DungeonLexer.INT
    assert tokens[5].type == DungeonLexer.CLOSED_PARENTH
    assert tokens[6].type == DungeonLexer.OPEN_CURL
    assert tokens[7].type == DungeonLexer.ID
    assert tokens[8].type == DungeonLexer.EQUAL_SIGN
    assert tokens[9].type == DungeonLexer.INT
    assert tokens[10].type == DungeonLexer.IF
    assert tokens[11].type == DungeonLexer.OPEN_PARENTH
    assert tokens[12].type == DungeonLexer.ID
    assert tokens[13].type == DungeonLexer.EQ
    assert tokens[14].type == DungeonLexer.INT
    assert tokens[15].type == DungeonLexer.CLOSED_PARENTH
    assert tokens[16].type == DungeonLexer.OPEN_CURL
    assert tokens[17].type == DungeonLexer.ID
    assert tokens[18].type == DungeonLexer.EQUAL_SIGN
    assert tokens[19].type == DungeonLexer.INT
    assert tokens[20].type == DungeonLexer.CLOSED_CURL
    assert tokens[21].type == DungeonLexer.CLOSED_CURL

def test_lexer_plus_equals():
    code = '+='
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.PEQ

def test_lexer_struct_assign():
    code = 'Cat {says = "meow"}'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.ID
    assert tokens[1].type == DungeonLexer.OPEN_CURL
    assert tokens[2].type == DungeonLexer.ID
    assert tokens[3].type == DungeonLexer.EQUAL_SIGN
    assert tokens[4].type == DungeonLexer.STRING
    assert tokens[5].type == DungeonLexer.CLOSED_CURL

def test_sqrt_op():
    code = 'sqrt(9)'

    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.SQRT
    assert tokens[1].type == DungeonLexer.OPEN_PARENTH
    assert tokens[2].type == DungeonLexer.INT
    assert tokens[3].type == DungeonLexer.CLOSED_PARENTH

def test_pow():
    code = 'pow(1,2)'

    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.POW
    assert tokens[1].type == DungeonLexer.OPEN_PARENTH
    assert tokens[2].type == DungeonLexer.INT
    assert tokens[3].type == DungeonLexer.COMMA
    assert tokens[4].type == DungeonLexer.INT
    assert tokens[5].type == DungeonLexer.CLOSED_PARENTH

def test_seed():
    code = 'seed(7)'

    tokens = get_tokens_from_string(code)

    assert tokens[0].type == DungeonLexer.SEED
    assert tokens[1].type == DungeonLexer.OPEN_PARENTH
    assert tokens[2].type == DungeonLexer.INT
    assert tokens[3].type == DungeonLexer.CLOSED_PARENTH
