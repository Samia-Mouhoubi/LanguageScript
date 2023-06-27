# une forme compacte pour creer une liste a partir d'un objet iterable
# syntaxe : ma_liste = [expression for element in liste_origine if condition]

l=[1,2,3,4,5,6]
s = [x*x for x in l]

print(l)
print(s)

d = [x*x for x in range(1,11)]
k = [x for x in d if x%2 == 0]
print(d)
print(k)




