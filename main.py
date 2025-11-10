import json
import sys

def read_clients_from_json_file(file):
    with open(file, 'r') as f:
        return json.load(f)

def dump_clients_in_json_file(clients, file):
    with open(file, 'w') as f:
        json.dump (clients, f, indent = 2)
    return clients


clients = read_clients_from_json_file("clients.json")
dump_clients_in_json_file(clients, "clients.json")


quitting_words = ["Bye", "bye", "q", "quit", "ciao bella", "4"]

def client_quitting():
    sys.exit()

def show_welcome_message():
    print("Envoie salement des thunes")

def write_conditions():
    print("""
Nos conditions d'utilisation :
En acceptant les présentes conditions générales, vous reconnaissez que la Banque agit toujours dans votre intérêt et
vous vous engagez à ne jamais contester, par quelque voie que ce soit, les décisions ou actions de la Banque.
""")


def confirmation():
    print("Les acceptez vous ? ") 
    print("1 - Oui ")
    print("2 - Non ")
    
def acceptation_condition():
    user_answer = int(input("1 pour ouiii 2 pour hell nah"))
    if user_answer == 1:
        print("super")
    elif user_answer == 2:
        print ("dommage chef")
        client_quitting()
    else:
        print("repond salement stp")
        acceptation_condition()

def conditions_totale():
    write_conditions()
    confirmation()   
    acceptation_condition()

def identification():
    identification_ID()
    identification_PIN()
    return ID_entrée

    
def identification_ID():
    global ID_entrée
    ID_entrée = int(input("Entrez votre ID"))
    ID = list(clients.keys())
    while ID_entrée not in ID:
        ID_entrée = int(input("Entrez votre ID"))

def identification_PIN():
    PIN_actuel = clients[ID_entrée]["PIN"]
    entry = int(input("Entrez votre code PIN : "))
    while entry!=PIN_actuel:
        entry = int(input("Veuillez réesayer : "))
        if entry==PIN_actuel:
            print("Accès autorisé")

def check_meney(solde):
    solde = clients[ID_entrée]["solde"]
    print (f" Vous avez actuellement {solde} € sur votre compte  ")

def menu():
    print("\nMenu :")
    print("1. Consulter le solde")
    print("2. Retirer de l'argent")
    print("3. Déposer de l'argent")
    print("4. Quitter")

def take_money(solde, montant):
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

def deposit_argent(solde, montant):
    montant = int(input("Entrez le montant à déposer (multiples de 5 €) : "))
    if montant % 5 != 0:
        print("Le montant doit être un multiple de 5 €.")
        return solde
    solde = solde + montant
    print(f"Dépôt de {montant} € effectué. Nouveau solde : {solde} €")
    return solde


def diff_path():
    choix = input("Votre choix : ")
    if choix == "1":
        check_money(solde)
        print(solde)
    elif choix == "2":
        take_money(somme_voulue)
    elif choix == "3":
        deposit_money(depot_depose)
    elif choix in quitting_words: 
        print("Au revoir !")
        client_quitting()
    else:
        print("Choix invalide.")


while not client_quitting() :
    show_welcome_message()
    conditions_totale()
    identification()
    menu()
    diff_path()
