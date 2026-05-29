from git_service import git_generate_commit
from typing import Any
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")


def main() -> Any:
    if not API_KEY:
        print("Error: Gemini api key is not set")
        print("Set it in you .env file based on the .env.example")
    print("Analyzing git changes")
    diff = git_generate_commit()


if __name__ == "__main__":
    pass
