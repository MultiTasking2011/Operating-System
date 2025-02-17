import time
import random

class game():
    def __init__(self):
        self.pokemonhealth = 100
        self.foepokemon = None
        self.yourpokemon = None
        self.pokemonchoice = """1. Charizard
                                2. Blastoise
                                3. Venusaur """
        
        self.charizardmoveset = """1. Fly [Flying Type] [90% Power] [95% Accuracy]
                                   2. Thunder Punch [Electric Type] [100% Accuracy]
                                   3. Inferno [Fire type] [100% Power] [50% Accuracy]
                                   4. Fire Punch [Fire type] [75% Power] [90% Accuracy]"""
        
        self.venusaurmoveset = """1. Frenzy Plant [Grass Type] [150% Power] [90% Accuracy]
                                2. Sludge Bomb [Poison Type] [90% Power] [100% Accuracy]
                                3. Earth Power [Ground Type] [90% Power] [100% Accuracy]
                                4. Leaf Storm [Grass Type] [130% Power] [90% Accuracy]"""
        
        self.blastoisemoveset = """1. Hydro Cannon [Water Type] [150% Power] [90% Accuracy]
                           2. Ice Beam [Ice Type] [90% Power] [100% Accuracy]
                           3. Flash Cannon [Steel Type] [80% Power] [100% Accuracy]
                           4. Dark Pulse [Dark Type] [80% Power] [100% Accuracy]"""
 

