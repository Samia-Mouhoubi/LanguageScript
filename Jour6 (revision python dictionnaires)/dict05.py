d1 = dict({100: 'jean', 200: 'fatma', 300: 'nabil', 400: 'ines', 500: 'mokhtar', 600: 'faical'})
# aupprime une cle au hasard
# print(d1.popitem())
# print(d1)
t = d1.keys()
# print(type(t))
# print(d1.keys())

for i in t:
    print(i)

#acceder aux valeurs
valeurs = d1.values()
print(type(valeurs))
# print(d1.values())

for v in valeurs:
    print(v)

# utilisation de tuples
variablesTuple = d1.items()
print((type(variablesTuple)))
for k,l in variablesTuple:
    print(k, "   ",l)


"""
() = tuple
{} = dictionnaire
[] = liste
{} = set
"""

for i in d1:
    print(i)
    print(type(i))


