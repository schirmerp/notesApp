from tkinter import *
from tkinter import ttk

from numpy import column_stack
from notedb import *
from tkinter import simpledialog
from datetime import date


w = Tk()

n_h = 450
n_w = 600
#w.geometry(f'{n_w}x{n_h}')
today = date.today()
d1 = today.strftime("%m/%d/%y")

def sticky_note():
    sn = Toplevel(w)
    sn.attributes('-topmost', True)
    sn.geometry('400x350')
    sn_text = Text(sn, width=30, height= 500, bg='yellow', font=( 'Courier_New', 15, 'bold'))
    sn_text.pack(fill='both')


def new_note():
    today_date = d1
    notes_title = notes_title_entry.get()
    notes = notes_entry.get("1.0", "end-1c")

    add_note('notes.txt', f'{today_date} : {notes_title} : {notes}')
    notes_title_entry.delete(0, END)
    notes_entry.delete('1.0', END)
    count.set(count_note())
def del_n():
    answer1 = simpledialog.askstring("Input", "Enter part of the note you want removed?",parent=w)
    del_note(answer1)
    count.set(count_note())

def view_n():
    answer1 = simpledialog.askstring("Input", "Enter part of the note you want to view?",parent=w)
    note_text = get_note(answer1)
    child_win= Toplevel(w)
    child_win.title("Note")
    child_win.attributes('-topmost', True)
    child_win.geometry("500x500")
    content= note_text
    Label(child_win, text=content).pack()
    

    


count = StringVar()
count.set(count_note())

notes_title_label = Label(w, text="Notes title:").grid(row=0, column=1)
notes_title_entry = Entry(w,  width=30)
notes_title_entry.grid(row=1, columnspan=2)
notes_label = Label(w, text="Notes:").grid(row=2, column=1)
notes_entry = Text(w, width=50,height=5)
notes_entry.grid(row=3, column=1, columnspan=2)
b1 = Button(w, text="Add Note", bg = 'Turquoise',fg='Red',command=new_note).grid(row=4, column=0)
b2 = Button(w,text='Delete Note', bg = 'Turquoise',fg='Red',command=del_n).grid(row=4, column=1)
button3 = Button(w,text='view notes', bg = 'Turquoise',fg='Red',command=sticky_note).grid(row=4, column=2)
counter = Label(w, textvariable=count)
counter.grid(row=6, column=1)
w.mainloop()


#add buttons connected to notedb functions