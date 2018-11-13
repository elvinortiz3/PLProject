import sys
from PySharp_executable import PySharp_Parse as parser


print("Welcome to PySharp")
print("(pre-alpha) ver. 1.0.0")
print("")

while True:
    try:
        s = input('PySharp >>')
    except EOFError:
        break
    print("")
    parser.do_parse(s)
    print("")
