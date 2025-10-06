def menu():
    solde = identification()
    while True:
        print("\nMenu :")
        print("1. Consulter le solde")
        print("2. Retirer de l'argent")
        print("3. Déposer de l'argent")
        print("4. Quitter")
        choix = int(input("Votre choix : "))
        if choix == 1:
            check_money(solde)
        elif choix == 2:
            solde = money_taken(solde)
        elif choix == 3:
            solde = money_given(solde)
        elif choix == 4:
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")
menu()
