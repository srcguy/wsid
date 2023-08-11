#What should I do? (WSID) beta 1 by src_guy
#2023

from tkinter import *
import tkinter as tk

root = tk.Tk()

root.geometry("300x200")

def new_sticky():
    sticky = Toplevel(root)
    sticky.title(sticky_name_raw.get())
    Label(sticky, text = sticky_content_raw.get()).place(relx=0.5, rely=0.5, anchor=CENTER)


Label(root, text="What should I do?", font=("System", 24)).place(x=0, y=2)
global sticky_name_raw
global sticky_content_raw
sticky_name_raw = tk.StringVar()
sticky_content_raw = tk.StringVar()
sticky_name = Entry(root, textvariable=sticky_name_raw)
sticky_content = Entry(root, textvariable=sticky_content_raw)
sticky_name.place(x=0, y=50)
sticky_content.place(x=0, y=75)
Label(root, text="Sticky name").place(x=100, y=50)
Label(root, text="Sticky content").place(x=100, y=75)
Button(root, text="Create new sticky note", command=new_sticky).place(x=0, y=100)

root.mainloop()