grammar RogueLang;

prog:   stat+ ;

stat:   printStat
      | varDecl
      | ifStat
      | forLoop
      | whileLoop
      | functionDecl
      | functionCall
      | arrayInit
      | expr
      ;

printStat         : PRINT OPEN_PARENTH expr CLOSED_PARENTH;
varDecl           : ID  (EQUAL_SIGN expr | arrayInit | args)?;
dataType          : baseType (OPEN_BRACK CLOSED_BRACK )? ;
baseType          : 'string' |'True' | 'False' | 'bool' | 'number' | ID;
ifStat            : IF OPEN_PARENTH expr CLOSED_PARENTH statBlock (ELIF OPEN_PARENTH expr CLOSED_PARENTH statBlock)* (ELSE statBlock)?;
statBlock         : OPEN_CURL stat* CLOSED_CURL;
forLoop           : FOR varDecl IN expr OPEN_CURL stat* CLOSED_CURL;
whileLoop         : WHILE OPEN_PARENTH expr CLOSED_PARENTH OPEN_CURL stat* CLOSED_CURL;
functionDecl      : DEF ID OPEN_PARENTH params? CLOSED_PARENTH OPEN_CURL stat* CLOSED_CURL;
functionCall      : ID OPEN_PARENTH args? CLOSED_PARENTH;
arrayInit         : OPEN_CURL expr (COMMA expr)* CLOSED_CURL;
params            : param (COMMA param)* ;
param             : ID ;
args              : expr (COMMA expr)* ;
expr              : functionCall
                  | expr OPEN_BRACK expr CLOSED_BRACK     //Accessing an array element
                  | expr OPEN_BRACK expr CLOSED_BRACK EQUAL_SIGN expr //Assinging to an array element
                  | expr DOT 'add' OPEN_PARENTH expr CLOSED_PARENTH   //Method to add an element to a dynamically sized array
                  | expr op=(MULT | DIV | MOD) expr
                  | expr op=(PLUS| MINUS) expr
                  | expr op=(GT | GTE | LT | LTE | EQ | NEQ) expr
                  | expr op=(AND | OR) expr
                  | NOT expr
                  | OPEN_PARENTH expr CLOSED_PARENTH
                  | ID
                  | STRING
                  | NUMBER
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
MOD               : '%' ;
AND               : 'and';
OR                : 'or';
NOT               : 'not';
TRUE              : 'True' ;
FALSE             : 'False' ;
COMMENT_SINGLELINE: '//' ~[\r\n]* -> skip ;
NUMBER            : '-'? NUMB + | '-'? NUMB+ '.' NUMB+ ;
STRING            : '"' (ESC | ~["\\])* '"' ; // Use fragment for escaped characters
ID                : LETTER (LETTER | NUMB)* ;

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
fragment NUMB             : [0-9_];

WS       : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines