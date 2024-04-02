import random

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_len = len(chosen_word)

end_of_games = False
lives = 6 # Number of lives the user has left.

# Import the logo from hangman_art.py 
from hangman_art import logo, stages 
print(logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')
 
# Create blanks
display = []
for _ in range(word_len):
    display += "_"

while not end_of_games:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")
        
    # Check guessed letter
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_games = True
            print("You lose.")
    
    if "_" not in display:
        end_of_games = True
        print("You win.")
    
    #Import the stages from hangman_art.py
    print(stages[lives])