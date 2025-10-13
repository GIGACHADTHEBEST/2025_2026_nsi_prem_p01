def retirer_argent(solde):
    montant = input("Entrez le montant à retirer (multiples de 5 €) : ")
    if montant % 5 != 0:
        print("Le montant doit être un multiple de 5 €.")
        return solde
    if montant > solde:
        print("Fonds insuffisants.")
        return solde
    billets = decomposer_billets(montant)
    print("Retrait effectué. Billets délivrés :")
    solde -= montant
    return solde
