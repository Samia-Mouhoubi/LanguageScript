d = {100: 'jean', 200: 'fatma', 300: 'nabil', 400: 'ines', 500: 'mokhtar'}

print(d)

# entrer un cle deja existente = ecraseer l'ancienne valeur
d[100] = "john"
d[200] = "faical"
d[300] = "bob"

print(d)

#supprimer une cle existente
del d[300]

# verifier si une cle existe avant de la supprimer
if 800 in d:
    del d[800]

print(d)

#supprimer toutes les entrees d'un dictionnaire
d.clear()

print(d)

#supprimer definitivement le dictionnaire
del d

#cette ligne cause une erreur car d n'existe plus
# print(d)

