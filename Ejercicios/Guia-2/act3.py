class Triangulo:

    lado1 = int(input("Cual es el lado 1? "))
    lado2 = int(input("Cual es el lado 2? "))
    lado3 = int(input("Cual es el lado 3? "))
    print("-------------------------------------")

    def iniciar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def mostrar(self):
        print(f"Lado 1: {self.lado1}")
        print(f"Lado 2: {self.lado2}")
        print(f"Lado 3: {self.lado3}")

    def mostrar_estado(self):

        if self.lado1>self.lado2 or self.lado1>self.lado3:
            print("El lado mayor es: ", self.lado1)
        elif self.lado2>self.lado1 or self.lado2>self.lado3:
            print("El lado mayor es: ", self.lado2)
        elif self.lado3>self.lado1 or self.lado3>self.lado2:
            print("El lado mayor es: ", self.lado3)

        if self.lado1 == self.lado2 == self.lado3:
            print("Es un triangulo equilatero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("Es un triangulo isosceles")
        else:
            print("Es un triangulo escaleno")

triangulo = Triangulo()
triangulo.iniciar(triangulo.lado1, triangulo.lado2, triangulo.lado3)
triangulo.mostrar()
triangulo.mostrar_estado()
print("-------------------------------------")
