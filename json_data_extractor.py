import os
import json
# Importa la funció tqdm de la llibreria tqdm per generar la barra de progrés
from tqdm import tqdm 

directori = r"C:\Users\Directori\OnTens - els\JSON"
# Agafem els fitxers JSON dins el directori, excepte si es diu "fitxer_sortida.json" que és on guardarem les dades 
# un cop les haguem tractat i processat
fitxers_json = [fitxer for fitxer in os.listdir(directori) if fitxer.endswith(".json") and fitxer != "fitxer_sortida.json"]
print("S'agafarà l'ID, nom, telèfon i correu dels locals dels seguents fitxers: ", fitxers_json)

dades_totals = []

for fitxer_json in fitxers_json:
    # Construeix la ruta completa al fitxer JSON
    ruta_fitxer = os.path.join(directori, fitxer_json)

    # Provem i capturem error
    try: 
        # Obre el fitxer JSON en mode de lectura i en codificació utf-8 ja que si no
        # especificava la codificació em donava problemes de lectura del fitxer JSON original
        with open(ruta_fitxer, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Accedeix a una clau [] concreta (en aquest cas "results") per poder agafar les dades anidades {} de dins de la clau
        results = data.get("results", [])
        # Substituim on aniria results per tqdm i després dins el parèntesi posem "results" i el missatge que mostrem per pantalla
        for result in tqdm(results, desc="Generant fitxer JSON"):
            dades_extretes = {
                "uidentifier": result.get("uidentifier"),
                "name": result.get("name"),
                "telephone": result.get("telephone"),
                "email": result.get("email")
            }
            # Posa les dades_extretes a la llista dades_totals
            dades_totals.append(dades_extretes)

    except json.JSONDecodeError as e:
        print(f"Error de sintaxi JSON al llegir {fitxer_json}: {e} , pots comprovar la sintaxi a https://jsonlint.com/ ")
    except Exception as e:
        print(f"Error al llegir {fitxer_json}: {e}")

#Escriu les dades_totals en un fitxer JSON de sortida, si no es pot crear el fitxer JSON mostra missatge
with open("fitxer_sortida.json", "w") as f:
    json.dump(dades_totals, f, indent=4)
print("Nou fitxer creat al mateix directori amb nom: fitxer_sortida.json")
