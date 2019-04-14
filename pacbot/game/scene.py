import pygame


class Scene:

    def __init__(self, width=560, height=720, caption="PAC BOT", bg_color=(0, 0, 0)):
        self.width = width
        self.height = height
        self._caption = caption
        self._scene = ""
        self._bg_color = bg_color
        self._background = ""
        self.pygame = pygame

    def create(self):
        self.pygame.init()
        self.pygame.display.set_caption(self._caption)
        self._scene = self.pygame.display.set_mode((self.width, self.height))
        self._background = pygame.Surface((self.width, self.height)).convert()
        self._background.fill(self._bg_color)
        self.pygame.display.flip()

    def is_active(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                return False
        return True

    def clear(self):
        self._scene.blit(self._background, (0, 0))

    def update(self):
        self.pygame.display.update()

    def render_rec(self, color, cords):
        self.pygame.draw.rect(self._scene, color, cords)
