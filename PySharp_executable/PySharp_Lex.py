import ply.lex as lex
import sys

# Implementation of lexical analyzer
reserved = {

    "playScale": "playScale",
    "createScale": "createScale",
    "HELP": "HELP",
    "EXIT": "EXIT",
    "NAME": "NAME",
    "EQUALS": "EQUALS"

}


# Create Tokens
tokens = list(reserved.values())

t_ignore = r' '
t_EQUALS = r'='

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'NAME'
    return t



def t_error(t):
    print("Unrecognized Character(s)")
    print(t)
    t.lexer.skip(1)


lexer = lex.lex()
