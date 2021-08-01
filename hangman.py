import random
from words import words
import string

def valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    random_word = valid_word(words)
    word_letters = set(random_word)     # set of unique letters in the word
    alphabets = set(string.ascii_uppercase)
    used_letters = set()    # to keep track of letters used already
    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print("You have used these letters: ", " ".join(used_letters))
        word_print = [letter if letter in used_letters else "-" for letter in random_word]
        print("The word is: ", " ".join(word_print))
        print(f"Lives left: {lives}")

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1

        elif user_letter in used_letters:
            print(f"You have already guessed {user_letter}")
        else:
            print("Invalid input!")

    if lives == 0:
        print(f"You lost! The word was {random_word}")
    else:
        print(f"You guessed the word: {random_word}!!")

hangman()