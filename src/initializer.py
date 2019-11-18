import sys
import os
from pathlib import Path
from github import Github

directory = sys.argv[1]
reponame = os.path.basename(directory)
username = sys.argv[2] #Your github username
password = sys.argv[3] #Your github password

def init():
    user = Github(username, password).get_user()
    repo = user.create_repo(reponame)
    print("Repository {0} was created.".format(reponame))
    print("Pushing files...")
    for dirpath, dirs, files in os.walk(directory):
        for file in files:
            folder = Path(os.path.join(dirpath, file)).parent.name
            path = "{0}/{1}".format(folder, file)
            with open(file, 'r') as content:
                repo.create_file(path, "Initial commit", content.read())
    print("Push finished.")

if __name__ == "__main__":
    init()