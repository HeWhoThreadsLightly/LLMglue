# Knight's Tour Puzzle Game User Manual

## Introduction

Welcome to the Knight's Tour Puzzle Game! This desktop application is based on the mathematical problem known as the "Knight's Tour". In this game, your objective is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty.

## Installation

To install and run the Knight's Tour Puzzle Game, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone or download the game's source code from the GitHub repository: [https://github.com/your-repository](https://github.com/your-repository)

3. Open a terminal or command prompt and navigate to the directory where you downloaded the source code.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - Windows:

     ```
     venv\Scripts\activate
     ```

   - macOS/Linux:

     ```
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Run the game by executing the `main.py` file:

   ```
   python main.py
   ```

8. The game window should open, and you can start playing the Knight's Tour Puzzle Game!

## Main Menu

When you launch the game, you will see the main menu with the following options:

- **Start Game**: Begins a new game. You can select the difficulty level or board size here.
- **Options/Settings**: Allows you to customize game settings, including sound volume, visual themes, and knight/chessboard appearances.
- **Tutorial**: Provides a brief interactive or video tutorial on how the game is played, detailing the knight's legal moves.
- **High Scores**: Displays a list of high scores, possibly with filters for different board sizes.
- **Exit**: Quits the game.

## Game Window

Once you start a new game, the game window will open, displaying the chessboard/grid and other game elements:

- **Chessboard/Grid Display**: Centrally displays the game board with a clear distinction between visited and unvisited squares. The current position of the knight is highlighted.
- **Move Counter**: Shows the number of moves made by the player.
- **Timer** (Optional): A timer showing how long the player has been attempting the current puzzle.
- **Undo Button**: Allows the player to undo the last move. This could be limited to a certain number of uses.
- **Hint Button**: Provides a hint for the next move. This could be limited to ensure the game remains challenging.
- **Pause/Menu Button**: Pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

## Options/Settings Window

In the options/settings window, you can customize various aspects of the game:

- **Visual Settings**: Options to change the theme of the chessboard and the knight. This could include color schemes or graphical styles.
- **Difficulty Settings**: Allows you to choose the size of the chessboard, affecting the difficulty. The window might also offer toggles for advanced features like the timer.

## High Scores Window

The high scores window displays a list of high scores achieved by players. It includes details such as player name, score (based on moves and time), and board size. You can also use filters to view scores for different board sizes or difficulty levels.

## Tutorial Window

The tutorial window provides an interactive step-by-step guide that introduces you to the game mechanics. It explains how the knight moves, the objective of the game, and any unique features such as hints and undos.

## Pause Menu (In-Game)

When you pause the game, a menu will appear with the following options:

- **Resume Game**: Returns to the game.
- **Restart Game**: Starts a new game with the same settings.
- **Settings**: Opens the options/settings window.
- **Main Menu**: Returns to the main menu (with a warning about losing current game progress).

## Additional Features

The Knight's Tour Puzzle Game includes additional features to enhance your gaming experience:

- **Game Mechanics**: The knight's legal moves are implemented based on chess rules. The knight is prevented from visiting a square more than once. The game detects when the player has successfully completed the tour or if the tour is no longer possible to complete.
- **Levels and Challenges**: The game offers boards of different sizes (e.g., 8x8, 6x6, 10x10) to cater to various levels of difficulty. It includes a timer and move counter to challenge players to complete the puzzle faster or in fewer moves.
- **Scoring and Progression**: The game implements a scoring system based on the time taken to complete the tour and the difficulty level of the board. High scores and player progress are saved.
- **Tutorials and Hints**: The game provides a brief interactive tutorial on how to play the game and move the knight. It also offers hints and the ability to undo moves to help beginners.

## Conclusion

Enjoy playing the Knight's Tour Puzzle Game! Challenge yourself to solve the puzzle and achieve high scores. Have fun and happy gaming!

```