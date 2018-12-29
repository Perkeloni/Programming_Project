from tkinter import *
import os



def add_car_exec(self):
    root.destroy()
    os.system("python Add_Car_Menu.py")

def car_data_exec(self):
    root.destroy()
    os.system("python Search_Car_Menu.py")

def client_data_exec(self):
    root.destroy()
    os.system("python Search_Client_Menu.py")


root = Tk()

root.geometry("300x300")
root.resizable(width=False, height=False)

add_car = Button(root, text="Add Car", font="Arial, 30")
car_data = Button(root, text="Car Database", font="Arial, 30")
client_data = Button(root, text="Client Database", font="Arial, 30")
welcome = Label(text="Welcome Admin", font="Arial, 25")

welcome.pack(fill=X, pady=10)
add_car.pack(fill=X)
car_data.pack(fill=X)
client_data.pack(fill=X)

add_car.bind("<Button-1>", add_car_exec)
car_data.bind("<Button-1>", car_data_exec)
client_data.bind("<Button-1>", client_data_exec)



root = mainloop()