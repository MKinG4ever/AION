from process import preprocess_text
from response import classify_intent, generate_response
from detect import detect_language
from names import extract_names


def main():
    user_input = input("You: ")
    language = detect_language(user_input)

    if language == 'unknown':
        print("Sorry, I can't detect the language.")
        return

    preprocessed_text = preprocess_text(user_input, language)
    intent = classify_intent(" ".join(preprocessed_text))
    response = generate_response(intent)

    # Extract names from the user input
    names = extract_names(user_input)
    if names:
        response += f" By the way, nice to meet you {', '.join(names)}!"

    print(f"Bot: {response}")


if __name__ == "__main__":
    while True:
        main()
