from random import randint

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.eat = 50           # 0 = rassasié ; 100 = affamé
        self.energy = 100       # 100 = en pleine forme ; 0 = épuisé
        self.joy = 100          # 100 = heureux ; 0 = déprimé
        self.life = True
        
    def describe(self):
        return f"Nom : {self.name} | Énergie : {self.energy} | Joie : {self.joy} | Faim : {self.eat}"
        
    def to_feed(self):
        self.eat = max(0, self.eat - 30)
        self.energy = max(0, self.energy - 5)
        return f"{self.name} mange une friandise !"
        
    def play(self):
        if self.energy < 20:
            return f"{self.name} est trop fatigué pour jouer..."
        
        self.joy = min(100, self.joy + 20)
        self.energy = max(0, self.energy - 20)
        self.eat = min(100, self.eat + 15)
        return f"{self.name} s'est bien amusé avec toi !"
        
    def sleep(self):
        self.energy = min(100, self.energy + 40)
        self.eat = min(100, self.eat + 15)
        return f"{self.name} fait une grosse sieste !"
