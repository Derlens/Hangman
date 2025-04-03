#Derlens Fadael
#Python Programming in ECE
#Mini-Project
#3/30/205

import random

# Game state variables
secret_word = ""
words_guessed = []
mistakes_made = 0
max_guesses = 6
players = []
current_player = ""

def load_words(filename):
    """Load words from a file and return a list of words."""
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            if words:
                     return (words)
            else:
                 return None 
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return None
    except Exception as e:
         print(f"An error occurred: {e}")
         return 

def choose_word(word_list):
    """Choose a random word from the list."""
    return random.choice(word_list)

def display_word(secret_word):
    """Display the word with guessed letters revealed."""
    return ' '.join(word if word in words_guessed else 'X' for word in secret_word)

def switch_player():
    """Switch to another player who has not played yet."""
    global current_player, mistakes_made
    remaining_players = [player for player in players if player != current_player]
    if remaining_players:
        current_player = random.choice(remaining_players)
        mistakes_made = 0
        print(f"Switching to next Player: {current_player}")
    else:
        print("All players have played. Game over!")
        exit()

def hangman():
    global secret_word, words_guessed, mistakes_made, current_player, players
    words = load_words('words.txt')
    

    print("\n                  Welcome to Hangman!\n")

    while True:
        num_players = input("Enter the number of player(s): ")
        if num_players.isdigit():
                num_players = int(num_players)
                break
        else:
             print("Invalid input! Please enter an integer.\n")
        
    players = [input(f"Enter name of Player {i+1}: ") for i in range(num_players)]
    current_player = random.choice(players)
    print(f"First player: {current_player}")
    
    while True:
        secret_word = choose_word(words)  

        print(f"\nCurrent Player: {current_player}")
        print(f"Mistakes left: {max_guesses - mistakes_made}")
        print(f"Guessed words: {', '.join(words_guessed)}")
        print(f"Hidden word: {display_word(secret_word)}")
        
        guess = input("Guess a word: ").lower()
        
        if len(guess) == 1 or not guess.isalpha():
            print("Please enter a word.")
            continue
        
        if guess in words_guessed:
            print("You already guessed that word.")
            continue
        
        words_guessed.append(guess)
        
        if guess == secret_word:
            print("Good guess!")
        else:
            mistakes_made += 1
            print("Wrong guess!")
            print(f"The hidden word was: {secret_word}")
        
        if all(word in words_guessed for word in secret_word):
            print(f"Congratulations {current_player}! You guessed the word: {secret_word}")
            break
        
        if mistakes_made >= max_guesses:
            print(f"\n                  ---GAME OVER!---\n{current_player} has reached max mistakes[6]. The word was: {secret_word}\n")
            while True:
                Choosing_Next__Player = input("\nDo you wish to continue with the next player?[Yes|No]: ").lower()
                if Choosing_Next__Player in ['y','n','yes','no']:
                   break
                else:
                     print("Invalid input")
                
            if Choosing_Next__Player == 'y' or 'yes':
               print(f"\nSwitching Player...\n")
               switch_player()
            elif Choosing_Next__Player == 'n' or 'no':
               print("Please, try again at any moment!")
               exit()
    

if __name__ == "__main__":
    hangman()
