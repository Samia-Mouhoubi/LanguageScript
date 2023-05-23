import json
# un fichier json sous forme de chaine de caractere
data='''{
    "nom": "samia",
    "salaire": 120000,
    "langages": [
        "java",
        "python",
        "javascript"
    ],
    "addresse": {
        "numero_appart": 19,
        "ville": "montreal",
        "telephone": {
            "mobile": "444555666",
            "fixe": "555666777"
        }
    }
}'''
print(type(data))
data_dict = json.loads(data)
print(type(data))

# print(data_dict["salaire])

# print(data_dict["adresse"])
# print(data_dict["nom"])
print(data_dict["addresse"])
print(data_dict["addresse"]["telephone"]["fixe"])