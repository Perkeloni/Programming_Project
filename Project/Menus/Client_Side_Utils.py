import math
import Car_Managing_Utils


def proccess_request(user_position, user_ammount, user_destination):
    final_car_list = []
    dist_list = {}
    sorted_car_list = []
    distance_final_list = []
    user_x = float(user_position[0])
    user_y = float(user_position[1])
    destination_x = float(user_destination[0])
    destination_y = float(user_destination[1])
    car_data = Car_Managing_Utils.update_class()  # I really should set this as global variables instead of reading from file everytime
    for item in car_data:
        distance = math.sqrt(((user_x - float(item.x)) ** 2) + ((user_y - float(item.y)) ** 2))
        buffer_var = {item.number: distance}
        dist_list.update(buffer_var)
    sorted_x = sorted(dist_list.items(), key=lambda kv: kv[1])
    sorted_x = dict(sorted_x)
    for key, value in sorted_x.items():
        temp = round(value, 1)
        distance_final_list.append(temp)
    for key in sorted_x:
        for item in car_data:
            if key == item.number:
                sorted_car_list.append(car_data[car_data.index(item)])
    if user_ammount <= 4:
        final_car_list = sorted_car_list
    if user_ammount > 4:
        for item2 in sorted_car_list:
            if item2.car_type == "van":
                van = sorted_car_list[sorted_car_list.index(item2)]
                final_car_list.append(van)
    user_destination_distance = math.sqrt(((destination_x - float(user_x)) ** 2) + ((destination_y - float(user_y)) ** 2))
    user_destination_distance = round(user_destination_distance, 1)
    return final_car_list, distance_final_list, user_destination_distance


def calculate_time_price(selection, distance, user_destination_distance):
    car_speed = selection.speed/60 #turning it into km per minute
    car_speed = round(car_speed, 2)
    total_cost = 0
    total_time = 0
    arrival_time = 0
    total_cost += selection.start_cost
    total_cost += selection.cost*(distance+user_destination_distance)
    arrival_time += round(distance/car_speed)
    total_time += round((distance+user_destination_distance)/car_speed)
    print(distance, user_destination_distance)
    print(arrival_time)
    print(total_cost)
    print(total_time)



