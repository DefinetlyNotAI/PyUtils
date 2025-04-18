from UpdateManager import GitUpdateManager

if __name__ == "__main__":
    repo_path = "../UpdateManager/"
    branch = "main"

    manager = GitUpdateManager(repo_path, branch)
    manager.update()
