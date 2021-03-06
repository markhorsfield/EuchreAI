from Player import Player

class Table:
    #Implements a circular list data structure to serve as table
    #You can visualize a four sided table with a player on each side
    #This will allow for smooth gameplay rotations for betting and playing tricks where winner leads next trick
    def __init__(self,):
        self.players = [Player(team) for team in range(4)]
        self.material = 'wood'

    #Return players
    def get_players(self):
        return self.players

    def set_players(self,players):
        self.players = players

    #Rotates players once around the table
    def rotate_once(self):
        last = self.players.pop(-1)
        self.players.insert(0, last)

    #This will rotate the table the correct number of times so that the player passed is the first in the list
    def set_first(self,player):
        num_rotations = self.players.index(player)
        for _ in range(num_rotations):
            self.rotate_once()