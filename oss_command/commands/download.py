import os

from oss2 import resumable_download
from oss2.exceptions import NoSuchKey
from oss2.exceptions import NotFound

from oss_command.commands.common import get_bucket
from oss_command.commands.list import _list_files
from oss_command.commands.list import MAX_FILE_COUNT


def download_from_oss(local_path, endpoint, remote_path):
    bucket = get_bucket(endpoint)
    print("Downloading {0}...".format(remote_path))
    try:
        return resumable_download(bucket, remote_path, local_path)
    except (NotFound, NoSuchKey):
        # FIXME: 最多只能下载 1000 个文件
        remote_files = _list_files(bucket, remote_path, MAX_FILE_COUNT)
        for remote_file in remote_files:
            rel = os.path.relpath(remote_file, remote_path)
            local_file = os.path.join(local_path, rel)
            local_file_dir = os.path.dirname(local_file)
            os.makedirs(local_file_dir, exist_ok=True)
            print("Downloading {0}...".format(remote_file))
            resumable_download(bucket, remote_file, local_file)
