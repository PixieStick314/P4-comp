grammar RogueLang;

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
varDecl           : 'var' dataType ID  ('=' expr | arrayInit | args)? ';' ;
dataType          : baseType ('[' ']')? ;
baseType          : 'int' | 'string' |'true' | 'false' | 'bool' | 'double' | ID | 'date' | 'time' | 'dateTime' ; 
ifStat            : 'if' '(' expr ')' '{' stat* '}' ('else' '{' stat* '}')? ';' ;
forLoop           : 'for' '(' varDecl expr ';' expr ')' '{' stat* '}' ';' ;
foreachLoop       : 'foreach' '(' varDecl 'in' expr ')' '{' stat* '}' ';' ; 
whileLoop         : 'while' '(' expr ')' '{' stat* '}' ';' ;
functionDecl      : 'function' ID '(' params? ')' '{' stat* '}' ';' ;
functionCall      : ID '(' args? ')' ';' ;
arrayInit         : '{' expr (',' expr)* '}' ';' ; //initialization with value
bsp               : 'BSP' bspDimension bspParameters ;
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
                  | BOOL
                  | DATE
                  | TIME
                  | DATETIME
                  | randomInt
                  | randomChoice
                  | enumValue
                  ;


// Lexer Rules
PLUS              : '+' ;
MINUS             : '-' ;
MULT              : '*' ;
DIV               : '/' ;
MOD               : '%' ;
TRUE              : 'true' ;
FALSE             : 'false' ;
BOOL              : 'bool' ;
ID                : LETTER (LETTER | NUMBER)* ;
INT               : NUMBER+ ;
STRING            : '"' (ESC | ~["\\])* '"' ; // Use fragment for escaped characters
DOUBLE            : NUMBER+ '.' NUMBER+ ;
DATE              : NUMBER NUMBER NUMBER NUMBER '-' NUMBER NUMBER '-' NUMBER NUMBER ;
TIME              : NUMBER NUMBER ':' NUMBER NUMBER ':' NUMBER NUMBER ;
DATETIME          : DATE ',' TIME ;
randomInt         : 'randomInt' '(' INT ',' INT ')' ;
randomChoice      : 'randomChoice' '(' expr (',' expr)+ ')' ;
enumDecl          : 'enum' ID '{' enumBody'}' ;
enumBody          : ID (',' ID)* ;
enumValue         : ID '.' ID ;
bspDimension      : '2D' | '3D' | INT 'D' ; // INT 'D' allows for specifying dimensions beyond 3
bspParameters     : '(' dimensionList ',' minSize ')' ;
dimensionList     : INT (',' INT)* ; // A list of integers representing the sizes in each dimension
minSize           : INT ; // Minimum size for partitioning

fragment LETTER : [a-zA-Z_]; // 
fragment ESC    : '\\' (['"\\tn]); // Define ESC for escape sequences in strings, doesn't work
fragment NUMBER : [0-9_]; // 

WS       : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines