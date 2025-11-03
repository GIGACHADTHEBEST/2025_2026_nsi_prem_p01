import json

clients = {
  "ID"=1234 : [
  "mdp"=1234
  "Nom":"Encoredeguèles",
  "Prénom":"Jevés",
  "Solde": 10000,
  "Dépots": ["montant" : 563, "date": "2025-10-05"],
  "Retraits": [] 
  ],
"ID"=6767:[
  "mdp"=6767
  "Nom":"Horlayzom",
  "Prénom":"Jade",
  "Solde": 1500,
  "Dépots": ["montant" : 563, "date": "2025-10-05"],
  "Retraits": [] 
  ],
"ID"=0000:[
  "mdp"=0000
  "Nom":"Horn",
  "Prénom":"Gabe",
  "Solde": 9005,
  "Dépots": ["montant" : 563, "date": "2025-10-05"],
  "Retraits": []
  ],
"ID"=9876:[
  "mdp"=9876
  "Nom":"Swamp",
  "Prénom":"Iso",
  "Solde": 10000,
  "Dépots": ["montant" : 563, "date": "2025-10-05"],
  "Retraits": []
  ],
"ID"=5555:[
  "mdp"=5555
  "Nom":"Hoho",
  "Prénom":"Gotaga", 
  "Solde": 10000,
  "Dépots": ["montant" : 563, "date": "2025-10-05"],
  "Retraits": []
  ]
}

def read_clients_from_json_file(file):
    with open(file, 'r') as f:
        clients = json.load(f)
    return clients

def dump_clients_in_json_file(clients, "clients.json"):
    with open(file, 'w') as f:
        json.dump (clients, f, indent = 2)
    return clients


dump_clients_in_json_file(clients, "clients.json")
clients = read_clients_from_json_file("clients.json")


quitting_words = ["Bye", "bye", "q", "quit", "ciao bella"]

def client_quitting(rep):
    return rep in quitting_words

def show_welcome_message():
    print("Envoie salement des thunes")

def write_conditions():
  print({"Nos conditions d'utilisation : En acceptant les présentes conditions générales, vous reconnaissez que la Banque agit toujours dans votre intérêt et vous vous engagez à ne jamais contester,} + \
  {par quelque voie que ce soit, y compris judiciaire,administrative ou médiatique, les décisions, actions ou omissions de la Banque, même en cas de perte financière, erreur manifeste ou comportement abusif.} + \
  {Vous vous engagez également à ne pas porter plainte, ni participer à aucune action collective ou individuelle contre la Jakob Banque."})

def confirmation():
  print("Les acceptez vous ? ") 

def acceptation_condition():
  user_answer = input (1 pour ouiii 2 pour hell nah) 
  if user_answer == 1:
    print("super")
  elif user_answer == 2:
    client_quitting()
  else:
    print("repond salement stp")

def conditions_totale():
  write_conditions()
  confirmation()
  acceptation_condition()

def identification_ID():
  ID_entrée = input("Entrez votre ID")
  while ID_entrée != ID:
    ID_entrée = input("Entrez votre ID")

def identification_mdp():
  mdp_actuel
  entry = int(input("Entrez votre code PIN : "))
  while entry!=mdp_actuel:
    if entry==mdp:
      print("Accès autorisé")
      entry = int(input("Veuillez réesayer : "))
    if entry==mdp:
      print("Accès autorisé")

solde = clients[ID]["solde"]

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

def check_money(solde, montant_retrait) : 
    print(clients[])
    
        


while not client_quitting() :
    show_welcome_message()
    conditions_totale()
    identification()
    menu()
    diff_path()
