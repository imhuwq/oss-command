from oss_command.commands.common import get_bucket

MAX_FILE_COUNT = 1000


def _list_files(bucket, remote_path, max_count=100):
    if max_count > MAX_FILE_COUNT:
        raise Exception("最多只能获取 1000 个文件")

    if remote_path and not remote_path.endswith("/"):
        remote_path += "/"

    is_truncated = True
    marker = ""
    remote_files = []
    while is_truncated and len(remote_files) < max_count:
        search_result = bucket.list_objects(remote_path, marker=marker, max_keys=max_count - len(remote_files))
        remote_objects = search_result.object_list
        for remote_object in remote_objects:
            if remote_object.key.endswith("/"):
                continue
            remote_files.append(remote_object.key)
        is_truncated = search_result.is_truncated
        marker = search_result.next_marker

    return remote_files


def list_files(endpoint, remote_path, max_count=100):
    bucket = get_bucket(endpoint)
    return _list_files(bucket, remote_path, max_count)
