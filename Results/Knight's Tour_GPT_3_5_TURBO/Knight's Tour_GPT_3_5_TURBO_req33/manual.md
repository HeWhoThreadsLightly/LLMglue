# Knight's Tour Puzzle Game User Manual

## Introduction

Welcome to the Knight's Tour Puzzle Game! This desktop application is based on the mathematical problem known as the "Knight's Tour". In this game, your objective is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty.

## Installation

To install and run the Knight's Tour Puzzle Game, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt.

3. Clone the repository or download the source code from [GitHub](https://github.com).

4. Navigate to the project directory in the terminal or command prompt.

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

6. Once the dependencies are installed, you can start the game by running the following command:

   ```
   python main.py
   ```

## Main Menu

When you start the game, you will see the main menu. The main menu provides several options:

- Start Game: Begins a new game. You can select the difficulty level or board size here.

- Options/Settings: Allows you to customize game settings, including sound volume, visual themes, and knight/chessboard appearances.

- Tutorial: Provides a brief interactive or video tutorial on how the game is played, detailing the knight's legal moves.

- High Scores: Displays a list of high scores, possibly with filters for different board sizes.

- Exit: Quits the game.

## Game Window

Once you start a new game, the game window will open. The game window consists of the following elements:

- Chessboard/Grid Display: Centrally displays the game board with a clear distinction between visited and unvisited squares. The current position of the knight is highlighted.

- Move Counter: Shows the number of moves made by the player.

- Timer (Optional): A timer showing how long the player has been attempting the current puzzle.

- Undo Button: Allows the player to undo the last move. This could be limited to a certain number of uses.

- Hint Button: Provides a hint for the next move. This could be limited to ensure the game remains challenging.

- Pause/Menu Button: Pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

## Game Mechanics

The game mechanics of the Knight's Tour Puzzle Game are based on chess rules. The knight moves in an L-shape, as it does in traditional chess. The game prevents the knight from visiting a square more than once. It also detects when the player has successfully completed the tour or if the tour is no longer possible to complete.

## Levels and Challenges

The game offers boards of different sizes to cater to various levels of difficulty. You can choose the size of the chessboard, which affects the difficulty. The game also includes a timer and move counter to challenge players to complete the puzzle faster or in fewer moves.

## Scoring and Progression

The game implements a scoring system based on the time taken to complete the tour and the difficulty level of the board. High scores and player progress are saved.

## Tutorials and Hints

The game provides a brief interactive tutorial on how to play the game and move the knight. It also offers hints and allows users to undo moves to help beginners.

## Customization and Preferences

You can customize the appearance of the chessboard and the knight. Options include changing the theme of the chessboard and the knight, such as color schemes or graphical styles. You can also mute sounds or music.

## Accessibility

The game supports keyboard navigation to ensure that users who cannot use a mouse can navigate efficiently through the application. Full functionality is accessible via keyboard shortcuts, and tab navigation is implemented through all interactive elements in a logical order.

## Conclusion

Enjoy playing the Knight's Tour Puzzle Game! Have fun solving the puzzles and challenging yourself with different board sizes and difficulty levels. If you have any questions or need assistance, please refer to the documentation or contact our support team. Happy gaming!