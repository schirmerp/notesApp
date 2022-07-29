#!/usr/bin/python3

from tkinter import *
import os
from tkinter.simpledialog import askstring
from datetime import date
from tkinter.colorchooser import askcolor

today = date.today()
d1 = today.strftime("%m/%d/%y")

w = Tk()
w.title("Joe Sticky Notes")
w.geometry("250x32")
def sn():
    sn = Toplevel(w)
    sn.title("Joe Note")
    sn.geometry('400x300+1500+0')
    sn.attributes('-topmost', True)
    sn_text = Text(sn, bg='#f2ed91', font=('Courier_New', 12, 'bold'))
    sn_text.pack(fill='both')
    
    def save_note():
        n = askstring("Save", "Enter filename for note to save:")
        path = os.path.abspath(os.getcwd())
        filename = f"{path}/{n}.txt"
        with open(filename, 'a') as f:
            f.write(str(d1) + '\n' + sn_text.get(1.0, 'end') + '\n')

    b2 = Button(sn, text="Save", command=save_note)
    b2.place(rely=1.0,relx=1.0, anchor='se')    
    def cc():
        colors = askcolor(title="Choose Color")
        sn_text.configure(bg=colors[1])

    m= Menu(sn)
    n_color = Menu(m)
    n_color.add_command(label="Color", command= cc)
    m.add_cascade(label="Change Color", m=n_color)
    sn.config(menu=m)
    
# add  color selection option to menu 
# add save option for note




b1 = Button(w, text='New Note', command= sn).grid(row=0, column=0)

w.mainloop()


