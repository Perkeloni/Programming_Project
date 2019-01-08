from tkinter import *
import os
import Car_Managing_Utils
import Error_PopUps

filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Databases/Login_Database'))

def display_list(car_object_list, criteria, database):

    def submit(self):
        selection = listbox.get(listbox.curselection())
        root.destroy()
        selection = selection.split(" ")
        selection = selection[0]
        display_info_list(selection)

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

    listbox.insert(END, "Select a item for more options")

    if database == "cars":

        listbox.insert(END, "Last values are Services and Money")

        if criteria[0] == "driver":
            for item in car_object_list:
                if item.driver.lower() == criteria[1].lower():
                    listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                                   item.driver + " " + item.license + " " + item.jobs + " " + item.money + "€")

        if criteria[0] == "brand":
            for item in car_object_list:
                if item.brand.lower() == criteria[1].lower():
                    listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                                   item.driver + " " + item.license + " " + item.jobs + " " + item.money + "€")

        if criteria[0] == "plate":
            for item in car_object_list:
                if item.license.lower() == criteria[1].lower():
                    listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                                   item.driver + " " + item.license + " " + item.jobs + " " + item.money + "€")

        if criteria[0] == "earnings+":
            for item in car_object_list:
                if float(item.money) >= criteria[1]:
                    listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                                   item.driver + " " + item.license + " " + item.jobs + " " + item.money + "€")

        if criteria[0] == "earnings-":
            for item in car_object_list:
                if float(item.money) <= criteria[1]:
                    listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                                   item.driver + " " + item.license + " " + item.jobs + " " + item.money + "€")

        if criteria[0] == "services+":
            for item in car_object_list:
                if int(item.jobs) >= criteria[1]:
                    listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                                   item.driver + " " + item.license + " " + item.jobs + " " + item.money + "€")

        if criteria[0] == "services-":
            for item in car_object_list:
                if int(item.jobs) <= criteria[1]:
                    listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                                   item.driver + " " + item.license + " " + item.jobs + " " + item.money + "€")
        if criteria == "None":
            for item in car_object_list:
                listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                                item.driver + " " + item.license + " " + item.jobs + " " + item.money + "€")

    if database == "users":

        listbox.insert(END, "User, password, 1=admin 0=user")

        with open(filename) as file:
            lines = file.readlines()
            for item in lines:
                listbox.insert(END, item)
            submit_button.destroy()
            
    root.mainloop()


def display_info_list(selection):

    root = Tk()

    def submit(self):
        root.destroy()
        Error_PopUps.inactive_set()
        Car_Managing_Utils.set_inactive(selection)
        os.system("python Admin_Menu.py")

    def cancel(self):
        root.destroy()
        os.system("python Admin_Menu.py")

    root.geometry("300x300")
    root.resizable(width=False, height=False)

    listbox = Listbox(root)
    listbox.pack(fill=BOTH, expand=1)

    submit_button = Button(root, text="Set Inactive")
    cancel_button = Button(root, text="Return")

    submit_button.pack()
    cancel_button.pack()

    submit_button.bind("<Button-1>", submit)
    cancel_button.bind("<Button-1>", cancel)

    listbox.insert(END, "Set Inactive or Click Return")

    car_list = Car_Managing_Utils.update_class()#could set this as global variable

    for item in car_list:
        if item.number == selection:
            number = int(selection) - 1
            result = car_list[number].__str__()
            result2 = result.split(" ")

            for item in result2:
                final_result = item.replace("_", " ")
                listbox.insert(END, final_result)

    root.mainloop()
