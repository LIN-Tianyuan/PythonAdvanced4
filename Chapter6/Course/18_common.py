my_list = [1, 2, 3]
my_tuple = (1, 2, 3, 4, 5)
my_str = "Python"

# len(conteneur): Compter le nombre d'élément
print(len(my_list))
print(len(my_tuple))
print(len(my_str))
print('----------')
print(max(my_list))
print(max(my_tuple))
print(max(my_str))
print('----------')
print(min(my_list))
print(min(my_tuple))
print(min(my_str))
"""
# Max
s = my_list[0]
a = 0
while a < len(my_list):
    if s < my_list[a]:
        s = my_list[a]
    a += 1
print(s)
"""
print('----------')
print(tuple(my_list))
print('----------')
my_list2 = [8, 5, 9, 2, 3, 4]
print(sorted(my_list2))
print('----------')
print('abc' < 'abd')
print('a' > 'A')
print('key2' > 'key1')
print('bgh' > 'byws')
