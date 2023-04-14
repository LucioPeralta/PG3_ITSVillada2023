def es_palindromo(palabra):
    palabra = palabra.lower()  # esto converte la palabra a minúsculas
    palabra_inversa = palabra[::-1]  # esto obtiene la inversa de la palabra
    
    if palabra == palabra_inversa:
        return True
    else:
        return False


palabra = input("Escribe una palabra: ")

if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")
