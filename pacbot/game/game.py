from pacbot.game.area import Area
from pacbot.game.pacman import PacMan
from pacbot.game.renderer import Renderer
import pygame

class Game:

    def __init__(self, scene):
        self.scene = scene
        self._area = Area()
        self._area.create_legacy_area()
        self.renderer = Renderer(scene, self._area)
        self._pacman = PacMan(3, 4)
        self.score = 0

    def render(self):
        self.renderer.render_area()
        self.renderer.render_pac_man(self._pacman)
        if self.scene.key_pressed(pygame.K_UP):
            self._pacman.move(self._area, 1)
        if self.scene.key_pressed(pygame.K_RIGHT):
            self._pacman.move(self._area, 2)
        if self.scene.key_pressed(pygame.K_DOWN):
            self._pacman.move(self._area, 3)
        if self.scene.key_pressed(pygame.K_LEFT):
            self._pacman.move(self._area, 4)
