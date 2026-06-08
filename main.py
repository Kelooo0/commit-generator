import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

from ai_service import ai_generate_commit
from git_service import git_generate_commit

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_DIR = Path(__file__).resolve().parent
FILENAME = BASE_DIR / "app.log"


def main():
    logger.remove()
    logger.add(
        sys.stderr, level="INFO", format="<level>{level: <8}</level> | {message}"
    )
    logger.add(FILENAME, level="DEBUG", mode="w")

    logger.debug("App start")
    logger.debug("Checking api key...")
    if not API_KEY:
        logger.error(
            "Gemini api key is not set, set it in your .env file based on .env.example"
        )
        logger.opt(exception=True).debug("Exception traceback:")
    logger.info("Analyzing git changes")
    diff = git_generate_commit()
    logger.debug("Git changes returned succesfully")
    logger.info("Generating commit...")
    commit = ai_generate_commit(diff, API_KEY)
    logger.debug("Commit message generated succesfully")
    print("\n" + "=" * 40)
    print(f"Proposed commit message:\n\033[1;32m{commit}\033[0m")
    print("=" * 40 + "\n")
    choice = input("Do you want to commit these changes? (Y/n): ").strip().lower()
    if choice in ("y", "yes", ""):
        logger.info("Commiting changes...")
        try:
            subprocess.run(["git", "commit", "-m", commit], check=True)
            logger.info("Commited succesfully")
        except subprocess.CalledProcessError:
            logger.error("An error occured while commiting changes")
            logger.opt(exception=True).debug("Exception traceback:")
            sys.exit(1)
    else:
        logger.info("Commiting canceled")
    logger.debug("App end")


if __name__ == "__main__":
    main()
