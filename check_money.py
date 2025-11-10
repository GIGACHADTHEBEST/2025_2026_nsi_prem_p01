def check_meney():
    global solde
    solde = clients[ID_entrée]["solde"]
    print (f" Vous avez actuellement {solde} € sur votre compte  ")
    return solde
