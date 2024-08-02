# Memory Match Game User Manual

## Introduction
The Memory Match Game is a simple yet engaging game where players are presented with a grid of cards. The objective of the game is to find all the matching pairs by remembering the locations of cards they have previously turned over. The game can be played on the desktop and offers different themes, difficulty levels, and a timer to challenge the player further.

## Installation
To play the Memory Match Game, you need to install the following dependencies:

- Python (version 3.6 or higher)
- Tkinter library (included in Python standard library)

You can install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

## Starting the Game
To start the Memory Match Game, follow these steps:

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
The select difficulty window allows the player to choose the difficulty level of the game. It provides the following options:

- Instruction text: A brief instruction on how to select the difficulty level.
- Difficulty level buttons: Buttons for each difficulty level (Easy, Medium, Hard). Clicking on one sets the game's difficulty and starts the game.
- Back button: Returns to the Main Menu.

## Game Window
The game window is where the actual gameplay takes place. It consists of the following elements:

- Game grid: The central area where the cards are displayed according to the chosen difficulty level. Cards are arranged in a grid layout that changes size based on the difficulty.
- Score panel: A panel displaying the current number of attempts, number of matches found, and the elapsed time.
- Pause/Menu Button: Pauses the game and opens a small menu with options to resume, restart, change difficulty, or return to the Main Menu.

## Settings Window
The settings window allows players to customize various aspects of the game. It includes the following options:

- Sound settings: Toggle switches for game sound effects and background music.
- Theme selection: Dropdown menu or buttons to select the card and background theme.
- Instructions: A section that outlines the game rules and controls.
- Back button: Saves any changes and returns to the Main Menu.

## High Scores Window
The high scores window displays the top scores from previous games. It includes the following features:

- Scores display: A list or table displaying the top scores, including details such as player name, score (based on attempts and time), and difficulty level.
- Clear scores button: An option to clear the high score history.
- Back button: Returns to the Main Menu.

## Game Over/Win Window
The game over/win window is displayed when the player completes the game. It includes the following options:

- Message: Displays a congratulatory message for completing the game and shows the final score and time.
- Play Again Button: Restarts the game at the same difficulty level.
- Change Difficulty Button: Returns the player to the "Select Difficulty" window to choose a new difficulty level.
- Main Menu Button: Returns to the Main Menu.

## Additional Features
The Memory Match Game includes several additional features to enhance the gameplay experience:

- Game logic: The game has the ability to shuffle and randomly place the cards at the start of each game.
- Difficulty levels: The game provides three levels of difficulty (Easy, Medium, Hard) with different grid sizes and numbers of cards.
- Themes and customization: Players can choose from different themes for the cards, which change the background of the game board and the card designs.
- Score and timing: The game includes a timer to track how long it takes for the player to complete the game. The player's score is based on the number of attempts made and the time taken to complete the game.
- Settings and controls: Players can restart the game, change difficulty levels, and switch themes without restarting the application. Sound effects for flipping cards, finding a match, and winning the game are included, with an option to mute the sounds.
- Data persistence: The game saves the player's best scores and settings using data persistence (local storage or a simple file-based approach).
- Bonus features: The game includes bonus features such as a multiplayer mode where two players take turns to find matches, animations for flipping cards and winning the game, and leaderboards for high scores among different players.

## Accessibility Features
The Memory Match Game includes several accessibility features to ensure a smooth user experience:

- Keyboard navigation: Full functionality is accessible via keyboard shortcuts, allowing users who cannot use a mouse to navigate efficiently through the application.
- Tab navigation: The game implements tab navigation through all interactive elements in a logical order.
- Visual indicators: The game provides visual indicators for the currently focused element.
- Screen reader support: The game uses alt text to describe images, icons, and other non-textual elements, making it accessible to screen reader users.

## Conclusion
The Memory Match Game is a fun and engaging game that challenges players to test their memory skills. With different themes, difficulty levels, and additional features, it offers a customizable and enjoyable gaming experience. Have fun playing and improving your memory!