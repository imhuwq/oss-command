from oss_command.commands.common import get_bucket
from oss_command.commands.list import _list_files


def delete_from_oss(endpoint, remote_path):
    bucket = get_bucket(endpoint)
    print("Deleting {0}...".format(remote_path))
    bucket.delete_object(remote_path)
    remote_files = _list_files(bucket, remote_path)
    if remote_files:
        bucket.batch_delete_objects(remote_files)
