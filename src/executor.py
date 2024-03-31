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

def main():
    # if length of command is < 2, exit
    if len(sys.argv[1]) < 2:
        print("Usage: python executor.py <file name>")
        print("Type python executor.py --help, -help, -h for additional help") #TODO: actually implement this
        sys.exit(1)

    input_file = sys.argv[1]
    language = sys.argv[2]

    # Choose the strategy based on the language argument
    if language == "python":
        strategy = PythonStrategy()
        suffix = '.py'
    elif language == "cpp":
        strategy = CppStrategy()
        suffix = '.cpp'
    elif language == "rust":
        strategy = RustStrategy()
        suffix = 'rust?'
    else:
        print(f"Unsupported language: {language}")
        sys.exit(1)

    # Create the lexer and parser
    lexer = RogueLangLexer(FileStream(input_file))
    stream = CommonTokenStream(lexer)
    parser = RogueLangParser(stream)
    
    # Parse the input file to generate the parse tree
    tree = parser.prog()

    # Visit the parse tree
    visitor = RogueVisitor(strategy)
    visitor.visit(tree)

    # Generate output filename
    output_filename = f"{input_file.rsplit('.', 1)[0]}_{language}{suffix}"
    
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
