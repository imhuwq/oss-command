import json

from oss_command import config


def ask_config():
    config_file = config.config_file
    oss_key = input("Oss Key: ")
    oss_scr = input("Oss Secret: ")
    cfg = {"key": oss_key, "secret": oss_scr}
    with open(config_file, "w") as f:
        json.dump(cfg, f)
