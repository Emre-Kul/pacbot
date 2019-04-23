from pacbot.game.actor import Actor
from pacbot.game.ghost import Ghost
from pacbot.game.maze import Maze


class Blinky(Ghost):

    def __init__(self, target: Actor, maze: Maze):
        super().__init__(13, 14, (255, 0, 0), target, maze)

    def chase(self):
        self.change_direction(2)
        pass

    def scatter(self):
        pass

    def move(self):
        self.chase()
        super().move()
