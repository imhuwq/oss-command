import os
import time
import unittest.mock as mock

import pytest

from oss_command.entrypoint import main
from oss_command.commands import upload_to_oss
from oss_command.commands import delete_from_oss
from tests import oss_endpoint
from tests import test_file
from tests import test_directory
from tests.test_config import _mock_config_file
from tests.test_config import _mock_input

cur_file = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_file)
tmp_file = str(time.time())


@mock.patch("sys.argv", [])
def test_help():
    with pytest.raises(SystemExit):
        main()


@mock.patch("sys.argv", ["", "config"])
@mock.patch("oss_command.config.config_file", _mock_config_file)
@mock.patch("builtins.input", _mock_input)
def test_config():
    main()


@mock.patch("sys.argv", ["", "upload", cur_file, oss_endpoint, tmp_file])
def test_upload():
    main()
    delete_from_oss(oss_endpoint, tmp_file)


@mock.patch("sys.argv", ["", "upload", cur_file, oss_endpoint])
def test_upload_invalid_parameter():
    with pytest.raises(SystemExit):
        main()


@mock.patch("sys.argv", ["", "exist", oss_endpoint, test_file])
def test_exist():
    main()


@mock.patch("sys.argv", ["", "exist", oss_endpoint])
def test_exist_invalid_parameter():
    with pytest.raises(SystemExit):
        main()


@mock.patch("sys.argv", ["", "exist", oss_endpoint, str(time.time())])
def test_exist_failed():
    with pytest.raises(SystemExit):
        main()


@mock.patch("sys.argv", ["", "delete", oss_endpoint, tmp_file])
def test_delete():
    upload_to_oss(cur_file, oss_endpoint, tmp_file)
    main()


@mock.patch("sys.argv", ["", "delete", oss_endpoint])
def test_delete_invalid_parameter():
    with pytest.raises(SystemExit):
        main()


@mock.patch("sys.argv", ["", "copy", oss_endpoint, test_file, tmp_file])
def test_copy():
    main()
    delete_from_oss(oss_endpoint, tmp_file)


@mock.patch("sys.argv", ["", "copy", oss_endpoint, test_file])
def test_copy_invalid_parameter():
    with pytest.raises(SystemExit):
        main()
        delete_from_oss(oss_endpoint, tmp_file)


@mock.patch("sys.argv", ["", "download", tmp_file, oss_endpoint, test_file])
def test_download():
    main()
    assert os.path.exists(tmp_file)
    os.remove(tmp_file)


@mock.patch("sys.argv", ["", "download", tmp_file, oss_endpoint])
def test_download_invalid_parameter():
    with pytest.raises(SystemExit):
        main()
        assert os.path.exists(tmp_file)
        os.remove(tmp_file)


@mock.patch("sys.argv", ["", "copy", oss_endpoint, test_directory, test_directory + "/" + "self"])
def test_command_fail_will_result_abnormal_exit():
    with pytest.raises(SystemExit):
        main()
