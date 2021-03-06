# Functions to manage car database.
import os
import tkinter.messagebox
from tkinter import *
import Error_PopUps

filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Databases/Car_Database'))


class Vehicles:

    def __init__(self, spec_list): #every var in here even if numerical is always given in string format
        self.number = spec_list[0]
        self.car_type = spec_list[1]
        self.brand = spec_list[2]
        self.driver = spec_list[3]
        self.license = spec_list[4]
        self.km = spec_list[5]
        self.jobs = spec_list[6]
        self.money = spec_list[7]
        self.x = spec_list[8]
        self.y = spec_list[9]
        self.busy = spec_list[10]
        self.active = spec_list[11]


        if self.car_type == "car":
            self.cost = 0.4  # per km
            self.start_cost = 3
            self.speed = 30  # km h

        if self.car_type == "van":
            self.cost = 0.7  # per km
            self.start_cost = 4
            self.speed = 25  # km h

    def busy_status(self):
        if self.busy == "0":
            self.busy = "1"
        elif self.busy == "1":
            self.busy = "0"

    def __str__(self):
        return "Number:_" + self.number + " Type:_" + self.car_type + " Brand:_" + self.brand + " Driver:_" + self.driver \
               + " License:_" + self.license + " KM:_" + self.km + " Services:_" + self.jobs + " Money:_" \
               + self.money + " X:_" + self.x + " Y:_" + self.y + " Busy:_" + (str(int(self.busy))) + " Active:_" + self.active


def update_class():
    global Vehicles
    program_running = True
    car_list = []

    with open(filename) as file:

        while program_running:
            line = file.readline()

            while line != "":
                line = line.replace("\n", "")
                line = line.split(" ")
                car = Vehicles(line)
                car_list.append(car)
                line = file.readline()

            del car_list[0]
            return car_list
            program_running = False


def write_car(brand, driver, license_plate, x, y, car_type):
    root = Tk()
    valid = False
    car_list = update_class() #Could set this to global variable instead of reading from file again
    x = float(x)
    y = float(y)

    for check in car_list:
        if check.license == license_plate:
            tkinter.messagebox.showinfo("Error", "Your license plate is already registered")
            root.destroy()
            os.system("python Add_Car_Menu.py")

    if len(license_plate) != 8:
        tkinter.messagebox.showinfo("Error", "Your license plate is not valid")
        root.destroy()
        os.system("python Add_Car_Menu.py")

    elif float(x) < 0.0 or float(x) > 5.0 or float(y) < 0.0 or float(y) > 5.0:
        tkinter.messagebox.showinfo("Error", "Your position is not valid")
        root.destroy()
        os.system("python Add_Car_Menu.py")

    else:
        valid = True

    if valid:
        number = int((car_list[-1]).number)
        number +=1

        file = open(filename, "a")
        input = (str(number) + " " + car_type + " " + brand + " " + driver + " " + license_plate + " " + "0.0" + " " + "0"
                 + " " + "0.0" + " " + str(x) + " " + str(y) + " " + "1" + " 0" + "\n")
        file.write(input)
        file.close()
        tkinter.messagebox.showinfo("Success", "Car Was Added")
        root.destroy()
        os.system("python Admin_Menu.py")


def set_inactive(car_number): #this actually sets both inactive and active if its already inactive
    file = open(filename, "r")
    data = file.readlines()

    for item in data:
        if car_number == item[0]:
            item2 = item
            item2 = item2.replace("\n", "")
            item2 = item2[::-1]
            if item2[0] == "0":
                item2 = item2.replace("0", "1", 1)
                loc = data.index(item)
                data.remove(item)
                item2 = item2[::-1]
                item2 = item2 + "\n"
                data.insert(loc, item2)
            elif item2[0] == "1":
                item2 = item2.replace("1", "0", 1)
                loc = data.index(item)
                data.remove(item)
                item2 = item2[::-1]
                item2 = item2 + "\n"
                data.insert(loc, item2)

    file.close()

    file = open(filename, "w")
    file.writelines(data)
    file.close()

def money_distance_change(selection, total_cost, total_distance):
    with open(filename) as file:
        database = file.readlines()
    for item in database:
        if item.split(" ")[0] == selection.number:
            selection.jobs = int(selection.jobs) + 1
            selection.money = float(selection.money) + float(total_cost)
            selection.km = int(total_distance) + int(total_distance)
            database[(database.index(item))] = str(selection.number + " " + selection.car_type + " " + selection.brand + " "
                                                   + selection.driver + " " + selection.license + " " + str(selection.km)
                                                   + " " + str(selection.jobs) + " " + str(selection.money) + " " +
                                                   selection.x + " " + selection.y + " " + selection.busy + " " +
                                                   selection.active + "\n")
    file = open(filename, "w")
    for item in database:
        file.write(item)
    file.close()
    Error_PopUps.car_called()
