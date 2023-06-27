# énoncé: ecrire un programme pour trouver le nombre d'occurence de chaque voyelle dans une chaine de caracteres
# exemple : automatisation de tests de chaine de caractères
# affichage : la voyelle a est apparue 6 fois

def compter_voyelles(chaine):
    # Dictionnaire pour stocker le compte de chaque voyelle
    dictionnaire_voyelles = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Mettre la chaîne en minuscule pour la rendre insensible à la casse
    chaine = chaine.lower()

    # Parcourir chaque caractère dans la chaîne
    for char in chaine:
        # Si le caractère est une voyelle, incrémenter son compteur
        if char in dictionnaire_voyelles:
            dictionnaire_voyelles[char] += 1

    # Renvoyer le dictionnaire contenant le compte de chaque voyelle
    return dictionnaire_voyelles


# Tester la fonction avec un exemple
chaine = "automatisation de tests de chaine de caractères"
voyelles_compte = compter_voyelles(chaine)

for voyelle, compte in voyelles_compte.items():
    print(f"La voyelle {voyelle} est apparue {compte} fois")




