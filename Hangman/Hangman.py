import random
import string
from Words import possible_words

def get_valid_word(possible_words):
    chosen_word = random.choice(possible_words)
    while '-' in chosen_word or ' ' in chosen_word:
         chosen_word = random.choice(possible_words)
    return(chosen_word).upper()

def hangman():
     lives = 6
     chosen_word = get_valid_word(possible_words)
     chosen_word_letters = set(chosen_word)
     alphabet = set(string.ascii_uppercase)
     used_letters = set()  #What the user has guessed    [0, 3 , 4 ]
     while len(chosen_word_letters) > 0 and lives > 0:     
         print("You have already used these letters: ", " ".join(used_letters)) #What the user already guessed
         #What the word currently looks like (e.g. W - R D)
         word_list = [letter if letter in used_letters else "-" for letter in chosen_word]
         print("Current word is: ", " ".join(word_list))
         user_letter = input("Please select a letter: ").upper()  #Collecting user input
         if user_letter in alphabet - used_letters:
             used_letters.add(user_letter)
             if user_letter in chosen_word_letters:
                chosen_word_letters.remove(user_letter)
             else:
                lives = lives - 1
                print(f"You've lost a life! You have {lives} left.")

         elif user_letter in used_letters:
                print("You have already used this letter. Please insert a different letter.")
         else:
                print("Invalid character, please try again.")
     if lives == 0 :
        print(f"You don't have anymore lives left! The word was {chosen_word}. Better luck next time!")
     else:
        print(f"Grats, you've guessed the word! The word was {chosen_word}!")


hangman()
    
          
     



