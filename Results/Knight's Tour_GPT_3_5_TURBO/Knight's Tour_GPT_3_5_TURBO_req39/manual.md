# Knight's Tour Puzzle Game User Manual

Welcome to the Knight's Tour Puzzle Game! This user manual will guide you through the installation process, explain the main functions of the game, and provide instructions on how to play.

## Table of Contents
1. Installation
2. Game Overview
3. Main Menu
4. Game Window
5. Options/Settings Window
6. High Scores Window
7. Tutorial Window
8. Pause Menu (In-Game)
9. Additional Features
10. Accessibility Features

## 1. Installation
To install the Knight's Tour Puzzle Game, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a command prompt or terminal window.

3. Navigate to the directory where you want to install the game.

4. Run the following command to install the required dependencies:
```
pip install -r requirements.txt
```

5. Once the installation is complete, you can run the game by executing the following command:
```
python main.py
```

## 2. Game Overview
The Knight's Tour Puzzle Game is based on the mathematical problem known as the "Knight's Tour". The objective of the game is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The knight moves in an L-shape, as it does in traditional chess.

The game offers various levels of difficulty, with different board sizes and optional features such as a timer and move counter. You can customize the game settings, access a tutorial, view high scores, and enjoy additional features like hints and undo moves.

## 3. Main Menu
The main menu is the starting point of the game. It provides options to start a new game, customize settings, access the tutorial, view high scores, and exit the game.

- **Start Game**: Begins a new game. Players can select the difficulty level or board size here.

- **Options/Settings**: Allows players to customize game settings, including sound volume, visual themes, and knight/chessboard appearances.

- **Tutorial**: Provides a brief interactive or video tutorial on how the game is played, detailing the knight's legal moves.

- **High Scores**: Displays a list of high scores, possibly with filters for different board sizes.

- **Exit**: Quits the game.

## 4. Game Window
The game window is where the puzzle game is played. It displays the chessboard/grid, the current position of the knight, the move counter, and optional features like a timer, undo button, hint button, and pause/menu button.

- **Chessboard/Grid Display**: Centrally displays the game board with a clear distinction between visited and unvisited squares. The current position of the knight is highlighted.

- **Move Counter**: Shows the number of moves made by the player.

- **Timer** (Optional): A timer showing how long the player has been attempting the current puzzle.

- **Undo Button**: Allows the player to undo the last move. This could be limited to a certain number of uses.

- **Hint Button**: Provides a hint for the next move. This could be limited to ensure the game remains challenging.

- **Pause/Menu Button**: Pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

## 5. Options/Settings Window
The options/settings window allows players to customize various aspects of the game.

- **Visual Settings**: Options to change the theme of the chessboard and the knight. This could include color schemes or graphical styles.

- **Difficulty Settings**: Allows users to choose the size of the chessboard, affecting the difficulty. The window might also offer toggles for advanced features like the timer.

## 6. High Scores Window
The high scores window displays a list of high scores achieved by players. It includes details such as player name, score (based on moves and time), and board size. Players can filter scores by board size or difficulty level.

## 7. Tutorial Window
The tutorial window provides a step-by-step guide that introduces the player to the game mechanics. It explains how the knight moves, the objective of the game, and any unique features (e.g., hints, undos).

## 8. Pause Menu (In-Game)
The pause menu can be accessed during gameplay by clicking the pause/menu button. It allows players to perform various actions without losing their progress.

- **Resume Game**: Returns to the game.

- **Restart Game**: Starts a new game with the same settings.

- **Settings**: Opens the options/settings window.

- **Main Menu**: Returns to the main menu (with a warning about losing current game progress).

## 9. Additional Features
The Knight's Tour Puzzle Game includes additional features to enhance the gameplay experience.

- **Game Mechanics**: The knight's legal moves are implemented based on chess rules. The knight is prevented from visiting a square more than once. The game detects when the player has successfully completed the tour or if the tour is no longer possible to complete.

- **Levels and Challenges**: The game offers boards of different sizes (e.g., 8x8, 6x6, 10x10) to cater to various levels of difficulty. A timer and move counter challenge players to complete the puzzle faster or in fewer moves.

- **Scoring and Progression**: The game implements a scoring system based on the time taken to complete the tour and the difficulty level of the board. High scores and player progress are saved.

- **Tutorials and Hints**: The game provides a brief interactive tutorial on how to play the game and move the knight. Hints and the ability to undo moves are available to help beginners.

- **Customization and Preferences**: Players can customize the appearance of the chessboard and the knight. Options to mute sounds or music are also available.

## 10. Accessibility Features
The Knight's Tour Puzzle Game includes accessibility features to ensure a more inclusive gaming experience.

- **Keyboard Navigation**: Full functionality is accessible via keyboard shortcuts to ensure that users who cannot use a mouse can navigate efficiently through the application. Tab navigation is implemented through all interactive elements in a logical order. Visual indicators are provided for the currently focused element.

- **Screen Reader Support**: Alt text is used to describe images, icons, and other non-textual elements. Labels and roles are used for complex elements (like drag-and-drop interfaces or custom controls) to ensure their purpose and state are conveyed to screen reader users.

- **High Contrast Mode**: Support for high contrast themes that make text, icons, and other elements more distinguishable for users with low vision. All text is readable, and all interactive elements are visible against background colors.

- **Text Size and Font Adjustments**: Users can adjust the text size without breaking the layout or losing functionality.

Congratulations! You are now ready to enjoy the Knight's Tour Puzzle Game. Have fun and challenge yourself to complete the tour!