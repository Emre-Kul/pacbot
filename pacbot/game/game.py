from pacbot.game.area import Area
from pacbot.game.pacman import PacMan
from pacbot.game.renderer import Renderer
import pygame

class Game:

    def __init__(self, scene):
        self.frame = 0
        self.scene = scene
        self._area = Area()
        self._area.create_legacy_area()
        self.renderer = Renderer(scene, self._area)
        self._pacman = PacMan(3, 4)
        self.score = 0

    def render(self):
        if self.frame == 0:
            self.scene.clear()
            self.renderer.render_area()
            self.renderer.render_pac_man(self._pacman)
            self._pacman.move(self._area)
            self.scene.update()
        pygame.time.wait(1)
        self.frame = (self.frame + 1) % 60

    def handle_input(self):
        if self.scene.key_pressed(pygame.K_UP):
            self._pacman.change_direction(1)
        if self.scene.key_pressed(pygame.K_RIGHT):
            self._pacman.change_direction(2)
        if self.scene.key_pressed(pygame.K_DOWN):
            self._pacman.change_direction(3)
        if self.scene.key_pressed(pygame.K_LEFT):
            self._pacman.change_direction(4)

    def control(self):
        pass