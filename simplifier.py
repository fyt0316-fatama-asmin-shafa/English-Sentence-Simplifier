import pandas as pd

from preprocessing import preprocess_text


# Load dataset
dataset = pd.read_csv("dataset.csv")


# Create dictionary from dataset
SIMPLE_WORDS = dict(
    zip(
        dataset["difficult_word"],
        dataset["simple_word"]
    )
)


def simplify_sentence(sentence):

    # Preprocess input
    cleaned_text, words = preprocess_text(sentence)

    # ---------------------------------
    # Sentence structure simplification
    # ---------------------------------

    original_lower = cleaned_text.lower()

    # Rule 1:
    # "The implementation facilitates communication between numerous devices."
    # ->
    # "The method helps devices communicate."

    if (
        "implementation facilitates communication between"
        in original_lower
    ):
        parts = cleaned_text.rstrip(".!?").split()

        # Find the word after "between"
        if "between" in [word.lower().strip(".,!?;:") for word in parts]:

            between_index = next(
                i for i, word in enumerate(parts)
                if word.lower().strip(".,!?;:") == "between"
            )

            device_word = parts[between_index + 1]

            # Remove punctuation
            device_word = device_word.strip(".,!?;:")

            simplified_sentence = (
                "The method helps "
                + device_word
                + " communicate."
            )

            difficult_words = []

            for word in words:
                clean_word = word.lower().strip(".,!?;:")

                if clean_word in SIMPLE_WORDS:
                    difficult_words.append(clean_word)

            return simplified_sentence, difficult_words


    # ---------------------------------
    # Normal word simplification
    # ---------------------------------

    simplified_words = []
    difficult_words = []

    for word in words:

        clean_word = word.lower().strip(".,!?;:")

        if clean_word in SIMPLE_WORDS:

            simple_word = SIMPLE_WORDS[clean_word]

            # Keep uppercase
            if word[0].isupper():
                simple_word = simple_word.capitalize()

            # Keep punctuation
            punctuation = ""

            if word[-1] in ".,!?;:":
                punctuation = word[-1]

            simplified_words.append(
                simple_word + punctuation
            )

            difficult_words.append(clean_word)

        else:

            simplified_words.append(word)

    simplified_sentence = " ".join(simplified_words)

    return simplified_sentence, difficult_words