Gwenolé Beillevaire
Jermolaj Adarcenko
Louis El-tantawi
Raphaël Botalla 


 Ce programme simule un système de gestion bancaire simplifié, permettant à un utilisateur de :
•	s’identifier avec un ID et un code PIN,
•	consulter son solde,
•	retirer ou déposer de l’argent,
•	accepter des conditions d’utilisation,
•	et quitter le programme proprement.
Les informations des clients (ID, PIN, solde, etc.) sont stockées dans un fichier JSON (clients.json).

Le programme demande d'abord à l'utilisateur d'accepter les conditions d'utilisation de la banque. Si elles ne sont pas acceptées, l'utilisateur se verra expulser du programme. SI il accepte les conditions un message d'approbation sera affiché et l'utilisateur pourra continuer à s'inscrire dans notre précieuse banque.

 
 
 La partie du programme visant à décomposer le montant de la somme d'argent que l'utilisateur cherche à retirer consiste à :
    - Vérifier que le montant est un multiple de 5 car il n'existe pas de billets qui ne sont pas multiples de 5.
    - Calculer automatiquemnt la répartition de billets nécessaires si l'utilisateur choisis de prendre la répartition donnée automatiquemnt par le distributeur ou si l'utilisateur se trompe dans la répartition de billets qu'il choisit
    - Demander à l'utilisateur si il veut répartir lui même ses billets cette répartition devra être égale à la somme demandée à l'origine sinon une message d'erreur s'affichera ainsi que la répartition automatqiue de billets,
    - Afficher de manière claire la répartition des billets automatiques ou choisies par l'utilisateur ainsi que les propositions données par le programme (ex: "Choisis un montant à retirer") et enfin les messages d'erreurs si il y en a eu.

 
