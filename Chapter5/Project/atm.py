money = 5000000
name = input("Veuillez entrer votre nom: ")


def query():
    print("---------Vérifiez votre solde----------")
    print(f"{name}, bonjour, il vous reste un solde de {money} euros.")
    main()


def save_money():
    global money
    save = int(input("Combien voulez-vous économiser? Veuillez entrer: "))
    print("---------Dépôts----------")
    print(f"{name}, bonjour, votre dépôt de {save} euros a été accepté.")
    money += save
    print(f"{name}, bonjour, il vous reste un solde de {money} euros.")
    main()


def draw_money():
    global money
    draw = int(input("Combien voulez-vous retirer? Veuillez entrer: "))
    print("---------Retraits----------")
    print(f"{name}, bonjour, votre retrait de {draw} euros a été effectué.")
    money = money - draw
    print(f"{name}, il vous reste un solde de {money} euros.")
    main()


def main():
    print("----------Menu principal----------")
    print(f"{name}, bonjour, bienvenue à ATM, veuillez sélectionner l'opération:")
    print("Vérifier le solde [Entrer 1]")
    print("Dépôts            [Entrer 2]")
    print("Retraits          [Entrer 3]")
    print("Sortie            [Entrer 4]")
    choice = int(input("Veuillez entrer votre choix: "))
    if choice == 1:
        query()
    if choice == 2:
        save_money()
    if choice == 3:
        draw_money()
    if choice == 4:
        print("Sortie du programme!")
    if choice not in [1, 2, 3, 4]:
        main()


main()