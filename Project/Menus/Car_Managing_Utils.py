#Functions to manage car database.
import os

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
        self.busy = False

        if self.car_type == "car":
            self.cost = 0.4  #per km
            self.start_cost = 3
            self.speed = 300

        if self.car_type == "van":
            self.cost = 7   #per km
            self.start_cost = 4
            self.speed = 250

    def busy_status(self):
        self.busy = True


    def __str__(self):
        return "Number: " + self.number + " Type: " + self.car_type + " Brand: " + self.brand + " Driver: " + self.driver\
               + " License: " + self.license + " KM: " + self.km + " Services: " + self.jobs + " Money: "\
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


car_list = update_class()
print(car_list)
print(car_list[0].brand)
print(car_list[0])




