import sys


def function_parser(func, expression=None):
    if func == "HELP":
        show_help()
    elif func == "EXIT":
        exit_case()
    else:
        print("Invalid function.")


def createScale(env1,env2):
    print("Generating Scale:\n")
    print(env1)
    print(env2)




def playScale(env):
    print("Playing Scale " + str(env[0]))



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
