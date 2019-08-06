from abc import ABC, abstractmethod


# abstract class for all players. to extend from it use Player1(Player)
# don't forget to implement the abstract methods
class Player(ABC):
    def __init__(self, troops=0):
        self.troops = troops
        self.territories = []
