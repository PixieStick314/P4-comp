grammar RogueLang;

prog:   object (stat)* ;

object: ID OPEN_CURL procedure (field | stat)* CLOSED_CURL;

procedure: PROCEDURE statBlock;

stat:   printStat
      | varDecl
      | functionDecl
      | ifStat
      | forLoop
      | whileLoop
      | statBlock
      | returnStat
      | expr;

field             : 'field' varDecl;
varDecl           : ID  (EQUAL_SIGN (expr | functionCall))?;
functionDecl      : DEF ID OPEN_PARENTH params? CLOSED_PARENTH statBlock;
printStat         : PRINT OPEN_PARENTH expr CLOSED_PARENTH;
ifStat            : IF OPEN_PARENTH expr CLOSED_PARENTH statBlock elifStat? elseStat?;
elifStat          : ELIF OPEN_PARENTH expr CLOSED_PARENTH statBlock elifStat?;
elseStat          : ELSE statBlock;
statBlock         : OPEN_CURL stat* CLOSED_CURL;
forLoop           : FOR varDecl IN expr statBlock;
whileLoop         : WHILE OPEN_PARENTH expr CLOSED_PARENTH statBlock;
functionCall      : ID OPEN_PARENTH args? CLOSED_PARENTH;
returnStat        : RETURN expr;
params            : param (COMMA param)* ;
param             : ID ;
args              : expr (COMMA expr)* ;
expr              : functionCall
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