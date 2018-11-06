import sys

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


def playScale(env):
    print("Playing Scale " + str(env[0]))


def Scale(env):
    print("Getting Scale")


def show_help():
    str = '''
    To declare an expression:

    Available Operators:
    

    Available functions:
    EXIT - close the program.
          '''
    print(str)


def exit_case():
    sys.exit(0)
