classeEtudiantAuto = {}
nbEtudiants = int(input("Entrez le nombre d'etudiants : "))
i = 1

while i<= nbEtudiants:
    nom = input("Entrez le nom de l'etudiant : ")
    note = input("entrez la note de l'etudiant : ")
    classeEtudiantAuto[nom] = note
    i+=1
print(classeEtudiantAuto)

print("nom de l'etudiant ","\t","note de l'etudiant %")
for e in classeEtudiantAuto :
    print("\t",e, "\t\t\t\t", classeEtudiantAuto[e])
