grammar RogueLang;

prog:   stat+ ;

stat:   printStat
      | varDecl
      | ifStat
      | forStat
      | expr
      ;

printStat : 'print:' expr ;
varDecl   : 'let' ID '=' expr ;
ifStat    : 'if' expr ':' stat ('else:' stat)? ;
forStat   : 'for' ID 'in' 'range(' expr ',' expr ')' ':' stat ;
expr      : <assoc=right> expr op=('*'|'/') expr
          | <assoc=right> expr op=('+'|'-') expr
          | INT
          | ID
          | STRING
          ;

ID       : [a-zA-Z_][a-zA-Z_0-9]* ;
INT      : [0-9]+ ;
STRING   : '"' ( ' ' | . )*? '"' ; // match quoted strings including spaces
WS       : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
