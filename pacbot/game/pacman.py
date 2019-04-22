from pacbot.game.maze import Maze
from pacbot.game.player import Player


class PacMan(Player):

    def __init__(self, x, y, maze: Maze):
        super().__init__(x, y, (0, 255, 0), maze)
