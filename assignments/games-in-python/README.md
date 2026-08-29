
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditional logic, and user input. This assignment will help you practice tracking game state, validating guesses, and creating a playable command-line game.

## 📝 Tasks

### 🛠️ Build the Core Game Loop

#### Description
Create a simple Hangman game where the player guesses letters to reveal a hidden word before they run out of chances.

#### Requirements
Completed program should:

- Use a predefined list of words and randomly choose one for each game
- Display the hidden word in a masked format such as `_ _ _ _`
- Prompt the player to enter one letter at a time
- Reveal correctly guessed letters in the right positions
- Track the number of incorrect guesses remaining
- Prevent duplicate guesses and handle invalid input gracefully

### 🛠️ Finalize Win/Loss Logic

#### Description
Add the logic that ends the game when the player wins or loses and clearly communicates the outcome.

#### Requirements
Completed program should:

- End the game when the word is fully guessed
- End the game when the player runs out of attempts
- Display a win message when the word is guessed correctly
- Display a lose message with the correct word when attempts are exhausted
- Print the final result in a friendly, readable format

Example gameplay:

```python
Word: _ _ a _
Guess a letter: a
Correct! Remaining attempts: 5

Word: _ a _ _
Guess a letter: e
Incorrect! Remaining attempts: 4
```
