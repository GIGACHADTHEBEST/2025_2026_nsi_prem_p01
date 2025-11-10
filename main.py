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
    try:
        user_answer = int(input("1 pour ouiii 2 pour hell nah"))
    except ValueError:
        print("Répond correctement stp")
        acceptation_condition()
        return  # Pour éviter de continuer après récursion
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
    return ID_entrée

def solde_for_all():
    global solde
    solde = clients[ID_entrée]["solde"]
    
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
    print("Accès autorisé")


def decomposer_billets(montant):
    if montant % 5 != 0:
        return "Le montant doit être un multiple de 5."

    billets = {}
    reste = montant

    for valeur in [50, 20, 10, 5]:
        billets[valeur], reste = divmod(reste, valeur)
    return billets

def afficher_billets(billets):
    if isinstance(billets, str):
        print(billets)
        return
    
    print("\n💶 Vous recevrez :")
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
        print(f"\n⚠️ La somme choisie ({total} €) ne correspond pas au montant demandé ({montant} €).")
        print("On vous proposera la décomposition automatique.")
        return decomposer_billets(montant)
    else:
        print("\n✅ Choix validé !")
        return choix
def check_money():
    global solde
    solde = clients[ID_entrée]["solde"]
    print (f" Vous avez actuellement {solde} € sur votre compte  ")
    return solde

def menu():
    print("\nMenu :")
    print("1. Consulter le solde")
    print("2. Retirer de l'argent")
    print("3. Déposer de l'argent")
    print("4. Quitter")

def take_money(solde):
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

def deposit_(solde):
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
        take_money(solde)
    elif choix == "3":
        deposit_money(solde)
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
    solde_for_all()
    diff_path()
