import sys
import os
import pygame

def function_parser(func, expression=None):
    if func == "HELP":
        show_help()
    elif func == "EXIT":
        exit_case()
    else:
        print("Invalid function.")


def createScale(env1,env2):
    print("Generating Scale:\n")
    print(env1 + " , " + env2)
    if(env1 == "A"):
        if(env2 == "Harmonic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Harmonics/Scales_Harmonics-Bb_Clarinet_1.mp3")
        elif(env2 == "Melodic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Melodics/Scales_Melodics-Bb_Clarinet_1.mp3")
        elif (env2 == "Natural"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Naturals/Scales-Bb_Clarinet_1.mp3")
        else:
            print(env2 + " is not a Type of Scale")
    elif (env1 == "B"):
        if (env2 == "Harmonic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Harmonics/Scales_Harmonics-Bb_Clarinet_2.mp3")
        elif (env2 == "Melodic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Melodics/Scales_Melodics-Bb_Clarinet_2.mp3")
        elif (env2 == "Natural"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Naturals/Scales-Bb_Clarinet_2.mp3")
        else:
            print(env2 + " is not a Type of Scale")
    elif (env1 == "C"):
        if (env2 == "Harmonic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Harmonics/Scales_Harmonics-Bb_Clarinet_3.mp3")
        elif (env2 == "Melodic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Melodics/Scales_Melodics-Bb_Clarinet_3.mp3")
        elif (env2 == "Natural"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Naturals/Scales-Bb_Clarinet_3.mp3")
        else:
            print(env2 + " is not a Type of Scale")
    elif (env1 == "D"):
        if (env2 == "Harmonic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Harmonics/Scales_Harmonics-Bb_Clarinet_4.mp3")
        elif (env2 == "Melodic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Melodics/Scales_Melodics-Bb_Clarinet_4.mp3")
        elif (env2 == "Natural"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Naturals/Scales-Bb_Clarinet_4.mp3")
        else:
            print(env2 + " is not a Type of Scale")
    elif (env1 == "E"):
        if (env2 == "Harmonic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Harmonics/Scales_Harmonics-Bb_Clarinet_5.mp3")
        elif (env2 == "Melodic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Melodics/Scales_Melodics-Bb_Clarinet_5.mp3")
        elif (env2 == "Natural"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Naturals/Scales-Bb_Clarinet_5.mp3")
        else:
            print(env2 + " is not a Type of Scale")
    elif (env1 == "F"):
        if (env2 == "Harmonic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Harmonics/Scales_Harmonics-Bb_Clarinet_6.mp3")
        elif (env2 == "Melodic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Melodics/Scales_Melodics-Bb_Clarinet_6.mp3")
        elif (env2 == "Natural"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Naturals/Scales-Bb_Clarinet_6.mp3")
        else:
            print(env2 + " is not a Type of Scale")
    elif (env1 == "G"):
        if (env2 == "Harmonic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Harmonics/Scales_Harmonics-Bb_Clarinet_7.mp3")
        elif (env2 == "Melodic"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Melodics/Scales_Melodics-Bb_Clarinet_7.mp3")
        elif (env2 == "Natural"):
            pygame.mixer.init()
            return pygame.mixer.music.load("scales/Naturals/Scales-Bb_Clarinet_7.mp3")
        else:
            print(env2 + " is not a Type of Scale")
    else:
      print(env1 + " is not a Scale")


def playScale(env):
    if(env == "Previous"):
        print("Playing Last Created Scale ")
    else:
        print("Playing Scale " + str(env[11]) + " in " + str(env[12:]))

    pygame.mixer.music.play()


def show_help():
    str = '''
    Available functions:
    createScale(scale,type)
    playScale(scale)
    
    EXIT - close the program.
    
    Scales: A,B,C,D,E,F,G
    Types: Harmonic, Natural, Melodic
          '''
    print(str)


def exit_case():
    sys.exit(0)
