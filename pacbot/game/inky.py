from pacbot.game.actor import Actor
from pacbot.game.astar import AStar
from pacbot.game.ghost import Ghost
from pacbot.game.maze import Maze


class Inky(Ghost):

    def __init__(self, target: Actor, maze: Maze):
        super().__init__(13, 14, (50, 255, 255), target, maze)

    def chase(self):
        target = [self.target.position[1], self.target.position[0]]
        a_star = AStar(self.maze, self.position, target)
        path = a_star.get_path()
        if len(path) > 0:
            d = self.get_direction_from_next_pos(path[0]['pos'])
            self.change_direction(d)

    def scatter(self):
        pass

    def move(self):
        self.chase()
        super().move()
