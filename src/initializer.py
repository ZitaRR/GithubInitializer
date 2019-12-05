import sys
import os
from pathlib import Path
from github import Github

directory = sys.argv[1]
reponame = os.path.basename(directory)
username = "YOUR USERNAME" #Your github username
password = "YOUR PASSWORD" #Your github password

def init():
    user = Github(username, password).get_user()
    repo = user.create_repo(reponame)
    print("Repository {0} was created.".format(reponame))
    print("Pushing files...")
    for dirpath, dirs, files in os.walk(directory):
        for file in files:
            fullpath = os.path.join(dirpath, file)
            relativePath = os.path.relpath(fullpath, directory)
            relativePath = relativePath.replace('\\', '/')
            folder = Path(fullpath).parent.name
            with open(fullpath, 'r') as content:
                repo.create_file(relativePath, "Initial commit", content.read())
    print("Push finished.")

if __name__ == "__main__":
    init()
