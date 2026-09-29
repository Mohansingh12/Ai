import tomllib

import test


def load_toml():
    with open(test, "r") as f:
        data = tomllib.load(f)
