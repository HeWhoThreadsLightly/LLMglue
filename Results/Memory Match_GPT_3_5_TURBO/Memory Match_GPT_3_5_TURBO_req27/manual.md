# Memory Match Game User Manual

## Introduction

Welcome to the Memory Match Game! This simple yet engaging game will test your memory and concentration skills. The objective of the game is to find all the matching pairs of cards by remembering their locations. The game can be played on your desktop and offers different themes, difficulty levels, and even a timer to challenge yourself further.

## Installation

To play the Memory Match Game, you need to install the following dependencies:

- Python (version 3.6 or higher)
- Tkinter library (included in Python standard library)

You can install the required dependencies by following these steps:

1. Open your command prompt or terminal.
2. Run the following command to install the dependencies:

   ```
   pip install -r requirements.txt
   ```

   If you are using Anaconda, you can use the following command instead:

   ```
   conda install --file requirements.txt
   ```

3. Wait for the installation to complete.

## Starting the Game

To start the Memory Match Game, follow these steps:

1. Open your command prompt or terminal.
2. Navigate to the directory where the game files are located.
3. Run the following command to start the game:

   ```
   python main.py
   ```

4. The game's main menu window will appear.

## Main Menu

The main menu window is the starting point of the game. It provides several options for you to choose from:

- **Title**: The game title is displayed prominently at the top of the window.
- **Play button**: Clicking this button takes you to the "Select Difficulty" window.
- **High scores button**: Opens a window displaying the high scores from previous games, including the player's name, score, and time.
- **Settings button**: Leads to a settings window where you can adjust sound preferences, choose themes, and view game instructions.
- **Exit button**: Clicking this button exits the game.

## Select Difficulty

The "Select Difficulty" window allows you to choose the difficulty level of the game. Follow these steps to select the difficulty level:

1. From the main menu, click the "Play" button.
2. The "Select Difficulty" window will appear.
3. Read the instruction text to understand how to select the difficulty level.
4. Click on one of the difficulty level buttons (Easy, Medium, Hard) to set the game's difficulty and start the game.
5. If you want to go back to the main menu, click the "Back" button.

## Game Window

The game window is where the Memory Match Game is played. It consists of the following components:

- **Game grid**: The central area where the cards are displayed according to the chosen difficulty level. The cards are arranged in a grid layout that changes size based on the difficulty.
- **Score panel**: A panel displaying the current number of attempts, number of matches found, and the elapsed time.
- **Pause/Menu Button**: Pauses the game and opens a small menu with options to resume, restart, change difficulty, or return to the main menu.

## Settings Window

The settings window allows you to customize various aspects of the game. It includes the following options:

- **Sound settings**: Toggle switches for game sound effects and background music.
- **Theme selection**: Dropdown menu or buttons to select the card and background theme.
- **Instructions**: A section that outlines the game rules and controls.
- **Back button**: Saves any changes and returns to the main menu.

## High Scores Window

The high scores window displays the top scores from previous games. It includes the following features:

- **Scores display**: A list or table displaying the top scores, including details such as player name, score (based on attempts and time), and difficulty level.
- **Clear scores button**: An option to clear the high score history.
- **Back button**: Returns to the main menu.

## Game Over/Win Window

The game over/win window appears when you complete the game. It includes the following options:

- **Message**: Displays a congratulatory message for completing the game and shows the final score and time.
- **Play Again Button**: Restarts the game at the same difficulty level.
- **Change Difficulty Button**: Returns you to the "Select Difficulty" window to choose a new difficulty level.
- **Main Menu Button**: Returns you to the main menu.

## Additional Features

The Memory Match Game includes additional features to enhance your gaming experience:

- **Game logic**: The game has the ability to shuffle and randomly place the cards at the start of each game.
- **Game logic**: You can flip cards and reveal their faces when clicked.
- **Game logic**: The game checks for matches when two cards are flipped. If they match, they remain face up; otherwise, they are flipped back.
- **Game logic**: The game keeps track of the number of attempts made and matches found.
- **Game logic**: The game implements a win condition when all matches are found.

## Conclusion

Congratulations! You are now ready to enjoy the Memory Match Game. Have fun testing your memory and concentration skills, and don't forget to challenge yourself with different difficulty levels and themes. Good luck!