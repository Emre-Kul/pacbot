from pacbot.bot.bot import Bot
from pacbot.game.scene import Scene
from pacbot.game.game import Game
from pacbot.common import utils


class App:

    def __init__(self):
        self.config = utils.load_config('config.json')
        self._scene = Scene()
        self.bot = Bot(self.config['GENERATION_SIZE'])
        self._game = Game(self._scene)
        self.save_data = []

    def start(self):
        self._game.scene.create()
        # self.run_simulation()
        self.run_simulation2()

    def run_simulation(self):
        last_best_score = 0
        simulation_count = self.config['SIMILATION_COUNT']
        render_count = self.config['RENDER_BEST_POPULATION_COUNT']
        for gen_index in range(simulation_count):
            self.bot.create_generation()
            for pop_index, population in enumerate(self.bot.populations):
                self._game.start()
                for move_index, move in enumerate(population['path']):
                    self._game.move_player(move)
                    if self._game.scene.is_active():
                        self._game.run()
                    if pop_index < render_count:
                        self._game.render()
                    if self._game.is_finished:
                        population['score'] = self._game.score
                        population['path'] = population['path'][:move_index]
                        break

            if last_best_score < self.bot.populations[0]["score"]:
                self.save_data.append(
                    {
                        "GENERATION": gen_index + 1,
                        "SCORE": self.bot.populations[0]["score"],
                        "POPULATION": self.bot.populations[0]["path"]
                    }
                )
                last_best_score = self.bot.populations[0]["score"]
            print("GEN : {}".format(gen_index + 1))
            print("Max Score : {}".format(self.bot.populations[0]["score"]))
            utils.write_json("data/replay_data.txt", self.save_data)

    def run_simulation2(self):
        last_best_score = 0
        simulation_count = self.config['SIMILATION_COUNT']
        render_count = self.config['RENDER_BEST_POPULATION_COUNT']
        for gen_index in range(simulation_count):
            self.bot.create_generation()
            for pop_index, population in enumerate(self.bot.populations):
                self._game.start()
                move_index = 0
                while not self._game.is_finished:
                    move = population['path'][move_index]
                    if self._game.is_player_moved():
                        self._game.move_player(move)
                        if move_index + 1 < len(population['path']):
                            move_index += 1
                    if self._game.scene.is_active():
                        self._game.run()
                    if pop_index < render_count:
                        self._game.render()

                population['score'] = self._game.score
                population['path'] = population['path'][:move_index + 1]

            if last_best_score < self.bot.populations[0]["score"]:
                self.save_data.append(
                    {
                        "GENERATION": gen_index + 1,
                        "SCORE": self.bot.populations[0]["score"],
                        "POPULATION": self.bot.populations[0]["path"]
                    }
                )
                last_best_score = self.bot.populations[0]["score"]
            print("GEN : {}".format(gen_index + 1))
            print("Max Score : {}".format(self.bot.populations[0]["score"]))
            utils.write_json("data/replay_data.txt", self.save_data)
