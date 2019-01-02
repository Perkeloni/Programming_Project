from tkinter import *
import Error_PopUps
import os
import Car_Managing_Utils
import Display_List


root = Tk()
root.geometry("300x300")
root.resizable(width=False, height=False)


def submit(self):
    valid = True
    name = var[0].get()
    brand = var[1].get()
    plate = var[2].get()

    earning = var[3].get()
    services = var[4].get()

    above = var[5].get()
    below = var[6].get()

    name_entry_result = (entry.get()).replace(" ", "_")
    value_entry_result = value_entry.get()

    check_list = [name, brand, plate, earning, services, above, below]

    if sum(check_list[0:3]) > 1 or sum(check_list[3:5]) > 1 or sum(check_list[5:7]) > 1:
        Error_PopUps.check_only_one()
        root.destroy()
        os.system("python Search_Car_Menu.py")
        valid = False

    if valid:
        car_object_list = Car_Managing_Utils.update_class() #can change to global variable source later
        root.destroy()
        if name:
            criteria = ["driver", name_entry_result]
            Display_List.display_list(car_object_list, criteria)
        if brand:
            criteria = ["brand", name_entry_result]
            Display_List.display_list(car_object_list, criteria)
        if plate:
            criteria = ["plate", name_entry_result]
            Display_List.display_list(car_object_list, criteria)
        if earning and above:
            criteria = ["earnings+", float(value_entry_result)]
            Display_List.display_list(car_object_list, criteria)
        if earning and below:
            criteria = ["earnings-", float(value_entry_result)]
            Display_List.display_list(car_object_list, criteria)
        if services and above:
            criteria = ["services+", int(value_entry_result)]
            Display_List.display_list(car_object_list, criteria)
        if services and below:
            criteria = ["services-", int(value_entry_result)]
            Display_List.display_list(car_object_list, criteria)
    if sum(check_list) == 0:
        criteria = "None"
        Display_List.display_list(car_object_list, criteria)






var = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()] #have yo use a .get method to take
                                                                                       #variables out of this bullshit like var[1].get()
frame_0 = Frame(root)
frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(root)
frame_4 = Frame(root)
frame_5 = Frame(root)
frame_6 = Frame(root)

frame_0.pack()
frame_1.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()
frame_5.pack()
frame_6.pack()

title = Label(frame_0, text="Search by:", font="Arial, 20")
valuesearch = Label(frame_3, text="Value Search by:", font="Arial, 20")

name_check = Checkbutton(frame_1, text="Name", variable=var[0])
brand_check = Checkbutton(frame_1, text="Brand", variable=var[1])
plate_check = Checkbutton(frame_1, text="License Plate", variable=var[2])
earning_check = Checkbutton(frame_4, text="Earnings", variable=var[3])
services_check = Checkbutton(frame_4, text="Services Performed", variable=var[4])

above_check = Checkbutton(frame_5, text="Above", variable=var[5])
below_check = Checkbutton(frame_5, text="Below", variable=var[6])

submit_button = Button(frame_6, text="Submit")

entry = Entry(frame_2)
value_entry = Entry(frame_3)



title.pack()
valuesearch.pack()

name_check.pack(side=LEFT, pady=5)
brand_check.pack(side=LEFT, pady=5)
plate_check.pack(side=LEFT, pady=5)
earning_check.pack(side=LEFT, pady=5)
services_check.pack(side=LEFT, pady=5)
above_check.pack(side=LEFT, pady=5)
below_check.pack(side=LEFT, pady=5)

entry.pack(side=BOTTOM, pady=5)
value_entry.pack(side=BOTTOM, pady=5)

submit_button.pack(side=BOTTOM)

submit_button.bind("<Button-1>", submit)

root = mainloop()