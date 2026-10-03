import streamlit as st

from simplifier import simplify_sentence


# Page configuration
st.set_page_config(
    page_title="English Sentence Simplifier",
    page_icon="📖",
    layout="centered"
)


# Title
st.title("📖 English Sentence Simplifier")

st.write(
    "Enter a difficult English sentence and get a simpler version."
)


# Text input
sentence = st.text_area(
    "Enter your sentence:",
    placeholder="Example: The implementation facilitates communication between devices."
)


# Button
if st.button("✨ Simplify Sentence"):

    if sentence.strip() == "":
        st.warning("Please enter a sentence.")

    else:

        # Simplify sentence
        simplified_sentence, difficult_words = simplify_sentence(sentence)


        # Original sentence
        st.subheader("Original Sentence")
        st.write(sentence)


        # Difficult words
        st.subheader("Difficult Words")

        if difficult_words:
            st.write(", ".join(difficult_words))
        else:
            st.write("No difficult words detected.")


        # Simplified sentence
        st.subheader("Simplified Sentence")
        st.success(simplified_sentence)