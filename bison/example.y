%{
#include <stdio.h>
%}

%token id

%%

program: expr { printf("Input accepted!\n"); }
       ;

expr: expr '+' term
    | term
    ;

term: term '*' factor
    | factor
    ;

factor: '(' expr ')'
      | id
      ;

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(const char *s) {
    printf("Error: %s\n", s);
    return 0;
}

