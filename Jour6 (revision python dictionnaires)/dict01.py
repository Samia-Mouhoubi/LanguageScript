# creer un dictionnaire vide
d = {}
print(type(d))

#autre facon de creer un dictionnaire
d1 = dict()
print(type(d1))

#remplir le dictionnaire / creer des clees
d[100] = "jean"
d[200] = "fatma"
d[300] = "nabil"
d[400] = "ines"
d[500] = "mokhtar"

print(d)
print(f"cle 200 = {d[200]}")

d2={"Samia":"championne en python","Soumaya":"l'experte","Mohammed":"le gentleman",100:"Xin"}
print(d2)
print(d2["Samia"])

#verifier si une cle existe avant de l'afficher
if(700 in d):
    print(d[700])

#acceder a une cle qui n'existe pas (cause une erreur)
# print(d[700])






