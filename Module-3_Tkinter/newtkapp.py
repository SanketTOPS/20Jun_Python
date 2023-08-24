from tkinter import *


main=Tk()
main.title("TOPS")
main.geometry('400x500')
main.config(bg='yellow')

menubar=Menu(main)
file_menu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=file_menu)
main.config(menu=menubar)

mainloop()