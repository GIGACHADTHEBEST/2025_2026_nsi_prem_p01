import json
import sys

def read_clients_from_json_file(file):
    with open(file, 'r') as f:
        return json.load(f)

def dump_clients_in_json_file(clients, file):
    with open(file, 'w') as f:
        json.dump(clients, f, indent=2)
    return clients


clients = read_clients_from_json_file("clients.json")

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
    identification_ID()
    identification_PIN()

def solde_for_all():
    global solde
    solde = clients[ID_entrée]["solde"]

def identification_ID():
    while True:
        try:
            ID_entrée = input("Entrez votre ID : ")

            if ID_entrée in clients:
                return ID_entrée

            print("ID invalide, réessayez.")
        except ValueError:
            print("Entrée invalide.")

def identification_PIN():
    PIN_actuel = clients[ID_entrée]["PIN"]
    entry = int(input("Entrez votre code PIN : "))
    while entry != PIN_actuel:
        entry = int(input("Veuillez réessayer : "))
    print("Accès autorisé")

def take_money(solde):
    montant = int(input("Entrez le montant à retirer : "))
    if montant % 5 != 0:
        print("Le montant doit être un multiple de 5 €.")
        return solde
    if montant > solde:
        print("Fonds insuffisants.")
        return solde
    solde -= montant
    print(f"Retrait de {montant} € effectué. Nouveau solde : {solde} €")
    return solde

def deposit_money(solde):
    montant = int(input("Entrez le montant à déposer : "))
    if montant % 5 != 0:
        print("Le montant doit être un multiple de 5 €.")
        return solde
    solde += montant
    print(f"Dépôt de {montant} € effectué. Nouveau solde : {solde} €")
    return solde

def check_money():
    global solde
    solde = clients[ID_entrée]["solde"]
    print(f"Vous avez actuellement {solde} €")
    return solde

def menu():
    print("\nMenu :")
    print("1. Consulter le solde")
    print("2. Retirer de l'argent")
    print("3. Déposer de l'argent")
    print("4. Quitter")


show_welcome_message()
conditions_totale()
identification()
solde_for_all()

while True:
    menu()
    choix = input("Votre choix : ")

    if choix == "1":
        check_money()

    elif choix == "2":
        solde = take_money(solde)
        clients[ID_entrée]["solde"] = solde
        dump_clients_in_json_file(clients, "clients.json")

    elif choix == "3":
        solde = deposit_money(solde)
        clients[ID_entrée]["solde"] = solde
        dump_clients_in_json_file(clients, "clients.json")

    elif choix in quitting_words or choix == "4":
        print("Au revoir !")
        client_quitting()

    else:
        print("Choix invalide.")
