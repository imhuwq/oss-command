import os
import oss2

from oss_command.commands.common import get_bucket


def upload_to_oss(local_path, endpoint, remote_path):
    bucket = get_bucket(endpoint)
    local_path = os.path.abspath(local_path)
    if os.path.isdir(local_path):
        for top, dirs, files in os.walk(local_path):
            for file in files:
                local_file = os.path.join(top, file)
                remote_file = local_file.replace(local_path, remote_path)
                print("Uploading {0}...".format(local_file))
                oss2.resumable_upload(bucket, remote_file, local_file)
    else:
        print("Uploading {0}...".format(local_path))
        oss2.resumable_upload(bucket, remote_path, local_path)
