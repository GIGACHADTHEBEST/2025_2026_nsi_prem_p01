def identification():
    entry = int(input("Entrez votre code PIN : "))
    mdp = 67
    while entry!=mdp:
        if entry==mdp:
            print("Accès autorisé")
        entry = int(input("Veuillez réesayer : "))
        if entry==mdp:
            print("Accès autorisé")
