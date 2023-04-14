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