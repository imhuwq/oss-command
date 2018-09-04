import os
import time

from tests import oss_endpoint

from oss_command.commands import upload_to_oss
from oss_command.commands import delete_from_oss
from oss_command.commands import check_file_exists
from oss_command.commands import list_files

cur_file = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_file)


def test_upload():
    remote_file = str(time.time())
    assert not check_file_exists(oss_endpoint, remote_file)
    upload_to_oss(cur_file, oss_endpoint, remote_file)
    assert check_file_exists(oss_endpoint, remote_file)
    delete_from_oss(oss_endpoint, remote_file)
    assert not check_file_exists(oss_endpoint, remote_file)


def test_upload_directory():
    remote_dir = str(time.time())
    assert not check_file_exists(oss_endpoint, remote_dir)
    upload_to_oss(cur_dir, oss_endpoint, remote_dir)
    assert check_file_exists(oss_endpoint, remote_dir)

    local_files = []
    for top, dirs, files in os.walk(cur_dir):
        for file in files:
            file = os.path.join(top, file)
            file = os.path.relpath(file, cur_dir)
            local_files.append(file)

    remote_files = []
    for file in list_files(oss_endpoint, remote_dir):
        remote_files.append(os.path.relpath(file, remote_dir))

    assert set(local_files) == set(remote_files)

    delete_from_oss(oss_endpoint, remote_dir)
    assert not check_file_exists(oss_endpoint, remote_dir)
