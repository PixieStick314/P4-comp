#   Executor.py
import sys
import os
# Add the path to the generated files so they can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'grammar_files', 'generated'))

from antlr4 import *
from grammar_files.generated.RogueLangLexer import RogueLangLexer
from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangVisitor import RogueLangVisitor
from modules.Strategy.LanguageStrategy import LanguageStrategy
from RogueVisitor import RogueVisitor
from modules.Strategy.PythonStrategy import PythonStrategy
from modules.Strategy.CppStrategy import CppStrategy
from modules.Strategy.RustStrategy import RustStrategy


def print_help():
    help_message = """
Usage: python executor.py <file name> <language> <output file name> [options]

<file name>: The path to the input file to be processed.
<language>: The target language for the output. Supported values are python, cpp, rust.
[options]: Additional options for execution, such as --verbose for detailed logging.

Examples:
python executor.py example.rogue python
python executor.py example.rogue cpp --verbose

Supported Languages:
Python

Type python executor.py --help for additional help
"""
    print(help_message)
    sys.exit(0)

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("--help", "-help", "-h"):
        print_help()

    # Initialize variables with None
    input_file = None
    language = "Python"
    output_filename = None

    # Assign command line arguments if they exist
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        language = sys.argv[2]
    if len(sys.argv) > 3:
        output_filename = sys.argv[3]

    # Prompt for missing arguments
    if not input_file:
        input_file = input("Enter the input file path: ")
    if not language:
        language = input("Enter the target language (python, cpp, rust)[python]: ")
    if not output_filename:
        output_filename = input("Enter the output file name (optional, press enter to skip): ")

    # Choose the strategy based on the language argument
    strategy = None
    suffix = None

    # Choose the strategy based on the language argument
    if language == "python":
        strategy = PythonStrategy()
        suffix = '.py'
    elif language == "cpp":
        strategy = CppStrategy()
        suffix = '.cpp'
    elif language == "rust":
        strategy = RustStrategy()
        suffix = 'rs'
    else:
        print(f"Unsupported language: {language}. Defaulting to Python.")
        language = "python"
        strategy = PythonStrategy()
        suffix = '.py'

    # Create the lexer and parser
    lexer = RogueLangLexer(FileStream(input_file))
    stream = CommonTokenStream(lexer)
    parser = RogueLangParser(stream)
    
    # Parse the input file to generate the parse tree
    tree = parser.prog()

    # Visit the parse tree
    visitor = RogueVisitor(strategy)
    visitor.visit(tree)

    # Determine output filename based on user input or default naming
    if not output_filename.strip():
        # Default output filename if not provided
        output_filename = f"{input_file.rsplit('.', 1)[0]}_{language}{suffix}"
    else:
        # Append language suffix if custom output filename is provided
        output_filename = f"{output_filename}{suffix}"

    
    with open(output_filename, "w") as output_file:
        output_file.write(visitor.output_buffer)
    print(f"Generated code has been written to {output_filename}")
    

# This is to enable testing, but does literally the same thing, it's just callable
def execute_rogue_script(file_path):
    input_stream = FileStream(file_path)
    lexer = RogueLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RogueLangParser(stream)
    tree = parser.prog()

    visitor = RogueVisitor()
    visitor.visit(tree)


if __name__ == '__main__':
    main()
