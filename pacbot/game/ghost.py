from pacbot.game.actor import Actor
from pacbot.game.maze import Maze


class Ghost(Actor):

    def __init__(self, x, y, color, target: Actor, maze: Maze):
        super().__init__(x, y, color, maze)
        self.target = target
        self.maze = maze
        self.frightened_duration = 0

    def set_frightened(self):
        self.frightened_duration = 10

    def is_frightened(self):
        return self.frightened_duration > 0
