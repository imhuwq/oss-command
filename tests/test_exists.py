import time

from tests import test_file
from tests import test_directory
from tests import oss_endpoint

from oss_command.commands import check_file_exists


def test_exist():
    assert check_file_exists(oss_endpoint, test_file)
    assert check_file_exists(oss_endpoint, test_directory)
    assert not check_file_exists(oss_endpoint, test_file + str(time.time()))
