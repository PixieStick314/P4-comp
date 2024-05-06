grammar RogueLang;

// Main program structure
prog:   stat* outputObject stat* ;

// object definition: creates an object with a procedure and optional output fields
outputObject: 'output' type ID OPEN_CURL (outputField | stat)* procedure (outputField | stat)* CLOSED_CURL;
type        : 'Custom'
            | 'TileMap';
// Procedure definition: a block of statements that defines a procedure
procedure         : PROCEDURE statBlock;
// Output field: an output declaration with a variable
outputField       : 'output' varDecl;

stat:   printStat
      | varDeclStat
      | assignStat
      | functionDecl
      | ifStat
      | forLoop
      | whileLoop
      | statBlock
      | returnStat
      | plusEquals
      | minusEquals
      | listPop
      | whiteNoiseStat     // WhiteNoise statement
      | structDef
      | seed
      | expr;

// Variable declarations and assignments
varDeclStat       : 'let' varDecl;
varDecl           : ID assignment?;

assignStat        : ID structFieldAccess* listAccess* assignment;
assignment        : EQUAL_SIGN struct
                  | EQUAL_SIGN list
                  | EQUAL_SIGN expr;

// Function declaration and calls
functionDecl      : DEF ID OPEN_PARENTH params? CLOSED_PARENTH statBlock;
functionCall      : ID OPEN_PARENTH args? CLOSED_PARENTH;

// Array and list structures
list              : OPEN_BRACK (listElement (COMMA listElement)*)? CLOSED_BRACK;
listElement       : expr | list;
listAccess        : OPEN_BRACK INT CLOSED_BRACK
                  | OPEN_BRACK ID CLOSED_BRACK;
listLength        : 'len' OPEN_PARENTH ID CLOSED_PARENTH;
listPop           : ID DOT 'pop' OPEN_PARENTH CLOSED_PARENTH;

// Structs
struct            : ID OPEN_CURL (structField assignment)* CLOSED_CURL;
structDef         : 'struct' ID OPEN_CURL structField+ CLOSED_CURL;
structField       : ID;
structFieldAccess : DOT ID listAccess*;

// Basic operations and control flow
plusEquals        : ID PEQ expr;
minusEquals       : ID MEQ expr;
printStat         : PRINT OPEN_PARENTH expr CLOSED_PARENTH;
ifStat            : IF OPEN_PARENTH expr CLOSED_PARENTH statBlock elifStat? elseStat?;
elifStat          : ELIF OPEN_PARENTH expr CLOSED_PARENTH statBlock elifStat?;
elseStat          : ELSE statBlock;
statBlock         : OPEN_CURL stat* CLOSED_CURL;
forLoop           : FOR ID IN ID statBlock;
whileLoop         : WHILE OPEN_PARENTH expr CLOSED_PARENTH statBlock;
returnStat        : RETURN expr;

// Algorithm implementations and random
whiteNoiseStat    : 'WhiteNoise' '(' ID (',' range)? ')' LAYER?;
random            : RANDOM IN range
                  | RANDOM IN ID;

seed              : SEED OPEN_PARENTH expr CLOSED_PARENTH;
range             : expr DOT DOT expr;

// Helpers
params            : ID (COMMA ID)* ;
args              : expr (COMMA expr)* ;

// Expression structures
expr              : functionCall
                  | ID structFieldAccess+
                  | ID listAccess+
                  | listLength
                  | random
                  | expr op=(MULT | DIV | MOD) expr
                  | expr op=(PLUS| MINUS) expr
                  | expr op=(GT | GTE | LT | LTE | EQ | NEQ) expr
                  | expr op=(AND | OR) expr
                  | NOT expr
                  | SQRT OPEN_PARENTH expr CLOSED_PARENTH
                  | POW OPEN_PARENTH expr COMMA expr CLOSED_PARENTH
                  | OPEN_PARENTH expr CLOSED_PARENTH
                  | ID
                  | INT
                  | FLOAT
                  | STRING
                  | TRUE
                  | FALSE
                  ;

// keywords
IF               : 'if';
ELIF             : 'elif';
ELSE             : 'else';         

RETURN           : 'return';
PRINT            : 'print' ;
FOR              : 'for' ;
IN               : 'in' ;
WHILE            : 'while' ;
DEF              : 'def' ;
LAYER            : 'layer';
PROCEDURE        : 'procedure';
SEED             : 'seed' ;
RANDOM           : 'random';

// Lexer Rules
PLUS              : '+' ;
MINUS             : '-' ;
MULT              : '*' ;
DIV               : '/' ;
GT                : '>' ;
GTE               : '>=';
LT                : '<' ;
LTE               : '<=';
EQ                : '==';
NEQ               : '!=';
PEQ               : '+=';
MEQ               : '-=';
MOD               : '%' ;
AND               : 'and';
OR                : 'or';
NOT               : 'not';
TRUE              : 'True' ;
FALSE             : 'False' ;
SQRT              : 'sqrt' ;
POW               : 'pow' ;

// Single line comments
COMMENT_SINGLELINE: '//' ~[\r\n]* -> skip ;

// Lexer rules for common tokens
INT               : '-'? DIGIT+;
FLOAT             : '-'? DIGIT+ '.' DIGIT+;
STRING            : '"' (ESC | ~["\\])* '"' ; // Use fragment for escaped characters
ID                : LETTER (LETTER | DIGIT)* ;

// Opening and closing symbols
OPEN_PARENTH     : '(' ;
CLOSED_PARENTH   : ')' ;
OPEN_BRACK       : '[' ;
CLOSED_BRACK     : ']' ;
OPEN_CURL        : '{' ;
CLOSED_CURL      : '}' ;
COMMA            : ',' ;
DOT              : '.' ;
EQUAL_SIGN       : '=' ;

// Lexer fragments for character components
fragment LETTER           : [a-zA-Z_];
fragment ESC              : '\\' (['"\\tn]); // Define ESC for escape sequences in strings, doesn't work
fragment DIGIT             : [0-9_];

// Whitespace handling
WS       : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines