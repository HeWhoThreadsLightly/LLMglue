# Knight's Tour Puzzle Game User Manual

## Introduction
Welcome to the Knight's Tour Puzzle Game! This game is based on the mathematical problem known as the "Knight's Tour". The objective of the game is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty. The knight moves in an L-shape, as it does in traditional chess.

## Installation
To play the Knight's Tour Puzzle Game, you need to install the following dependencies:

- Python (version 3.6 or higher)
- Tkinter library (usually included with Python)

You can install the dependencies by running the following command:

```
pip install -r requirements.txt
```

## Starting the Game
To start the game, run the following command:

```
python main.py
```

## Main Menu
When you start the game, you will see the main menu. The main menu provides the following options:

- Start Game: Begins a new game. You can select the difficulty level or board size here.
- Options/Settings: Allows you to customize game settings, including sound volume, visual themes, and knight/chessboard appearances.
- Tutorial: Provides a brief interactive or video tutorial on how the game is played, detailing the knight's legal moves.
- High Scores: Displays a list of high scores, possibly with filters for different board sizes.
- Exit: Quits the game.

## Game Window
Once you start a new game, you will see the game window. The game window consists of the following elements:

- Chessboard/Grid Display: Centrally displays the game board with a clear distinction between visited and unvisited squares. The current position of the knight is highlighted.
- Move Counter: Shows the number of moves made by the player.
- Timer (Optional): A timer showing how long the player has been attempting the current puzzle.
- Undo Button: Allows the player to undo the last move. This could be limited to a certain number of uses.
- Hint Button: Provides a hint for the next move. This could be limited to ensure the game remains challenging.
- Pause/Menu Button: Pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

## Options/Settings Window
In the options/settings window, you can customize the following settings:

- Visual Settings: Options to change the theme of the chessboard and the knight. This could include color schemes or graphical styles.
- Difficulty Settings: Allows you to choose the size of the chessboard, affecting the difficulty. The window might also offer toggles for advanced features like the timer.

## High Scores Window
The high scores window displays a list of high scores, with details such as player name, score (based on moves and time), and board size. You can also filter scores by board size or difficulty level.

## Tutorial Window
The tutorial window provides an interactive step-by-step guide that introduces you to the game mechanics, including how the knight moves, the objective of the game, and any unique features (e.g., hints, undos).

## Pause Menu (In-Game)
The pause menu allows you to perform the following actions while the game is paused:

- Resume Game: Returns to the game.
- Restart Game: Starts a new game with the same settings.
- Settings: Opens the options/settings window.
- Main Menu: Returns to the main menu (with a warning about losing current game progress).

## Additional Features
The Knight's Tour Puzzle Game includes the following additional features:

- Game mechanics: The knight's legal moves are implemented based on chess rules.
- The knight is prevented from visiting a square more than once.
- The game detects when the player has successfully completed the tour or if the tour is no longer possible to complete.
- Levels and challenges: The game offers boards of different sizes (e.g., 8x8, 6x6, 10x10) to cater to various levels of difficulty.
- The game includes a timer and move counter to challenge players to complete the puzzle faster or in fewer moves.
- Scoring and progression: The game implements a scoring system based on the time taken to complete the tour and the difficulty level of the board. High scores and player progress are saved.
- Tutorials and hints: The game provides a brief interactive tutorial on how to play the game and move the knight. Hints and undo moves are available to help beginners.
- Customization and preferences: Players can customize the appearance of the chessboard and the knight. Options to mute sounds or music are also available.
- Accessibility: The game supports keyboard navigation, screen reader support, and high contrast mode to ensure accessibility for all users.

## Conclusion
Enjoy playing the Knight's Tour Puzzle Game! Have fun solving the puzzles and challenging yourself with different board sizes and difficulty levels. Good luck!