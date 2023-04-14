def contar_vocales(frase):
    # convertir a minusculas para quq de igual si se escribe en mayuscula o minuscula
    frase = frase.lower()
    
    # defino las vocales
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    # inicio un contador de vocales
    contador = 0
    
    # se recorre cada caracter de la frase y contar las vocales
    for caracter in frase:
        if caracter in vocales:
            contador += 1
    
    return contador

frase = input("Escribe una frase: ")

cantidad_vocales = contar_vocales(frase)
print(f"La frase tiene {cantidad_vocales} vocales.")
