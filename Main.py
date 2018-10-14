import os
import pygame
from tkinter.filedialog import askdirectory

from tkinter import *

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
[6:10 PM, 10/14/2018] +1 (787) 391-8188: javihdznovoa
[6:13 PM, 10/14/2018] +1 (787) 391-8188: import os
import pygame
from tkinter.filedialog import askdirectory

from tkinter import *

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

for items in listofsongs:
    listbox.insert(END,items)

nextbutton = Button(root, text = "Next Song")
nextbutton.pack()

previousbutton = Button(root, text = "Previous Song")
previousbutton.pack()

stopbutton = Button(root, text = "Stop Song")
stopbutton.pack()

directorychooser()

root.mainloop()