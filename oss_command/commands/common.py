import os
import json

import oss2

from oss_command import config


def load_config():
    config_file = config.config_file
    cfg = dict()
    if not os.path.exists(config_file):
        key = os.environ.get("oss_command_key", None)
        secret = os.environ.get("oss_command_secret", None)
        if not key and not secret:
            raise Exception("Run oss_command config first")
        cfg["key"] = key
        cfg["secret"] = secret
        return cfg
    with open(config_file, "r") as f:
        cfg = json.load(f)
    return cfg


def get_bucket(endpoint):
    cfg = load_config()
    auth = oss2.Auth(cfg["key"], cfg["secret"])
    bucket_name, endpoint = endpoint.split(".", 1)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)
    return bucket
