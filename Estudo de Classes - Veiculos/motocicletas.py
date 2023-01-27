#conceito de herança de uma classe
#herdar informações de outras classes
from veiculos import Veiculos
class motos(Veiculos):
    def empinar(self):
        print("Conduzindo apenas sobre a roda traseira")

    # Polimorfísmo:
    def freiar(self):
        return super().freiar() + "motocicleta"