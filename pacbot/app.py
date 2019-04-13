from pacbot.game.scene import *


class App:

    def __init__(self):
        self._scene = Scene()

    def start(self):
        self._scene.create()
        while self._scene.is_active():
            self._scene.update()
