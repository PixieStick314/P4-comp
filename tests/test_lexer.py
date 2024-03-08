from grammar_files.generated.RogueLangLexer import RogueLangLexer
from antlr4 import CommonTokenStream, InputStream


def get_tokens_from_string(str):
    lexer = RogueLangLexer(InputStream(str))
    stream = CommonTokenStream(lexer)
    stream.fill()
    tokens = stream.tokens
    return tokens

def get_token_number(token_name):
    lexer_file = open('src/grammar_files/generated/RogueLang.tokens', 'r')
    lines = lexer_file.readlines()

    # I'm not sure this method will work for every future lexer rule, but currently it works
    for line in lines:
        if token_name in line:
            token_number = line.partition('=')
            return int(token_number[2].strip())

    return None


def test_lexer_ID():
    code = 'my_var1'
    tokens = get_tokens_from_string(code)

    # Doing it this way means if token order changes, we have to rewrite the tests
    assert tokens[0].type == get_token_number('ID')
    assert tokens[1].type == -1 # -1 corresponds to type EOF

def test_lexer_INT():
    code = '1'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == get_token_number('INT')
    assert tokens[1].type == -1

def test_lexer_STRING():
    code = '"hello"'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == get_token_number('STRING')
    assert tokens[1].type == -1

def test_lexer_multiple_tokens():
    code = 'my_var1 1 "hello"'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == get_token_number('ID')
    assert tokens[1].type == get_token_number('INT')
    assert tokens[2].type == get_token_number('STRING')
    assert tokens[3].type == -1

def test_lexer_TRUE():
    code = 'true'
    tokens = get_tokens_from_string(code)

    assert tokens[0].type == get_token_number('TRUE')
    assert tokens[1].type == -1