age = 20
year = 3
level = 1
if age > 18 and age < 30:
    print("Adultes en forme, continuez à juger.")
    if year > 2:
        print("Vous êtes un adulte âgé de moins de 30 ans et vous travaillez depuis plus de 2 ans."
              "vous remplissez les conditions et vous pouvez recevoir les cadeaux.")
    elif level > 3:
        print("Cadeaux direct pour les adultes ayant un niveau supérieur à 3.")
    else:
        print("Désolé, l'âge correspond, mais pas assez de temps pour l'inscrire.")
else:
    print("Désilé, pas de cadeaux.")
