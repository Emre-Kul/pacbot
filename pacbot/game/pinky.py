from pacbot.game.actor import Actor
from pacbot.game.ghost import Ghost
from pacbot.game.maze import Maze


class Pinky(Ghost):

    def __init__(self, target: Actor, maze: Maze):
        super().__init__(13, 14, (255, 50, 255), target, maze)

    def chase(self):
        pass

    def scatter(self):
        pass

    def move(self):
        self.chase()
        super().move()
