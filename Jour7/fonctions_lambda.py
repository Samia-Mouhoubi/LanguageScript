# fonction lambda = fonction anonyme

# def fonction_normale(n):
#     return n*n


# print(fonction_normale(3))


resultat = lambda n:n*n
print(resultat(6))
print(resultat(7))


#syntaxe d'une fonction lambda ( anonyme ) : lambda arguments:expression a executer

test1 = lambda x,y:x*y
print(test1(4,5))

#exercice : calcul de deux nombres a et b
r = lambda a,b:a+b
print(r(3,5))

#exercice : retourner le nombre le plus grand entre 2 nombres
maximum = lambda x, y: x if x > y else y
print(maximum(11,8))


#exercice :  





