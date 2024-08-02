# Memory Match Game User Manual

## Introduction

Welcome to the Memory Match Game! This simple yet engaging game is designed to test your memory and concentration skills. The objective of the game is to find all the matching pairs of cards by remembering their locations. The game offers different themes, difficulty levels, and even a timer to challenge you further.

## Installation

To play the Memory Match Game, you need to have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can install the game's dependencies by running the following command in your terminal or command prompt:

```
pip install -r requirements.txt
```

## Starting the Game

To start the game, open a terminal or command prompt and navigate to the directory where you have saved the game files. Run the following command to start the game:

```
python main.py
```

## Main Menu

When you start the game, you will see the Main Menu window. The Main Menu provides several options for you to choose from:

- **Title**: The game title is displayed prominently at the top of the window.

- **Play button**: Clicking this button takes you to the "Select Difficulty" window, where you can choose the difficulty level and start the game.

- **High scores button**: Clicking this button opens a window displaying the high scores from previous games. The high scores include the player's name, score, and time.

- **Settings button**: Clicking this button leads to a settings window where you can adjust sound preferences, choose themes, and view game instructions.

- **Exit button**: Clicking this button allows you to exit the game.

## Select Difficulty

In the "Select Difficulty" window, you can choose the difficulty level for the game. The difficulty level determines the size of the game grid and the number of cards to match. The available difficulty levels are:

- **Easy**: 4x4 grid, 8 cards to match.

- **Medium**: 6x6 grid, 18 cards to match.

- **Hard**: 8x8 grid, 32 cards to match.

To choose a difficulty level, click on the corresponding button. Once you have selected a difficulty level, the game will start automatically.

## Game Window

The Game Window is where the Memory Match game is played. It consists of the following components:

- **Game grid**: The central area where the cards are displayed. The grid size and number of cards depend on the chosen difficulty level.

- **Score panel**: A panel displaying the current number of attempts, number of matches found, and the elapsed time.

- **Pause/Menu Button**: Clicking this button pauses the game and opens a small menu with options to resume, restart, change difficulty, or return to the Main Menu.

## Settings Window

The Settings Window allows you to customize various aspects of the game. It includes the following options:

- **Sound settings**: Toggle switches for game sound effects and background music.

- **Theme selection**: Dropdown menu or buttons to select the card and background theme.

- **Instructions**: A section that outlines the game rules and controls.

- **Back button**: Clicking this button saves any changes and returns to the Main Menu.

## High Scores Window

The High Scores Window displays the top scores from previous games. It includes the following information:

- **Scores display**: A list or table displaying the player's name, score (based on attempts and time), and difficulty level.

- **Clear scores button**: Clicking this button clears the high score history.

- **Back button**: Clicking this button returns to the Main Menu.

## Game Over/Win Window

When you complete the game by finding all the matching pairs, the Game Over/Win Window is displayed. It includes the following options:

- **Message**: Displays a congratulatory message for completing the game and shows the final score and time.

- **Play Again Button**: Clicking this button restarts the game at the same difficulty level.

- **Change Difficulty Button**: Clicking this button returns you to the "Select Difficulty" window to choose a new difficulty level.

- **Main Menu Button**: Clicking this button returns you to the Main Menu.

## Additional Features

The Memory Match Game includes additional features to enhance your gaming experience:

- **Shuffle and random placement**: The game shuffles and randomly places the cards at the start of each game.

- **Card flipping**: You can flip cards and reveal their faces by clicking on them.

- **Matching check**: The game checks for matches when two cards are flipped. If they match, the cards remain face up. Otherwise, they are flipped back.

- **Attempts and matches tracking**: The game keeps track of the number of attempts made and matches found.

- **Win condition**: The game implements a win condition when all matches are found.

- **Difficulty levels**: The game provides three levels of difficulty: Easy, Medium, and Hard. The difficulty level affects the grid size and the number of cards to match.

## Conclusion

Congratulations! You are now ready to enjoy the Memory Match Game. Have fun testing your memory and concentration skills, and try to beat your own high scores!