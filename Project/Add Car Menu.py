from tkinter import *

root = Tk()
root.geometry("300x300")

frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(root)
frame_4 = Frame(root)
frame_5 = Frame(root)
frame_6 = Frame(root)

frame_1.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()
frame_5.pack()
frame_6.pack()

title = Label(frame_1, text="Insert Car Specifications", font="Arial, 15", pady=10)
car_brand = Label(frame_1, text="Car Brand:")
car_plate = Label(frame_2, text="Car Plate:")
car_driver = Label(frame_3, text="Car Driver:")
car_position = Label(frame_4, text="Car Position:")
X_label = Label(frame_5, text="X:")
Y_label = Label(frame_5, text="Y:")

check_car = Checkbutton(frame_6, text="Car")
check_van = Checkbutton (frame_6, text="Van")

brand_entry = Entry(frame_1)
plate_entry = Entry(frame_2)
driver_entry = Entry(frame_3)
positionX_entry = Entry(frame_5)
positionY_entry = Entry(frame_5)

positionX_entry.config(width=5)
positionY_entry.config(width=5)

title.pack(side=TOP)
car_brand.pack(pady=10, side=LEFT, padx=(18, 0))
car_plate.pack(pady=10, side=LEFT, padx=(5, 0))
car_driver.pack(pady=10, side=LEFT)
car_position.pack(pady=5, side=LEFT)

X_label.pack(side=LEFT)
positionX_entry.pack(pady=10, side=LEFT)
Y_label.pack(side=LEFT)
positionY_entry.pack(pady=10, side=LEFT)

check_car.pack(side=LEFT, pady=10)
check_van.pack(side=RIGHT, pady=10)

brand_entry.pack(pady=10, side=LEFT)
plate_entry.pack(pady=10, side=LEFT)
driver_entry.pack(pady=10, side=LEFT)

root = mainloop()