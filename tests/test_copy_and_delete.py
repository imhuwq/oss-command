import time

import pytest

from tests import test_file
from tests import test_directory
from tests import oss_endpoint

from oss_command.commands import copy_file
from oss_command.commands import check_file_exists
from oss_command.commands import delete_from_oss


def test_copy_file():
    target = test_file + str(time.time())
    assert not check_file_exists(oss_endpoint, target)
    copy_file(oss_endpoint, test_file, target)
    assert check_file_exists(oss_endpoint, target)
    delete_from_oss(oss_endpoint, target)
    assert not check_file_exists(oss_endpoint, target)


def test_copy_directory():
    target = test_directory + str(time.time())
    assert not check_file_exists(oss_endpoint, target)
    copy_file(oss_endpoint, test_directory, target)
    assert check_file_exists(oss_endpoint, target)
    delete_from_oss(oss_endpoint, target)
    assert not check_file_exists(oss_endpoint, target)


def test_copy_file_to_directory_name():
    target = test_file + str(time.time()) + "/"
    assert not check_file_exists(oss_endpoint, target)
    copy_file(oss_endpoint, test_file, target)
    assert check_file_exists(oss_endpoint, target)
    delete_from_oss(oss_endpoint, target)
    assert not check_file_exists(oss_endpoint, target)


def test_copy_directory_into_self():
    target = test_directory + "/" + "self"
    assert not check_file_exists(oss_endpoint, target)
    with pytest.raises(Exception):
        copy_file(oss_endpoint, test_directory, target)
