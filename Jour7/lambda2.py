# les filtres :traitement en masse des structures de données itérables

# filter(fonction,structure de données à traiter)

liste = [5, 10, 15, 20, 25, 30]


def paire(n):
    if n % 2 == 0:
        return True
    else:
        return False


resultat = filter(paire, liste)
print(type(resultat))
liste_pair = list(resultat)
print(liste_pair)
# une liste -> on fait un traitement avec filter -> on stocke avec list

s = "samia"
print(list(s))


# exercice : refaire avec fonction lambda

pair = lambda n:True if n % 2 == 0 else False
resultat2 = filter(pair, liste)
liste_pair2 = list(resultat2)
print(liste_pair2)




