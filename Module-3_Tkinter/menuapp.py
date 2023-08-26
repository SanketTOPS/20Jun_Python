import os
from tkinter import *
from tkinter import ttk,messagebox

screen=Tk()
screen.title("MenubarApp")
screen.config(bg="yellow")
screen.geometry("400x500")

menubar=Menu(screen)

fileMenu=Menu(menubar,tearoff=0)
fileMenu.add_command(label="New") #submenu
fileMenu.add_command(label="Open") #submenu
fileMenu.add_command(label="Save") #submenu
fileMenu.add_command(label="Save As") #submenu
menubar.add_cascade(label='File',menu=fileMenu) #root menu

editMenu=Menu(menubar)
menubar.add_cascade(label="Edit")

selectionMenu=Menu(menubar)
menubar.add_cascade(label="Selction")


def openCalc():
    os.system("calc")

def openNotepad():
    os.system("notepad")


viewMenu=Menu(menubar,tearoff=0)
viewMenu.add_command(label="Calc",command=openCalc)
viewMenu.add_command(label="Notepad",command=openNotepad)
menubar.add_cascade(label="Application",menu=viewMenu)

screen.config(menu=menubar)

mainloop()