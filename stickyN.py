from tkinter import *


w = Tk()

def sn():
    sn = Toplevel(w)
    sn.geometry('400x300')
    sn.attributes('-topmost', True)
    sn_text = Text(sn, bg='yellow', font=('Courier_New', 15, 'bold'))
    sn_text.pack(fill='both')
    b2 = Button(sn, text="Save")
    m= Menu(sn)
    save = Menu(m)
    save.add_command(label='Save', command ='save')
    save.add_separator()
    save.add_command(label='New', command= 'new')
    m.add_cascade(label='File', m=save)
    sn.config(menu=m)
    




n_t = StringVar()
b1 = Button(w, text='New Note', command= sn).grid(row=0, column=0)

w.mainloop()