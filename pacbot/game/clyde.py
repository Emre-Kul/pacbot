from pacbot.game.actor import Actor
from pacbot.game.astar import AStar
from pacbot.game.ghost import Ghost
from pacbot.game.maze import Maze


class Clyde(Ghost):

    def __init__(self, target: Actor, maze: Maze):
        super().__init__(17, 14, (255, 0, 0), target, maze)

    def chase(self):
        target_pos = self.get_next_pos_from_direction(self.target.position, self.target.direction, 4)
        a_star = AStar(self.maze, self.position, [target_pos[1], target_pos[1]])
        path = a_star.get_path()
        if len(path) > 0:
            d = self.get_direction_from_next_pos(path[0]['pos'])
            self.change_direction(d)

    def scatter(self):
        pass

    def move(self):
        self.chase()
        super().move()
