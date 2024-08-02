# Memory Match Game User Manual

## Introduction

Welcome to the Memory Match Game! This simple yet engaging game is designed to test your memory skills. The objective of the game is to find all the matching pairs of cards by remembering their locations. The game offers different themes, difficulty levels, and even a timer to challenge you further.

## Installation

To play the Memory Match Game, you need to install the following dependencies:

- Python (version 3.6 or higher)
- Tkinter library (version 8.6)

You can install the dependencies by running the following command:

```
pip install -r requirements.txt
```

## Starting the Game

To start the game, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the game files are located.
3. Run the following command:

```
python main.py
```

4. The main menu window will appear.

## Main Menu

The main menu window is the starting point of the game. It provides several options for you to choose from:

- **Title**: The game title is displayed prominently at the top of the window.
- **Play button**: Clicking this button takes you to the "Select Difficulty" window.
- **High scores button**: Opens a window displaying the high scores from previous games, including the player's name, score, and time.
- **Settings button**: Leads to a settings window where you can adjust sound preferences, choose themes, and view game instructions.
- **Exit button**: Clicking this button exits the game.

## Select Difficulty

In the "Select Difficulty" window, you can choose the difficulty level of the game. Follow these steps:

1. Click on one of the difficulty level buttons (Easy, Medium, Hard).
2. The game's difficulty will be set, and the game will start.

## Game Window

The game window is where the actual gameplay takes place. It consists of the following elements:

- **Game grid**: The central area where the cards are displayed according to the chosen difficulty level. The cards are arranged in a grid layout that changes size based on the difficulty.
- **Score panel**: A panel displaying the current number of attempts, number of matches found, and the elapsed time.
- **Pause/Menu Button**: Pauses the game and opens a small menu with options to resume, restart, change difficulty, or return to the Main Menu.

## Settings Window

The settings window allows you to customize various aspects of the game. It includes the following options:

- **Sound settings**: Toggle switches for game sound effects and background music.
- **Theme selection**: Dropdown menu or buttons to select the card and background theme.
- **Instructions**: A section that outlines the game rules and controls.
- **Back button**: Saves any changes and returns to the Main Menu.

## High Scores Window

The high scores window displays the top scores from previous games. It includes the following features:

- **Scores display**: A list or table displaying the top scores, including details such as player name, score (based on attempts and time), and difficulty level.
- **Clear scores button**: An option to clear the high score history.
- **Back button**: Returns to the Main Menu.

## Game Over/Win Window

When you complete the game, the game over/win window will appear. It includes the following options:

- **Message**: Displays a congratulatory message for completing the game and shows the final score and time.
- **Play Again Button**: Restarts the game at the same difficulty level.
- **Change Difficulty Button**: Returns you to the "Select Difficulty" window to choose a new difficulty level.
- **Main Menu Button**: Returns you to the Main Menu.

## Additional Features

The Memory Match Game includes several additional features to enhance your gaming experience:

- **Game logic**: The game has the ability to shuffle and randomly place the cards at the start of each game.
- **Difficulty levels**: The game provides three levels of difficulty: Easy (4x4 grid), Medium (6x6 grid), and Hard (8x8 grid). The difficulty level affects the number of cards (and thus, the number of matches) that need to be found.
- **Themes and customization**: You can choose from different themes for the cards, such as animals, space, or plants. Themes can change the background of the game board and the card designs.
- **Score and timing**: The game includes a timer to track how long it takes for you to complete the game. You will be scored based on the number of attempts made and the time taken to complete the game. The game also implements a high score feature that saves your best scores.
- **Settings and controls**: The game provides options to restart the game, change difficulty levels, and switch themes without restarting the application.

## Conclusion

Congratulations! You are now ready to enjoy the Memory Match Game. Have fun testing your memory skills and challenging yourself with different themes and difficulty levels. Good luck!