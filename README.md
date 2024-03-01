How to use.

Pre-requisites:
    -python3,
    -java,
    downloading this and putting it in the root project folder: https://www.antlr.org/download/antlr-4.13.1-complete.jar
    idk what else, might be something, might not, let me know.

Steps:
    1:  Write the RogueLang.g4 file, idk how this shit works yet.
    2:  In a terminal, run: .\antlr4_run.bat
        I:  This generates the /grammar_files/generated Parser and Lexer files.
    3:  Write the executor.py file
        I: These lines set up the lexer and parser for parsing the .rogue file:
            Ia: FileStream(file_name) creates a stream to read from the specified file.
            Ib: RogueLangLexer(FileStream(file_name)) creates a lexer instance for tokenizing the file content.
            Ic: CommonTokenStream(lexer) generates a stream of tokens from the lexer output.
            Id: RogueLangParser(stream) creates a parser instance with the token stream to parse the tokens according to the grammar rules.
        II: tree = parser.prog()
            IIa: This line invokes the prog rule on the parser to parse the entire content of the .rogue file, resulting in a parse tree.¨
        III: visitor = RogueExecutor(), visitor.visit(tree)
            IIIa: visitor.visit(tree) begins the traversal of the parse tree. For each node in the tree, the corresponding method in RogueExecutor is called, executing the code written in your .rogue file. 
    4:  Write the rogue_executor.py file
        I:  This is where we'll probably be spending most of our time.
    5:  In the terminal, run either:
        python .\src\executor.py .\tests\test_files\"filename".rogue
        or:
        python .\tests\test_executor.py to run the whole shebang at once. For now, doesn't work.
    6:  That's fucking it!

TODO:
    Figure out why the fuck test_executor.py isn't fucking working!
    executor.py:
        Make a sys.argv response lib for testing
    
    rogue_executor.py:
        Add arithmetic, conditionals, loops, and variables.