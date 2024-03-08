grammar RogueLang;

// Parser Rules
prog:   stat+ ;

stat:   printStat
      | varDecl
      | ifStat
      | forLoop
      | foreachLoop
      | whileLoop
      | functionDecl
      | functionCall
      | arrayInit
      | enumDecl
      | expr
      ;

printStat         : 'print' '(' expr ')' ';' ;
varDecl           : 'var' dataType ID ('=' expr | arrayInit)? ';' ;
dataType          : baseType ('[' ']')? ;
baseType          : 'int' | 'string' | 'bool' | 'double' | ID | 'date' | 'time' | 'dateTime' ; 
ifStat            : 'if' '(' expr ')' '{' stat* '}' ('else' '{' stat* '}')? ';' ;
forLoop           : 'for' '(' varDecl expr ';' expr ')' '{' stat* '}' ';' ;
foreachLoop       : 'foreach' '(' varDecl 'in' expr ')' '{' stat* '}' ';' ; 
whileLoop         : 'while' '(' expr ')' '{' stat* '}' ';' ;
functionDecl      : 'function' ID '(' params? ')' '{' stat* '}' ';' ;
functionCall      : ID '(' args? ')' ';' ;
arrayInit         : '{' expr (',' expr)* '}' ';' ; //initialization with value
params            : param (',' param)* ;
param             : dataType ID ;
args              : expr (',' expr)* ;
expr              : expr '[' expr ']'     //Accessing an array element
                  | expr '[' expr ']' '=' expr //Assinging to an array element
                  | expr '.add(' expr ')'   //Method to add an element to a dynamically sized array
                  | expr op=('*' | '/') expr
                  | expr op=('+' | '-') expr
                  | expr op=('<' | '<=' | '>' | '>=' | '==' | '!=') expr
                  | '(' expr ')'
                  | ID
                  | INT
                  | STRING
                  | DOUBLE
                  | TRUE
                  | FALSE
                  | DATE
                  | TIME
                  | DATETIME
                  | randomInt
                  | randomChoice
                  | enumValue
                  ;

randomInt         : 'randomInt' '(' INT ',' INT ')' ;
randomChoice      : 'randomChoice' '(' expr (',' expr)+ ')' ;
enumDecl          : 'enum' ID '{' enumBody'}' ;
enumBody          : ID (',' ID)* ;
enumValue         : ID '.' ID ;


// Lexer Rules
PLUS              : '+' ;
MINUS             : '-' ;
MULT              : '*' ;
DIV               : '/' ;
ID                : LETTER (LETTER | NUMBER)* ;
INT               : NUMBER+ ;
STRING            : '"' (ESC | ~["\\])* '"' ; // Use fragment for escaped characters
DOUBLE            : NUMBER+ '.' NUMBER+ ;
TRUE              : 'true' ;
FALSE             : 'false' ;
DATE              : NUMBER NUMBER NUMBER NUMBER '-' NUMBER NUMBER '-' NUMBER NUMBER ;
TIME              : NUMBER NUMBER ':' NUMBER NUMBER ':' NUMBER NUMBER ;
DATETIME          : DATE ',' TIME ;

fragment LETTER : [a-zA-Z_]; // 
fragment ESC    : '\\' (['"\\tn]); // Define ESC for escape sequences in strings, doesn't work
fragment NUMBER : [0-9_]; // 

WS       : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines