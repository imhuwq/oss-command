import sys
import traceback
from functools import wraps

from oss_command.commands import ask_config
from oss_command.commands import upload_to_oss
from oss_command.commands import delete_from_oss
from oss_command.commands import download_from_oss
from oss_command.commands import check_file_exists
from oss_command.commands import copy_file


def ensure_failure_exit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            exit(1)

    return wrapper


class Config:
    HELP_TEXT = "{0:<20} 以交互的方式配置 key 和 secret".format("config")

    @staticmethod
    @ensure_failure_exit
    def run():
        return ask_config()


class Upload:
    HELP_TEXT = "{0:<20} 上传本地文件到 oss\n{1:<20} [local_path] [bucket.endpoint] [remote_path]".format("upload", "")

    @staticmethod
    @ensure_failure_exit
    def run():
        if len(sys.argv) < 5:
            print(Upload.HELP_TEXT)
            exit(1)
        local, endpoint, remote = sys.argv[2:5]
        return upload_to_oss(local, endpoint, remote)


class Delete:
    HELP_TEXT = "{0:<20} 从 oss 删除文件\n{1:<20} [bucket.endpoint] [remote_path]".format("delete", "")

    @staticmethod
    @ensure_failure_exit
    def run():
        if len(sys.argv) < 4:
            print(Delete.HELP_TEXT)
            exit(1)
        endpoint, remote = sys.argv[2:4]
        return delete_from_oss(endpoint, remote)


class Download:
    HELP_TEXT = "{0:<20} 下载 oss 文件到本地\n{1:<20} [local_path] [bucket.endpoint] [remote_path]".format("download", "")

    @staticmethod
    @ensure_failure_exit
    def run():
        if len(sys.argv) < 5:
            print(Download.HELP_TEXT)
            exit(1)
        local, endpoint, remote = sys.argv[2:5]
        return download_from_oss(local, endpoint, remote)


class Exist:
    HELP_TEXT = "{0:<20} 检查指定文件是否存在\n{1:<20} [bucket.endpoint] [remote_path]".format("exist", "")

    @staticmethod
    @ensure_failure_exit
    def run():
        if len(sys.argv) < 4:
            print(Exist.HELP_TEXT)
            exit(1)
        endpoint, remote_path = sys.argv[2:4]
        if not check_file_exists(endpoint, remote_path):
            exit(1)


class Copy:
    HELP_TEXT = "{0:<20} 在 oss 复制文件\n{1:<20} [bucket.endpoint] [remote_src] [remote_dst]".format("copy", "")

    @staticmethod
    @ensure_failure_exit
    def run():
        if len(sys.argv) < 5:
            print(Copy.HELP_TEXT)
            exit(1)
        endpoint, remote_src, remote_dst = sys.argv[2:5]
        return copy_file(endpoint, remote_src, remote_dst)


class Help:
    HELP_TEXT = "{0:<20} 显示该条帮住消息".format("help")

    @staticmethod
    def run():
        print("Usage: oss_command <command> [options]\n")
        print("Commands: ")
        print(Config.HELP_TEXT)
        print(Upload.HELP_TEXT)
        print(Delete.HELP_TEXT)
        print(Download.HELP_TEXT)
        print(Exist.HELP_TEXT)
        print(Copy.HELP_TEXT)
        print(Help.HELP_TEXT)


COMMANDS = {
    "help": Help,
    "config": Config,
    "upload": Upload,
    "delete": Delete,
    "download": Download,
    "exist": Exist,
    "copy": Copy
}


def main():
    if len(sys.argv) < 2:
        Help.run()
        exit(1)

    command = sys.argv[1]
    COMMANDS[command].run()
