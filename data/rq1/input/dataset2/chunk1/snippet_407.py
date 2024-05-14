#Source: https://stackoverflow.com/questions/38918748/why-does-mocking-open-and-returning-a-filenotfounderror-raise-attributeerror
import os

import so_config


def load_savelocation():
    path = os.path.join(so_config.ROOT, so_config.SAVELOCATION_FN)
    savelocation_path = os.path.normpath(path)
    try:
        with open(savelocation_path) as f:
            so_config.SAVELOCATION_PATH = f.readline()
    except FileNotFoundError:
        so_config.SAVELOCATION_PATH = so_config.ROOT