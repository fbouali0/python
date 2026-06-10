# Exemple de string contenant plusieurs lignes
import json

data = """

"""
# Transformer le string en liste
result = [line.strip() for line in data.strip().splitlines()]

# Afficher la liste
print(len(result))

# Valeurs fixes
siteid = "100000093"
latitude = 36.8196103
longitude = 10.1877546


# Génération de la nouvelle liste
creationPayload = [
    {
        "assetnum": asset,
        "siteid": siteid,
        "invuselinenum": 1,
        "itemnum": "0171706",
        "n_gps_latitude": latitude,
        "n_gps_longitude": longitude
    }
    for asset in result
]

# Génération de l'objet final
validationPayload = {
    "action": "PLANTMETER",
    "assets": [
        {
            "assetnum": asset,
            "siteid": "100000093",
            "sap_plant": "5715",
            "sap_sloc": "5030",
            "profile": "RDC"
        }
        for asset in result
    ]
}

# validation
# with open("validation.json", "w", encoding="utf-8") as file:
#     json.dump(validationPayload, file, indent=4, ensure_ascii=False)

# Sauvegarde dans un fichier JSON
# with open("creation.json", "w", encoding="utf-8") as file:
#     json.dump(creationPayload, file, indent=4, ensure_ascii=False)

import os

batch_size = 100

# Créer le dossier json s'il n'existe pas
os.makedirs(".json", exist_ok=True)

for i in range(0, len(creationPayload), batch_size):
    batch = creationPayload[i:i + batch_size]

    file_name = os.path.join(
        ".json",
        f"creation_{i // batch_size + 1}.json"
    )

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(batch, file, indent=4, ensure_ascii=False)

    print(f"Created {file_name} with {len(batch)} items")

print("Fichiers .json générés avec succès avec {} assets:".format(len(result)))