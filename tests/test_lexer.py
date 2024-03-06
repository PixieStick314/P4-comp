from grammar_files.generated.RogueLangLexer import RogueLangLexer
from antlr4 import CommonTokenStream, InputStream


def get_tokens_from_str(str):
    lexer = RogueLangLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    stream.fill()
    tokens = stream.tokens
    return tokens

def test_lexer_INT():
    code = '1'
    tokens = get_tokens_from_str(code)
    assert tokens == [
        1 # This should be the token type INT and the value 1, but I don't know how the lexer formats it
    ]
