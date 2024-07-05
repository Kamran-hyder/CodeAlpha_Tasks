import random
import hangman_stages
import words

game_over = False
lives = 6
display = []

name = input("\nMay I know your name: ")

print(f"\n{name}, Welcome to Hangman Game")
print("\nIn this game, You have to save the hangman by guessing the word")

chosen_word = random.choice(words.words)

print(f"\n{chosen_word}\n") #apple

for i in range(len(chosen_word)): #0 1 2 3 4
    display += '_'

print(display)

while not game_over:
    guessed_letter = input("\nGuess a letter: ").lower() #r

    for position in range(len(chosen_word)): #0 1 2 3 4
        letter = chosen_word[position]

        if letter == guessed_letter:
            display[position] = guessed_letter

    print(display)
    
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("\nYou lose!!")
            print(f"\nThe word was {chosen_word}")

    if '_' not in display:
        game_over = True
        print("\nYou Win!!")
        print(f"\nYou're Right, The word is {chosen_word}")
    print(hangman_stages.hangman[lives])