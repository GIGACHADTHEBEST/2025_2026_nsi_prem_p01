def menu():
    identification()
    while True:
        print("\nMenu :")
        print("1. Consulter le solde")
        print("2. Retirer de l'argent")
        print("3. Déposer de l'argent")
        print("4. Quitter")
        choix = input("Votre choix : ")
        if choix == "1":
            consulter_solde(solde)
        elif choix == "2":
            solde = retirer_argent(solde)
        elif choix == "3":
            solde = deposer_argent(solde)
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")
