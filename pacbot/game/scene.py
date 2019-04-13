import pygame


class Scene:

    def __init__(self, width=500, height=500, caption="PAC BOT"):
        self._width = width
        self._height = height
        self._caption = caption
        self._scene = ""
        self._pygame = pygame

    def create(self):
        self._pygame.init()
        self._pygame.display.set_caption(self._caption)
        self._scene = self._pygame.display.set_mode((self._width, self._height))
        # self._pygame.draw.rect(self._scene, (255, 0, 0), (200, 150, 100, 50))
        self._pygame.display.flip()

    def is_active(self):
        for event in self._pygame.event.get():
            if event.type == self._pygame.QUIT:
                return False
        return True

    def update(self):
        self._pygame.display.update()