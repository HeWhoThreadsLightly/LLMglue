# Knight's Tour Puzzle Game User Manual

## Introduction

Welcome to the Knight's Tour Puzzle Game! This desktop application is based on the mathematical problem known as the "Knight's Tour". In this game, your objective is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty.

## Installation

To install and run the Knight's Tour Puzzle Game, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a terminal or command prompt and navigate to the directory where you want to install the game.

3. Clone the game repository from GitHub by running the following command:
   ```
   git clone https://github.com/chatdev-org/knights-tour-puzzle-game.git
   ```

4. Navigate to the game directory:
   ```
   cd knights-tour-puzzle-game
   ```

5. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Starting the Game

To start the Knight's Tour Puzzle Game, follow these steps:

1. Open a terminal or command prompt and navigate to the game directory.

2. Run the following command to start the game:
   ```
   python main.py
   ```

3. The game window will appear, showing the main menu.

## Main Menu

The main menu of the Knight's Tour Puzzle Game provides several options:

- **Start Game**: Begins a new game. You can select the difficulty level or board size here.

- **Options/Settings**: Allows you to customize game settings, including sound volume, visual themes, and knight/chessboard appearances.

- **Tutorial**: Provides a brief interactive or video tutorial on how the game is played, detailing the knight's legal moves.

- **High Scores**: Displays a list of high scores, possibly with filters for different board sizes.

- **Exit**: Quits the game.

## Game Window

Once you start a new game, the game window will appear. It consists of the following elements:

- **Chessboard/Grid Display**: Centrally displays the game board with a clear distinction between visited and unvisited squares. The current position of the knight is highlighted.

- **Move Counter**: Shows the number of moves made by the player.

- **Timer** (Optional): A timer showing how long the player has been attempting the current puzzle.

- **Undo Button**: Allows the player to undo the last move. This could be limited to a certain number of uses.

- **Hint Button**: Provides a hint for the next move. This could be limited to ensure the game remains challenging.

- **Pause/Menu Button**: Pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

## Gameplay

To play the Knight's Tour Puzzle Game, follow these steps:

1. Start a new game from the main menu.

2. The chessboard will be displayed, and the knight will start at a random position.

3. Use your mouse to click on an unvisited square to move the knight to that position. The knight moves in an L-shape, as it does in traditional chess.

4. The move counter will be updated, showing the number of moves made.

5. You can use the undo button to undo the last move if needed.

6. If you get stuck, you can use the hint button to get a hint for the next move.

7. The game continues until you visit every square on the chessboard exactly once.

8. Once you complete the puzzle, you can view your score and try again or return to the main menu.

## Conclusion

Congratulations! You are now ready to enjoy the Knight's Tour Puzzle Game. Have fun exploring different board sizes and difficulty levels, and challenge yourself to solve the puzzle in the fewest moves possible. Good luck!