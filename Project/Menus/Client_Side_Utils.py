import math
import Car_Managing_Utils



def proccess_request(user_position, user_destination):
    dist_list = {}
    user_x = float(user_position[0])
    user_y = float(user_position[1])
    user_destination_x = float(user_destination[0])
    user_destination_y = float(user_destination[1])
    car_data = Car_Managing_Utils.update_class()  # I really should set this as global variables instead of reading from file everytime
    for item in car_data:
        distance = math.sqrt(((user_x - float(item.x)) ** 2) + ((user_y - float(item.y)) ** 2))
        buffer_var = {item.number: distance}
        dist_list.update(buffer_var)
    sorted_x = sorted(dist_list.items(), key=lambda kv: kv[1])
    sorted_x = dict(sorted_x)
    print(sorted_x)
    print (type(sorted_x))

