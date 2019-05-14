from random import *


class Bot:
    def __init__(self, gen_size):
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
        for i in range(self.gen_size):
            self.populations.append(self.create_population())

    def create_population(self):
        population = {'path': [], 'score': 0}
        for i in range(self.pop_size):
            population['path'].append(randint(0, 3))
        return population

    def kill_worst_populations(self):
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
            best_paths = [self.populations[0]['path'], self.populations[1]['path']]
            for i in range(min(len(best_paths[0]), len(best_paths[1]))):
                rand = randint(0, 1)
                path.append(best_paths[rand][i])

            if len(best_paths[0]) < len(best_paths[1]):
                path = path + best_paths[1][len(best_paths[0]):len(best_paths[1])]
            else:
                path = path + best_paths[0][len(best_paths[1]):len(best_paths[0])]

        # burayı kaldırmam gerekebilir crosoverın ruhuna aykırı
        path = (path + self.create_population()['path'])[:self.pop_size]

        return {'path': path, 'score': 0}
