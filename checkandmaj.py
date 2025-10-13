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
    print(f"Retrait de {montant} € effectué. Nouveau solde : {solde} €")
    return solde

def deposer_argent(solde):
    montant = input("Entrez le montant à déposer (multiples de 5 €) : ")
    if montant % 5 != 0:
        print("Le montant doit être un multiple de 5 €.")
        return solde
    solde += montant
    print(f"Dépôt de {montant} € effectué. Nouveau solde : {solde} €")
    return solde
