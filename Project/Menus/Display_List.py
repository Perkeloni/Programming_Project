from tkinter import *
import os


def display_list(car_object_list, criteria):

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
    listbox.insert(END, "Last values are Services and Money")

    if criteria[0] == "driver":
        for item in car_object_list:
            if item.driver.lower() == criteria[1].lower():
                listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                               item.driver + " " + item.license + " " + item.jobs + " " + item.money)

    if criteria[0] == "brand":
        for item in car_object_list:
            if item.brand.lower() == criteria[1].lower():
                listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                               item.driver + " " + item.license + " " + item.jobs + " " + item.money)

    if criteria[0] == "plate":
        for item in car_object_list:
            if item.license.lower() == criteria[1].lower():
                listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                               item.driver + " " + item.license + " " + item.jobs + " " + item.money)

    if criteria[0] == "earnings+":
        for item in car_object_list:
            if int(item.money) >= criteria[1]:
                listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                               item.driver + " " + item.license + " " + item.jobs + " " + item.money)

    if criteria[0] == "earnings-":
        for item in car_object_list:
            if int(item.money) <= criteria[1]:
                listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                               item.driver + " " + item.license + " " + item.jobs + " " + item.money)

    if criteria[0] == "services+":
        for item in car_object_list:
            if int(item.jobs) >= criteria[1]:
                listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                               item.driver + " " + item.license + " " + item.jobs + " " + item.money)

    if criteria[0] == "services-":
        for item in car_object_list:
            if int(item.jobs) <= criteria[1]:
                listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                               item.driver + " " + item.license + " " + item.jobs + " " + item.money)
    if criteria == "None":
        for item in car_object_list:
            listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                            item.driver + " " + item.license + " " + item.jobs + " " + item.money)





    root.mainloop()




