#currently unused

from tkinter import *

root = Tk()
root.geometry("300x300")
root.resizable(width=False, height=False)

frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(root)
frame_4 = Frame(root)
frame_5 = Frame(root)

frame_1.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()

title = Label(frame_1, text="How do you want to search:", font="Arial, 15")

alphabetic = Button(frame_2, text="Alphabetically")
name_search = Label(frame_3, text="By Name:")
name_entry = Entry(frame_3)

submit_button = Button(frame_4, text="Submit")

title.pack(pady=15)
alphabetic.pack(pady=15)
name_search.pack(side=LEFT, pady=15)
name_entry.pack(side=LEFT, pady=15)
submit_button.pack(pady=15)

root = mainloop()