class Masse:
    kg = None
    g = None

    def __init__(self, g):
        self.set(g)
    
    def into_g(self):
        return self.kg*1000 + self.g

    def set(self, g):
        self.kg, self.g = divmod(g, 1000)