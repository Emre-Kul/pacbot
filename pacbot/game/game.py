from pacbot.game.area import Area
from pacbot.game.pacman import PacMan


class Game:

    def __init__(self):
        self._pac_man = PacMan
        self._area = Area()
        self.score = 0
