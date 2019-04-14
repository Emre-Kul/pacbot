from pacbot.game.scene import Scene
from pacbot.game.game import Game


class App:

    def __init__(self):
        self._scene = Scene()
        self._game = Game(self._scene)

    def start(self):
        self._scene.create()
        while self._scene.is_active():
            self._scene.clear()
            self._game.render()
            self._scene.update()
