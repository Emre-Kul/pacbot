import json


def load_config(filename="config.json"):
    with open(filename) as config_json:
        config = json.load(config_json)
        return config

