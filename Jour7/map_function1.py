# map(la fonction a eexecuter, la structure de données itérable(range,dictionnaire,liste,chaine de caracteres))
liste = [1, 2, 3, 4, 5, 6]

def double_element(n):
    return 2*n
# print(double_element(2))

liste2 = list(map(double_element,liste))
print(liste2)

liste3 = list(map(lambda x:x*x,liste))
print(liste3)



