grammar Workflow;

program : statement* EOF ;

statement
    : addStmt
    | borrowStmt
    | returnStmt
    | queryStmt
    ;

addStmt
    : 'add' 'resource' fieldList
    ;

borrowStmt
    : 'borrow' ID fieldList
    ;

returnStmt
    : 'return' ID fieldList
    ;

queryStmt
    : 'query'
    ;

fieldList
    : fieldAssign+
    ;

fieldAssign
    : ID '=' value
    ;

value
    : STRING
    | ID
    ;

ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING : '"' ~["\r\n]* '"' ;

WS : [ \t\r\n]+ -> skip ;
