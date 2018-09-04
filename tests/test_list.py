import pytest

from tests import test_file
from tests import test_directory
from tests import oss_endpoint
from tests import massive_directory

from oss_command.commands import list_files
from oss_command.commands.list import MAX_FILE_COUNT


def test_list_files():
    files = list_files(oss_endpoint, "", 1000)
    assert test_file in files
    files = list_files(oss_endpoint, test_directory, 1000)
    assert all(map(lambda x: x.startswith(test_directory), files))


def test_list_files_max_count():
    files = list_files(oss_endpoint, massive_directory, max_count=1)
    assert len(files) == 1, len(files)
    files = list_files(oss_endpoint, massive_directory, max_count=32)
    assert len(files) == 32
    files = list_files(oss_endpoint, massive_directory, max_count=1000)
    assert len(files) <= 1000, len(files)


def test_list_files_beyond_max_count():
    with pytest.raises(Exception):
        list_files(oss_endpoint, "", MAX_FILE_COUNT + 1)
