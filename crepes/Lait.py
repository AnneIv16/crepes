from Volume import *

class Lait:

    qte_lait = None

    def __init__(self, volume):
        self.qte_lait = Volume(volume)

    def ajouter(self, proportion):
        new_ml = self.qte_lait.into_ml() - self.qte_lait.into_ml()*proportion
        self.qte_lait.set(new_ml)
        print("Lalala on rajoute du lait !")