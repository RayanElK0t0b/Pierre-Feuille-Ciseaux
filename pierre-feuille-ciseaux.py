# On définie une fonction pierreFeuilleCiseaux qui prend en paramètre le nombre de rounds voulu pour la victoire ainsi que le nombre de points voulu pour gagner un round
def pierreFeuilleCiseaux(totalRounds, totalPoints):
    # On importe la librairie "random"
    import random
    # On initialise le nombre de rounds gagnés par le joueur à 0
    roundsJoueur = 0
    # On initialise le nombre de rounds gagnés par l'ordinateur à 0
    roundsOrdinateur = 0
    # On initialise le nombre de points du joueur à 0
    pointsJoueur = 0
    # On initialise le nombre de points de l'ordinateur à 0
    pointsOrdinateur = 0
    # On initialise le numéro du round à 0
    roundNumber = 0
    # On définie un booléan qui nous dis si le coup du joueur est valable ou non, le joueur n'ayant pas encore jouer, il est faux
    coupValable = False
    # Saut d'une ligne
    print()
    # Affichage du message "DÉBUT DE LA PARTIE !"
    print("DÉBUT DE LA PARTIE !")
    # Saut d'une ligne
    print()
    # Affichage des règles du jeu
    print("Règles du jeu : Vous jouez contre un ordinateur et en même temps que lui au tour par tour.")
    print("Vous et l'ordinateur avez le choix entre 3 coups différents : Pierre, Feuille, Ciseaux.")
    print("La Pierre bat les Ciseaux, les Ciseaux battent la Feuille, la Feuille bat la Pierre")
    print("Le joueur ayant un signe gagnant remporte 1 point. Il lui faut "+str(totalPoints)+" pour gagner un round, et "+str(totalRounds)+" pour gagner la partie")
    # Saut d'une ligne
    print()
    # Tant que le nombre de rounds gagnés par le joueur ET que le nombre de rounds gagnés par l'ordinateur sont infèrieur au nombre de rounds voulu pour la victoire
    while roundsJoueur < totalRounds and roundsOrdinateur < totalRounds:
        # Alors on ajoute 1 a au nombre du round
        roundNumber = roundNumber + 1
        # On affiche le numéro du round
        print("ROUND "+str(roundNumber))
        # Saut d'une ligne
        print()
        # Tant que le nombre de points du joueur ET que le nombre de points de l'ordinateur sont infèrieur au nombre de points voulu pour gagner un round
        while pointsJoueur < totalPoints and pointsOrdinateur < totalPoints:
            # Alors on demande au joueur quel coup il veut jouer
            coupJoueur = input("Votre coup : ")
            # Tant que le joueur ne donne pas de coup valable
            while coupValable == False:
                # Alors on considère son coup comme valable
                coupValable = True
                # Si le joueur joue "Pierre" ou "pierre"
                if coupJoueur == "Pierre" or coupJoueur == "pierre":
                    # Alors on définie l'ID du coup du joueur à 0
                    coupJoueurID = 0
                # Si le joueur joue "Feuille" ou "feuille"
                elif coupJoueur == "Feuille" or coupJoueur == "feuille":
                    # Alors on définie l'ID du coup du joueur à 1
                    coupJoueurID = 1
                # Si le joueur joue "Ciseaux" ou "ciseaux"
                elif coupJoueur == "Ciseaux" or coupJoueur == "ciseaux":
                    # Alors on définie l'ID du coup du joueur à 2
                    coupJoueurID = 2
                # Si le joueur rentre "Exit" ou "exit"
                elif coupJoueur == "Exit" or coupJoueur == "exit":
                    # Tant que le joueur ne répond pas "Oui", "oui", "Non" ou "non"
                    while coupJoueur != "Oui" and coupJoueur != "oui" and coupJoueur != "Non" and coupJoueur != "non":
                        # Alors on demande au joueur s'il veut quitter la partie
                        coupJoueur = input("Voulez vous quitter la partie ? : ")
                        # Alors si le joueur rentre "Oui" ou "oui"
                        if coupJoueur == "Oui" or coupJoueur == "oui":
                            # Alors afficher un message de fin de partie
                            print("Fin de la partie, vous avez quitté")
                            # La fonction ne retourne rien
                            return
                        # Si le joueur rentre "Non" ou "non"
                        elif coupJoueur == "Non" or coupJoueur == "non":
                            # On affiche un message qui indique que la partie reprend
                            print("La partie reprend !")
                        # Sinon 
                        else:
                            # Alors on affiche un message d'erreur
                            print("Vous devez répondre par oui ou par non !")
                    # On demande au joueur de rejouer
                    coupJoueur = input("Votre coup : ")
                    # Le coup du joueur est non valable
                    coupValable = False
                # Sinon
                else:
                    # Alors on affiche un message d'erreur
                    print("Ce coup n'existe pas ! Vous devez jouer Pierre, Feuille ou Ciseaux.")
                    # On demande au joueur de rejouer
                    coupJoueur = input("Votre coup : ")
                    # On considère que son coup n'est pas valable
                    coupValable = False
            # On appel la fonction randint avec comme minimum 0 et comme maximum 2 qui renvoie un entier aléatoire entre son minimum et son maximum compris
            coupOrdiID = random.randint(0,2)
            # Si l'ID du coup de l'ordinateur est 0
            if coupOrdiID == 0:
                # On affiche que l'ordinateur a jouer Pierre
                print("L'ordinateur a joué Pierre")
                # Si l'ID du coup du joueur est 0
                if coupJoueurID == 0:
                    # Alors on affiche que personne ne gagne de points
                    print("Personne ne gagne de point.")
                # Si l'ID du coup du joueur est 1
                elif coupJoueurID == 1:
                    # Alors on affiche que le joueur gagne un point
                    print("Vous gagnez 1 point!")
                    # On ajoute 1 au compteur de points du joueur
                    pointsJoueur += 1
                # Si l'ID du coup du joueur est 2
                elif coupJoueurID == 2:
                    # Alors on affiche que l'ordinateur gagne un point
                    print("L'ordinateur gagne 1 point.")
                    # On ajoute 1 au compteur de point de l'ordinateur
                    pointsOrdinateur += 1
            # Si l'ID du coup de l'ordinateur est 1
            elif coupOrdiID == 1:
                # On affiche que l'ordianteur à jouer Feuille
                print("L'ordinateur a joué Feuille")
                # Si l'ID du coup du joueur est 0
                if coupJoueurID == 0:
                    # Alors on affiche que l'ordinateur gagne un point
                    print("L'ordinateur gagne 1 point.")
                    # On ajoute 1 au compteur de point de l'ordinateur
                    pointsOrdinateur += 1
                # Si l'ID du coup du joueur est 1
                elif coupJoueurID == 1:
                    # Alors on affiche que personne ne gagne de points
                    print("Personne ne gagne de point.")
                # Si l'ID du coup du joueur est 2
                elif coupJoueurID == 2:
                    # Alors on affiche que le joueur gagne un point
                    print("Vous gagnez 1 point !")
                    # On ajoute 1 au compteur de points du joueur
                    pointsJoueur += 1
            # Si l'ID du coup de l'ordinateur est 2
            elif coupOrdiID == 2:
                # On affiche que l'ordianteur à jouer Ciseaux
                print("L'ordinateur a joué Ciseaux")
                # Si l'ID du coup du joueur est 0
                if coupJoueurID == 0:
                    # Alors on affiche que le joueur gagne un point
                    print("Vous gagnez 1 point !")
                    # On ajoute 1 au compteur de points du joueur
                    pointsJoueur += 1
                # Si l'ID du coup du joueur est 1
                elif coupJoueurID == 1:
                    # Alors on affiche que l'ordinateur gagne un point
                    print("L'ordinateur gagne 1 point.")
                    # On ajoute 1 au compteur de point de l'ordinateur
                    pointsOrdinateur += 1
                # Si l'ID du coup du joueur est 2
                elif coupJoueurID == 2:
                    # Alors on affiche que personne ne gagne de points
                    print("Personne ne gagne de points.")
            # On affiche le score actuel du round dans lequel on se trouve
            print("Score : Ordinateur "+str(pointsOrdinateur)+" - "+str(pointsJoueur)+" Joueur")
            # Saut d'une ligne
            print()
            # On definie que le coup du joueur n'est plus valable et donc faux
            coupValable = False
        # Si le joueur a autant de point que necessaire pour gagner un round
        if pointsJoueur == totalPoints:
            # Alors on ajoute 1 au compteur de round gagné du joueur
            roundsJoueur += 1
            # On affiche un message de félicitations
            print("Bravo ! Vous remportez le Round "+str(roundNumber)+".")
        # Sinon
        else:
            # Alors on ajoute 1 au compteur de round gagné de l'ordinateur
            roundsOrdinateur += 1
            # On affiche un message de "dommage"
            print("Dommage ! Le Round "+str(roundNumber)+" est remporté par l'ordinateur.")
        # Saut d'une ligne
        print()
        # On réinitialise les points du joueur et de l'ordinateur à 0
        pointsJoueur = pointsOrdinateur = 0
        # On affiche le nombre de rounds gagné par le joueur et par l'ordinateur
        print("Score Total : Ordinateur "+str(roundsOrdinateur)+" - "+str(roundsJoueur)+" Joueur")
    # Saut d'une ligne
    print()
    # Si le joueur a gagné autant de rounds que necessaire pour gagner la partie
    if roundsJoueur == totalRounds:
        # Alors on affiche un message de félicitations
        print("Félicitations ! Vous remportez la Partie !")
        # On initialise le gagnant de la partie à "joueur"
        winner = "joueur"
    # Sinon
    else:
        # Alors on affiche un message de "dommage"
        print("Oh non ! L'ordinateur remporte la Partie...")
        # On initialise le gagnant de la partie à "ordianteur"
        winner = "ordinateur"
    # Saut d'une ligne
    print()
    # On affiche un message de fin de partie
    print("Fin de la partie, merci d'avoir joué !")
    # Saut d'une ligne
    print()
    # On retourne le gagnant
    return winner

pierreFeuilleCiseaux(3, 3)