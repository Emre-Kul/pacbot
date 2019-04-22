from pacbot.game.chase_behavior import ChaseBehavior
from pacbot.game.maze import Maze
from pacbot.game.player import Player


class Ghost(Player):

    def __init__(self, x, y, target: Player, maze: Maze, chase_behavior: ChaseBehavior):
        super().__init__(x, y, (255, 0, 0), maze)
        self.chase_behavior = chase_behavior
        self.target = target
        self.maze = maze

    def move(self):
        self.chase_behavior.chase(self)
        super().move()
