# Memory Match Game User Manual

## Introduction

Welcome to the Memory Match Game! This simple yet engaging game is designed to test your memory and concentration skills. The objective of the game is to find all the matching pairs of cards by remembering their locations. The game offers different themes, difficulty levels, and even a timer to challenge you further.

## Installation

To play the Memory Match Game, you need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you can install the game's dependencies by running the following command in your terminal or command prompt:

```
pip install -r requirements.txt
```

## Starting the Game

To start the game, open a terminal or command prompt and navigate to the directory where you have downloaded the game files. Run the following command:

```
python main.py
```

This will launch the game's main menu window.

## Main Menu

The main menu window is the starting point of the game. It provides several options for you to choose from:

- **Title**: The game title is displayed prominently at the top of the window.

- **Play button**: Clicking this button takes you to the "Select Difficulty" window, where you can choose the difficulty level of the game.

- **High scores button**: Clicking this button opens a window displaying the high scores from previous games. The high scores include the player's name, score, and time.

- **Settings button**: Clicking this button leads you to a settings window where you can adjust sound preferences, choose themes, and view game instructions.

- **Exit button**: Clicking this button allows you to exit the game.

## Select Difficulty

In the "Select Difficulty" window, you can choose the difficulty level of the game. The difficulty level determines the size of the game grid and the number of cards to match. The window includes the following options:

- **Instruction text**: A brief instruction on how to select the difficulty level.

- **Difficulty level buttons**: Buttons for each difficulty level (Easy, Medium, Hard). Clicking on one sets the game's difficulty and starts the game.

- **Back button**: Clicking this button returns you to the main menu.

## Game Window

Once you have selected the difficulty level, the game window will appear. The game window consists of the following elements:

- **Game grid**: The central area where the cards are displayed according to the chosen difficulty level. The cards are arranged in a grid layout that changes size based on the difficulty.

- **Score panel**: A panel displaying the current number of attempts, number of matches found, and the elapsed time.

- **Pause/Menu Button**: Clicking this button pauses the game and opens a small menu with options to resume, restart, change difficulty, or return to the main menu.

## Settings Window

In the settings window, you can customize various aspects of the game. The settings window includes the following options:

- **Sound settings**: Toggle switches for game sound effects and background music.

- **Theme selection**: Dropdown menu or buttons to select the card and background theme.

- **Instructions**: A section that outlines the game rules and controls.

- **Back button**: Clicking this button saves any changes and returns you to the main menu.

## High Scores Window

The high scores window displays the top scores from previous games. It includes the following options:

- **Scores display**: A list or table displaying the top scores, including details such as player name, score (based on attempts and time), and difficulty level.

- **Clear scores button**: Clicking this button allows you to clear the high score history.

- **Back button**: Clicking this button returns you to the main menu.

## Game Over/Win Window

When you complete the game, the game over/win window will appear. It includes the following options:

- **Message**: Displays a congratulatory message for completing the game and shows the final score and time.

- **Play Again Button**: Clicking this button restarts the game at the same difficulty level.

- **Change Difficulty Button**: Clicking this button returns you to the "Select Difficulty" window to choose a new difficulty level.

- **Main Menu Button**: Clicking this button returns you to the main menu.

## Additional Features

The Memory Match Game includes some additional features to enhance your gaming experience:

- **Shuffle and random placement**: The game shuffles and randomly places the cards at the start of each game, ensuring a unique experience every time.

- **Card flipping**: You can flip the cards and reveal their faces by clicking on them.

- **Matching check**: The game checks for matches when two cards are flipped. If they match, the cards remain face up. Otherwise, they are flipped back.

- **Attempts and matches tracking**: The game keeps track of the number of attempts made and matches found.

- **Win condition**: The game implements a win condition when all matches are found.

- **Difficulty levels**: The game provides three levels of difficulty: Easy (4x4 grid), Medium (6x6 grid), and Hard (8x8 grid). The difficulty level affects the number of cards and matches that need to be found.

- **Themes and customization**: You can choose from different themes for the cards, such as animals, space, and plants. Themes can also change the background of the game board and the card designs.

Enjoy playing the Memory Match Game and have fun improving your memory skills!

```