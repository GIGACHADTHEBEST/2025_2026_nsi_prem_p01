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
