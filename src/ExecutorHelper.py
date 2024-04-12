# ExecutorHelper.py
import sys
from modules.Interpreter.Visitor import Visitor

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
Python, C++, Rust

Type python executor.py --help for additional help
"""
    print(help_message)
    sys.exit(0)

def parse_arguments():
    # Initialize variables with default values
    input_file = None
    language = "python"  # Default to python if not specified
    output_filename = None

    # Check for help flag
    if len(sys.argv) > 1 and sys.argv[1] in ("--help", "-help", "-h"):
        print_help()

    # Assign command line arguments if they exist
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        language = sys.argv[2]
    if len(sys.argv) > 3:
        output_filename = sys.argv[3]

    return input_file, language, output_filename

def get_visitor(language):
    if language == "python":
        suffix = '.py'
        return suffix, Visitor()
    else:
        raise ValueError(f"Unsupported language: {language}")