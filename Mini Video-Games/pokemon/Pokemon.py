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
        
        self.venusarmoveset = """1. """
