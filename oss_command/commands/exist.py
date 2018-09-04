from oss_command.commands.common import get_bucket


def check_file_exists(endpoint, remote_path):
    bucket = get_bucket(endpoint)
    if bucket.object_exists(remote_path):
        print("{0} exists".format(remote_path))
        return True

    remote_dir = remote_path
    if not remote_dir.endswith("/"):
        remote_dir += "/"
    files = bucket.list_objects(remote_dir, max_keys=1).object_list
    if len(files) == 1:
        print("{0} exists".format(remote_dir))
        return True

    print("{0} does not exist".format(remote_path))
    return False
