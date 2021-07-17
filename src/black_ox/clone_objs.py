"""Module: Pull the database objects from Github to local directory!"""
import os
import shutil
import stat

from git import Repo


def remove_readonly_file(_, name, __):
    """Change the mode of the file from read-only to write!"""
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)


def clone_db_objs(target_dir, git_url):
    """Pull the database objects from Github to local directory!"""
    try:
        if os.path.isdir(target_dir):
            shutil.rmtree(target_dir, onerror=remove_readonly_file)
            print(f"Clone starts for repo: {git_url}")
            Repo.clone_from(git_url, target_dir)
            print(f"Clone ends for repo: {git_url}")
        else:
            print(f"Clone starts for repo: {git_url}")
            Repo.clone_from(git_url, target_dir)
            print(f"Clone ends for repo: {git_url}")

    except OSError as error:
        print(f"Error: {error.filename} - {error.strerror}.")
