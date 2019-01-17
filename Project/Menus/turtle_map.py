import turtle


def turtle_map(user_destination, user_location, car_list):

    def set_user_location(user_location):
        user = turtle.Turtle()
        user.penup()
        user.left(90)
        user.forward(250)
        user.left(90)
        user.forward(250)
        user.left(90)
        user.forward(500)
        user.left(90)
        user_x = user_location[0]*100
        user_y = user_location[1]*100
        user.forward(user_x)
        user.left(90)
        user.forward(user_y)
        user.color("green")

    def set_user_destination(user_destination):
        destination = turtle.Turtle()
        destination.penup()
        destination.left(90)
        destination.forward(250)
        destination.left(90)
        destination.forward(250)
        destination.left(90)
        destination.forward(500)
        destination.left(90)
        destination_x = user_destination[0] * 100
        destination_y = user_destination[1] * 100
        destination.forward(destination_x)
        destination.left(90)
        destination.forward(destination_y)
        destination.color("red")

    def set_cars(car_object_list):

        for item in car_object_list:
            car = turtle.Turtle()
            car.penup()
            car.left(90)
            car.forward(250)
            car.left(90)
            car.forward(250)
            car.left(90)
            car.forward(500)
            car.left(90)
            x = float(item.x)*100
            y = float(item.y)*100
            car.forward(x)
            car.left(90)
            car.forward(y)








    map = turtle.Turtle()

    map.penup()
    map.forward(250)
    map.right(90)
    map.pendown()
    map.forward(250)
    map.right(90)
    map.forward(500)
    map.right(90)
    map.forward(500)
    map.right(90)
    map.forward(500)
    map.right(90)
    map.forward(250)

    map.ht()

    set_user_location(user_location)
    set_user_destination(user_destination)
    set_cars(car_list)




    turtle.done()


def turtle_close():
    turtle.Screen().bye()
