# Importer le module json
import json

# Préparer des données
data = [
    {"name": "Kevin", "age": 16},
    {"name": "Laurent", "age": 20}
]


# Convertir les données python au format json
data_json = json.dumps(data)
print(data_json)

# Convertir les données json en données python
data_python = json.loads(data_json)
print(data_python)


