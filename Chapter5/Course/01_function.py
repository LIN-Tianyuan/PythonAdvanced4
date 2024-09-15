def park():
    print("Bienvenue au parc d'attractions, veuillez montrer votre ticket.")


def check(number):
    park()
    if number <= 100:
        print("Votre nombre est inférieur à 100, vous pouvez maintenant entrer pour visiter. ")
    else:
        print("Votre nombre est supérieur à 100, salle comble, revenez la prochaine fois.")


check(99)

def check_age(age):
    if age > 18:
        return "SUCCESS"
    return None
result = check_age(5)
print(result)
if not result:
    print("Not enter.")
