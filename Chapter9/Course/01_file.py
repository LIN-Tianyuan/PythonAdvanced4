"""
try:
    f = open('linux.txt', 'r')
except:
    f = open('linux.txt', 'w')
"""

print("----------")
try:
    print(name)
except NameError as e:
    print("Erreur de nom de variable non défnie.")
print("----------")
try:
    print(1/0)
except (ZeroDivisionError, NameError) as e:
    print(e)
print("----------")

try:
    print(1)
except Exception as e:
    print(e)
else:
    print("Je suis else, le code qui est exécuté quand il n'y a pas d'exception.")
print("----------")


try:
    f = open('test.txt', 'r')
except:
    f = open('test.txt', 'w')
else:
    print("Aucune anomalie, donc heureux")
finally:
    f.close()