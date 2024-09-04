import streamlit as st
from googletrans import Translator

# Function to enqueue an item
def enq(item, que):
    que.append(item)

# Function to dequeue an item
def deq(que):
    if len(que) == 0:
        return None
    return que.pop(0)

# Function to translate text using Google Translate
def trans(sentence, translater, dest_lang):
    # Translate the entire sentence to maintain correct syntax
    translated_sentence = translater.translate(sentence, dest=dest_lang).text
    return translated_sentence

# Streamlit main function
def main():
    st.title("Language Translator with Data Structure")

    # Text input from the user
    text = st.text_input("Enter Text to Translate:")

    # Language selection
    languages = {
        "Tamil": "ta",
        "Telugu": "te",
        "Hindi": "hi",
        "Malayalam": "ml",
        "Kannada": "kn",
        "English": "en"
    }

    selected_lang = st.selectbox("Select the Output Language:", list(languages.keys()))

    if st.button("Translate"):
        if text:
            translator = Translator()

            # Queue for translated words
            queue = []

            try:
                # Translate the entire text
                translated_sentence = trans(text, translator, languages[selected_lang])

                # Enqueue each translated word into the queue
                for word in translated_sentence.split():
                    enq(word, queue)

                # Dequeue and construct the final translated output
                translated_output = []
                while len(queue) > 0:
                    translated_output.append(deq(queue))

                # Display the final translated text
                st.text_area("Translated Text:", " ".join(translated_output))

            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please enter text to translate.")

if __name__ == "__main__":
    main()
