from pacbot.game.chase_random import ChaseRandom
from pacbot.game.ghost import Ghost
from pacbot.game.maze import Maze
from pacbot.game.pacman import PacMan
from pacbot.game.renderer import Renderer
import pygame


class Game:

    def __init__(self, scene):
        self.frame = 0
        self.scene = scene
        self.maze = Maze()
        self.maze.create_legacy_area()
        self.renderer = Renderer(scene, self.maze)
        self.pac_man = PacMan(13, 26, self.maze)
        self.ghosts = self.create_ghosts()
        self.score = 0
        self.is_finished = False

    def create_ghosts(self):
        return [Ghost(15, 26, self.pac_man, self.maze, ChaseRandom())]

    def render(self):
        if self.frame == 0:
            self.scene.clear()
            self.renderer.render_maze()
            self.renderer.render_player(self.pac_man)
            for ghost in self.ghosts:
                self.renderer.render_player(ghost)
            if not self.is_finished:
                self.pac_man.move()
                self.refresh_area()
                for ghost in self.ghosts:
                    ghost.move()
            self.scene.update()
        pygame.time.wait(1)
        self.frame = (self.frame + 1) % 60

    def refresh_area(self):
        pos = self.pac_man.position
        if self.maze.mtr[pos[1]][pos[0]] > 1:
            self.maze.mtr[pos[1]][pos[0]] = 1
            self.maze.bait_count -= 1
            self.score += 10

        if self.maze.bait_count <= 0:
            self.is_finished = True

    def handle_input(self):
        if self.scene.key_pressed(pygame.K_UP):
            self.pac_man.change_direction(1)
        if self.scene.key_pressed(pygame.K_RIGHT):
            self.pac_man.change_direction(2)
        if self.scene.key_pressed(pygame.K_DOWN):
            self.pac_man.change_direction(3)
        if self.scene.key_pressed(pygame.K_LEFT):
            self.pac_man.change_direction(4)

    def control(self):
        pass
