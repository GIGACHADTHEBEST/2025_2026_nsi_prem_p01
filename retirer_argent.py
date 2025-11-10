def retirer_argent(solde):
    montant = int(input("Entrez le montant à retirer (multiples de 5 €) : "))
    if montant % 5 != 0:
        print("Le montant doit être un multiple de 5 €.")
        return solde
    elif montant > solde:
        print("Fonds insuffisants.")
        return solde
    billets = decomposer_billets(montant)
    print("Retrait effectué. Billets délivrés :")
    solde = solde-montant
    print(f"Retrait de {montant} € effectué. Nouveau solde : {solde} €")
    return solde
