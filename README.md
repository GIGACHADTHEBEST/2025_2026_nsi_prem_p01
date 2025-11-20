Gwenolé Beillevaire
Jermolaj Adarcenko
Louis El-tantawi
Raphaël Botalla 


 Ce programme simule un système de gestion bancaire simplifié, permettant à un utilisateur de :
•	accepter des conditions d’utilisation,
•	s’identifier avec un ID et un code PIN,
•	retirer ou déposer de l’argent,
•	consulter son solde,
•	et quitter le programme proprement.
Les informations des clients (ID, PIN, solde, etc.) sont stockées dans un fichier JSON (clients.json).

-  Le programme demande d'abord à l'utilisateur d'accepter les conditions d'utilisation de la banque. Si elles ne sont pas acceptées, l'utilisateur se verra expulser du programme. SI il accepte les conditions un message d'approbation sera affiché et l'utilisateur pourra continuer à s'inscrire dans notre précieuse banque. Les conditions sont définis par "write_conditions" et le fait d'accepter ces conditions est définis par "confirmation" et "acceptation_condition".
-  Le programme permet de s'indentifier avec un ID avec la fonction "identification_ID" et un code PIN avec la fonction "identification_PIN". En effet l'utilisateur après avoir entrer son ID doit entrer son mot de passe. Si il ne correspond pas, l'accès au compte sera refusé et l'utilisateur sera invité à entrer le bon mot de passe.

Le programme permet avant tout à l'utilisateur de choisir l'action qu'il veut faire entre consulter son solde, retirer de l'argent, déposer de l'argent et quitter le compte. C'est la fonction "menu" qui permet ce choix. Vous entrez le numéro qui correpond à vos besoins et vous erez dirigé vers un nouveau choix.


Le programme permet à l'utilisateur de retirer ou de déposer de l'argent sur son compte. Pour retirer de l'argent le programme propose à l'utilisateur de choisir ses billets.
La partie du programme visant à décomposer le montant de la somme d'argent que l'utilisateur cherche à retirer consiste à :
    - Choisir un montant à retirer.
    - Vérifier que le montant est un multiple de 5 car il n'existe pas de billets qui ne sont pas multiples de 5 mais aussi si le montant est supérieur au solde avec la fonction "take_money"
    - Calculer automatiquemnt la répartition de billets nécessaires si l'utilisateur choisis de prendre la répartition donnée automatiquemnt par le distributeur ou si l'utilisateur se trompe dans la répartition de billets qu'il choisit. C'est avec la fonction "decomposer_billets" que le programme permet ça.
    - Demander à l'utilisateur si il veut répartir lui même ses billets cette répartition devra être égale à la somme demandée à l'origine sinon une message d'erreur s'affichera ainsi que la répartition automatqiue de billets avec la fonction "choisir_billets"
    - Afficher de manière claire la répartition des billets automatiques ou choisies par l'utilisateur ainsi que les propositions données par le programme (ex: "Choisis un montant à retirer") et enfin les messages d'erreurs si il y en a eu avec la fonction "afficher_billets".
Le programmme permet à l'utilisateur de déposer de l'argent sur son compte. Le programme demande à l’utilisateur d’entrer un montant positif et multiple de 5 pour déposer de l’argent.
Le montant saisi est ensuite directement ajouté au solde et enregistré dans le fichier JSON. Le montant choisis sera ajouté au solde initial et le solde sera réinitialiser et mis à jour sur votre compte en banque. Cette fonction du programme est définie par " deposit_money ".

Les options du programme proposent à l'utilisateur de consulter son solde grâce à la fonction " check_money " qui consiste donc à vérifier son solde.

Si l'utilisateur le décide il peut quitter le programme grâce à la fonction " quitting_words ".

Role des membre du groupe dans le projet :
- Jermolajs :
   - Principal codeur du projet
   - Impliqué dans toutes les fonctions du programme
   - Participation au json
   - Correction et amélioration du programme
   - création du menu
- Louis :
   - Implication dans toutes les fonctions du programme
   - Création de la fonction "take_money" et "deposit_money"
   - création des différents choix dans l'interface
- Gwenolé :
   - Ecriture parfaite ET magnifique ET incroyable ET meilleur ET rarissime du readme tout a fait splendide
   - cocréation de la fonction "choisir_billets"
   - aide dans les fonctions "take_money" et "deposit_money"
- Raphaël :
   - Participation au json
   - Création de fonction "write_conditions"
   - cocréation de la fonction "choisir_billets"
 
Très grande difficultée dans la réalisation du json et de l'appel personnalisé de chaque utilisateur grace à l'ID qui permet de personnaliser chaque donnée (nom, prénom, PIN, solde...). D'autres difficultées moins conséquentes sont apparus, le fait de les résoudre nous a permis de nous forger pour améliorer drastiquement notre capacité à coder. 
   

 
