import tkinter
from tkinter import ttk,messagebox

screen=tkinter.Tk()

screen.title("FirstApp")
screen.geometry('400x500')
screen.config(bg='orange')

lbl_fnm=tkinter.Label(text='Firstname:',bg='orange',font='Calibri 15 bold',fg='red')
#lbl_fnm.pack()
#lbl_fnm.place(x=0,y=0)
lbl_fnm.grid(row=0,column=0,sticky='W')

lbl_lnm=tkinter.Label(text='Lastname:',bg='orange',font='Calibri 15 bold',fg='red')
lbl_lnm.grid(row=1,column=0,sticky='W')
#lbl_lnm.pack()
#lbl_lnm.place(x=0,y=30)


txt_fnm=tkinter.Entry()
txt_fnm.grid(row=0,column=1,sticky='W')

txt_lnm=tkinter.Entry()
txt_lnm.grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(text='Male', value=0,bg='orange',font='Calibri 15 bold',fg='red').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(text='Female', value=1,bg='orange',font='Calibri 15 bold',fg='red').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text='Web Dev.',bg='orange',font='Calibri 15 bold',fg='red').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text='Desktop Dev.',bg='orange',font='Calibri 15 bold',fg='red').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text='Mobile Dev.',bg='orange',font='Calibri 15 bold',fg='red').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text='Hybrid Dev.',bg='orange',font='Calibri 15 bold',fg='red').grid(row=6,column=0,sticky='W')


city=['Ahmedabad','Rajkot','Baroda','Jamnagar','Junagadh']
ttk.Combobox(values=city).grid(row=7,column=0,sticky='W')

def btnclick():
    #print("Button Clickd")
    #messagebox.askokcancel("Download!","Do you want to continue?")
    #messagebox.askquestion("Download!","Do you want to continue?")
    #messagebox.askretrycancel("Download!","Do you want to continue?")
    #messagebox.askyesno("Download!","Do you want to continue?")
    #messagebox.askyesnocancel("Download!","Do you want to continue?")

    #messagebox.showerror("Error!","Somethingwent wrong...Try again!")
    #messagebox.showinfo("Success","Your data has been submitted!")
    #messagebox.showwarning("Warning","Your disk is full!")
    print(f"Firstname:{txt_fnm.get()}")
    print(f"Lastname:{txt_lnm.get()}")

tkinter.Button(text="Submit",font='Calibri 15 bold',command=btnclick).place(x=160,y=300)

tkinter.mainloop()