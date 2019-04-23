from pacbot.game.actor import Actor
from pacbot.game.astar import AStar
from pacbot.game.ghost import Ghost
from pacbot.game.maze import Maze

# pacmanin 4 tile önü

class Pinky(Ghost):

    def __init__(self, target: Actor, maze: Maze):
        super().__init__(13, 14, (255, 50, 255), target, maze)

    def chase(self):
        target_pos = self.get_next_pos_from_direction(self.target.position, self.target.direction, 4)
        a_star = AStar(self.maze, self.position, target_pos)
        path = a_star.get_path()
        if len(path) > 0:
            d = self.get_direction_from_next_pos(path[0]['pos'])
            self.change_direction(d)
        pass

    def scatter(self):
        pass

    def move(self):
        self.chase()
        super().move()
