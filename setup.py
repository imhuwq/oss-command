from setuptools import setup, find_packages

VERSION = "0.4.0"

setup(
    name="oss_command",
    version=VERSION,
    author="huweiqiang",
    author_email="huweiqiang@gizmotech.cn",
    packages=find_packages(),
    install_requires=["oss2"],
    entry_points={
        "console_scripts": ["oss_command=oss_command.entrypoint:main"],
    }
)
