import Login_Menu
import os


program_running = True
entry = False
admin = False

file = open(r"C:\Users\User\PycharmProjects\Projecto_Programação\Project\Databases\Login Database", "r")

while program_running == True:
    line = file.readline()
    while line != "":
        line = line.replace("/n", "")
        line = line.split(" ")
        if Login_Menu.login == (line[0]) and Login_Menu.password == (line[1]):
            if line[2] == 1:
                admin = True
        line = file.readline()
    program_running = False

if admin == True:
    os.system("python Admin_Menu.py")

