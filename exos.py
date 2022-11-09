# DEBUT

# Déclaration des variables r, s, e, rh
r = 12000
s = 1250
e = 10
rh = 230

# ASSERTION UN

# On pose l'assertion finale Un
assertionFinaleUn = ((( 365 * 3 ) / ( 24 - ( 16 - 8 )))  * ( rh ) > r) == (e * s < r )

# On isole l'assertion de gauche et on vérifie si elle est vraie ou fausse
assertionUnUn = ((( 365 * 3 ) / ( 24 - ( 16 - 8 ))) * ( rh ) > r)  # True
# On affiche la valeure de vérité de l'assertion de gauche
print("The left assertion is "+str(assertionUnUn))

# On isole l'assertion de droite et on vérifie si elle est vraie ou fausse
assertionUnDeux =  e * s < r # False
# On affiche la valeure de vérité de l'assertion de droite
print("The right assertion is "+str(assertionUnDeux))

# On vérifie si l'assertion de droite et de gauche ont la même valeur
assertionFinaleUn = assertionUnUn == assertionUnDeux # False
# On affiche la valeure de vérité de l'assertion finale
print("The initial assertion is "+str(assertionFinaleUn))

# ASSERTION DEUX

# On pose l'assertion finale Deux
# assertionFinaleDeux = (( 365 * 3 ) / ( 4 - ( 12 - 8 ))  * (rh) > r) == (e * s < r)

# On isole l'assertion de gauche et on vérifie si elle est vraie ou fausse
# assertionDeuxUn = (( 365 * 3 ) / ( 4 - ( 12 - 8 ))  * (rh) > r) # False

# On isole l'assertion de droite et on vérifie si elle est vraie ou fausse
# assertionDeuxDeux = e * s < r # False

# On vérifie si l'assertion de droite et de gauche ont la même valeur
# assertionFinaleDeux = assertionDeuxUn == assertionDeuxDeux # True


# FONCTION

def retournerSixPlusTrois():
    # Calcul de 6 + 3
    return 6 + 3


def retournerSixPlusX(x, y):
    # Calcul de x + y
    return x + y


# EXERCICES


def add(x, y):
    # Addition de x par y
    return x + y


def sub(x, y):
    # Soustraction de x par y
    return x - y


def multiply(x, y):
    # Multiplication de x par y
    return x * y


def divide(x, y):
    # Si y = 0, impossible de diviser x par y
    if y == 0:
        # Alors afficher un message d'erreur 
        print("Vous ne pouvez pas diviser par 0 !")
        # Et on ne renvoie rien
        return
    #Si y != 0, on effectue la division de x par y
    else :
        # Alors on effectue la division de x par y
        return x / y


def modulo(x, y):
    # Reste de la division euclidienne de x par y
    return x % y


def salaireNet(salaireBrut, feesPercentage):
    # Calcul du pourcentage d'impôts
    fees = salaireBrut * (feesPercentage / 100)
    # Calcul du salaire net
    return salaireBrut - fees


def calculSalaireParSeconde(salaireHoraire, heureParJourOuvrable, jourOuvrable):
    # Calcul du salaire annuel
    salaireAnnuel = salaireHoraire * heureParJourOuvrable * jourOuvrable
    # Calcul du nombre de secondes par an
    nbSecondeParAn = 365 * 24 * 60 * 60
    # Calcul du salaire par seconde
    return salaireAnnuel / nbSecondeParAn


# Calcul de l'addition pour x = 10 et y = 5
addition = add(10, 5)

# Calcul de la soustraction pour x = 10 et y = 5
soustraction = sub(10, 5)

# Calcul de multiplication pour x = 10 et y = 5
multiplication = multiply(10, 5)

# Calcul de la division pour x = 10 et y = 5
division = divide(10, 5)

# Calcul du reste de la division euclidienne pour x = 10 et y = 5
reste = modulo(11, 5)

# Calcul du slaire net publique pour x = 10 et y = 5
salairePublique = salaireNet(2000, 15)

# Calcul du salaire net privé pour x = 10 et y = 5
salairePrive = salaireNet(2000, 23)

# Calcul du salaire par seconde pour x = 10 et y = 5
salaireParSeconde = calculSalaireParSeconde(20, 10, 225)


# Affichage du résultat de l'addition
print("10 + 5 = "+ str(addition))

# Affichage du résultat de la soustraction
print("10 - 5 = "+ str(soustraction))

# Affichage du résultat de la multiplication
print("10 * 5 = "+ str(multiplication))

# Affichage du résultat de la division
print("10 / 5 = "+ str(division))

# Affichage du résultat du reste de la division euclidienne
print("11 modulo 5 = "+ str(reste))

# Affichage du salaire net publique
print("Le salaire net dans le publique est : "+str(salairePublique))

# Affichage du salaire net privé
print("Le salaire net dans le privé est : "+str(salairePrive))

# Affichage du salaire par seconde
print("Le salaire par seconde est de : "+str(salaireParSeconde))


# Exemple de if, else, else if

# On veut savoir combien de personnes peuvent rentrer en même temps dans un magasin pendant la pandémie de Covid-19

# Le nombre de personne est indiqué ici
nbPersonne = 1

# Si la personne est seule
if nbPersonne == 1 :
    #Elle peut rentrer
    print("Tu rentres")
# Si les personnes sont deux
elif nbPersonne == 2:
    #Elles peuvent rentrer mais il vaut mieux se séparer si possible
    print("Vous rentrez mais séparez vous si possible")
# Si les personnes sont 3 ou plus 
else:
    #Elles ne peuvent pas rentrer
    print("Vous ne rentrez pas")


# Exemple de boucles

# On veut jouer des tours jusqu'à arriver au tour 5

#Définition de la fonction Jouer Un Tour
def jouerUnTour() :
    print("Vous êtes au "+str(tour)+" tour.")

# Le numéro du tour initial est 0
tour = 1

# Tant que je ne suis pas au tour 5
while tour <= 5 :
    # Appeler la fonction Jouer Un Tour
    jouerUnTour()
    # Ajouter un tour au compteur des tours / Passer au tour suivant
    tour = tour + 1


# Exercice:
    # Faire un mini jeu qui affiche un message lorsque input renvoie le bon caratère
    # Le caractère doit être paramétrable


# Importation les librairies string et random
import string
import random
from unittest import result

# Assignation d'un caractère aléatoire à une variable caractère mystère
caractereMystere = random.choice(string.ascii_letters)

# Affichage d'un message d'instruction
print("Devinez le caractère mystère : ")
# Essai de deviner le caractère mystère par le joueur
caractereGuess = input()

# Tant que l'utilisateur n'a pas trouver le caractère mystère
#while caractereMystere != caractereGuess :
    # Affichage d'un message d'échec
    #print("Non ! Le caractere mystere n'est pas : " + caractereGuess)
    # Affichage du message de nouvelle tentative
    #print("Nouvelle tentative :")
    # Nouvelle tentative du joueur
    #caractereGuess = input()

# Affichage du message de réussite
print("Oui ! Le caracter mystère est : " + caractereGuess)


# Concaténation 

# Informations de la personne concernée
prenom = "Rayouyou"
nom = "Chad"
age = 23

# Affichage de son prénom et de son nom sans un espace
print(prenom+nom)
# Affichage de son prénom et de son nom avec un espace
print(prenom+""+nom)
# Affichage du prénom, du nom et de l'âge avec des espaces
print(prenom+""+nom+""+str(age))

# Exercice Tableau / Listes

# On créé une liste 
tablo = [0,10,15,5,14,7,6,3,4,8,4,9,5,1,7,5,2,1,8,4,4,6,8]

# Pour récupérer 15 je prebds dans le tableau l'index 3 - 1 parce que le premier index est 0
tablo[2] # Renvoie 15

len(tablo) # Renvoie le nombre d'éléments qu'il y a dans le tableau


# Tableau dans un tableau

# Tableau avec plusieur type de données
tableauMultiType = ["RayouyouChad", True, tablo, 4>2, None]
# Tableau Unidimensionnel
tableauDimUn = [0, 1, 2, 3]
# Tableau Unidimensionnel
tableauDimDeux = [0, 1, 21, 3]
# Tableau Bidimensionel
tableauMultiDim = [tableauDimUn, tableauDimDeux]
tableauMultiDim[1][2] # Renvoie 21

tableauCleVal = {"Cle" : "Valeur"}
tableauCleVal["Cle"] # Renvoie "Valeur"

# foreach key : valeur in tableauCLeVal
    # print(key) # Renvoie "Cle"
    # print(valeur) # Renvoie "Valeur"


# Exercice 1
# Faire une fonction qui concatene 2 chaînes de caractere, les séparants par une virgule

# Déclaration des chaînes de caractère

def concatenate(chaineUn, chaineDeux):
    # Concatenation et affichage
    print(chaineUn+", "+chaineDeux)


# Exercice 2
# Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere avec l'ensembles des occuration d'un chiffre 
# Example : Pour le tableau [0,1,1,1,0,1,1,0,1] -- fonction(tableau,0) doit renvoyer "0, 4, 7". N'hésitez pas a implémenter la première fonction.

# Création du tableau
tableau=[1,2,3,5,1,3,2,2,1,5,2,1,3,2,5,1,2,3,1,2,3,2,3,3,1]

def explore(tableau, valeurRecherche):
    #Création d'un string vide
    resultat = ""
    # Pour chaque élément du tableau
    for i in range(len(tableau)):
        # Si l'élément i du tableau est égal à x
        if tableau[i] == valeurRecherche:
            # Alors, le rajouter avec "' " à la chaine de caractère finale
            resultat = resultat + str(tableau[i]) + ", "
    # Suppression des deux dernières caractères qui sont ", " du string final
    resultat[:-2]
    # Affichage du résultat
    print(resultat)


# Exercice 3
# Faire une fonction afficher un message

def affichage(messageType):
    # Convertion du message en string
    message = str(messageType)
    # Affichage du message
    print(message)


# Exercice 4
# Tel que
listeUtilisateur = {
    "Rayouyou" : "motdepasse",
    "Michel" : "password",
    "Toto" : "12345",
    "JhonDoe" : "azerty"
}
# Ecrivez la fonction login(userName, password, listUser) permettant d'afficher un message de connexion si  le combo user/passeword est bon.


def login(userName, password, listUser):
    # Pour toutes les clés de listUser
    for c in listUser:
        # Si la clé correspond au UserName et que le password rentré en paramètre correspond au password de la clé
        if c == userName and listUser[c] == password :
            # Alors, afficher un message de connexion
            print("Vous êtes connécté(e) !")
            # Sortir de la fonction
            return
    # Si on ne sort pas de la fonction, afficher ce message d'erreur
    print("Nom d'utilisateur ou mot de passe incorrect !")


# FIN