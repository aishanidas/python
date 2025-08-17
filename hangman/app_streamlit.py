import streamlit as st


# --- Game Data ---
word = "PYTHON"
guessed = st.session_state.get("guessed", [])
wrong = st.session_state.get("wrong", [])

# --- Input ---
st.title("🎯 Hangman Game")
st.text("Guess the Word!")
display = [letter if letter in guessed else "_" for letter in word]
#display = [' _ ',' _ ',' _ ',' _ ',' _ ',' _ ']
st.text(" ".join(display))

guess = st.text_input("Enter a letter", max_chars=1).upper()
if guess and guess not in guessed:
    if guess in word:
        guessed.append(guess)
    else:
        wrong.append(guess)

st.session_state.guessed = guessed
st.session_state.wrong = wrong

# --- Game State ---
if set(guessed) >= set(word):
    st.success("🎉 You guessed the word!")
elif len(wrong) >= 6:
    st.error("💀 You lost! The word was " + word)
else:
    st.write(f"❌ Wrong guesses: {', '.join(wrong)}")

