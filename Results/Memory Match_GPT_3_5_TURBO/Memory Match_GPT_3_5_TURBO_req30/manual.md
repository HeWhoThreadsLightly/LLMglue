# Memory Match Game User Manual

## Introduction

Welcome to the Memory Match Game! This simple yet engaging game challenges your memory and concentration skills. The objective of the game is to find all the matching pairs of cards by remembering their locations. The game offers different difficulty levels, themes, and even a timer to make it more challenging.

## Installation

To play the Memory Match Game, you need to install Python and the required dependencies. Follow the steps below to get started:

1. Install Python: If you don't have Python installed on your computer, download and install it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Install dependencies: Open a terminal or command prompt and navigate to the project directory. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Starting the Game

To start the Memory Match Game, follow the steps below:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the following command to start the game:

   ```
   python main.py
   ```

3. The game will open in a new window.

## Main Menu

The Main Menu is the starting point of the game. It provides options to start the game, view high scores, adjust settings, and exit the game.

### Play Button (REQ2)

Clicking the "Play" button takes you to the "Select Difficulty" window, where you can choose the difficulty level for the game.

### High Scores Button (REQ3)

Clicking the "High Scores" button opens a window displaying the high scores from previous games. The high scores include the player's name, score, and time.

### Settings Button (REQ4)

Clicking the "Settings" button opens a window where you can adjust sound preferences, choose themes, and view game instructions.

### Exit Button (REQ5)

Clicking the "Exit" button closes the game.

## Select Difficulty Window

The Select Difficulty window allows you to choose the difficulty level for the game.

### Difficulty Level Buttons (REQ7)

The window displays buttons for each difficulty level: Easy, Medium, and Hard. Clicking on a button sets the game's difficulty and starts the game.

### Back Button (REQ8)

Clicking the "Back" button returns you to the Main Menu.

## Game Window

The Game Window is where the game is played. It consists of a game grid and a score panel.

### Game Grid (REQ9)

The game grid is the central area where the cards are displayed. The grid layout changes size based on the chosen difficulty level. Each card is initially face down.

### Score Panel (REQ10)

The score panel displays the current number of attempts, the number of matches found, and the elapsed time.

### Pause/Menu Button (REQ11)

Clicking the "Pause/Menu" button pauses the game and opens a small menu with options to resume, restart, change difficulty, or return to the Main Menu.

## Settings Window

The Settings Window allows you to adjust various game settings.

### Sound Settings (REQ12)

Toggle switches are provided to enable or disable game sound effects and background music.

### Theme Selection (REQ13)

You can choose different themes for the cards and background. Themes include animals, space, and plants.

### Instructions (REQ14)

The Instructions section provides a brief overview of the game rules and controls.

### Back Button (REQ15)

Clicking the "Back" button saves any changes and returns you to the Main Menu.

## High Scores Window

The High Scores Window displays the top scores from previous games.

### Scores Display (REQ16)

The window shows a list or table of the top scores, including player name, score (based on attempts and time), and difficulty level.

### Clear Scores Button (REQ17)

Clicking the "Clear Scores" button clears the high score history.

### Back Button (REQ18)

Clicking the "Back" button returns you to the Main Menu.

## Game Over/Win Window

The Game Over/Win Window is displayed when the game is completed.

### Message (REQ19)

The window displays a congratulatory message for completing the game, along with the final score and time.

### Play Again Button (REQ20)

Clicking the "Play Again" button restarts the game at the same difficulty level.

### Change Difficulty Button (REQ21)

Clicking the "Change Difficulty" button returns you to the "Select Difficulty" window to choose a new difficulty level.

### Main Menu Button (REQ22)

Clicking the "Main Menu" button returns you to the Main Menu.

## Additional Features

The Memory Match Game includes additional features to enhance gameplay.

### Game Logic

The game logic includes the ability to shuffle and randomly place the cards at the start of each game (REQ23). You can flip cards and reveal their faces when clicked (REQ24). The game checks for matches when two cards are flipped and leaves them face up if they match; otherwise, it flips them back (REQ25). The game keeps track of the number of attempts made and matches found (REQ26). A win condition is implemented when all matches are found (REQ27).

### Difficulty Levels

The game offers three levels of difficulty: Easy (4x4 grid), Medium (6x6 grid), and Hard (8x8 grid) (REQ28). The difficulty level affects the number of cards and matches that need to be found (REQ29).

### Themes and Customization

You can choose from different themes for the cards, such as animals, space, and plants (REQ30).

## Conclusion

Enjoy playing the Memory Match Game! Challenge yourself to find all the matching pairs and achieve high scores. Have fun and exercise your memory skills!