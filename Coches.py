
class coches:
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("tenemos ", gasolina, "litros")

    def arrancar(self):
        if self.gasolina>0:
            print("Arranca")
        else: 
            print("No arrancar")          
    def conducir (self):
        if self.gasolina>0:
            self.gasolina -=1
            print("Quedan", self.gasolina," Litros")
        else:
            print("No se mueve")
                
       