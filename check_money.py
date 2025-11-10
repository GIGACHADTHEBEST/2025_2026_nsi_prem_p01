money_given = int(input("Entre la valeur de l argent que tu veux déposer"))
clients[ID]["Solde"]= money_given + clients[ID]["Solde"]
print(f"votre compte a maitenant {money_given} de plus donc votre compte a {clients[ID]["Solde"]} euros" )
