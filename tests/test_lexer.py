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

    assert tokens[0].type == RogueLangLexer.NUMBER
    assert tokens[1].type == -1

def test_lexer_DOUBLE():
    code = '1.1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.NUMBER
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
    assert tokens[1].type == RogueLangLexer.NUMBER
    assert tokens[2].type == RogueLangLexer.STRING
    assert tokens[3].type == -1

def test_lexer_TRUE():
    code = 'true'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.TRUE
    assert tokens[1].type == -1

def test_lexer_FALSE():
    code = 'false'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.FALSE
    assert tokens[1].type == -1

def test_lexer_whitespace():
    code = '  1  1  \n  1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.NUMBER
    assert tokens[1].type == RogueLangLexer.NUMBER
    assert tokens[2].type == RogueLangLexer.NUMBER
    assert tokens[3].type == -1