#!/usr/bin/env python3

import yaml
import os

from clone_objs import clone_db_objs
from create_objs import create_db_objects
# Get the current execute file path
file_path = os.path.realpath(__file__)
# print(file_path)

# Get the current directory
cur_dir = os.path.dirname(file_path)
# print(cur_dir)

# Target local git directory
target_dir = os.path.join(cur_dir, "target")
# print(target_dir)

config_file = os.path.join(cur_dir, "config", "config.yml")
# print(config_file)

with open(config_file, "r") as config:
    cfg = yaml.safe_load(config)

git_url = cfg["GitHub"]["DB_Objects"]
# print(git_url)


def main():
    """Main function executes all submodules!"""
    clone_db_objs(target_dir, git_url)
    create_db_objects(target_dir)


if __name__ == "__main__":

    try:
        main()

    except OSError as error:
        print(f"Error: {error.filename} - {error.strerror}.")
