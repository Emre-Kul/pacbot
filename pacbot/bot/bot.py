from random import *


class Bot:
    def __init__(self, gen_size, mutation_rate=0):
        self.mutation_rate = mutation_rate
        self.pop_size = 250
        self.gen_size = gen_size
        self.populations = []
        pass

    def create_generation(self):
        if len(self.populations) == 0:
            self.create_first_generation()
        else:
            self.kill_worst_populations()
            for i in range(self.gen_size - len(self.populations)):
                new_population = self.crosover_bests()
                self.mutate(new_population)
                new_population['path'] = (new_population['path'] + self.create_population()['path'])[:self.pop_size]
                self.populations.append(new_population)

    def create_first_generation(self):
        for i in range(self.gen_size):
            self.populations.append(self.create_population())

    def create_population(self):
        population = {'path': [], 'score': 0}
        population['path'].append(randint(0, 3))
        i = 1
        while i < self.pop_size - 1:
            poss = [0, 1, 2, 3]
            poss.remove(population['path'][i - 1])
            rand_move = poss[randint(0, len(poss) - 1)]
            population['path'].append(rand_move)
            i += 1
        return population

    def kill_worst_populations(self):
        if len(self.populations) > 0:
            new_gen = sorted(self.populations, key=lambda k: k['score'])
            new_gen.reverse()
            self.populations = new_gen[:2]

    def fitness_func(self, population):
        return population['score']

    def mutate(self, population):
        for idx in range(len(population['path'])):
            if uniform(0, 1) < self.mutation_rate:
                population['path'][idx] = randint(0, 3)

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

        return {'path': path, 'score': 0}
