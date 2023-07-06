import random

# Create a list of 5 letter words
words = ["apple", "banana", "cherry", "date", "elder"]

# Choose a random word from the list
word = random.choice(words)

# Shuffle the letters of the word
letters = list(word)
random.shuffle(letters)

# Print the shuffled letters
print("".join(letters))

# Prompt the user to guess the original word
guess = input("Guess the original word: ")

# Check if the guess is correct
if guess == word:
  print("Correct!")
else:
  print("Incorrect. The correct word was:", word)
