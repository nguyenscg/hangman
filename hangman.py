import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Print it

chosen_word = random.choice(word_list) # this should return an element from the list 'word_list'
print(chosen_word)

# Ask the user to guess a letter and assign their answer to variable called guess. Make the String stored in guess lowercase.
guess = input("Guess a letter: ").lower()
print(guess)

# Check if the letter the user guessed guess is one of the letters in the chosen_word. Loop through each of the letters in the chosen_word and print "Right" if the letter is a match, "Wrong" if it's not
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")