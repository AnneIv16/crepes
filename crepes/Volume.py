class Volume:
    l = None
    cl = None
    ml = None

    def __init__(self, ml):
        self.set(ml)

    def into_ml(self):
        return self.l*1000 + self.cl*100 + self.ml

    def set(self, ml):
        self.l, self.ml = divmod(ml, 1000)
        self.cl, self.ml = divmod(ml, 10)