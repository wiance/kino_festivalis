class Vartotojas:
    def __init__(self, nickname):
        self.nickname = nickname
        self.rezervacijos = [] 

    def __str__(self):
        return f"Vartotojas: {self.nickname}"