print("Ejercicio 1")

lista = [2, 4, 6, 8, 10]
numero = int(input("Escriba un numero: "))

if numero in lista:
    indice = lista.index(numero)
    print(f"El número {numero} está en la posición {indice} de la lista.")
else:
    print(f"El número {numero} no está en la lista.")

print("Ejercicio 2")

print("Calculadora de años biciestos")

año = int(input("Escriba un año para saber si es biciesto o no?"))

resultado = año % 4 == 0 and año % 100 != 0 or año % 400 == 0

if resultado == 1:
    print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es un año bisiesto")

print("Ejercicio 3")

ancho = int(input("Qual es el ancho de la figura deseada? "))
alto = int(input("Qual es el alto de la figura deseada? "))
caracter = input("Que caracter desea usar? ")

for i in range(alto):
    for j in range(ancho):
        print(caracter, end="")
    print()

#Triangulo

def imprimir_triangulo(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j), end=' ')
        print()

imprimir_triangulo(6)

print("Ejercicio 4")

lista = [64, 34, 25, 12, 22, 11, 90]

def ordenar(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

resultado = ordenar(lista)
print(resultado)

print("Ejercicio 5")

def es_palindromo(palabra):
    palabra = palabra.lower()  
    palabra_inversa = palabra[::-1]  
    
    if palabra == palabra_inversa:
        return True
    else:
        return False


palabra = input("Escribe una palabra: ")

if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")

print("Ejercicio 6")

def contar_vocales(frase):
    
    frase = frase.lower()
    
    
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    
    contador = 0
    
    
    for caracter in frase:
        if caracter in vocales:
            contador += 1
    
    return contador

frase = input("Escribe una frase: ")

cantidad_vocales = contar_vocales(frase)
print(f"La frase tiene {cantidad_vocales} vocales.")

print("Ejercicio 7")

def es_numero_step(numero):
    numero_str = str(numero)  
    longitud = len(numero_str)
    
    if longitud < 2:  
        return False
    
    es_ascendente = True
    es_descendente = True
    
    for i in range(1, longitud):
        if int(numero_str[i]) != int(numero_str[i-1]) + 1:
            es_ascendente = False
        
        if int(numero_str[i]) != int(numero_str[i-1]) - 1:
            es_descendente = False
        
        if not es_ascendente and not es_descendente:  
            return False
    
    return True

numero = input("Escribe un número: ")

if es_numero_step(numero):
    print(f"{numero} es un número Step.")
else:
    print(f"{numero} no es un número Step.")