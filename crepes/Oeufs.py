class Oeufs:

    nb_oeufs = None

    def __init__(self, nb):
        self.nb_oeufs = nb

    def ajouter(self, proportion):
        self.nb_oeufs -= round(self.nb_oeufs*proportion)
        print("Lalala on rajoute des oeufs !")
    
    def battre(self):
        print("Bonk bonk, on bat les oeufs !")