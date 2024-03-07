from grammar_files.generated.RogueLangLexer import RogueLangLexer
from antlr4 import CommonTokenStream, InputStream


def get_tokens_from_str(str):
    lexer = RogueLangLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    stream.fill()
    tokens = stream.tokens
    return tokens

def test_lexer_ID():
    code = 'myVar'
    tokens = get_tokens_from_str(code)

    assert tokens[0].type == 16
    assert tokens[1].type == -1

def test_lexer_INT():
    code = '1'
    tokens = get_tokens_from_str(code)

    assert tokens[0].type == 17 # INT is currently type 17
    assert tokens[1].type == -1 # -1 corresponds to type EOF

def test_lexer_STRING():
    code = '"hello"'
    tokens = get_tokens_from_str(code)

    assert tokens[0].type == 18
    assert tokens[1].type == -1