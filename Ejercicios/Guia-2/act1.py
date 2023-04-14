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