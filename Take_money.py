def take_money(ID):
    solde = clients[ID]["Solde"]
    while True:
        try:
            montant = int(input("Entrez le montant à retirer : "))
        except ValueError:
            print("Entrée invalide, entrez un nombre.")
            continue
        if montant <= 0:
            print("Montant invalide.")
            continue
        if montant % 5 != 0:
            print("Le montant doit être un multiple de 5 €.")
            continue
        if montant > solde:
            print("Fonds insuffisants.")
            continue
        print("\nSouhaitez-vous :")
        print("1 - Décomposition automatique des billets")
        print("2 - Choisir vous-même les billets")
        mode = input("1 - Décomposition automatique des billets 2 - Choisir vous-même les billets. Votre choix : ")
        if mode == "2":
            billets = choisir_billets(montant)
            print("\nDécomposition choisie :")
            afficher_billets(billets)
        else:
            billets = decomposer_billets(montant)
            print("\nDécomposition automatique :")
            afficher_billets(billets)
        solde -= montant
        clients[ID]["Solde"] = solde
        if "Retraits" not in clients[ID]:
            clients[ID]["Retraits"] = []
            clients[ID]["Retraits"].append(montant)
        dump_clients_in_json_file(clients, "clients.json")
        print(f"\nRetrait de {montant} € effectué. Nouveau solde : {solde} €")
        break
    return solde
