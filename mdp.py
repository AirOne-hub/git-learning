import random

majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minuscules = "abcdefghijklmnopqrstuvwxyz"
chiffres = "0123456789"
speciaux = "!@#$%^&*()-_=+<>?/"

taille =16

tous = majuscules + minuscules + chiffres + speciaux
mot_de_passe = "".join(random.choice(tous) for _ in range(taille))

print(mot_de_passe)