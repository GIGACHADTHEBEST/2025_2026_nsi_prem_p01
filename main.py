quitting_words = ["Bye", "bye", "q", "quit", "ciao bella"]

def client_quitting(rep):
    return rep in quitting_words

def show_welcome_message():
    print("Envoie salement des thunes")

def menu():
    print("\nMenu :")
    print("1. Consulter le solde")
    print("2. Retirer de l'argent")
    print("3. Déposer de l'argent")
    print("4. Quitter")

def diff_path():
    choix = int(input("Votre choix : "))
    if choix == 1:
        check_money(solde)
        print(solde)
    elif choix == 2:
        take_money(somme_voulue)
        solde = solde - take_money(somme_voulue)
        print(print (f" Vous avez actuellement {solde} € sur votre compte  "))
    elif choix == 3:
        deposit_money(depot_depose)
        solde = solde + deposit_money(depot_depose)
        print(solde)
    elif choix == 4: 
        print("Au revoir !")
    else:
        print("Choix invalide.")
        


while not client_quitting() :
    show_welcome_message()
    identification()
    menu()
    diff_path()
