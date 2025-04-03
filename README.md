Hangman Game

Overview
This is a Python implementation of the classic word-guessing game Hangman. The game allows multiple players to take turns guessing a secret word, with a maximum of six incorrect guesses before the game ends.

Features
Supports multiple players

Loads words from an external file (words.txt)

Randomly selects a secret word for each round

Displays guessed letters and hidden portions of the word

Allows players to switch after reaching the maximum number of mistakes

Game Rules
The program selects a secret word from words.txt.

A player tries to guess the word by entering full words (not single letters).

If the guessed word matches the secret word, the player wins the round.

If the guessed word is incorrect, the mistake count increases.

Each player has a maximum of 6 incorrect guesses before switching to the next player.

The game continues until all players have played or a player wins.

Installation & Setup
Ensure you have Python 3 installed.

Clone or download this repository.

Prepare a words.txt file in the same directory, containing words for the game (one word per line).

Run the game with:

bash
Copy

Edit
python hangman.py
File Structure
hangman.py – Main script to run the game

words.txt – List of possible secret words

How to Play
Run the script.

Enter the number of players.

Each player takes turns guessing words.

The game ends when a player correctly guesses the word or all players run out of turns.

Future Enhancements
Improve the UI with ASCII art for Hangman

Add difficulty levels with different word lengths

Implement a scoring system
