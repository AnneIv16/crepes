from Masse import *

class Farine:

    qte_farine = None

    def __init__(self, masse):
        self.qte_farine = Masse(masse)

    def ajouter(self, proportion):
        new_g = self.qte_farine.into_g() - self.qte_farine.into_g()*proportion
        self.qte_farine.set(new_g)
        print("Lalala on rajoute de la farine !")
