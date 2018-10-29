import ply.yacc as yacc

from PySharp_executable import PySharp_Lex

tokens = PySharp_Lex.tokens
forest = []


def p_assign(p):
    '''
    assign :
    '''



def p_expr(p):
    '''
    expr :
     '''
    p[0] = p[1]


def p_term(p):
    '''
    term : NAME term
         | NAME
    '''
    p[0] = list()
    p[0].append(p[1])

    if len(p) is 3:
        p[0] = p[0] + p[2]


def p_func(p):
    '''
    func :
    '''



def p_error(p):
    print("Syntax error.")







def do_parse(s):
    parser.parse(s)


parser = yacc.yacc()