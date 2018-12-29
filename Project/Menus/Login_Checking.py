#print(Login_Menu.login)
#print(Login_Menu.password)
import os

def check_login(login, password):

    global admin
    program_running = True
    entry = False
    admin = False

    file = open(r"C:\Users\User\PycharmProjects\Projecto_Programação\Project\Databases\Login_Database", "r")

    while program_running == True:
        line = file.readline()

        while line != "":
            line = line.replace("/n", "")
            line = line.split(" ")

            if login == (line[0]) and password == (line[1]):
                if int(line[2]) == 1:
                    admin = True

            line = file.readline()

        program_running = False
        file.close()

    if admin:
        os.system("python Admin_Menu.py")

