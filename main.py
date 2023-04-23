"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True, deleteDuplicates=False):

    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    
    listaOrdenda = sorted(items, reverse=(not ascending))

    if deleteDuplicates:
        listaOrdenda = list(set(listaOrdenda))  # Elimina palabras duplicadas

    return listaOrdenda #sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        #print("Se debe indicar el fichero como primer argumento")
        print(translateMessage("Se debe indicar el fichero como primer argumento"))
        print(translateMessage("El segundo argumento indica si se quieren eliminar duplicados"))
        sys.exit(1)
    wordFile = translateMessage("Se leerán las palabras del fichero")
    print(f"{wordFile} {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        file    = translateMessage("El fichero")
        file1   = translateMessage("no existe" )
        print(f"{file} {filename} {file1}")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))

def translateMessage(message):
    #Diccionario de traducciones
    translations = {
        "Se debe indicar el fichero como primer argumento":"The file must be specified as the first argument",
        "El segundo argumento indica si se quieren eliminar duplicados":"The second argument indicates whether you want to remove duplicates",
        "Se leerán las palabras del fichero":"The words of the file will be read",
        "El fichero":"The file",
        "no existe":"does not exist"
    }

    # Verificar si el mensaje está en el diccionario de traduccion
    if message in translations:
        return translations[message]
    else:
        #Si el mensaje no está en el diccionario
        return message
