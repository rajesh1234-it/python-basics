# hangman game

import random  # For selecting a random word from the list

# Function to get a random word from a predefined list
def get_random_word():
    words = ['python', 'developer', 'hangman', 'programming', 'function', 'variable']
    return random.choice(words)

# Function to display the hangman figure based on remaining tries
def display_hangman(tries):
    stages = [
        # Final state: full hangman
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        # Initial empty gallows
        '''
           -----
           |   |
               |
               |
               |
               |
        =========
        '''
    ]
    return stages[tries]  # Return the appropriate stage for current tries

# Main function to run the Hangman game
def play_hangman():
    word = get_random_word()                # Random word to guess
    word_letters = set(word)                # Unique letters in the word
    guessed_letters = set()                 # Letters the user has guessed
    tries = 6                               # Number of incorrect tries allowed

    print("Welcome to Hangman!")
    print(display_hangman(tries))

    # Game loop
    while tries > 0 and word_letters:
        # Show current state of the word
        print(f"\nWord: {' '.join([letter if letter in guessed_letters else '_' for letter in word])}")
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        # If letter already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
        # If guess is correct
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print("Good guess!")
        # If guess is wrong
        else:
            guessed_letters.add(guess)
            tries -= 1
            print("Wrong guess.")

        print(display_hangman(tries))  # Show updated hangman

    # Win or lose message
    if not word_letters:
        print(f"Congratulations!you win, You guessed the word '{word}' correctly.")
    else:
        print(f"Game over! you loose, The word was '{word}'.")

# Start the game
if __name__ == "__main__":
    play_hangman()
