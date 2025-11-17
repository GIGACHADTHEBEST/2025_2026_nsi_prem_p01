import json
import sys

def read_clients_from_json_file(file):
    with open(file, 'r') as f:
        return json.load(f)

def dump_clients_in_json_file(clients, file):
    with open(file, 'w') as f:
        json.dump(clients, f, indent=2)
    return clients

clients_data = read_clients_from_json_file("clients.json")
clients = clients_data["clients"]

quitting_words = ["Bye", "bye", "q", "quit", "ciao bella", "4"]

def client_quitting():
    print("Au revoir !")
    sys.exit()

def show_welcome_message():
    print("Envoie salement des thunes")

def write_conditions():
    print("""
Nos conditions d'utilisation :

En acceptant ces conditions, vous reconnaissez officiellement que la Banque est toujours parfaite, 
même lorsqu’elle ne l’est absolument pas. Vous acceptez également de ne jamais porter plainte, 
même en cas de vol, disparition mystérieuse de votre argent, ou intrusion de pigeons dans votre compte.

Vous vous engagez aussi à sourire en toutes circonstances, à répondre "oui" sans lire les petits astérisques,
et à ne jamais demander pourquoi les frais augmentent chaque mardi à 3h17 du matin.

Merci de votre compréhension, ou de l’illusion de celle-ci.
""")

def confirmation():
    print("Les acceptez vous ? ")
    print("1 - Oui ")
    print("2 - Non ")

def acceptation_condition():
    try:
        user_answer = int(input("1 pour ouiii 2 pour hell nah : "))
    except ValueError:
        print("Répond correctement stp")
        return acceptation_condition()

    if user_answer == 1:
        print("super")
    elif user_answer == 2:
        print("dommage chef")
        client_quitting()

def conditions_totale():
    write_conditions()
    confirmation()
    acceptation_condition()

def identification():
    ID = identification_ID()
    identification_PIN(ID)
    return ID

def identification_ID():
    while True:
        ID = input("Entrez votre ID : ") 
        if ID in clients:
            return ID
        print("ID invalide, réessayez.")

def identification_PIN(ID):
    PIN_actuel = clients[ID]["PIN"]
    while True:
        try:
            entry = int(input("Entrez votre code PIN : "))
        except ValueError:
            print("Code PIN invalide, entrez un nombre.")
            continue
        if entry == PIN_actuel:
            print("Accès autorisé")
            break
        print("Code PIN incorrect, réessayez.")

def check_money(ID):
    solde = clients[ID]["Solde"]  # utilise la clé "Solde"
    print(f"Vous avez actuellement {solde} €")
    return solde
    
def take_money(ID):
    solde = clients[ID]["Solde"]  # utilise la clé "Solde"
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
        mode = input("Votre choix : ")
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
        clients[ID].setdefault("Retraits", []).append(montant)
        dump_clients_in_json_file(clients, "clients.json")
        print(f"\nRetrait de {montant} € effectué. Nouveau solde : {solde} €")
        break
    return solde

def deposit_money(ID):
    solde = clients[ID]["Solde"]  # utilise la clé "Solde"
    while True:
        try:
            montant = int(input("Entrez le montant à déposer : "))
        except ValueError:
            print("Entrée invalide, entrez un nombre.")
        if montant <= 0:
            print("Montant invalide.")
        if montant % 5 != 0:
            print("Le montant doit être un multiple de 5 €.") 
        solde += montant
        clients[ID]["Solde"] = solde
        clients[ID].setdefault("Depots", []).append(montant)
        dump_clients_in_json_file(clients, "clients.json")
        print(f"Dépôt de {montant} € effectué. Nouveau solde : {solde} €")
        break
    return solde
    
def decomposer_billets(montant):
    billets = {}
    reste = montant
    for valeur in [50, 20, 10, 5]:
        billets[valeur], reste = divmod(reste, valeur)
    return billets

def afficher_billets(billets):
    print("\nVous recevrez :")
    for valeur, quantite in billets.items():
        if quantite > 0:
            print(f"- {quantite} billet(s) de {valeur} €")

def choisir_billets(montant):
    print(f"\nMontant à retirer : {montant} €")
    print("Composez vos billets (entrez 0 si vous ne voulez pas ce type de billet)")
    total = 0
    choix = {}
    for valeur in [50, 20, 10, 5]:
        max_billets = montant // valeur
        try:
            quantite = int(input(f"Combien de billets de {valeur} € ? (max {max_billets}) : "))
        except ValueError:
            print("Entrée invalide, remise à 0.")
            quantite = 0
        if quantite < 0 or quantite > max_billets:
            print("Quantité invalide, remise à 0.")
            quantite = 0
        choix[valeur] = quantite
        total += valeur * quantite

    if total != montant:
        print(f"\nLa somme choisie ({total} €) ne correspond pas au montant demandé ({montant} €).")
        print("On vous proposera la décomposition automatique.")
        return decomposer_billets(montant)
    else:
        print("\nChoix validé !")
        return choix

def menu():
    print("\nMenu :")
    print("1. Consulter le solde")
    print("2. Retirer de l'argent")
    print("3. Déposer de l'argent")
    print("4. Quitter")

show_welcome_message()
conditions_totale()
ID_entrée = identification()

while True:
    menu()
    choix = input("Votre choix : ")

    if choix == "1":
        check_money(ID_entrée)
    elif choix == "2":
        take_money(ID_entrée)
    elif choix == "3":
        deposit_money(ID_entrée)
    elif choix in quitting_words or choix == "4":
        client_quitting()
    else:
        print("Choix invalide.")
