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
    choix = int(input("Votre choix : "))
        


while not client_quitting() :
    show_welcome_message()
    identification()
    menu()
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
