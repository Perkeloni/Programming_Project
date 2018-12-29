#print(Login_Menu.login)
#print(Login_Menu.password)

def check_password(login, password):

    global admin
    program_running = True
    entry = False
    admin = False
    print(login)
    print(password)

    file = open(r"C:\Users\User\PycharmProjects\Projecto_Programação\Project\Databases\Login_Database", "r")

    while program_running == True:
        line = file.readline()

        while line != "":
            line = line.replace("/n", "")
            line = line.split(" ")
            print(line[0])
            print(line[1])
            if login == (line[0]) and password == (line[1]):
                if line[2] == 1:
                    admin = True
            line = file.readline()

        program_running = False
        file.close()

    if admin == True:
        os.system("python Admin_Menu.py")

