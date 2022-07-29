from tkinter import *
from tkinter import ttk
import sys
import os
from tkinter import simpledialog


w=Tk()
def save_note():
    save = Toplevel(sn)
    save.geometry('100x100') 
    answer1 = simpledialog.askstring("Input", "Enter part of the note you want to view?",parent=sn)
    dir = os.path.abspath(os.getcwd())
    text = sn_text.get()
    with open(f"{dir}/{answer1}.txt", 'w') as f:
        f.write(text)
def sticky_note():
    sn = Toplevel(w)
    sn.attributes('-topmost', True)
    sn.geometry('400x350')
    sn_text = Text(sn, width=30, height= 500, bg='yellow', font=( 'Courier_New', 15, 'bold'))
    sn_text.pack(fill='both')
    bs = Button(sn, text="Save", bg="light blue", fg="red", command=save_note).grid(stick='NE')

    







b1= Button(w, text="New Note", bg="light blue", fg= 'red', command=sticky_note ).grid(row=0, column=1) 
b2= Button(w, text="Find Note", bg="light blue", fg= 'red', command="find_note" ).grid(row=0, column=2)
b3= Button(w, text="New Note", bg="light blue", fg= 'red', command="new_note" ).grid(row=0, column=3)  



w.mainloop()