from tkinter import *
from tkinter import ttk
from notedb import *
from tkinter import simpledialog
from datetime import date


w = Tk()
n_h = 450
n_w = 600
w.geometry(f'{n_w}x{n_h}')
today = date.today()
d1 = today.strftime("%m/%d/%y")


def add_note(a,b):
    with open(f"{a}", "a+") as f:
        f.write(str(b) + "\n")
    return a  

def get_note(a):
    with open(f"notes.txt", "r+") as f:
        read = f.readlines()
        for line in read:
            z = re.search(a, line)
            if z:
                 print(line, z.group(0))


def del_note(a):
    with open("notes.txt", "r+") as f:
        with open("temp.txt", "w") as t:
            read = f.readlines()
            for line in read:
                z = re.search(a, line)
                if z:
                    pass
                else:
                    t.write(line)
        os.rename("temp.txt", "notes.txt")


def new_note():
    today_date = d1
    notes_title = notes_title_entry.get()
    notes = notes_entry.get("1.0", "end-1c")

    add_note('notes.txt', f'{today_date} : {notes_title} : {notes}')
def del_n():
    answer1 = simpledialog.askstring("Input", "Enter part of the note you want removed?",parent=w)
    del_note(answer1)

def view_n():
    answer1 = simpledialog.askstring("Input", "Enter part of the note you want to view?",parent=w)
    note_text = get_note(answer1)
    child_win= Toplevel(w)
    child_win.title("Note")
    child_win.geometry("500x500")
    content= note_text
    Label(child_win, text=content, font=('Bell MT', 20, 'bold')).pack()
    w.withdraw()
   
#Create an Entry Widget
 
#Let us create a button in the Main window
   
    



date_label = Label(w, text="Date:").place(x=10,y=20)
date_entry = Entry(w,  width=20)
date_entry.place(x=50,y=20)
notes_title_label = Label(w, text="Notes title:").place(x=10,y=50)
notes_title_entry = Entry(w,  width=30)
notes_title_entry.place(x=80,y=50)
notes_label = Label(w, text="Notes:").place(x=10,y=90)
notes_entry = Text(w, width=50,height=5)
notes_entry.place(x=60,y=90)
b1 = Button(w, text="Add Note", bg = 'Turquoise',fg='Red',command=new_note).place(x=10,y=190)
b2 = Button(w,text='Delete Note', bg = 'Turquoise',fg='Red',command=del_n).place(x=110,y=190)
button3 = Button(w,text='view notes', bg = 'Turquoise',fg='Red',command=view_n).place(x=210,y=190)


w.mainloop()


#add buttons connected to notedb functions