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
varDecl           : ID  ('=' expr | arrayInit | args)?;
dataType          : baseType (openBrack closedBrack )? ;
baseType          : 'string' |'true' | 'false' | 'bool' | 'number' | ID; 
ifStat            : IF openParenth ifExpr closedParenth openCurlBrack ifBlock closedCurlBrack (ELIF openParenth elifExpr closedParenth openCurlBrack elifBlock closedBrack)* (ELSE openCurlBrack elseBlock closedCurlBrack)?;
ifExpr            : expr;
ifBlock           : stat* ;
elifExpr          : expr;
elifBlock         : stat* ;
elseBlock         : stat* ;
forLoop           : 'for' varDecl 'in' expr openCurlBrack stat* closedCurlBrack;
whileLoop         : 'while' openParenth expr closedParenth openCurlBrack stat* closedCurlBrack;
functionDecl      : 'def' ID openParenth params? closedParenth openCurlBrack stat* closedCurlBrack;
functionCall      : ID openParenth args? RETURN? closedParenth;
arrayInit         : openCurlBrack expr (comma expr)* closedCurlBrack; //initialization with value
bsp               : 'BSP' bspDimension bspParameters ;
params            : param (comma param)* ;
param             : ID ;
args              : expr (comma expr)* ;
randomNumber      : 'randomNumber' openParenth NUMBER comma NUMBER closedParenth ;
randomChoice      : 'randomChoice' openParenth expr (comma expr)+ closedParenth ;
enumDecl          : 'enum' ID openCurlBrack enumBody closedCurlBrack ;
enumBody          : ID (comma ID)* ;
enumValue         : ID '.' ID ;
bspDimension      : '2D' | '3D' | NUMBER 'D' ; // INT 'D' allows for specifying dimensions beyond 3
bspParameters     : openParenth dimensionList comma minSize closedParenth ;
dimensionList     : NUMBER (comma NUMBER)* ; // A list of integers representing the sizes in each dimension
minSize           : NUMBER ; // Minimum size for partitioning
expr              : expr openBrack expr closedBrack     //Accessing an array element
                  | expr openBrack expr closedBrack '=' expr //Assinging to an array element
                  | expr '.add'openParenth expr closedParenth   //Method to add an element to a dynamically sized array
                  | expr op=(MULT | DIV | MOD) expr
                  | expr op=(PLUS| MINUS) expr
                  | expr op=(GT | GTE | LT | LTE | EQ | NEQ) expr
                  | expr op=(AND | OR) expr
                  | NOT expr
                  | openParenth expr closedParenth 
                  | ID
                  | STRING
                  | NUMBER
                  | TRUE
                  | FALSE
                  | randomNumber
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

// keywords
IF               : 'if';
ELIF             : 'elif';
ELSE             : 'else';         
RETURN           : 'return';     

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
TRUE              : 'true' ;
FALSE             : 'false' ;
COMMENT_SINGLELINE: '//' ~[\r\n]* -> skip ;
NUMBER            : '-'? NUMB + | '-'? NUMB+ '.' NUMB+ ;
STRING            : '"' (ESC | ~["\\])* '"' ; // Use fragment for escaped characters
ID                : LETTER (LETTER | NUMB)* ;

fragment LETTER   : [a-zA-Z_]; //
fragment ESC      : '\\' (['"\\tn]); // Define ESC for escape sequences in strings, doesn't work
fragment NUMB   : [0-9_]; //

WS       : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines