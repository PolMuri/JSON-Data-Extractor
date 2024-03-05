# La llibreria és per Obtenir la llista de fitxers d'un directori: Utilitzes la funció os.listdir(directori) 
# per obtenir una llista de tots els fitxers que es troben en el directori especificat.
import os
import json

# Directori que conté els fitxers JSON, la r és indica que es tracta d"una cadena de caràcters "raw" o "bruta". 
# És per evitar l"interpretació especial de caràcters d'escape (com \n o \t) i per tractar la cadena de caràcters tal com és, sense canviar-ne el contingut.

# HAS DE POSAR EL DIRECTORI (no fitxer!) ON TENS ELS JSON! 
directori = r"C:\Users\Directori\OnTens\JSONs"

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

        for result in results:
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




