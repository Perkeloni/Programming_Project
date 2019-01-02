import tkinter.messagebox
from tkinter import *
import os


def wrong_login():
    root = Tk()

    tkinter.messagebox.showinfo("Error No Login", "Your Login Is Not Registered")

    root.destroy()
    os.system("python Login_Menu.py")


def check_only_one():
    root = Tk()

    tkinter.messagebox.showinfo("Error", "Check only one box per item")

    root.destroy()


def nothing_inserted():
    root = Tk()

    tkinter.messagebox.showinfo("Error", "Nothing was Inserted")

    root.destroy()
