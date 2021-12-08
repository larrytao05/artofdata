class Pokemon:
    def __init__(self, name, height, type1, type2, id, weight) -> None:
        self.name = name
        self.height = height
        self.type1 = type1
        self.type2 = type2
        self.id = id
        self.weight = weight
    
    def __str__(self) -> str:
        return self.id + ", " + self.name + ", " + str(self.height) + ", " + str(self.weight) + ", " + self.type1 + ", " + self.type2