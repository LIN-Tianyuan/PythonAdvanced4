def user_info(name, age, gender):
    print(f"Votre nom est {name}, votre âge est {age} ans et votre sexe est {gender}.")


# Paramètres de localisation
user_info("alex", 13, "Masculin")
# Paramètres des mots-clés
user_info(name="michael", age=15, gender="Masculin")
user_info(age=12, name="lucas", gender="Masculin")
print('------------------------------------------------------------------')


# Paramètres par défaut
def user_info1(name, age, gender="Masculin"):
    print(f"Votre nom est {name}, votre âge est {age} ans et votre sexe est {gender}.")


user_info1("alex", 13)
user_info1("laurent", 13, "Féminin")
print('------------------------------------------------------------------')


# Paramètres de longueur indéterminée
# passage de position
def user_info2(*args):
    print(args)


user_info2("alex")
user_info2("laurent", 13)
user_info2("laurent", 13, "Féminin")


# passage de mot-clé
def user_info3(**kwargs):
    print(kwargs)


user_info3(name="michael", age=15, gender="Masculin")

