import streamlit as st
import random

# Function to generate a random number between 1 and 100
def generate_random_number():
    return random.randint(1, 100)

# Function to play the number guessing game
def play_game(secret_number, guessed_number):
    if guessed_number < secret_number:
        return "Too low! Try a higher number."
    elif guessed_number > secret_number:
        return "Too high! Try a lower number."
    else:
        return "Congratulations! You guessed the correct number."

# Streamlit app
def main():
    st.title("Number Guessing Game")

    # Use a session state to maintain the state across runs
    session_state = st.session_state

    # Initialize session state variables if they don't exist
    if 'secret_number' not in session_state:
        session_state.secret_number = generate_random_number()

    # User input for guessing the number
    guessed_number = st.number_input("Guess the number (between 1 and 100):", min_value=1, max_value=100, key="guess_input")

    # Play the game and display the result
    result = play_game(session_state.secret_number, guessed_number)
    st.write(result)

if __name__ == "__main__":
    main()
