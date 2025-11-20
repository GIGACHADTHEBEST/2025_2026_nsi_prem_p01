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
        if entry == PIN_actuel:
            print("Accès autorisé")
            break
        print("Code PIN incorrect, réessayez.")
