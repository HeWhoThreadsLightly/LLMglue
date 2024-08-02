# Memory Match Game User Manual

## Introduction

Welcome to the Memory Match Game! This simple yet engaging game challenges your memory and concentration skills. The objective of the game is to find all the matching pairs of cards by remembering their locations. The game features different difficulty levels, themes, and a timer to make it more challenging and enjoyable.

## Installation

To play the Memory Match Game, you need to have Python installed on your computer. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

Once you have Python installed, you can install the game's dependencies by running the following command in your terminal or command prompt:

```
pip install -r requirements.txt
```

## Starting the Game

To start the Memory Match Game, open a terminal or command prompt and navigate to the directory where the game files are located. Then, run the following command:

```
python main.py
```

This will launch the game's main menu window.

## Main Menu

The main menu is the starting point of the game. It provides options to start the game, view high scores, adjust settings, and exit the game.

### Play Button (REQ2)

Clicking the "Play" button takes you to the "Select Difficulty" window, where you can choose the difficulty level for the game.

### High Scores Button (REQ3)

Clicking the "High Scores" button opens a window displaying the high scores from previous games. The high scores include the player's name, score, and time.

### Settings Button (REQ4)

Clicking the "Settings" button opens a window where you can adjust sound preferences, choose themes, and view game instructions.

### Exit Button (REQ5)

Clicking the "Exit" button closes the game.

## Select Difficulty Window

In the "Select Difficulty" window, you can choose the difficulty level for the game. The difficulty level determines the size of the game grid and the number of cards to match.

### Difficulty Level Buttons (REQ7)

There are three difficulty levels to choose from: Easy, Medium, and Hard. Clicking on a difficulty level button sets the game's difficulty and starts the game.

### Back Button (REQ8)

Clicking the "Back" button returns you to the main menu.

## Game Window

The game window is where the Memory Match Game is played. It consists of a game grid, a score panel, and a pause/menu button.

### Game Grid (REQ9)

The game grid is the central area where the cards are displayed. The grid size changes based on the chosen difficulty level. The cards are initially face down, and you need to flip them to find matching pairs.

### Score Panel (REQ10)

The score panel displays the current number of attempts, the number of matches found, and the elapsed time.

### Pause/Menu Button (REQ11)

The pause/menu button allows you to pause the game and open a small menu with options to resume, restart, change difficulty, or return to the main menu.

## Settings Window

The settings window allows you to adjust various game settings, including sound preferences, themes, and game instructions.

### Sound Settings (REQ12)

In the sound settings section, you can toggle switches for game sound effects and background music. You can enable or disable these sounds according to your preference.

### Theme Selection (REQ13)

The theme selection section allows you to choose different themes for the cards and the game board background. Themes can include animals, space, plants, and more.

### Instructions (REQ14)

The instructions section provides a brief overview of the game rules and controls. It helps you understand how to play the game and enjoy it to the fullest.

### Back Button (REQ15)

Clicking the "Back" button saves any changes made in the settings and returns you to the main menu.

## High Scores Window

The high scores window displays the top scores from previous games. It includes details such as the player's name, score (based on attempts and time), and difficulty level.

### Clear Scores Button (REQ17)

The clear scores button allows you to clear the high score history. Use this option if you want to start fresh and remove all previous high scores.

### Back Button (REQ18)

Clicking the "Back" button returns you to the main menu.

## Game Over/Win Window

The game over/win window appears when you complete the game by finding all the matching pairs. It displays a congratulatory message, the final score, and the time taken to complete the game.

### Play Again Button (REQ20)

Clicking the "Play Again" button restarts the game at the same difficulty level. Use this option if you want to play another round with the same settings.

### Change Difficulty Button (REQ21)

Clicking the "Change Difficulty" button returns you to the "Select Difficulty" window. Use this option if you want to choose a new difficulty level for the next game.

### Main Menu Button (REQ22)

Clicking the "Main Menu" button returns you to the main menu. Use this option if you want to go back to the main menu and explore other options.

## Additional Features

The Memory Match Game includes additional features to enhance your gaming experience.

### Game Logic (REQ23, REQ24, REQ25, REQ26, REQ27)

The game logic allows you to shuffle and randomly place the cards at the start of each game. You can flip cards to reveal their faces when clicked, check for matches when two cards are flipped, keep track of the number of attempts made and matches found, and implement a win condition when all matches are found.

### Difficulty Levels (REQ28, REQ29)

The game offers three difficulty levels: Easy, Medium, and Hard. Each difficulty level has a different grid size and number of cards to match. Choose the difficulty level that suits your skill level.

### Themes and Customization (REQ30, REQ31)

The game provides different themes for the cards and the game board background. You can choose themes like animals, space, plants, and more. Themes change the visual appearance of the game and add variety to your gameplay.

### Score and Timing (REQ32, REQ33, REQ34)

The game includes a timer to track how long it takes for you to complete the game. Your score is calculated based on the number of attempts made and the time taken. The game also features a high score feature that saves your best scores.

### Settings and Controls (REQ35, REQ36)

The game allows you to restart the game, change difficulty levels, and switch themes without restarting the application. You can also enable or disable sound effects for flipping cards, finding a match, and winning the game. The settings and controls provide flexibility and customization options.

### Development Considerations (REQ37)

The game implements data persistence for high scores and settings. Your high scores and preferences are saved even if you close the game. The game uses local storage or a simple file-based approach to store this data.

## Bonus Features

The Memory Match Game includes bonus features to make your gaming experience even more enjoyable.

### Multiplayer Mode (REQ38)

The game offers a multiplayer mode where two players can take turns to find matches. Challenge your friends or family members and see who can find the most matching pairs!

### Animations (REQ39)

The game includes animations for flipping cards and winning the game. These animations add visual appeal and make the gameplay more engaging.

### Leaderboards (REQ40)

The game features leaderboards for high scores among different players. Compete with other players and try to reach the top of the leaderboards!

## Accessibility Features

The Memory Match Game includes accessibility features to ensure that everyone can enjoy the game.

### Keyboard Navigation (REQ41, REQ42, REQ43)

The game provides full functionality via keyboard shortcuts. You can navigate through all interactive elements using the keyboard, making the game accessible to users who cannot use a mouse. Tab navigation is implemented to navigate through interactive elements in a logical order. Visual indicators are provided to highlight the currently focused element.

### Screen Reader Support (REQ44, REQ45)

The game includes alt text to describe images, icons, and other non-textual elements. Labels and roles are used for complex elements to convey their purpose and state to screen reader users. The game aims to provide a seamless experience for users who rely on screen readers.

### High Contrast Mode (REQ46)

The game supports high contrast themes that make text, icons, and other elements more distinguishable for users with low vision. High contrast themes improve visibility and ensure that the game is accessible to users with different visual abilities.

## Conclusion

Thank you for choosing the Memory Match Game! We hope you enjoy playing the game and challenging your memory skills. If you have any questions or feedback, please don't hesitate to contact our support team. Happy gaming!

```