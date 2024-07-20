import spacy

# Load language models
nlp_en = spacy.load("en_core_web_sm")
nlp_fa = spacy.load("xx_ent_wiki_sm")  # Generic multilingual model with some Persian support


def preprocess_text(text: str, language: str):
    """
    Preprocess the input text by tokenizing and lemmatizing.

    :param text: The input text to preprocess.
    :param language: The language of the text ('en' or 'fa').
    :return: List of lemmatized tokens.
    """
    nlp = nlp_en if language == 'en' else nlp_fa
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]


# Example usage
if __name__ == "__main__":
    text_en = "Hello, how can I help you today?"
    text_fa = "سلام، چگونه می‌توانم به شما کمک کنم؟"

    print(preprocess_text(text_en, 'en'))
    print(preprocess_text(text_fa, 'fa'))
