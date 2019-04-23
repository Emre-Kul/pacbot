from pacbot.game.actor import Actor
from pacbot.game.ghost import Ghost
from pacbot.game.maze import Maze
from random import *


class Clyde(Ghost):

    def __init__(self, target: Actor, maze: Maze):
        super().__init__(13, 14, (255, 90, 50), target, maze)

    def chase(self):
        directions = []
        for direction in self.possible_directions():
            if direction == self.direction or (
                    direction - self.direction == 2 or direction - self.direction == -2) and self.moving:
                continue
            directions.append(direction)

        rand = randint(0, len(directions) - 1)
        self.change_direction(directions[rand])

    def scatter(self):
        pass

    def move(self):
        self.chase()
        super().move()
