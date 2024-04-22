grammar RogueLang;

prog:   object (stat)* ;

object: ID OPEN_CURL procedure (field | stat)* CLOSED_CURL;

procedure         : PROCEDURE statBlock;
field             : 'field' varDecl;

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
      | expr;

varDeclStat       : 'let' varDecl;
varDecl           : ID assignment?;
assignStat        : ID assignment;
assignment        : EQUAL_SIGN expr
                  | EQUAL_SIGN list;
functionDecl      : DEF ID OPEN_PARENTH params? CLOSED_PARENTH statBlock;
list              : OPEN_BRACK (expr (COMMA expr)*)? CLOSED_BRACK;
listElement       : ID OPEN_BRACK NUMBER CLOSED_BRACK
                  | ID OPEN_BRACK ID CLOSED_BRACK;
listLength        : 'len' OPEN_PARENTH ID CLOSED_PARENTH;
listPop           : ID DOT 'pop' OPEN_PARENTH CLOSED_PARENTH;
plusEquals        : ID PEQ expr;
minusEquals       : ID MEQ expr;
printStat         : PRINT OPEN_PARENTH expr CLOSED_PARENTH;
ifStat            : IF OPEN_PARENTH expr CLOSED_PARENTH statBlock elifStat? elseStat?;
elifStat          : ELIF OPEN_PARENTH expr CLOSED_PARENTH statBlock elifStat?;
elseStat          : ELSE statBlock;
statBlock         : OPEN_CURL stat* CLOSED_CURL;
forLoop           : FOR ID IN ID statBlock;
whileLoop         : WHILE OPEN_PARENTH expr CLOSED_PARENTH statBlock;
functionCall      : ID OPEN_PARENTH args? CLOSED_PARENTH;
params            : ID (COMMA ID)* ;
args              : expr (COMMA expr)* ;
returnStat        : RETURN expr;
random            : 'random' IN range
                  | 'random' IN ID;
range             : expr DOT DOT expr;
expr              : functionCall
                  | listElement
                  | listLength
                  | random
                  | expr op=(MULT | DIV | MOD) expr
                  | expr op=(PLUS| MINUS) expr
                  | expr op=(GT | GTE | LT | LTE | EQ | NEQ) expr
                  | expr op=(AND | OR) expr
                  | NOT expr
                  | OPEN_PARENTH expr CLOSED_PARENTH
                  | ID
                  | NUMBER
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

PROCEDURE        : 'procedure';

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
COMMENT_SINGLELINE: '//' ~[\r\n]* -> skip ;
NUMBER            : '-'? DIGIT + | '-'? DIGIT+ '.' DIGIT+ ;
STRING            : '"' (ESC | ~["\\])* '"' ; // Use fragment for escaped characters
ID                : LETTER (LETTER | DIGIT)* ;

OPEN_PARENTH     : '(' ;
CLOSED_PARENTH   : ')' ;
OPEN_BRACK       : '[' ;
CLOSED_BRACK     : ']' ;
OPEN_CURL        : '{' ;
CLOSED_CURL      : '}' ;
COMMA            : ',' ;
DOT              : '.' ;
EQUAL_SIGN       : '=' ;

fragment LETTER           : [a-zA-Z_];
fragment ESC              : '\\' (['"\\tn]); // Define ESC for escape sequences in strings, doesn't work
fragment DIGIT             : [0-9_];

WS       : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines