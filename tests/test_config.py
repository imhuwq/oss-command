import os
import json
import unittest.mock as mock

import pytest

from oss_command.commands import ask_config
from oss_command.config import config_file
from oss_command.commands.common import load_config


def test_load_config():
    if os.path.exists(config_file):
        config = load_config()
        assert config["key"]
        assert config["secret"]


@mock.patch("oss_command.config.config_file", "/not/exist/path.whatever")
def test_load_none_exist_config():
    os.environ.pop("oss_command_key", None)
    os.environ.pop("oss_command_secret", None)
    with pytest.raises(Exception) as e:
        load_config()
    assert str(e.value) == "Run oss_command config first"


@mock.patch("oss_command.config.config_file", "/not/exist/path.whatever")
@mock.patch("os.environ", dict())
def test_load_from_environment():
    os.environ["oss_command_key"] = "a fake key"
    os.environ["oss_command_secret"] = "a fake secret"
    cfg = load_config()
    assert cfg["key"] == "a fake key"
    assert cfg["secret"] == "a fake secret"


_mock_config_file = "/tmp/fake_oss_command_config.json"


def _mock_input(prompt):
    if prompt.startswith("Oss Key: "):
        return "a fake key"
    elif prompt.startswith("Oss Secret: "):
        return "a fake secret"
    return None


@mock.patch("oss_command.config.config_file", _mock_config_file)
@mock.patch("builtins.input", _mock_input)
def test_ask_config():
    ask_config()
    assert os.path.exists(_mock_config_file)
    with open(_mock_config_file, "r") as f:
        cfg = json.load(f)
        assert cfg["key"]
        assert cfg["secret"]
    os.remove(_mock_config_file)
