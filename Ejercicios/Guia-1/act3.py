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

