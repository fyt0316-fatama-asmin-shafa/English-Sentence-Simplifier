import re


def clean_text(text):
    """
    Clean the input text.
    """

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove spaces before punctuation
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)

    # Remove leading and trailing spaces
    text = text.strip()

    return text


def tokenize_text(text):
    """
    Split the sentence into words.
    """

    cleaned_text = clean_text(text)

    words = cleaned_text.split()

    return words


def preprocess_text(text):
    """
    Complete preprocessing pipeline.
    """

    cleaned_text = clean_text(text)

    words = tokenize_text(cleaned_text)

    return cleaned_text, words