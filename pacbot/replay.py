from pacbot.game.scene import Scene
from pacbot.game.game import Game
from pacbot.common import utils
import time

class ReplayApp:

    def __init__(self):
        self._scene = Scene()
        self._game = Game(self._scene)

    def start(self):
        self._game.scene.create()
        # self.replay_simulations()
        self.replay_simulations2()
        while self._game.scene.is_active():
            time.sleep(1)

    def replay_simulations(self):
        simulations = utils.load_json('data/replay_data.txt')
        for simulation in simulations:
            self._game.start()
            for move_index, move in enumerate(simulation['POPULATION']):
                self._game.move_player(move)
                if self._game.scene.is_active():
                    self._game.run()
                    self._game.render()
            print("GEN : {}".format(simulation['GENERATION']))
            print("Max Score : {}".format(simulation['SCORE']))

    def replay_simulations2(self):
        simulations = utils.load_json('data/replay_data.txt')
        for simulation in simulations:
            self._game.start()
            move_index = 0
            while  not self._game.is_finished:
                move = simulation['POPULATION'][move_index]
                if self._game.is_player_moved():
                    self._game.move_player(move)
                    if move_index + 1 < len(simulation['POPULATION']):
                        move_index += 1
                if self._game.scene.is_active():
                    self._game.run()
                    self._game.render()
            print("GEN : {}".format(simulation['GENERATION']))
            print("Max Score : {}".format(simulation['SCORE']))
