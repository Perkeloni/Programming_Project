import os
import re
import tkinter.messagebox
from tkinter import *


def check_login(login, password):

    global admin
    program_running = True
    entry = False
    admin = False

    file = open(r"C:\Users\User\PycharmProjects\Projecto_Programação\Project\Databases\Login_Database", "r")

    while program_running == True:
        line = file.readline()

        while line != "":
            line = line.replace("/n", "")
            line = line.split(" ")

            if login == (line[0]) and password == (line[1]):
                if int(line[2]) == 1:
                    admin = True
                else:
                    entry = True

            line = file.readline()

        program_running = False
        file.close()

    if admin:
        os.system("python Admin_Menu.py")
    elif entry:
        os.system("python Client_Request_Car_Menu.py")
    else:
        return 1


def create_account(login, password):

    root = Tk()
    print(password)

    if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#%]{6,12}$", password):
        file = open(r"C:\Users\User\PycharmProjects\Projecto_Programação\Project\Databases\Login_Database", "a")
        file.write(login, " ", password, "0")
        file.close()
        root.destroy()

    else:
        tkinter.messagebox.showinfo("Creating an Account", "Your password must contain, 6 letters, 1 uppercase, and a @ # or %")
        print(password)
        root.destroy()
        os.system("python Login_Menu.py")


