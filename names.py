import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")


def extract_entities(text: str):
    """
    Extract named entities from the input text.

    :param text: The input text to extract entities from.
    :return: List of entities.
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities


def extract_names(text: str):
    """
    Extract names from the input text using named entity recognition.

    :param text: The input text to extract names from.
    :return: List of names.
    """
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    return names


# Example usage
if __name__ == "__main__":
    text = "I need support with my order, John Doe."
    entities = extract_entities(text)
    names = extract_names(text)

    print(f"Entities: {entities}")
    print(f"Names: {names}")
