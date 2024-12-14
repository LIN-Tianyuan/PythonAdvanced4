number = int(input("Veuillez entrer un nombre entier: "))
a = 1
list1 = []
list_lucky = []
while a <= number:
    list1.append(a)
    a = a + 1
print(f"La liste nums est: {list1}")

for number in list1:
    if number % 6 == 0:
        list_lucky.append(number)

print(f"La liste lucky est: {list_lucky}")
