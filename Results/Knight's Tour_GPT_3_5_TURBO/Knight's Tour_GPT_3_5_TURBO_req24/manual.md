# Knight's Tour Puzzle Game User Manual

## Introduction

Welcome to the Knight's Tour Puzzle Game! This desktop puzzle game is based on the mathematical problem known as the "Knight's Tour". In this game, your objective is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty.

## Installation

To install and run the Knight's Tour Puzzle Game, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a terminal or command prompt.

3. Clone the repository or download the source code from the following link: [Knight's Tour Puzzle Game](https://github.com/your-repository-link)

4. Navigate to the project directory in the terminal or command prompt.

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

6. Once the dependencies are installed, you can start the game by running the following command:

   ```
   python main.py
   ```

7. The game will open in a new window, and you can start playing!

## Main Menu

When you start the game, you will see the main menu. The main menu provides several options for customizing the game and starting a new game. The options available in the main menu are as follows:

- Start Game: Begins a new game. You can select the difficulty level or board size here.

- Options/Settings: Allows you to customize game settings, including sound volume, visual themes, and knight/chessboard appearances.

- Tutorial: Provides a brief interactive or video tutorial on how the game is played, detailing the knight's legal moves.

- High Scores: Displays a list of high scores, possibly with filters for different board sizes.

- Exit: Quits the game.

## Game Window

Once you start a new game, the game window will open. The game window displays the chessboard/grid and provides various features to help you solve the puzzle. The features available in the game window are as follows:

- Chessboard/Grid Display: Centrally displays the game board with a clear distinction between visited and unvisited squares. The current position of the knight is highlighted.

- Move Counter: Shows the number of moves made by the player.

- Timer (Optional): A timer showing how long you have been attempting the current puzzle.

- Undo Button: Allows you to undo the last move. This could be limited to a certain number of uses.

- Hint Button: Provides a hint for the next move. This could be limited to ensure the game remains challenging.

- Pause/Menu Button: Pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

## Options/Settings Window

In the options/settings window, you can customize various aspects of the game. The options available in the options/settings window are as follows:

- Visual Settings: Options to change the theme of the chessboard and the knight. This could include color schemes or graphical styles.

- Difficulty Settings: Allows you to choose the size of the chessboard, affecting the difficulty. The window might also offer toggles for advanced features like the timer.

## High Scores Window

The high scores window displays a list of high scores achieved by players. The high scores are based on the number of moves and time taken to complete the puzzle. The high scores window may also provide filters to view scores for different board sizes or difficulty levels.

## Tutorial Window

The tutorial window provides an interactive step-by-step guide that introduces you to the game mechanics. It explains how the knight moves, the objective of the game, and any unique features such as hints and undos.

## Pause Menu (In-Game)

The pause menu can be accessed during the game by clicking the pause/menu button. The pause menu provides the following options:

- Resume Game: Returns to the game.

- Restart Game: Starts a new game with the same settings.

- Settings: Opens the options/settings window.

- Main Menu: Returns to the main menu (with a warning about losing current game progress).

## Additional Features

The Knight's Tour Puzzle Game includes additional features to enhance the gameplay experience. These features are as follows:

- Game Mechanics: The game implements the knight's legal moves based on chess rules.

- Preventing Revisiting Squares: The knight is prevented from visiting a square more than once.

- Detecting Successful Completion: The game detects when the player has successfully completed the tour or if the tour is no longer possible to complete.

- Levels and Challenges: The game offers boards of different sizes (e.g., 8x8, 6x6, 10x10) to cater to various levels of difficulty.

## Conclusion

Congratulations! You are now ready to enjoy the Knight's Tour Puzzle Game. Have fun solving the puzzles and challenging yourself with different board sizes and difficulty levels. Good luck!