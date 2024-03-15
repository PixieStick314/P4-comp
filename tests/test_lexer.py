from grammar_files.generated.RogueLangLexer import RogueLangLexer
from antlr4 import CommonTokenStream, InputStream


def get_tokens_from_string(str):
    lexer = RogueLangLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    stream.fill()
    tokens = stream.tokens
    return tokens


def test_lexer_ID():
    code = 'my_var1'
    tokens = get_tokens_from_string(code)

    # Doing it this way means if token order changes, we have to rewrite the tests
    assert tokens[0].type == RogueLangLexer.ID
    assert tokens[1].type == -1 # -1 corresponds to type EOF

def test_lexer_INT():
    code = '1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.INT
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
    code = 'true'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == RogueLangLexer.TRUE
    assert tokens[1].type == -1