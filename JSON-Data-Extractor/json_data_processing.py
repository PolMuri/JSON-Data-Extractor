# La llibreria és per Obtenir la llista de fitxers d'un directori: Utilitzes la funció os.listdir(directori) 
# per obtenir una llista de tots els fitxers que es troben en el directori especificat.
import os
import json

# Directori que conté els fitxers JSON, la r és indica que es tracta d"una cadena de caràcters "raw" o "bruta". 
# És per evitar l"interpretació especial de caràcters d'escape (com \n o \t) i per tractar la cadena de caràcters tal com és, sense canviar-ne el contingut.

# HAS DE POSAR EL DIRECTORI ON TENS ELS JSON! 
print("SI EL JSON DE SORTIDA (fitxer_sortida.json) JA ESTA CREAT DONARA ERROR PER PANTALLA I NO ES MODIFICARA EL JA CREAT")
print("SI VOLEM GENERAR UN NOU fitxer_sortida.json CAL BORRAR EL VELL")
directori = r"C:\Users\Directori\OnTens\JSONs"

# Obté una llista de tots els fitxers en el directori
# Crea una llista que contingui noms de fitxers que acabin en ".json"
# Es crea una variable temporal "fitxer" que agafa el valor de cada element de la llista retornada per os.listdir(directori).
fitxers_json = [fitxer for fitxer in os.listdir(directori) if fitxer.endswith(".json") and fitxer != "fitxer_sortida.json"]

print("S'agafara el nom de local i l'ocupacio dels seguents fitxers: ", fitxers_json)

# Inicialitza una llista buida per emmagatzemar les dades de tots els fitxers
dades_totals = []

for fitxer_json in fitxers_json:
    # Construeix la ruta completa al fitxer JSON
    ruta_fitxer = os.path.join(directori, fitxer_json)

    try:
        # Obre el fitxer JSON en mode de lectura
        with open(ruta_fitxer, "r") as f:
            dades = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error de sintaxi JSON al llegir {fitxer_json}: {e} , pots comprovar la sintaxi a https://jsonlint.com/ ")
    except Exception as e:
        print(f"Error al llegir {fitxer_json}: {e}")
    
    # Extreu els camps que ens interessen de les dades i els afegeix a la llista dades_totals
    dades_extretes = {
        "name": dades.get("name"),
        "occupationMeals": dades.get("occupationMeals"),
        "occupationWeek": dades.get("occupationWeek")
    }
    # Posa les dades_extretes a la llista dades_totals
    dades_totals.append(dades_extretes)

#Escriu les dades_totals en un fitxer JSON de sortida, si no es pot crear el fitxer JSON mostra missatge
with open("fitxer_sortida.json", "w") as f:
    json.dump(dades_totals, f, indent=4)
print("Nou fitxer creat al mateix directori amb nom: fitxer_sortida.json")



