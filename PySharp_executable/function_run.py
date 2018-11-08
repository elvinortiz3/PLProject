import sys
from PySharp_executable import env_Converter as conv


def function_parser(func, expression=None):
    if func == "createScale":
        createScale(expression)
    elif func == "playScale":
        playScale(expression)
    elif func == "Scale":
        Scale(expression)
    elif func == "HELP":
        show_help()
    elif func == "EXIT":
        exit_case()
    else:
        print("Invalid function.")


def createScale(env):
    print("Generating Scale:\n")
    expression = conv.env_to_expr(env)
    print(expression)


def playScale(env):
    print("Playing Scale " + str(env[0]))
    expression = conv.env_to_expr(env)
    print(expression)

def Scale(env):
    print("Getting Scale")
    expression = conv.env_to_expr(env)
    print(expression)

def show_help():
    str = '''
    Available functions:
    createScale(scale,type)
    playScale(scale)
    Scale(var)

    
    EXIT - close the program.
          '''
    print(str)


def exit_case():
    sys.exit(0)
