#lire les donnees a partir d'un fichier json
import json
fichier= open("../data.json","r")
data_json=json.load(fichier)
print(data_json)
