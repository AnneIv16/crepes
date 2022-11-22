from Crepes import *

def main():

    oeufs=5
    farine=500
    sucre=250
    lait=1500

    crepes = Crepes(oeufs, farine, sucre, lait)
    crepes.sucre.ajouter(1)
    crepes.oeufs.ajouter(1)
    crepes.oeufs.battre()
    crepes.farine.ajouter(1)
    crepes.touiller()
    for i in range(4):
        crepes.lait.ajouter(0.25)
        crepes.touiller()

    print("\nBonnes crêpes d'anniversaire Mathilde !!!")

if __name__=="__main__":
    main()