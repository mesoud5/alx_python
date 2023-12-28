def multiply_list_map(my_list=[], number=0):
    result_list = list(map(lambda x: x * number, my_list))
    return result_list
mesoud_list = [1, 4, 6, 9, 5]
mesoud_number = 3
print(multiply_list_map(mesoud_list, mesoud_number))