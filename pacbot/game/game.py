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
        self.start()

    def create_ghosts(self):
        return [
            # Clyde(self.player, self.maze), # clyde is random will be fixed
            # Inky(self.player, self.maze),
            Blinky(self.player, self.maze),
            Pinky(self.player, self.maze)
        ]

    def start(self):
        self.is_finished = False
        self.score = 0
        self.frame = 0
        self.maze.create_legacy_area()
        self.player = Player(13, 26, self.maze)
        self.ghosts = self.create_ghosts()

    def run(self):
        self.control_collision()
        if self.is_finished:
            return
        if self.frame % 3 == 0:
            self.player.move()
            self.refresh_maze()
        if self.frame % 5 == 0:
            for ghost in self.ghosts:
                ghost.move()
        self.frame += 1

    def render(self):
        self.scene.clear()
        self.renderer.render_maze()
        self.renderer.render_actor(self.player)
        for ghost in self.ghosts:
            self.renderer.render_actor(ghost)
        self.scene.update()

    def refresh_maze(self):
        pos = self.player.position
        if self.maze.mtr[pos[1]][pos[0]] > 1:
            self.maze.mtr[pos[1]][pos[0]] = 1
            self.maze.bait_count -= 1
            self.score += 10

        if self.maze.bait_count <= 0:
            self.is_finished = True

    def control_collision(self):
        for ghost in self.ghosts:
            if ghost.position[0] == self.player.position[0] and ghost.position[1] == self.player.position[1]:
                self.is_finished = True

    def move_player(self, key=-1):
        if key > -1:
            self.player.change_direction(key)
            return
        self._handle_keyboard()

    def is_player_moved(self):
        return self.player.direction == self.player.next_direction

    def _handle_keyboard(self):
        if self.scene.key_pressed(pygame.K_LEFT):
            self.player.change_direction(0)
        if self.scene.key_pressed(pygame.K_UP):
            self.player.change_direction(1)
        if self.scene.key_pressed(pygame.K_RIGHT):
            self.player.change_direction(2)
        if self.scene.key_pressed(pygame.K_DOWN):
            self.player.change_direction(3)
        if self.scene.key_pressed(pygame.K_TAB):
            self.start()
