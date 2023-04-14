lista = [2, 4, 6, 8, 10]
numero = int(input("Escriba un numero: "))

if numero in lista:
    indice = lista.index(numero)
    print(f"El número {numero} está en la posición {indice} de la lista.")
else:
    print(f"El número {numero} no está en la lista.")