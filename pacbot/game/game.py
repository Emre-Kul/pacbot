from pacbot.game.blinky import Blinky
from pacbot.game.clyde import Clyde
from pacbot.game.inky import Inky
from pacbot.game.maze import Maze
from pacbot.game.pinky import Pinky
from pacbot.game.player import Player
from pacbot.game.renderer import Renderer
import pygame


class Game:

    def __init__(self, scene):
        self.frame = 0
        self.scene = scene
        self.maze = Maze()
        self.maze.create_legacy_area()
        self.renderer = Renderer(scene, self.maze)
        self.player = Player(13, 26, self.maze)
        self.ghosts = self.create_ghosts()
        self.score = 0
        self.is_finished = False

    def create_ghosts(self):
        # g = []
        # for i in range(20):
        #    g.append(Ghost(13, 14, self.pac_man, self.maze, ChaseRandom()))
        # return g
        return [
            Clyde(self.player, self.maze),
            Inky(self.player, self.maze),
            Blinky(self.player, self.maze),
            Pinky(self.player, self.maze)
        ]

    def render(self):
        if self.frame == 0:
            self.scene.clear()
            self.renderer.render_maze()
            self.renderer.render_actor(self.player)
            for ghost in self.ghosts:
                self.renderer.render_actor(ghost)
            if not self.is_finished:
                self.player.move()
                self.refresh_area()
                for ghost in self.ghosts:
                    ghost.move()
            self.scene.update()
        pygame.time.wait(1)
        self.frame = (self.frame + 1) % 60

    def refresh_area(self):
        pos = self.player.position
        if self.maze.mtr[pos[1]][pos[0]] > 1:
            self.maze.mtr[pos[1]][pos[0]] = 1
            self.maze.bait_count -= 1
            self.score += 10

        if self.maze.bait_count <= 0:
            self.is_finished = True

    def handle_input(self):
        if self.scene.key_pressed(pygame.K_LEFT):
            self.player.change_direction(0)
        if self.scene.key_pressed(pygame.K_UP):
            self.player.change_direction(1)
        if self.scene.key_pressed(pygame.K_RIGHT):
            self.player.change_direction(2)
        if self.scene.key_pressed(pygame.K_DOWN):
            self.player.change_direction(3)

    def control(self):
        pass
