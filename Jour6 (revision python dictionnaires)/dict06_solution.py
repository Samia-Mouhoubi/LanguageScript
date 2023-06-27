phrase = input("entrer un texte")
phraseFinal = phrase.lower()
# print(phraseFinal)

setVoyelle = {"a", "e", "i", "o", "u", "y", "a"}
print(type(setVoyelle))
print(setVoyelle)

d = dict()
for x in phraseFinal:
    if x in setVoyelle:
        d[x] = d.get(x,0)+1 # si la valeur n'existe pas elle sera remplacée par 0

#print(d)

for k,v in d.items():
    print(k," est apparue ",v, " fois")

