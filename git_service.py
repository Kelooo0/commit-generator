import subprocess
import sys

from loguru import logger


def git_generate_commit():
    try:
        logger.debug("Running subprocess")
        result = subprocess.run(
            ["git", "diff", "--cached"], capture_output=True, text=True, check=True
        )
        diff = result.stdout.strip()

        if not diff:
            logger.info("No changes found")
            sys.exit(0)

        return diff
    except subprocess.CalledProcessError:
        logger.error("This is not a git respository or git is not installed")
        logger.opt(exception=True).debug("Exception traceback:")
        sys.exit(1)
