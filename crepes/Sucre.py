from Masse import *

class Sucre:

    qte_sucre = None

    def __init__(self, masse):
        self.qte_sucre = Masse(masse)

    def ajouter(self, proportion):
        new_g = self.qte_sucre.into_g() - self.qte_sucre.into_g()*proportion
        self.qte_sucre.set(new_g)
        print("Lalala on rajoute du sucre !")