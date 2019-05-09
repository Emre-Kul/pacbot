from random import *


class Bot:
    def __init__(self, gen_size=4):
        self.pop_size = 1000
        self.gen_size = gen_size
        self.populations = []
        pass

    def create_generation(self):
        if len(self.populations) == 0:
            self.create_first_generation()
        else:
            self.kill_worst_populations()
            for i in range(self.gen_size - len(self.populations) - 2):
                self.populations.append(self.create_population())
            for i in range(2):
                self.populations.append(self.crosover_bests())

    def create_first_generation(self):
        for i in range(self.gen_size ):
            self.populations.append(self.create_population())

    def create_population(self):
        population = {'path': [], 'score': 0}
        for i in range(self.pop_size):
            population['path'].append(randint(0, 3))
        return population

    def kill_worst_populations(self):
        # kill half of them
        # print(self.populations)
        if len(self.populations) > 0:
            new_gen = sorted(self.populations, key=lambda k: k['score'])
            new_gen.reverse()
            self.populations = new_gen[:2]

    def fitness_func(self):
        pass

    def mutate(self):
        pass

    def crosover_bests(self):
        path = []
        if len(self.populations) >= 2:
            for i in range(self.pop_size):
                rand = randint(0, 1)
                path.append(self.populations[rand]['path'][i])
        return {'path': path, 'score': 0}