from pacbot.game.actor import Actor
from pacbot.game.maze import Maze


class Renderer:
    def __init__(self, scene, maze: Maze):
        self.maze = maze
        self.scene = scene
        self.x_diff = self.scene.width/self.maze.width
        self.y_diff = self.scene.height/self.maze.height
        pass

    def render_maze(self):
        mtr = self.maze.mtr
        for i in range(len(mtr)):
            for j in range(len(mtr[i])):
                if mtr[i][j] == 0:
                    self.scene.render_rec((0, 0, 255), (j * self.x_diff, i * self.y_diff, self.x_diff, self.y_diff))
                if mtr[i][j] == 2:
                    self.scene.render_rec((255, 255, 255), (j * self.x_diff + 10, i * self.y_diff + 10, self.x_diff / 10, self.y_diff / 10))
                if mtr[i][j] == 3:
                    self.scene.render_rec((255, 255, 255), (j * self.x_diff + 5, i * self.y_diff + 5, self.x_diff / 2, self.y_diff / 2))

    def render_actor(self, actor: Actor):
        pos = actor.position
        self.scene.render_rec(actor.color, (pos[0] * self.x_diff, pos[1] * self.y_diff, self.x_diff, self.y_diff))
