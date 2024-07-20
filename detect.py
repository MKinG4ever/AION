from langdetect import detect


def detect_language(text: str) -> str:
    """
    Detect the language of the input text.

    :param text: The input text to detect the language.
    :return: Detected language ('en' or 'fa').
    """
    detected_lang = detect(text)
    if detected_lang == 'en':
        return 'en'
    elif detected_lang == 'fa':
        return 'fa'
    else:
        return 'en'


# Example usage
if __name__ == "__main__":
    text = "سلام، چگونه می‌توانم به شما کمک کنم؟"
    print(detect_language(text))
