import os
import pygame
from Tkinter.filedialog import askdirectory

from Tkinter import *

root = Tk()
root.minsize(300,300)

listofsongs = []

index = 0

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)
            print(files)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

label = Label(root,text="Music Player")
label.pack()

listbox = Listbox(root)
listbox.pack()

directorychooser()


root.mainloop()