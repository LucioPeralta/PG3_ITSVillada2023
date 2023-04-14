strings = ["Hola", "profesores", "esto", "funciona", "de", 10]
with open("Guia-3/act5.txt", "w") as f:
    for string in strings:
        try:
            f.write(str(string) + "\n")
        except TypeError as e:
            print(f"Error: {e}. No se pudo escribir el elemento {string} en el archivo.")
