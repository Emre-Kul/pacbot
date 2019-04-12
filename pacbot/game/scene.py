import pygame


class Scene:

    def __init__(self, width=500, height=500, caption="PAC BOT"):
        self._width = width
        self._height = height
        self._caption = caption
        self._scene = ""

    def create(self):
        pygame.init()
        pygame.display.set_caption(self._caption)
        self._scene = pygame.display.set_mode((self._width, self._height))
        pygame.display.flip()
