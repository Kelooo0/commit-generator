# Commit Generator
Commit Generator is a CLI tool designed for quick and simple generation of commit messages based on changes made in Git project. It uses Google Gemini to generate AI responses. The tool can generate the commit message and make the commit for you.

## Features

- Automated commit generation
- Git integration
- Handling google-genai package


## Showcase

![Showcase](assets/img/cg_showcase.png)
![Log](assets/img/log.png)


## Installation

### 1. Clone the repository

- git clone https://github.com/Kelooo0/commit-generator.git
- cd commit-generator

### 2. Install virtual environment

- Windows: python -m venv .venv
- Linux/macOS: python3 -m venv .venv

### 3. Activate virtual environment

- Windows: .venv\Scripts\activate
- Linux/macOS: source .venv/bin/activate

### 4. Install dependencies

- Go to root folder
- Run: pip install -r requirements.txt

### 5. Configuration

- Basing on .env.example file create .env file
- Set API_KEY to your gemini api key created at: https://aistudio.google.com/

### 6. How to run

- Standard option
    - Run the generator from main.py file
- Global Command
    - You will need to create a .bat (Windows) or .sh (Linux) script that allows you to use the generator<br>
    from any directory. You will also need to add the directory of the generator to PATH variable

# Project structure

```text
commit-generator/
├── assets/             # Project documentation
├── ai_service.py       # Generates commit message
├── git_service.py      # Handles Git project changes
├── logger.py           # Creates setup for logs
├── main.py             # App entrypoint
├── .env.example        # Template for .env configuration
├── requirements.txt    # Project dependencies
└── README.md
