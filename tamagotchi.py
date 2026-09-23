from random import randint


"""Ceci est une app de gestion d'un animal virtuel"""


class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.eat = 50           # 0 = rassasié ; 100 = affamé
        self.energy = 100       # 100 = en pleine forme ; 0 = épuisé
        self.joy = 100          # 100 = heureux ; 0 = déprimé
        self.life = True
        
    def describe(self):
        description = (f"Nom = {self.name} - "
                       f"Energie = {self.energy} "
                       f"Bonheur = {self.joy}")
        return description
        
        
    def to_feed(self):
        self.eat = max(0, self.eat - 30)
        self.energy = max (0, self.energy - 5)
        print(f"n\{self.name} mange une friandise")
        
        
    def play(self):
        if self.energie < 20:
            print(f"\n{self.nom} est trop fatigué pour jouer...")
        return
        self.joy = min(100, self.joy + 20)
        print(f"n\{self.name} est heureux(se) d'être à tes côtés")
        self.energy = max(0, self.energy -20)
        self.eat = min(100, self.eat +15)
        
    def sleep(self):
        self.energy = min(100, self.energy +40)
        self.eat = min(100, self.eat +15)
        print(f"{self.name} fait une grosse sieste ! ")
        