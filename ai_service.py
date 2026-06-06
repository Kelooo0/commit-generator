import sys

from google import genai
from google.genai import types

from logger import log


def ai_generate_commit(diff, API_KEY):
    log.debug("Setting up AI client")
    client = genai.Client(api_key=API_KEY)

    config = types.GenerateContentConfig(
        system_instruction="""
                You are an expert software engineer. Analyze the provided git diff and generate
                a short, concise commit message using Conventional Commits format (e.g., feat(auth): ..., fix(ui): ...).
                Do not include any markdown bolding, quotes, code blocks, or explanations.
                Return ONLY the raw commit message string so it can be directly piped into a command.
            """,
        temperature=0.2,
    )
    log.debug("Generating response...")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=diff, config=config
        )
        return response.text.strip()

    except Exception:
        log.exception("An AI service error occured while generating response")
        sys.exit(1)
