# ecrire un programme pour saisir le nom de l'etudiant
# et saisir la note (en %) de l'etudiant sous forme de dictionnaire
# ensuite afficher le contenu dans la console sous forme de table

d = {}

def saisir():
    n = int(input("Veuillez saisir le nombre d'etudiants : "))
    for i in range(1,n+1) :
        if (i == 1) :
            etudiant = str(input(f"Veuillez saisir le nom du {i} er etudiant : "))
        else :
            etudiant = str(input(f"Veuillez saisir le nom du {i} eme etudiant : "))
        note = int(input(f"Veuillez saisir la note de {etudiant} : "))
        pourcent = f"{note}%"
        d[etudiant] = pourcent

def afficher():
    for i in d:
        print (f"la note de {i} : {d[i]}")

saisir()
afficher()





