import tkinter.messagebox
from tkinter import *
import os


def wrong_login():
    root = Tk()

    tkinter.messagebox.showinfo("Error No Login", "Your Login Is Not Registered")

    root.destroy()
    os.system("python Login_Menu.py")
