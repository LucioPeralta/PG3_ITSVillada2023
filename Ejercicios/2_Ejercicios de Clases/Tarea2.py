print("Ejercicio 1")

class Persona:

    nombre = input("Cual es tu nombre? ")
    edad = int(input("Cual es tu edad? "))
    print("-------------------------------------")

    def iniciar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

persona1 = Persona()
persona1.iniciar(Persona.nombre, Persona.edad)
persona1.mostrar()
print("-------------------------------------")

print("Ejercicio 2")

class Alumno:
    nombre = input("Cual es tu nombre? ")
    nota = int(input("Cual es tu nota? "))
    print("-------------------------------------")

    def iniciar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def mostrar_estado(self):
        if self.nota >= 6:
            print(f"{self.nombre} esta aprobado")
        else:
            print(f"{self.nombre} esta reprobado")

alumno1 = Alumno()
alumno1.iniciar(alumno1.nombre, alumno1.nota)
alumno1.mostrar()
alumno1.mostrar_estado()
print("-------------------------------------")

print("Ejercicio 3")

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

print("Ejercicio 4")

class Operaciones:

    numero1 = int(input("Cual es el primer numero? "))
    numero2 = int(input("Cual es el segundo numero? "))
    print("-------------------------------------")
    
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma = self.numero1 + self.numero2
        print(f"El resultado de la operacion es: {suma}")

    def restar(self):
        resta = self.numero1 - self.numero2
        print(f"El resultado de la operacion es: {resta}")

    def multiplicar(self):
        multiplicar = self.numero1 * self.numero2
        print(f"El resultado de la operacion es: {multiplicar}")

    def dividir(self):

        if self.numero1 == 0 or self.numero2 == 0:
            print("No se puede dividir entre 0")
        else:
            dividir = self.numero1 / self.numero2
            print(f"El resultado de la operacion es: {dividir}")

operacion = Operaciones(Operaciones.numero1, Operaciones.numero2)

print("-------------------------------------")

print("Ejercicio 5")

class Persona:
    def __init__(self):
        self.nombre = input('Ingresa tu nombre: ')
        self.edad = input('Ingresa tu edad: ')

    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input('Ingresa su sueldo: '))
    
    def pagar_impuesto(self):
        if self.sueldo > 3000:
            print('Debe pagar impuestos')
        else:
            print('No debe pagar impuestos')


persona = Persona()
persona.mostrar()

empleado = Empleado()
empleado.mostrar()
empleado.pagar_impuesto()

print("-------------------------------------")
print("Ejercicio 6")

class Familia:
    def __init__(self, papa, mama, hijos):
        self.papa = papa
        self.mama = mama
        self.hijos = hijos

    def __str__(self):
        return f"Padre: {self.papa}\nMadre: {self.mama}\nHijos: {self.hijos}"
    

hijos = ['Lucio', 'Debora']

familia = Familia('Carlos', 'Gisela', hijos)
print(familia.__str__())
