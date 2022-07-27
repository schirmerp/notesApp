from tkinter import *
import sys
import os
import re



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
                return line
                

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


def count_note():
    count = 0
    with open(f"notes.txt", "r+") as f:
        read = f.readlines()
        for line in read:
            count += 1
    return count