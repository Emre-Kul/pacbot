from pacbot.game.chase_behavior import ChaseBehavior
from pacbot.game.player import Player
from random import *


class ChaseRandom(ChaseBehavior):

    def __init__(self):
        super().__init__()

    def chase(self, target: Player):
        directions = []
        for direction in target.possible_directions():
            if direction == target.direction or (direction - target.direction == 2 or direction - target.direction == -2) and target.moving:
                continue
            directions.append(direction)

        rand = randint(0, len(directions) - 1)
        target.change_direction(directions[rand])

