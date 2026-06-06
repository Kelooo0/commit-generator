import subprocess
import sys

from logger import log


def git_generate_commit():
    try:
        log.debug("Running subprocess")
        result = subprocess.run(
            ["git", "diff", "--cached"], capture_output=True, text=True, check=True
        )
        diff = result.stdout.strip()

        if not diff:
            log.info("No changes found")
            sys.exit(0)

        return diff
    except subprocess.CalledProcessError:
        log.error("This is not a git respository or git is not installed")
        sys.exit(1)
