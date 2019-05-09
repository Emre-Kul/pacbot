from pacbot.bot.bot import Bot
from pacbot.game.scene import Scene
from pacbot.game.game import Game


class App:

    def __init__(self):
        self._scene = Scene()
        self.bot = Bot()  # population count
        self._game = Game(self._scene)

    def start(self):
        self._game.scene.create()
        self.run_simulation()

    def run_simulation(self):
        gen_index = 0
        simulation_count = 1000
        # while gen_index < simulation_count:
        while gen_index >= 0:
            self.bot.create_generation()
            gen_index += 1
            pop_index = 0
            path_index = 0
            print("GEN : {}".format(gen_index))
            while pop_index < len(self.bot.populations):
                population = self.bot.populations[pop_index]
                if path_index < len(population['path']):
                    self._game.move_player(population['path'][path_index])
                    path_index += 1
                if self._game.scene.is_active():
                    self._game.run()
                    if pop_index == 0:
                        self._game.render()
                if self._game.is_finished:
                    # print(self._game.score)
                    self.bot.populations[pop_index]['score'] = self._game.score
                    self._game.start()
                    if pop_index == 0:
                        print("Max : {}".format(self.bot.populations[0]["score"]))
                    pop_index += 1
                    path_index = 0
