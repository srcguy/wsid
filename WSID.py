#What should I do? (WSID) beta 3 by src_guy
#2023

from tkinter import *
from tkinter import colorchooser
import tkinter as tk

root = tk.Tk()

root.geometry("300x200")

root.title("What Should I Do?")

global sticky_name_raw
global sticky_content_raw
sticky_name_raw = tk.StringVar()
sticky_content_raw = tk.StringVar()

def new_sticky():
    sticky = Toplevel(root)
    sticky.title(sticky_name_raw.get())
    sticky.configure(bg=sticky_bg_color)
    Label(sticky, bg=sticky_bg_color, fg=sticky_txt_color, text = sticky_content_raw.get()).place(relx=0.5, rely=0.5, anchor=CENTER)

def sticky():
    sticky_menu = Toplevel(root)
    sticky_menu.geometry("300x209")
    sticky_menu.title("Sticky notes creator")
    Label(sticky_menu, text="Sticky notes creator", font=("David", 16)).place(x=0, y=9)
    sticky_name = Entry(sticky_menu, textvariable=sticky_name_raw)
    sticky_content = Entry(sticky_menu, textvariable=sticky_content_raw)
    sticky_name.place(x=0, y=50)
    sticky_content.place(x=0, y=75)
    Label(sticky_menu, text="Sticky name").place(x=100, y=50)
    Label(sticky_menu, text="Sticky content").place(x=100, y=75)
    def change_bg_color():
        global sticky_bg_color
        sticky_bg_color = colorchooser.askcolor()[1]
        Button(sticky_menu, text="ㅤㅤㅤㅤㅤ", bg=sticky_bg_color).place(x=150, y=100)
    def change_txt_color():
        global sticky_txt_color
        sticky_txt_color = colorchooser.askcolor()[1]
        Button(sticky_menu, text="ㅤㅤㅤㅤㅤ", bg=sticky_txt_color).place(x=150, y=125)
    Button(sticky_menu, text="Change background color", command=change_bg_color).place(x=0, y=100)
    Button(sticky_menu, text="Change text color", command=change_txt_color).place(x=0, y=125)
    Button(sticky_menu, text="Create new sticky note", command=new_sticky).place(x=0, y=150)
    Button(sticky_menu, text="Exit", bg="red", command=sticky_menu.destroy).place(x=0, y=175)

def todo_save():
    file = open("todo.txt", "w")
    file.write(todo_content.get("1.0","end"))
    file.close()

def todo():
    todo_menu = Toplevel(root)
    todo_menu.geometry("300x209")
    todo_menu.title("To do creator")
    Label(todo_menu, text="To do creator", font=("David", 16)).place(x=0, y=9)
    global todo_content
    todo_content = Text(todo_menu, width=30, height=5)
    todo_content.place(x=0, y=50)
    Button(todo_menu, text="Save", command=todo_save).place(x=0, y=150)
    Button(todo_menu, text="Exit", command=todo_menu.destroy, bg="red").place(x=50, y=150)

def todo_list():
    todo_menu_list = Toplevel(root)
    todo_menu_list.geometry("300x209")
    todo_menu_list.title("To do list")
    file = open("todo.txt", "r")
    Label(todo_menu_list, text=file.read()).place(relx=0.5, rely=0.5, anchor=CENTER)

Label(root, text="What should I do?", font=("System", 24)).place(x=0, y=2)
Button(root, text="Sticky notes", command=sticky).place(x=0, y=50)
Button(root, text="To do creator", command=todo).place(x=0, y=100)
Button(root, text="To do list", command=todo_list).place(x=100, y=100)
Button(root, text="Exit", bg="red", command=root.destroy).place(x=0, y=150)

root.mainloop()