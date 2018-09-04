import os
import time
import shutil

from tests import test_file
from tests import test_directory
from tests import oss_endpoint

from oss_command.commands.list import list_files
from oss_command.commands import download_from_oss


def test_download_file():
    local = os.path.join("/tmp", str(time.time()))
    assert not os.path.exists(local)
    download_from_oss(local, oss_endpoint, test_file)
    assert os.path.exists(local)
    os.remove(local)


def test_download_directory():
    local_dir = os.path.join("/tmp", str(time.time()))
    assert not os.path.exists(local_dir)
    download_from_oss(local_dir, oss_endpoint, test_directory)
    assert os.path.exists(local_dir)
    remote_files = list_files(oss_endpoint, test_directory)
    download_files = []
    for top, dirs, files in os.walk(local_dir):
        for file in files:
            local_file = os.path.join(top, file)
            local_rel_file = os.path.relpath(local_file, local_dir)
            download_files.append(os.path.join(test_directory, local_rel_file))
    for file in remote_files:
        assert file in download_files
    shutil.rmtree(local_dir)
