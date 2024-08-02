# Knight's Tour Puzzle Game User Manual

## Introduction

Welcome to the Knight's Tour Puzzle Game! This desktop application is based on the mathematical problem known as the "Knight's Tour". In this game, you control a chess knight and your objective is to move the knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty.

## Installation

To install the Knight's Tour Puzzle Game, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a terminal or command prompt.

3. Navigate to the directory where you want to install the game.

4. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary dependencies, including the Tkinter library for the graphical user interface.

## Starting the Game

To start the Knight's Tour Puzzle Game, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where you installed the game.

3. Run the following command to start the game:

   ```
   python main.py
   ```

   This will launch the game window.

## Main Menu

The main menu of the game provides several options:

- Start Game: Begins a new game. You can select the difficulty level or board size here.

- Options/Settings: Allows you to customize game settings, including sound volume, visual themes, and knight/chessboard appearances.

- Tutorial: Provides a brief interactive or video tutorial on how the game is played, detailing the knight's legal moves.

- High Scores: Displays a list of high scores, possibly with filters for different board sizes.

- Exit: Quits the game.

## Game Window

Once you start a new game, the game window will be displayed. It consists of the following elements:

- Chessboard/Grid Display: Centrally displays the game board with a clear distinction between visited and unvisited squares. The current position of the knight is highlighted.

- Move Counter: Shows the number of moves made by the player.

- Timer (Optional): A timer showing how long the player has been attempting the current puzzle.

- Undo Button: Allows the player to undo the last move. This could be limited to a certain number of uses.

- Hint Button: Provides a hint for the next move. This could be limited to ensure the game remains challenging.

- Pause/Menu Button: Pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

## Options/Settings Window

The options/settings window allows you to customize various aspects of the game:

- Visual Settings: Options to change the theme of the chessboard and the knight. This could include color schemes or graphical styles.

- Difficulty Settings: Allows you to choose the size of the chessboard, affecting the difficulty. The window might also offer toggles for advanced features like the timer.

## High Scores Window

The high scores window displays a list of high scores achieved by players. It includes details such as player name, score (based on moves and time), and board size. You can also filter the scores by board size or difficulty level.

## Tutorial Window

The tutorial window provides an interactive step-by-step guide that introduces you to the game mechanics. It explains how the knight moves, the objective of the game, and any unique features such as hints and undos.

## Pause Menu (In-Game)

The pause menu can be accessed during the game by clicking the Pause/Menu button. It provides the following options:

- Resume Game: Returns to the game.

- Restart Game: Starts a new game with the same settings.

- Settings: Opens the Options/Settings window.

- Main Menu: Returns to the main menu (with a warning about losing current game progress).

## Game Mechanics

The Knight's Tour Puzzle Game implements the knight's legal moves based on chess rules. The knight moves in an L-shape, as it does in traditional chess. Your objective is to move the knight across the chessboard, visiting every square exactly once.

## Conclusion

Congratulations! You are now ready to enjoy the Knight's Tour Puzzle Game. Have fun solving the puzzles and challenging yourself with different board sizes and difficulty levels. Good luck!