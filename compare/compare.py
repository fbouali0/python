import json

# Charger un fichier JSON
def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


file1 = input("Premier fichier JSON : ")
file2 = input("Deuxième fichier JSON : ")

json1 = load_json(file1)
json2 = load_json(file2)

compare_mode = input("Comparer par (key/value) : ").strip().lower()

if compare_mode == "key":

    keys1 = set(json1.keys())
    keys2 = set(json2.keys())

    only_in_file1 = keys1 - keys2
    only_in_file2 = keys2 - keys1

    print("\n=== Clés présentes uniquement dans", file1, "===")
    if only_in_file1:
        for k in sorted(only_in_file1):
            print(k)
    else:
        print("Aucune")

    print("\n=== Clés présentes uniquement dans", file2, "===")
    if only_in_file2:
        for k in sorted(only_in_file2):
            print(k)
    else:
        print("Aucune")

elif compare_mode == "value":

    all_keys = set(json1.keys()) | set(json2.keys())

    print("\n=== Différences clé / valeur ===")

    differences = False

    for key in sorted(all_keys):

        value1 = json1.get(key, "__MISSING__")
        value2 = json2.get(key, "__MISSING__")

        if value1 != value2:
            differences = True
            print(f"\nClé : {key}")
            print(f"  {file1} : {value1}")
            print(f"  {file2} : {value2}")

    if not differences:
        print("Aucune différence.")

else:
    print("Choix invalide. Tape 'key' ou 'value'.")