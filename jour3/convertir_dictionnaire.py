import json
etudiant ={"nom":"samia","id":123,"specialite":"assurance qualite"}
print(type(etudiant))
etudiant_json = json.dumps(etudiant)
print(type(etudiant_json))