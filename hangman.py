import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Print it

chosen_word = random.choice(word_list) # this should return an element from the list 'word_list'
print(chosen_word)

# Ask the user to guess a letter and assign their answer to variable called guess. Make the String stored in guess lowercase.
guess = input("Guess a letter: ").lower()
# print(guess)

# Check if the letter the user guessed guess is one of the letters in the chosen_word. Loop through each of the letters in the chosen_word and print "Right" if the letter is a match, "Wrong" if it's not
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# Create an empty string called placeholder
# placeholder = ""
# # for each letter in the chosen_word, add a _ to the placeholder
# for letter in chosen_word:
#     placeholder += "_"
# print(placeholder)


# create an empty string called 'display'
# loop through each letter in the chosen_word
# if the letter at that position matches guess then reveal that letter in the display at the position
# print display and you should see the guessed letter in the correct position
# but every letter that is not matched is represented with a '_'
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)