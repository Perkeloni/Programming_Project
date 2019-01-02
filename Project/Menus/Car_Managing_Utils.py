# Functions to manage car database.
import os
import tkinter.messagebox
from tkinter import *
import Display_List

filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Databases/Car_Database'))


class Vehicles:

    def __init__(self, spec_list):
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
        self.active = [10]
        self.busy = False

        if self.car_type == "car":
            self.cost = 0.4  # per km
            self.start_cost = 3
            self.speed = 300

        if self.car_type == "van":
            self.cost = 7  # per km
            self.start_cost = 4
            self.speed = 250

    def busy_status(self):
        self.busy = True

    def __str__(self):
        return "Number: " + self.number + " Type: " + self.car_type + " Brand: " + self.brand + " Driver: " + self.driver \
               + " License: " + self.license + " KM: " + self.km + " Services: " + self.jobs + " Money: " \
               + self.money + " X: " + self.x + " Y: " + self.y + " Busy:" + (str(int(self.busy)))


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

            return car_list
            program_running = False


def write_car(brand, driver, license_plate, x, y, car_type):
    root = Tk()
    valid = False
    car_list = update_class() #Could set this to global variable instead of reading from file again

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
                 + " " + "0.0" + " " + x + " " + y + " " + "1" + "\n")
        file.write(input)
        file.close()
        tkinter.messagebox.showinfo("Success", "Car Was Added")
        root.destroy()
        os.system("python Admin_Menu.py")


def set_inactive(car_number):
    file = open(filename, "r")
    data = file.readlines()

    line = data[(int(car_number)-1)]
    line = line[::-1]
    line = line.replace("1", "0", 1)
    line = line[::-1]
    data[(int(car_number)-1)] = line

    file.close()

    file = open(filename, "w")
    print(data)
    file.writelines(data)
    file.close()
