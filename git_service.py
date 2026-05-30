import subprocess, sys
from logger import log


def git_generate_commit() -> str:
    try:
        log.debug("Running subprocess")
        result = subprocess.run(
            ["git", "diff", "--cached"], capture_output=True, text=True, check=True
        )
        diff = result.stdout.strip()

        if not diff:
            log.debug("No changes found")
            print(
                "No changes in staging area, Use 'git add <files>' to prepare changes"
            )
            sys.exit(0)
        return diff
    except subprocess.CalledProcessError:
        log.error("Subprocess error occured")
        print("This is not a git respository or git is not installed")
        sys.exit(1)
