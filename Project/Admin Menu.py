from tkinter import *

root = Tk()

root.geometry("300x300")
add_car = Button(root, text="Add Car", font="Arial, 30")
car_data = Button(root, text="Car Database", font="Arial, 30")
client_data = Button(root, text="Client Database", font="Arial, 30")
welcome = Label(text="Welcome Admin", font="Arial, 25")

welcome.pack(fill=X, pady=10)
add_car.pack(fill=X)
car_data.pack(fill=X)
client_data.pack(fill=X)





root = mainloop()