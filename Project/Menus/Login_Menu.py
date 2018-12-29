from tkinter import *
import Login_Checking

password = None
login = None
error = False

def check_password(self):

    password = password_entry.get()
    login = login_entry.get()

    root.destroy()

    Login_Checking.check_login(login, password)

root = Tk()
root.geometry("300x300")
root.resizable(width=False, height=False)

password_entry = Entry(root)
login_entry = Entry(root)

password_text = Label(text="Password:")
login_text = Label(text="Login:")
title = Label(text="Transports")

submit_button = Button(root, text="Submit")
create_button = Button(root, text="Create Account")

title.config(font=("Arial, 30"))

title.grid(row=0, sticky=N, padx=45)
login_text.grid(row=1, column=0, pady=(100,5), padx=(30,180), sticky=E)
password_text.grid(row=2, column=0, padx=(30,180), sticky=E)

login_entry.grid(row=1, columnspan=2, pady=(100,5), padx=(50,0))
password_entry.grid(row=2, columnspan=2, padx=(50,0))

submit_button.grid(row=3, column=0, padx=(0,50))
create_button.grid(row=3, column=0,  padx=(100,0))

submit_button.bind("<Button-1>", check_password)



root = mainloop()

