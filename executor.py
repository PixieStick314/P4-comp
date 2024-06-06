#   Executor.py
import sys
import argparse
import os
from antlr4 import *
from grammar_files.generated.DungeonLexer import DungeonLexer
from grammar_files.generated.DungeonParser import DungeonParser
from modules.AST.ASTBuilder import ASTBuilder
from modules.Interpreter.Interpreter import Interpreter

# Add the path to the generated files so they can be imported
sys.path.append(os.path.join(os.path.dirname(__file__),
                '..', 'grammar_files', 'generated'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))


def executor(file_path, verbose):
    lexer = DungeonLexer(FileStream(file_path))
    stream = CommonTokenStream(lexer)
    parser = DungeonParser(stream)
    tree = parser.prog()

    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)

    visitor = Interpreter()
    visitor.set_verbose(verbose)
    output = visitor.visit(ast)

    return output


if __name__ == '__main__':
    # Sets up arg parsing
    parser = argparse.ArgumentParser(
        description="A compiler for the dngn language")
    # Adds path arg to provide script file path via cli
    parser.add_argument('-p', '--p', '-path', '--path', metavar="PARAM",
                        type=str, help='Parameter for file path of script to compile')
    # Adds verbose mode, set to false by default
    parser.add_argument('-v', '--v', '-verbose', '--verbose', action='store_true',
                        help="If flag is present, verbose mode will be enabled")
    args = parser.parse_args()

    # Sets verbose to args.v which is true if flag is present
    verbose = args.v

    if args.p:
        file_path = args.p
        result = executor(file_path, verbose)
    else:
        input_file = input('Enter the input file path: ')
        result = executor(input_file, verbose)

    print(result)
