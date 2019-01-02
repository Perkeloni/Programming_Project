from tkinter import *
import os


def display_list(car__object_list):

    def submit(self):
        selection = listbox.get(listbox.curselection())
        print(selection)


    def cancel(self):
        root.destroy()
        os.system("python Admin_Menu.py")

    root = Tk()

    root.geometry("300x300")
    root.resizable(width=False, height=False)

    listbox = Listbox(root)
    listbox.pack(fill=BOTH, expand=1)

    submit_button = Button(root, text="Submit")
    cancel_button = Button(root, text="Cancel")

    submit_button.pack()
    cancel_button.pack()

    submit_button.bind("<Button-1>", submit)
    cancel_button.bind("<Button-1>", cancel)

    listbox.insert(END, "Select a car for more options")

    for item in car__object_list:
        listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                       item.driver + " " + item.license + " " + item.jobs + " " + item.money)

    root.mainloop()




