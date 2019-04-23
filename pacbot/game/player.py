from pacbot.game.actor import Actor
from pacbot.game.maze import Maze


class Player(Actor):

    def __init__(self, x, y, maze: Maze):
        super().__init__(x, y, (255, 255, 50), maze)
