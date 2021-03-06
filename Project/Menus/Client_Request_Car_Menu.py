#Must- Input own coordinates. Input destination coordinates
#Must input time desired to reach destination and ammount of people to transport

from tkinter import *
import tkinter.messagebox
import Client_Side_Utils
import Display_List

root = Tk()
root.geometry("300x300")
root.resizable(width=False, height=False)


def request(self):
    Valid = True
    people_ammount = int(ammount_entry.get())
    user_position = [float(positionX_entry_user.get()), float(positionY_entry_user.get())]
    user_destination = [float(positionX_entry_destination.get()), float(positionY_entry_destination.get())]
    for item in user_position:
        if item > 5:
            Valid = False
    for item in user_destination:
        if item > 5:
            Valid = False
    if not Valid:
        tkinter.messagebox.showinfo("Error", "Your Position/Destination is not valid, must be between 0 and 5")
    elif people_ammount > 6:
        tkinter.messagebox.showinfo("Error", "Our service does not transport more than 6 people")
    else:
        Valid = True
    if Valid:
        root.destroy()
        final_car_list, distance_final_list, user_destination_distance = Client_Side_Utils.proccess_request(user_position, people_ammount, user_destination)
        Display_List.display_request_list(final_car_list, distance_final_list, user_destination_distance, user_position, user_destination)





frame_0 = Frame(root)
frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(root)
frame_4 = Frame(root)
frame_5 = Frame(root)
frame_6 = Frame(root)
frame_7 = Frame(root)

frame_0.pack()
frame_1.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()
frame_5.pack()
frame_6.pack()
frame_7.pack()

title = Label(frame_0, text="Welcome User", font=("Arial, 20"))
subtitle = Label(frame_1, text="Input your request", font=("Arial, 15"))

user_position = Label(frame_3, text="Your position:")
user_destination = Label(frame_5, text="Where do you want to go?")
user_ammount = Label(frame_2, text="How many people?")

submit_button = Button(frame_7, text="Submit")

positionX_entry_user = Entry(frame_4)
positionY_entry_user = Entry(frame_4)
positionX_entry_destination = Entry(frame_6)
positionY_entry_destination = Entry(frame_6)
ammount_entry = Entry(frame_2)

positionX_entry_user.config(width=10)
positionY_entry_user.config(width=10)
positionX_entry_destination.config(width=10)
positionY_entry_destination.config(width=10)

X_label_user = Label(frame_4, text="X:")
Y_label_user = Label(frame_4, text="Y:")
X_label_destination = Label(frame_6, text="X:")
Y_label_destination = Label(frame_6, text="Y:")

title.pack()
subtitle.pack(pady=10)
user_position.pack(pady=10)
user_destination.pack(pady=10)
user_ammount.pack(side=LEFT, pady=5)

ammount_entry.pack(side=RIGHT)

X_label_user.pack(side=LEFT)
positionX_entry_user.pack(pady=7, side=LEFT)
Y_label_user.pack(side=LEFT)
positionY_entry_user.pack(pady=7, side=LEFT)

X_label_destination.pack(side=LEFT)
positionX_entry_destination.pack(pady=7, side=LEFT)
Y_label_destination.pack(side=LEFT)
positionY_entry_destination.pack(pady=7, side=LEFT)

submit_button.pack()

submit_button.bind("<Button-1>", request)

root = mainloop()