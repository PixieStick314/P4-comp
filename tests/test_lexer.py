#   test_lexer.py
from _pytest.mark.expression import TokenType

from grammar_files.generated.RogueLangLexer import RogueLangLexer
from antlr4 import CommonTokenStream, InputStream


def get_tokens_from_string(str):
    lexer = RogueLangLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    stream.fill()
    tokens = stream.tokens
    return tokens

def test_lexer_PLUS():
    code = '+'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.PLUS
    assert tokens[1].type == -1

def test_lexer_MINUS():
    code = '-'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.MINUS
    assert tokens[1].type == -1

def test_lexer_MULT():
    code = '*'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.MULT
    assert tokens[1].type == -1

def test_lexer_DIV():
    code = '/'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.DIV
    assert tokens[1].type == -1

def test_lexer_MOD():
    code = '%'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.MOD
    assert tokens[1].type == -1

def test_lexer_ID():
    code = 'my_var1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.ID
    assert tokens[1].type == -1

def test_lexer_INT():
    code = '1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.INT
    assert tokens[1].type == -1

def test_lexer_DOUBLE():
    code = '1.1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.FLOAT
    assert tokens[1].type == -1

def test_lexer_STRING():
    code = '"hello"'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.STRING
    assert tokens[1].type == -1

def test_lexer_multiple_tokens():
    code = 'my_var1 1 "hello"'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.ID
    assert tokens[1].type == RogueLangLexer.INT
    assert tokens[2].type == RogueLangLexer.STRING
    assert tokens[3].type == -1

def test_lexer_TRUE():
    code = 'True'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.TRUE
    assert tokens[1].type == -1

def test_lexer_FALSE():
    code = 'False'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.FALSE
    assert tokens[1].type == -1

def test_lexer_dot():
    code = '.'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.DOT
    assert tokens[1].type == -1

def test_lexer_whitespace():
    code = '  1  1  \n  1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.INT
    assert tokens[1].type == RogueLangLexer.INT
    assert tokens[2].type == RogueLangLexer.INT
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

    assert tokens[0].type == RogueLangLexer.IF
    assert tokens[1].type == RogueLangLexer.OPEN_PARENTH
    assert tokens[2].type == RogueLangLexer.ID
    assert tokens[3].type == RogueLangLexer.EQ
    assert tokens[4].type == RogueLangLexer.INT
    assert tokens[5].type == RogueLangLexer.CLOSED_PARENTH
    assert tokens[6].type == RogueLangLexer.OPEN_CURL
    assert tokens[7].type == RogueLangLexer.ID
    assert tokens[8].type == RogueLangLexer.EQUAL_SIGN
    assert tokens[9].type == RogueLangLexer.INT
    assert tokens[10].type == RogueLangLexer.IF
    assert tokens[11].type == RogueLangLexer.OPEN_PARENTH
    assert tokens[12].type == RogueLangLexer.ID
    assert tokens[13].type == RogueLangLexer.EQ
    assert tokens[14].type == RogueLangLexer.INT
    assert tokens[15].type == RogueLangLexer.CLOSED_PARENTH
    assert tokens[16].type == RogueLangLexer.OPEN_CURL
    assert tokens[17].type == RogueLangLexer.ID
    assert tokens[18].type == RogueLangLexer.EQUAL_SIGN
    assert tokens[19].type == RogueLangLexer.INT
    assert tokens[20].type == RogueLangLexer.CLOSED_CURL
    assert tokens[21].type == RogueLangLexer.CLOSED_CURL

def test_lexer_plus_equals():
    code = '+='
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.PEQ
