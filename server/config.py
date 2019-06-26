import json
import os

with open(os.path.abspath("config.json"), 'r') as config_file:
    config = json.load(config_file)