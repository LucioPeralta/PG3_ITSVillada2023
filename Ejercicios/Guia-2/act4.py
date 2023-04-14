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