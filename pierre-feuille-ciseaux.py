def pierreFeuilleCiseaux(totalRounds, totalPoints):
    roundsJoueurUn = 0
    roundsJoueurDeux = 0
    pointsJoueurUn = 0
    pointsJoueurDeux = 0
    roundNumber = 0
    int(coupJoueurID)
    print("DÉBUT DE LA PARTIE !")
    print()
    while roundsJoueurUn < totalRounds and roundsJoueurDeux < totalRounds:
        roundNumber = roundNumber + 1
        print("ROUND "+str(roundNumber))
        print()
        while pointsJoueurUn < totalPoints and pointsJoueurDeux < totalPoints :
            print("Quel coup voulez-vous jouer : Pierre, Feuille ou Ciseaux ?")
            coupJoueur = input("Votre coup : ")
            if coupJoueur == "Pierre":
                coupJoueurID = 0
            elif coupJoueur == "Feuille":
                coupJoueurID = 1
            elif coupJoueur == "Ciseaux":
                coupJoueurID = 2
            else:
                print("Ce coup n'existe pas ! Vous devez jouer pierre, feuille ou ciseaux.")
            
            
            
            