# creer un dictionnaire vide
d = dict()
d1 = dict({100: 'jean', 200: 'fatma', 300: 'nabil', 400: 'ines', 500: 'mokhtar'})

d2 = dict([(100, 'jean'),(200, 'fatma'),(300, 'nabil')])
"""
Dans cette expression, la liste [ (100, 'jean'), (200, 'fatma'), (300, 'nabil') ] contient trois tuples,
 où chaque tuple représente une paire clé-valeur du dictionnaire. Chaque tuple contient un entier en tant
  que clé et une chaîne de caractères en tant que valeur.
"""

print(d)
print(d1)
print(d2)

print(f"La taille du dictionnaire d2 est : {len(d2)}")
# 2 facon de recuperrer la valeur d'une cle du dictionnaire
print(d2.get(100))
print(d2[100])

# supprimer une cle ou afficher un message si on la trouve pas
print(d2.get(1000, "Valeur non trouvee"))

# pop supprime une cle et retourne la valeur de la cle supprimmee
print(d2.pop(100))
print(d2)


