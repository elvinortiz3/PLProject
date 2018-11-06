import ply.lex as lex
import sys

# Implementation of lexical analyzer

# Create Tokens


keywords = (

    "PlayScale", "CreateScale", "Scale"

)

tokens = keywords + (

    "Harmonic", "Natural", "Melodic",
    "A", "B", "C", "D", "E", "F", "G",

)

reserved = {

    "A", "B", "C", "D", "E", "F", "G",
    "CreateScale", "Scale", "PlayScale",
    "Harmonic", "Natural", "Melodic"

}

t_EQUALS = r'\='
t_ignore = r' '


def t_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'NAME'
    return t


def t_error(t):
    print("Unrecognized Character(s)")
    # print(t)
    t.lexer.skip(1)


lexer = lex.lex()
