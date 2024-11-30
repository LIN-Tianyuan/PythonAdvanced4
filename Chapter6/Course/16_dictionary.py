"""
stu_score = {"Alex": 99, "Michael": 88, "Lucas": 77}
print(stu_score["Alex"])
print(stu_score["Lucas"])
"""
"""
stu_score = {
    "Alex": {"C": 77, "Python": 66, "Java": 33},
    "Michael": {"C": 88, "Python": 86, "Java": 55},
    "Lucas": {"C": 99, "Python": 96, "Java": 66}
}

print(stu_score["Michael"]["Python"])
"""
stu_score = {"Alex": 99, "Michael": 88, "Lucas": 77}
# Ajouter
stu_score["Kevin"] = 66
print(stu_score)
# Modifier
stu_score["Kevin"] = 55
print(stu_score)
# Supprimer
value = stu_score.pop("Kevin")
print(value)
print(stu_score)
# Vider
# stu_score.clear()
# print(stu_score)
# Obtenir toutes les clés
keys = stu_score.keys()
print(keys)
# Itération
for key in keys:
    print(f"Student: {key}, Score: {stu_score[key]}")
# Longueur du dictionnaire
print(len(stu_score))