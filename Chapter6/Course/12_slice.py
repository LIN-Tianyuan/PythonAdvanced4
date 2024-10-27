my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:4]
print(new_list) # [2, 3, 4]
new_list2 = my_list[::2]
print(new_list2)

my_tuple = (1, 2, 3, 4, 5)
# new_tuple = my_tuple[0:4]
new_tuple = my_tuple[:4]
print(new_tuple)    # (1, 2, 3, 4)

my_str = "12345"
new_str = my_str[:4]
print(new_str)

my_str2 = "12345"
new_str2 = my_str2[::-1]
print(new_str2)

my_list3 = [1, 2, 3, 4, 5]
# new_list3 = my_list3[-2:-4:-1]
new_list3 = my_list3[3:1:-1]
print(new_list3)

my_tuple2 = (1, 2, 3, 4, 5)
new_tuple2 = my_tuple2[4:1:-2]
print(new_tuple2)