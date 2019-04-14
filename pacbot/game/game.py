from pacbot.game.area import Area
# from pacbot.game.pacman import PacMan
from pacbot.game.renderer import Renderer


class Game:

    def __init__(self, scene):
        self.renderer = Renderer(scene)
        # self._pac_man = PacMan
        self._area = Area()
        self._area.create_legacy_area()
        self.score = 0

    def render(self):
        self.renderer.render_area(self._area)
        # self.renderer.render_area(Area())
