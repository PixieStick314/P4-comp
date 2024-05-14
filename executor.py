#   Executor.py
import sys
import argparse
import os
from antlr4 import *
from grammar_files.generated.DungeonLexer import DungeonLexer
from grammar_files.generated.DungeonParser import DungeonParser
from modules.Interpreter.Interpreter import Interpreter
from modules.executorHelper import check_verbose

# Add the path to the generated files so they can be imported
sys.path.append(os.path.join(os.path.dirname(__file__),
                '..', 'grammar_files', 'generated'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

# verbose = any(flag in sys.argv for flag in [
#               "-v", "--v", "-verbose", "--verbose"])
# path_given = any(flag in sys.argv for flag in ["-p", "--p", "-path", "--path"])


def executor(file_path, verbose=False):
    lexer = DungeonLexer(FileStream(file_path))
    stream = CommonTokenStream(lexer)
    parser = DungeonParser(stream)
    tree = parser.prog()

    visitor = Interpreter()  # Create Interpreter instance
    visitor.set_verbose(verbose)  # Set verbosity flag
    output = visitor.visit(tree)

    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A compiler for the dngn language")
    parser.add_argument('-p', '--p', '-path', '--path', metavar="PARAM",
                        type=str, help='Parameter for file path of script to compile')
    parser.add_argument('-v', '--v', '-verbose', '--verbose', action='store_true',
                        help="If flag is present, verbose mode will be enabled")
    args = parser.parse_args()
    verbose = args.v

    if args.p:
        file_path = args.p
        result = executor(file_path, verbose)
    else:
        input_file = input('Enter the input file path: ')
        result = executor(input_file, verbose)

    print(result)
