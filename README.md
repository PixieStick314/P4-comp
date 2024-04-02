#   Using the Language



#   Extending the language

This guide outlines the process of adding new functionalities to the programming language: RogueLang, including extending the grammar, updating the parser and visitor classes, and enhancing the language strategies to support code generation in multiple target languages.

## Table of Contents

- [Step 1: Modify the Grammar](#step-1-modify-the-grammar)
- [Step 2: Regenerate Parser and Lexer](#step-2-regenerate-parser-and-lexer)
- [Step 3: Update the Visitor Class](#step-3-update-the-visitor-class)
- [Step 4: Extend the LanguageStrategy Interface](#step-4-extend-the-languagestrategy-interface)
- [Step 5: Implement Strategy Methods](#step-5-implement-strategy-methods)
- [Step 6: Test Your Extensions](#step-6-test-your-extensions)
- [Step 7: Documentation](#step-7-documentation)

###  Step 1: Modify the grammar

Start by updating the grammar definition file (`RogueLang.g4` file). Add new rules or modify existing ones to reflect the new language features.

```antlr
// Example of adding a new grammar rule for switch-case statements
switchStatement
    : 'switch' 'openParenthesies' expression 'closedParenthesies' 'openBrace' caseStatement* defaultStatement? 'closeBrace'
    ;
```

###  Step 2: Reenerate parser and lexer

Run antlr4_run.bat to regenerate the parser, lexer, and visitor files.

###  Step 3: Update the visitor class

Adjust your custom visitor class to handle the new grammar constructs, generating appropriate code strings or performing other actions as needed.

```RogueVisitor.py
// Example of extending the visitor to handle a new construct
class RogueVisitor(YourLanguageVisitor):
    def visitSwitchStatement(self, ctx):
        # Logic for visiting the switch statement
        pass
```

###  Step 4: Extend the LanguageStrategy interface

Enhance the LanguageStrategy interface with methods corresponding to the new language features, ensuring all strategy classes will implement them.

```LanguageStrategy.py
class LanguageStrategy:
    def switch_statement(self, expression, cases, default):
        raise NotImplementedError
```

###  Step 5: Implement Strategy Methods

Implement the new methods in each concrete strategy class, such as PythonStrategy, CppStrategy, etc., to support code generation for the new features.

```PythonStrategy.py
class PythonStrategy(LanguageStrategy):
    def switch_statement(self, expression, cases, default):
        # Python-specific implementation
        pass
```
###  Step 6: Test your extensions

Thoroughly test the new language features across all target languages, ensuring correct behavior and syntax generation.

###  Step 7: Documentation

Update the language's documentation to include the new features, providing usage examples and highlighting any limitations.