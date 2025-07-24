# YouTube and Website Summarizer

This is a Streamlit application that summarizes content from YouTube videos or websites using language models provided by Groq through LangChain.

## Features

- Summarizes YouTube videos or website content
- Supports models like `gemma2-9b-it` and `llama-3.1-8b-instant`
- Provides structured summaries in plain text
- Simple and clean user interface
- Requires only a valid URL and Groq API key

## Technologies Used

- Python
- Streamlit
- LangChain
- Groq API

## Installation

```bash
# Clone the repository
git clone https://github.com/Sayan-Pal847/Youtube-video-and-URL-content-summarizer.git
cd Youtube-video-and-URL-content-summarizer

# Create a virtual environment
python -m venv .venv

# Activate the environment
# For Windows:
.venv\Scripts\activate

# For macOS/Linux:
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
