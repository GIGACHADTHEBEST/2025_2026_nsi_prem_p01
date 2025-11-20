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
    user_answer = input("1 pour continuer, autre chose pour quitter : ")
    if user_answer == "1":
        print("Super, on continue !")
    else:
        print("Merci, bonne journée !")
        sys.exit(0)

def conditions_totale():
    write_conditions()
    confirmation()
    acceptation_condition()
