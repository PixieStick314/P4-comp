import sys
import os
# Add the path to the generated files so they can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'grammar_files', 'generated'))

from antlr4 import *
from grammar_files.generated.RogueLangLexer import RogueLangLexer
from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangVisitor import RogueLangVisitor
from rogue_visitor import RogueVisitor

def main():
    # if length of command is < 2, exit
    if len(sys.argv) < 2:
        print("Usage: python executor.py <file name>")
        print("Type python executor.py --help, -help, -h for additional help") #TODO: actually implement this
        sys.exit(1)

    file_name = sys.argv[1]

    # Create the lexer and parser
    lexer = RogueLangLexer(FileStream(file_name))
    stream = CommonTokenStream(lexer)
    parser = RogueLangParser(stream)
    
    # Parse the input file to generate the parse tree
    tree = parser.prog()

    # Visit the parse tree
    visitor = RogueVisitor()
    visitor.visit(tree)

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
