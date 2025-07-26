import random

# List of 5 predefined words
word_list = ["apple", "robot", "chair", "snake", "candy"]

# Choose a random word from the list
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Create a blank display for the word
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Main game loop
while incorrect_guesses < max_guesses and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print(f"Incorrect guesses left: {max_guesses - incorrect_guesses}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess!")
        incorrect_guesses += 1


if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game over! The word was:", secret_word)




