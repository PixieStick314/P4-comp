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
      

printStat         : PRINT OPEN_PARENTH expr CLOSED_PARENTH;
varDecl           : ID  (EQUAL_SIGN expr | arrayInit | args)?;
dataType          : baseType (OPEN_BRACK CLOSED_BRACK )? ;
baseType          : 'string' |'True' | 'False' | 'bool' | 'number' | ID;
ifStat            : IF OPEN_PARENTH ifExpr CLOSED_PARENTH OPEN_CURL ifBlock CLOSED_CURL (ELIF OPEN_PARENTH elifExpr CLOSED_PARENTH OPEN_CURL elifBlock CLOSED_CURL)* (ELSE OPEN_CURL elseBlock CLOSED_CURL)?;
ifExpr            : expr;
ifBlock           : stat* ;
elifExpr          : expr;
elifBlock         : stat* ;
elseBlock         : stat* ;
forLoop           : FOR varDecl IN expr OPEN_CURL stat* CLOSED_CURL;
whileLoop         : WHILE OPEN_PARENTH expr CLOSED_PARENTH OPEN_CURL stat* CLOSED_CURL;
functionDecl      : DEF ID OPEN_PARENTH params? CLOSED_PARENTH OPEN_CURL stat* CLOSED_CURL;
functionCall      : ID OPEN_PARENTH args? RETURN? CLOSED_PARENTH;
arrayInit         : OPEN_CURL expr (COMMA expr)* CLOSED_CURL; //initialization with value
bsp               : 'BSP' bspDimension bspParameters ;
params            : param (COMMA param)* ;
param             : ID ;
args              : expr (COMMA expr)* ;
randomNumber      : RANDOM_NUMBER OPEN_PARENTH NUMBER COMMA NUMBER CLOSED_PARENTH ;
randomChoice      : RANDOM_CHOICE OPEN_PARENTH expr (COMMA expr)+ CLOSED_PARENTH ;
enumDecl          : ENUM ID OPEN_CURL enumBody CLOSED_CURL ;
enumBody          : ID (COMMA ID)* ;
enumValue         : ID DOT ID ;
bspDimension      : '2D' | '3D' | NUMBER 'D' ; // INT 'D' allows for specifying dimensions beyond 3
bspParameters     : OPEN_PARENTH dimensionList COMMA minSize CLOSED_PARENTH ;
dimensionList     : NUMBER (COMMA NUMBER)* ; // A list of integers representing the sizes in each dimension
minSize           : NUMBER ; // Minimum size for partitioning
expr              : expr OPEN_BRACK expr CLOSED_BRACK     //Accessing an array element
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
                  | randomNumber
                  | randomChoice
                  | enumValue 
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
RANDOM_NUMBER    : 'randomNumber' ;
RANDOM_CHOICE    : 'randomChoice' ;
ENUM             : 'enum' ;

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

fragment LETTER           : [a-zA-Z_]; //
fragment ESC              : '\\' (['"\\tn]); // Define ESC for escape sequences in strings, doesn't work
fragment NUMB             : [0-9_]; //

WS       : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines