import json
import os


def load_json(filename):
    with open(os.path.abspath(filename)) as data_json:
        data = json.load(data_json)
        return data


def load_config(filename):
    config = load_json(filename)
    # TODO : Will add error checks for configs etc
    config['SIMILATION_COUNT'] = int(config['SIMILATION_COUNT'])
    config['GENERATION_SIZE'] = int(config['GENERATION_SIZE'])
    config['RENDER_BEST_POPULATION_COUNT'] = int(config['RENDER_BEST_POPULATION_COUNT'])
    return config


def write_json(filename, data):
    with open(os.path.abspath(filename), 'w') as outfile:
        json.dump(data, outfile)


def read_population_from_file():
    pass