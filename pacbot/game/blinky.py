from pacbot.game.actor import Actor
from pacbot.game.astar import AStar
from pacbot.game.ghost import Ghost
from pacbot.game.maze import Maze


class Blinky(Ghost):

    def __init__(self, target: Actor, maze: Maze):
        super().__init__(17, 14, (255, 0, 0), target, maze)

    def chase(self):
        a_star = AStar(self.maze, self.position, self.target.position)
        path = a_star.get_path()
        if len(path) > 0:
            d = self.get_direction_from_next_pos(path[0]['pos'])
            self.change_direction(d)

    def scatter(self):
        pass

    def move(self):
        self.chase()
        super().move()
