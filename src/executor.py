#   Executor.py
import sys
import os
# Add the path to the generated files so they can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'grammar_files', 'generated'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from antlr4 import *
from grammar_files.generated.RogueLangLexer import RogueLangLexer
from grammar_files.generated.RogueLangParser import RogueLangParser

from ExecutorHelper import parse_arguments, print_help, get_visitor

def main():
    input_file, language, output_filename = parse_arguments()

    if not input_file or not language:
        print("Missing required arguments.")
        print_help()

    lexer = RogueLangLexer(FileStream(input_file))
    stream = CommonTokenStream(lexer)
    parser = RogueLangParser(stream)
    tree = parser.prog()

    suffix, visitor = get_visitor(language)
    generated_code = visitor.visit(tree)

    if not output_filename or not output_filename.strip():
        output_filename = f"{input_file.rsplit('.', 1)[0]}_{language}{suffix}"
    else:
        output_filename += suffix
    
    with open(output_filename, "w") as output_file:
        output_file.write(visitor.output_buffer)
    print(f"Generated code has been written to {output_filename}")

if __name__ == '__main__':
    main()
