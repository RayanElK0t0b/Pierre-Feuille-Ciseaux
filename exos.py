#DEBUT

#DECLARATION DES VARIABLES

r = 12000
s = 1250
e = 10
rh = 230

#ASSERTION UN

assertionFinaleUn = ((( 365 * 3 ) / ( 24 - ( 16 - 8 )))  * ( rh ) > r) == (e * s < r )

assertionUnUn = ((( 365 * 3 ) / ( 24 - ( 16 - 8 ))) * ( rh ) > r)  # True

assertionUnDeux =  e * s < r # False

assertionFinaleUn = assertionUnUn == assertionUnDeux # False

#ASSERTION DEUX

#assertionFinaleDeux = (( 365 * 3 ) / ( 4 - ( 12 - 8 ))  * (rh) > r) == (e * s < r)

#assertionDeuxUn = (( 365 * 3 ) / ( 4 - ( 12 - 8 ))  * (rh) > r) # False

#assertionDeuxDeux = e * s < r # False

#assertionFinaleDeux = assertionDeuxUn == assertionDeuxDeux # True

#FONCTION

def retournerSixPlusTrois():
    return 6 + 3
def retournerSixPlusX(x, y):
    return x + y

retournerSixPlusTrois()
retournerSixPlusX(9, 4)

#EXERCICES

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

def salaireNet(brut, coefficient):
    return brut - brut * coefficient

def salaireParSecondeParAn(salaireHoraire, heureParJourOuvre, nombreDeJourOuvreParAn):
    return (nombreDeJourOuvreParAn * heureParJourOuvre * salaireHoraire) / 31540000

a = add(10, 5)
b = sub(10, 5)
c = multiply(10, 5)
d = divide(10, 5)
e = modulo(11, 5)
salairePublique = salaireNet(2000, 15/100)
salairePrivé = salaireNet(2000, 23/100)
salaireParSeconde = salaireParSecondeParAn(20, 10, 225)

print("10 + 5 = "+ str(a))
print("10 - 5 = "+ str(b))
print("10 * 5 = "+ str(c))
print("10 / 5 = "+ str(d))
print("11 modulo 5 = "+ str(e))
print("Le salaire net dans le publique est : "+str(salairePublique))
print("Le salaire net dans le privé est : "+str(salairePrivé))
print("Le salaire par seconde est de : "+str(salaireParSeconde))


#FIN