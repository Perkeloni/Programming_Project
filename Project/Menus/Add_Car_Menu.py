from tkinter import *
import Car_Managing_Utils
import Error_PopUps
import os


def add_car(self):

    valid = False
    car_type = None
    brand = brand_entry.get()
    license_plate = plate_entry.get()
    driver = driver_entry.get()
    driver = driver.replace(" ", "_")
    x = positionX_entry.get()
    y = positionY_entry.get()
    car = checks[0].get()
    van = checks[1].get()

    if car and van == 1:
        root.destroy()
        Error_PopUps.check_only_one()
        os.system("python Add_Car_Menu.py")

    if car == 1:
        car_type = "car"
        valid = True
    if van ==1:
        car_type = "van"
        valid = True

    if car_type is None:
        root.destroy()
        Error_PopUps.nothing_inserted()
        os.system("python Admin_Menu.py")

    if valid:
        root.destroy()
        Car_Managing_Utils.write_car(brand, driver, license_plate, x, y, car_type)


root = Tk()
root.geometry("300x300")
root.resizable(width=False, height=False)

checks = [IntVar(), IntVar()]

################################ Defining the layout widgets to include in the window

frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(root)
frame_4 = Frame(root)
frame_5 = Frame(root)
frame_6 = Frame(root)
frame_7 = Frame(root)

frame_1.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()
frame_5.pack()
frame_6.pack()
frame_7.pack()

title = Label(frame_1, text="Insert Car Specifications", font="Arial, 15", pady=10)
car_brand = Label(frame_1, text="Car Brand:")
car_plate = Label(frame_2, text="Car Plate:")
car_driver = Label(frame_3, text="Car Driver:")
car_position = Label(frame_4, text="Car Position:")
X_label = Label(frame_5, text="X:")
Y_label = Label(frame_5, text="Y:")

check_car = Checkbutton(frame_6, text="Car", variable=checks[0])
check_van = Checkbutton (frame_6, text="Van", variable=checks[1])

brand_entry = Entry(frame_1)
plate_entry = Entry(frame_2)
driver_entry = Entry(frame_3)
positionX_entry = Entry(frame_5)
positionY_entry = Entry(frame_5)

submit_button = Button(frame_7, text="Submit")

positionX_entry.config(width=5)
positionY_entry.config(width=5)

################################# End

#########################################Inputing the widgets defined above into the window

title.pack(side=TOP)
car_brand.pack(pady=7, side=LEFT, padx=(18, 0))
car_plate.pack(pady=7, side=LEFT, padx=(5, 0))
car_driver.pack(pady=7, side=LEFT)
car_position.pack(pady=5, side=LEFT)

X_label.pack(side=LEFT)
positionX_entry.pack(pady=7, side=LEFT)
Y_label.pack(side=LEFT)
positionY_entry.pack(pady=7, side=LEFT)

check_car.pack(side=LEFT, pady=7)
check_van.pack(side=RIGHT, pady=7)

brand_entry.pack(pady=7, side=LEFT)
plate_entry.pack(pady=7, side=LEFT)
driver_entry.pack(pady=7, side=LEFT)

submit_button.pack(side=BOTTOM)

submit_button.bind("<Button-1>", add_car)

######################################## End

root = mainloop()