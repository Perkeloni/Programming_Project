from tkinter import *


root = Tk()
root.geometry("300x300")
root.resizable(width=False, height=False)

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

root = mainloop()