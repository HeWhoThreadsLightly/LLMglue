# Memory Match Game User Manual

## Introduction

Welcome to the Memory Match Game! This is a simple yet engaging game where you need to find matching pairs of cards by remembering their locations. The game features different themes, difficulty levels, and a timer to challenge you further. This user manual will guide you through the installation process, explain the main functions of the game, and provide instructions on how to play.

## Installation

To play the Memory Match Game, you need to install the following dependencies:

- Python (version 3.6 or higher)
- Tkinter (version 8.6)

You can install the dependencies by running the following command:

```
pip install -r requirements.txt
```

## Starting the Game

To start the game, open a terminal or command prompt and navigate to the directory where the game files are located. Then, run the following command:

```
python main.py
```

This will launch the game and display the main menu window.

## Main Menu

The main menu window is the starting point of the game. It provides several options for you to choose from:

- **Title**: The game title is displayed prominently at the top of the window.
- **Play button**: Clicking this button takes you to the "Select Difficulty" window.
- **High scores button**: Opens a window displaying the high scores from previous games, including the player's name, score, and time.
- **Settings button**: Leads to a settings window where you can adjust sound preferences, choose themes, and view game instructions.
- **Exit button**: Clicking this button exits the game.

## Select Difficulty

The select difficulty window allows you to choose the difficulty level of the game. It provides the following options:

- **Instruction text**: A brief instruction on how to select the difficulty level.
- **Difficulty level buttons**: Buttons for each difficulty level (Easy, Medium, Hard). Clicking on one sets the game's difficulty and starts the game.
- **Back button**: Returns to the Main Menu.

## Game Window

The game window is where the main gameplay takes place. It consists of the following elements:

- **Game grid**: The central area where the cards are displayed according to the chosen difficulty level. Cards are arranged in a grid layout that changes size based on the difficulty.
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

The game over/win window is displayed when you complete the game. It includes the following options:

- **Message**: Displays a congratulatory message for completing the game and shows the final score and time.
- **Play Again Button**: Restarts the game at the same difficulty level.
- **Change Difficulty Button**: Returns you to the "Select Difficulty" window to choose a new difficulty level.
- **Main Menu Button**: Returns you to the Main Menu.

## Additional Features

The Memory Match Game includes several additional features to enhance your gaming experience:

- **Game logic**: The game has the ability to shuffle and randomly place the cards at the start of each game.
- **Difficulty levels**: There are three levels of difficulty (Easy, Medium, Hard) with different grid sizes and numbers of cards.
- **Themes and customization**: You can choose from different themes for the cards, which change the background of the game board and the card designs.
- **Score and timing**: The game includes a timer to track how long it takes for you to complete the game. Your score is based on the number of attempts made and the time taken.
- **Settings and controls**: You can restart the game, change difficulty levels, and switch themes without restarting the application. Sound effects can be enabled or disabled.
- **Data persistence**: The game saves high scores and settings using local storage or a simple file-based approach.
- **Bonus features**: There are bonus features such as multiplayer mode, animations for flipping cards and winning the game, and leaderboards for high scores among different players.

## Accessibility Features

The Memory Match Game includes several accessibility features to ensure a smooth gaming experience for all users:

- **Keyboard navigation**: Full functionality is accessible via keyboard shortcuts to ensure that users who cannot use a mouse can navigate efficiently through the application.
- **Tab navigation**: Tab navigation is implemented through all interactive elements in a logical order.
- **Visual indicators**: Visual indicators are provided for the currently focused element.
- **Screen reader support**: Alt text is used to describe images, icons, and other non-textual elements. Labels and roles are used for complex elements to ensure their purpose and state are conveyed to screen reader users.

## Conclusion

Congratulations! You are now ready to enjoy the Memory Match Game. Have fun finding matching pairs of cards and challenging yourself with different difficulty levels and themes. Good luck and happy gaming!

```