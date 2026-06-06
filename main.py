import os
import subprocess
import sys

from dotenv import load_dotenv

from ai_service import ai_generate_commit
from git_service import git_generate_commit
from logger import log

load_dotenv()

API_KEY = os.getenv("API_KEY")


def main():
    log.debug("App start")
    log.debug("Checking api key...")
    if not API_KEY:
        log.error(
            "Gemini api key is not set, set it in your .env file based on .env.example"
        )
    log.info("Analyzing git changes")
    diff = git_generate_commit()
    log.debug("Git changes returned succesfully")
    log.info("Generating commit...")
    commit = ai_generate_commit(diff, API_KEY)
    log.debug("Commit message generated succesfully")
    print("\n" + "=" * 40)
    print(f"Proposed commit message:\n\033[1;32m{commit}\033[0m")
    print("=" * 40 + "\n")
    choice = input("Do you want to commit these changes? (Y/n): ").strip().lower()
    if choice in ("y", "yes", ""):
        log.info("Commiting changes...")
        try:
            subprocess.run(["git", "commit", "-m", commit], check=True)
            log.info("Commited succesfully")
        except subprocess.CalledProcessError:
            log.exception("An error occured while commiting changes")
            sys.exit(1)
    else:
        log.info("Commiting canceled")
    log.debug("App end")


if __name__ == "__main__":
    main()
