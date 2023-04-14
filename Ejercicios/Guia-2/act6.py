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