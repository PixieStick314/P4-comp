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
      | enumDecl
      | expr
      ;

printStat         : 'print' openParenth expr closedParenth;
varDecl           : dataType ID  ('=' expr | arrayInit | args)?;
dataType          : baseType (openBrack closedBrack )? ;
baseType          : 'int' | 'string' |'true' | 'false' | 'bool' | 'double' | ID | 'date' | 'time' | 'dateTime' ; 
ifStat            : 'if' openParenth expr closedParenth openCurlBrack stat* closedCurlBrack ('else' openCurlBrack stat* closedCurlBrack)?;
forLoop           : 'for' varDecl 'in' expr openCurlBrack stat* closedCurlBrack;
whileLoop         : 'while' openParenth expr closedParenth openCurlBrack stat* closedCurlBrack;
functionDecl      : 'def' ID openParenth params? closedParenth openCurlBrack stat* closedCurlBrack;
functionCall      : ID openParenth args? closedParenth;
arrayInit         : openCurlBrack expr (comma expr)* closedCurlBrack; //initialization with value
bsp               : 'BSP' bspDimension bspParameters ;
params            : param (comma param)* ;
param             : dataType ID ;
args              : expr (comma expr)* ;
randomInt         : 'randomInt' openParenth INT comma INT closedParenth ;
randomChoice      : 'randomChoice' openParenth expr (comma expr)+ closedParenth ;
enumDecl          : 'enum' ID openCurlBrack enumBody closedCurlBrack ;
enumBody          : ID (comma ID)* ;
enumValue         : ID '.' ID ;
bspDimension      : '2D' | '3D' | INT 'D' ; // INT 'D' allows for specifying dimensions beyond 3
bspParameters     : openParenth dimensionList comma minSize closedParenth ;
dimensionList     : INT (comma INT)* ; // A list of integers representing the sizes in each dimension
minSize           : INT ; // Minimum size for partitioning
expr              : expr openBrack expr closedBrack     //Accessing an array element
                  | expr openBrack expr closedBrack '=' expr //Assinging to an array element
                  | expr '.add'openParenth expr closedParenth   //Method to add an element to a dynamically sized array
                  | expr op=('*' | '/') expr
                  | expr op=('+' | '-') expr
                  | expr op=('<' | '<=' | '>' | '>=' | '==' | '!=') expr
                  | openParenth expr closedParenth
                  | ID
                  | INT
                  | STRING
                  | DOUBLE
                  | TRUE
                  | FALSE
                  | randomInt
                  | randomChoice
                  | enumValue
                  ;


openParenth      : '(' ;
closedParenth    : ')' ;
openBrack        : '[' ;
closedBrack      : ']' ;
openCurlBrack    : '{' ;
closedCurlBrack  : '}' ;
comma            : ',' ;              

// Lexer Rules
PLUS              : '+' ;
MINUS             : '-' ;
MULT              : '*' ;
DIV               : '/' ;
MOD               : '%' ;
GREATER_THAN      : '>' ;
TRUE              : 'true' ;
FALSE             : 'false' ;
INT               : NUMBER+ ;
DOUBLE            : NUMBER+ '.' NUMBER+ ;
STRING            : '"' (ESC | ~["\\])* '"' ; // Use fragment for escaped characters
ID                : LETTER (LETTER | NUMBER)* ;

fragment LETTER   : [a-zA-Z_]; //
fragment ESC      : '\\' (['"\\tn]); // Define ESC for escape sequences in strings, doesn't work
fragment NUMBER   : [0-9_]; //

WS       : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines