from Farine import *
from Lait import *
from Sucre import *
from Oeufs import *

class Crepes:

    oeufs = None
    farine = None
    sucre = None
    lait = None

    def __init__(self, nb_oeufs, qte_farine, qte_sucre, qte_lait):
        self.oeufs = Oeufs(nb_oeufs)
        self.farine = Farine(qte_farine)
        self.sucre = Sucre(qte_sucre)
        self.lait = Lait(qte_lait)

    def touiller(self):
        print("Et tu touilles et tu touilles !")
