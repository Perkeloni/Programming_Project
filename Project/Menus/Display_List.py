from tkinter import *
import os
import Car_Managing_Utils
import Error_PopUps
import Client_Side_Utils

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
            number = int(selection) - 2
            result = car_list[number].__str__()
            result2 = result.split(" ")

            for item in result2:
                final_result = item.replace("_", " ")
                listbox.insert(END, final_result)

    root.mainloop()


def display_request_result(arrival_time, total_time, total_cost, car_selection, total_distance):

    def submit(self):
        #  MISSING CODE THIS WILL DISPLAY THE FUCK YOUR MOM
        root2.destroy()
        Car_Managing_Utils.money_distance_change(car_selection, total_cost, total_distance)


    def cancel(self):
        root2.destroy()

    root2 = Tk()

    root2.geometry("400x300")
    root2.resizable(width=False, height=False)

    listbox = Listbox(root2)
    listbox.pack(fill=BOTH, expand=1)

    submit_button = Button(root2, text="Submit")
    cancel_button = Button(root2, text="Cancel")

    submit_button.pack()
    cancel_button.pack()

    submit_button.bind("<Button-1>", submit)
    cancel_button.bind("<Button-1>", cancel)

    listbox.insert(END, "All Values Given are Estimates")
    listbox.insert(END, "Time is Given in Minutes")
    listbox.insert(END, "Arrival Time: " + str(arrival_time))
    listbox.insert(END, "Time to Reach Destination: " + str(total_time))
    listbox.insert(END, "Total Price: " + str(total_cost))

    root2.mainloop()


def display_request_list(car_object_list, sorted_distance, user_destination_distance):

    def submit(self):
        #  MISSING CODE THIS WILL DISPLAY THE PRICE AND ETA BOTH TO THE DESTINATION AS WELL AS TO THE USER.
        selection = listbox.get(listbox.curselection())
        selection2 = selection.split(" ")
        distance = float(selection2[-1])

        for item in car_object_list:
            if selection[0] == item.number:
                selection = item
                break
        root.destroy()
        arrival_time, total_time, total_cost, car_selection, total_distance = Client_Side_Utils.calculate_time_price(selection, distance, user_destination_distance)
        display_request_result(arrival_time, total_time, total_cost, car_selection, total_distance)

    def cancel(self):
        root.destroy()
        os.system("python Client_Request_Car_Menu.py")

    root = Tk()

    root.geometry("400x300")
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
    listbox.insert(END, "Number-Type-Brand-Driver-License-Jobs")

    for item in car_object_list:
        item.driver2 = item.driver.replace("_", " ")
        listbox.insert(END, item.number + " " + item.car_type + " " + item.brand + " " +
                       item.driver2 + " " + item.license + " " + item.jobs + " " + "Distance " + str(sorted_distance[car_object_list.index(item)]))

    root.mainloop()



