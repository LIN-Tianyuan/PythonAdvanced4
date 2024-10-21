name = "Alex"
print(name[0])      # A
print(len(name))    # 4
print(name[3])      # x
print(name[-1])     # x

# Trouver la valeur de l'indice d'un string
name_string = "Leo and laurent"
print(name_string.index('and'))
print(name_string.index('Leo'))
print(name_string.index('laurent'))
print(name_string[3])

# Substitution de chaîne de caractères
new_name_string = name_string.replace("Leo", "Kevin")
print(name_string)
print(new_name_string)

# Fractionnement des chaînes de caractères
name_list = name_string.split(" ")
print(name_list)

# Suppression des espaces avant et arrière
name_string2 = "  Leo and laurent   "
new_name_string2 = name_string2.strip()
print(new_name_string2)  # Leo and laurent

# Suppression de la chaîne spécifiée  avant et arrière
name_string3 = "12Leo and laurent21"
new_name_string3 = name_string3.strip('12')
print(new_name_string3)  # Leo and laurent

# Compter le nombre d'occurrences d'une chaîne de caractères
name_string4 = "Jean-Lucas and Lucas"
print(name_string4.count("Lucas"))  # 2




