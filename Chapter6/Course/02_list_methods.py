name_list = ['Leo', 'Lucas', 'Laurent']
print(name_list.index('Lucas'))
name_list.insert(1, 'Kevin')
print(name_list)

my_list = [1, 2, 3]
# my_list[0] = 5
my_list.append(4)
print(my_list)
print('-------------------')
my_list2 = [1, 2, 3]
my_list2.append([4, 5, 6])
print(my_list2)
print('-------------------')
my_list3 = [1, 2, 3]
my_list3.extend([4, 5, 6])
print(my_list3)
print('-------------------')
my_list4 = [1, 2, 3]
del my_list4[0]
print(my_list4)
print('-------------------')
my_list5 = [1, 2, 3]
my_list5.pop(0)
print(my_list5)
print('-------------------')
my_list6 = [1, 2, 3, 2, 3]
my_list6.remove(2)
print(my_list6)
print('-------------------')
my_list7 = [1, 2, 3]
my_list7.clear()
print(my_list7)
print('-------------------')
my_list8 = [1, 1, 1, 2, 3]
print(my_list8.count(1))
print(len(my_list8))