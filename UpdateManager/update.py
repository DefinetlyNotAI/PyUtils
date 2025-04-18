import subprocess
import sys
from TerminalPrint import TPrint

tprint = TPrint()


class GitUpdateManager:
    def __init__(self, repo_path: str, branch: str = "main"):
        self.repo_path = repo_path
        self.branch = branch

    def run_git_command(self, *args):
        """Run a Git command and return the output."""
        try:
            result = subprocess.run(
                ["git", "-C", self.repo_path, *args],
                text=True,
                capture_output=True,
                check=True
            )
            tprint.info(f"Command succeeded: git {' '.join(args)}")
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            tprint.error(f"Git command failed: git {' '.join(args)}")
            tprint.error(f"Error: {e.stderr.strip()}")
            sys.exit(1)

    def fetch_updates(self):
        """Fetch updates from the remote repository."""
        tprint.info("Fetching updates...")
        self.run_git_command("fetch", "--all")

    def check_status(self):
        """Check the status of the repository."""
        tprint.info("Checking repository status...")
        status = self.run_git_command("status", "--porcelain")
        if status:
            tprint.warning("Uncommitted changes detected. Please commit or stash them before updating.")
            sys.exit(1)

    def merge_updates(self):
        """Merge updates from the remote branch."""
        tprint.info(f"Merging updates from branch '{self.branch}'...")
        try:
            self.run_git_command("merge", f"origin/{self.branch}")
        except SystemExit:
            tprint.error("Merge conflicts detected. Please resolve them manually.")
            sys.exit(1)

    def update(self):
        """Perform the full update process."""
        tprint.info("Starting update process...")
        self.check_status()
        self.fetch_updates()
        self.merge_updates()
        tprint.info("Update completed successfully.")
