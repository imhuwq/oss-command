from oss2.exceptions import NoSuchKey
from oss2.exceptions import NotFound

from oss_command.commands.common import get_bucket
from oss_command.commands.list import _list_files
from oss_command.commands.list import MAX_FILE_COUNT


def copy_file(endpoint, src, dst):
    bucket = get_bucket(endpoint)
    print("Copying {0} to {1}...".format(src, dst))
    try:
        bucket.copy_object(bucket.bucket_name, src, dst)
    except (NotFound, NoSuchKey):
        if dst.startswith(src if src.endswith("/") else src + "/"):
            raise Exception("不能把文件夹复制到自己的子文件夹内")
        # FIXME: 只能复制 1000 个文件

        remote_files = _list_files(bucket, src, MAX_FILE_COUNT)
        for src_file in remote_files:
            dst_file = src_file.replace(src, dst)
            print("Copying {0}...".format(src_file))
            bucket.copy_object(bucket.bucket_name, src_file, dst_file)
