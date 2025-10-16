def write_conditions():
  print("Nos conditions d'utilisation : En acceptant les présentes conditions générales, vous reconnaissez que la Banque 
  agit toujours dans votre intérêt et vous vous engagez à ne jamais contester, par quelque voie que ce soit, y compris judiciaire,
  administrative ou médiatique, les décisions, actions ou omissions de la Banque, même en cas de perte financière, erreur manifeste 
  ou comportement abusif.Vous vous engagez également à ne pas porter plainte, ni participer à aucune action collective ou individuelle contre la Jakob Banque.")

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

