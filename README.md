# AION Chatbot

A multilingual chatbot supporting English and Persian (Farsi), built using Python and spaCy.

## Features

- Supports English and Persian languages
- Intent classification and entity extraction
- Predefined responses and dynamic response generation
- Name extraction from user input

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/MKinG4ever/AION.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Download language models:
    ```bash
    python -m spacy download en_core_web_sm
    python -m spacy download xx_ent_wiki_sm
    ```

## Usage

Run the main script to start the chatbot:
```bash
python main.py
