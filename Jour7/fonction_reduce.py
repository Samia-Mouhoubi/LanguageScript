# pour une sequece d'elements iterable, reduire cette liste a un seul element specifique
from functools import reduce

l=[10,20,30,40,50,60]

resultat = reduce(lambda x,y:x+y, l)

print(type(resultat))
print(resultat)

chaine = "samia"
liste_char = list (chaine)
print(liste_char)
resultat2 = reduce(lambda x,y:x+y, liste_char)
print(resultat2)



liste3 = ["alpha", "bravo", "charlie", "delta"]
#1ere facon
res = reduce(lambda x, y: x + y[0], liste3, "")
print(res)
#2eme facon
print(reduce(lambda x,y:x+y,map(lambda x:x[0],liste3)))