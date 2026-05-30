from git_service import git_generate_commit
from ai_service import ai_generate_commit
from typing import Any
from dotenv import load_dotenv
import os
import subprocess, sys
from logger import log

load_dotenv()

API_KEY = os.getenv("API_KEY")


def main() -> Any:
    log.debug("Program start")
    log.debug("Checking api key...")
    if not API_KEY:
        log.error("Api key is not set")
        print("Error: Gemini api key is not set")
        print("Set it in your .env file based on the .env.example")
    log.debug("Analyzing git changes")
    print("Analyzing git changes...")
    diff = git_generate_commit()
    log.debug("Git changes returned succesfully")
    log.debug("Generating commit...")
    commit = ai_generate_commit(diff, API_KEY)
    log.debug("Commit message generated succesfully")
    print("\n" + "=" * 40)
    print(f"Proposed commit message:\n\033[1;32m{commit}\033[0m")
    print("=" * 40 + "\n")
    choice = input("Do you want to commit these changes? (Y/n): ").strip().lower()
    if choice in ("y", "yes", ""):
        log.debug("Commiting changes...")
        try:
            subprocess.run(["git", "commit", "-m", commit], check=True)
            print("Commited succesfully")
        except subprocess.CalledProcessError:
            log.error("An error occured while commiting changes")
            print("An error occured while commiting changes")
            sys.exit(1)
    else:
        log.debug("Commiting canceled")
        print("Commiting canceled")


if __name__ == "__main__":
    main()
