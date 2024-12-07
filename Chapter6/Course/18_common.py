my_list = [1, 2, 3]
my_tuple = (1, 2, 3, 4, 5)
my_str = "Python"

# len(conteneur): Compter le nombre d'élément
print(len(my_list))
print(len(my_tuple))
print(len(my_str))

s = my_list[0]
a = 0
while a < len(my_list):
    if s < my_list[a]:
        s = my_list[a]
    a += 1
print()