import ply.yacc as yacc

from PySharp_executable import PySharp_Lex, function_run

tokens = PySharp_Lex.tokens


def p_assign(p):
    '''
    assign : func
    '''



def p_assign_createScale(p):
    '''
    assign_createScale : createScale NAME NAME
    '''

    p[0] = p[1] + p[2] + p[3]
    function_run.createScale(p[2],p[3])


def p_assign_playScale(p):
    '''
    assign_playScale : playScale assign_createScale
    '''
    p[0] = p[1] + p[2]
    function_run.playScale(p[2])


def p_func(p):
    '''
    func : assign_createScale
        | assign_playScale
        | HELP
        | EXIT
    '''

    if str(p[1]) == "HELP" or str(p[1]) == "EXIT":
        function_run.function_parser(p[1])

def p_error(p):
    print("Syntax error." + str(p))


def do_parse(s):
    parser.parse(s)


parser = yacc.yacc()
