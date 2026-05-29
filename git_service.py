import subprocess, sys


def git_generate_commit() -> str:
    try:
        result = subprocess.run(
            ["git", "diff", "--cached"], capture_output=True, text=True, check=True
        )
        diff = result.stdout.strip()

        if not diff:
            print(
                "No changes in staging area, Use 'git add <files>' to prepare changes"
            )

        return diff
    except subprocess.CalledProcessError:
        print("This is not a git respository or git is not installed")
        sys.exit(1)
