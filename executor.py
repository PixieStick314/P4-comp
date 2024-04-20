#   Executor.py
import sys
import os
from antlr4 import *
from grammar_files.generated.RogueLangLexer import RogueLangLexer
from grammar_files.generated.RogueLangParser import RogueLangParser
from modules.Interpreter.Interpreter import Interpreter

# Add the path to the generated files so they can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'grammar_files', 'generated'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))


def executor(file_path):
    lexer = RogueLangLexer(FileStream(file_path))
    stream = CommonTokenStream(lexer)
    parser = RogueLangParser(stream)
    tree = parser.prog()

    visitor = Interpreter()
    output = visitor.visit(tree)
    return output


if __name__ == '__main__':
    input_file = input('Enter the input file path: ')
    result = executor(input_file)
    print(result)
