# Memory Match Game User Manual

## Introduction

Welcome to the Memory Match Game! This simple yet engaging game challenges your memory and concentration skills. The objective of the game is to find all the matching pairs of cards by remembering their locations. The game features different difficulty levels, themes, and a timer to make it more challenging and enjoyable.

## Installation

To play the Memory Match Game, you need to install the following dependencies:

- Python 3.x
- Tkinter library

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

The main menu window is the starting point of the game. It provides several options for the player:

- Title: The game title is displayed prominently at the top of the window.
- Play button: Clicking this button takes the player to the "Select Difficulty" window.
- High scores button: Opens a window displaying the high scores from previous games, including the player's name, score, and time.
- Settings button: Leads to a settings window where players can adjust sound preferences, choose themes, and view game instructions.
- Exit button: Clicking this button exits the game.

## Select Difficulty

In the "Select Difficulty" window, the player can choose the difficulty level for the game. The window includes the following options:

- Instruction text: A brief instruction on how to select the difficulty level.
- Difficulty level buttons: Buttons for each difficulty level (Easy, Medium, Hard). Clicking on one sets the game's difficulty and starts the game.
- Back button: Returns to the Main Menu.

## Game Window

The game window is where the Memory Match Game is played. It includes the following elements:

- Game grid: The central area where the cards are displayed according to the chosen difficulty level. Cards are arranged in a grid layout that changes size based on the difficulty.
- Score panel: A panel displaying the current number of attempts, number of matches found, and the elapsed time.
- Pause/Menu Button: Pauses the game and opens a small menu with options to resume, restart, change difficulty, or return to the Main Menu.

## Settings Window

The settings window allows players to customize their game experience. It includes the following options:

- Sound settings: Toggle switches for game sound effects and background music.
- Theme selection: Dropdown menu or buttons to select the card and background theme.
- Instructions: A section that outlines the game rules and controls.
- Back button: Saves any changes and returns to the Main Menu.

## High Scores Window

The high scores window displays the top scores from previous games. It includes the following options:

- Scores display: A list or table displaying the top scores, including details such as player name, score (based on attempts and time), and difficulty level.
- Clear scores button: An option to clear the high score history.
- Back button: Returns to the Main Menu.

## Game Over/Win Window

The game over/win window appears when the player completes the game. It includes the following options:

- Message: Displays a congratulatory message for completing the game and shows the final score and time.
- Play Again Button: Restarts the game at the same difficulty level.
- Change Difficulty Button: Returns the player to the "Select Difficulty" window to choose a new difficulty level.
- Main Menu Button: Returns to the Main Menu.

## Additional Features

The Memory Match Game includes additional features to enhance the gameplay experience:

- Game logic: The game has the ability to shuffle and randomly place the cards at the start of each game.
- Difficulty levels: The game provides three levels of difficulty (Easy, Medium, Hard) with different grid sizes and numbers of cards.
- Themes and customization: Players can choose from different themes for the cards, which change the background of the game board and the card designs.
- Score and timing: The game includes a timer to track how long it takes for the player to complete the game. The player's score is based on the number of attempts made and the time taken.
- Settings and controls: Players can restart the game, change difficulty levels, and switch themes without restarting the application. Sound effects can be enabled or disabled.
- Development considerations: The game implements data persistence for high scores and settings using local storage or a simple file-based approach.

## Bonus Features

The Memory Match Game also includes some bonus features to further enhance the gameplay experience:

- Multiplayer mode: Two players can take turns to find matches.
- Animations: The game includes animations for flipping cards and winning the game.
- Leaderboards: The game implements leaderboards for high scores among different players.

## Accessibility

The Memory Match Game is designed to be accessible to all players. It includes the following accessibility features:

- Keyboard navigation: Full functionality can be accessed via keyboard shortcuts to ensure that users who cannot use a mouse can navigate efficiently through the application.
- Tab navigation: Interactive elements are ordered logically for easy navigation using the Tab key.

Enjoy playing the Memory Match Game and have fun improving your memory skills!