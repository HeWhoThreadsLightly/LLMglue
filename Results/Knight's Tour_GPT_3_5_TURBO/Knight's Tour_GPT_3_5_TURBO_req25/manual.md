# Knight's Tour Puzzle Game User Manual

## Introduction
Welcome to the Knight's Tour Puzzle Game! This desktop application is based on the mathematical problem known as the "Knight's Tour". In this game, you control a chess knight and your objective is to move the knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty.

## Installation
To install the Knight's Tour Puzzle Game, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a terminal or command prompt and navigate to the directory where you want to install the game.

3. Clone the game repository by running the following command:
   ```
   git clone https://github.com/your-username/knights-tour-puzzle-game.git
   ```

4. Navigate to the cloned repository:
   ```
   cd knights-tour-puzzle-game
   ```

5. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Starting the Game
To start the Knight's Tour Puzzle Game, follow these steps:

1. Open a terminal or command prompt and navigate to the directory where you installed the game.

2. Run the following command to start the game:
   ```
   python main.py
   ```

3. The game window will appear, showing the main menu.

## Main Menu
The main menu provides several options for customizing the game and starting a new game. Here are the available options:

- **Start Game**: Begins a new game. You can select the difficulty level or board size here.

- **Options/Settings**: Allows you to customize game settings, including sound volume, visual themes, and knight/chessboard appearances.

- **Tutorial**: Provides a brief interactive or video tutorial on how the game is played, detailing the knight's legal moves.

- **High Scores**: Displays a list of high scores, possibly with filters for different board sizes.

- **Exit**: Quits the game.

## Game Window
Once you start a new game, the game window will appear. Here are the main components of the game window:

- **Chessboard/Grid Display**: Centrally displays the game board with a clear distinction between visited and unvisited squares. The current position of the knight is highlighted.

- **Move Counter**: Shows the number of moves made by the player.

- **Timer** (Optional): A timer showing how long the player has been attempting the current puzzle.

- **Undo Button**: Allows the player to undo the last move. This could be limited to a certain number of uses.

- **Hint Button**: Provides a hint for the next move. This could be limited to ensure the game remains challenging.

- **Pause/Menu Button**: Pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

## Options/Settings Window
The options/settings window allows you to customize various aspects of the game. Here are the available options:

- **Visual Settings**: Options to change the theme of the chessboard and the knight. This could include color schemes or graphical styles.

- **Difficulty Settings**: Allows you to choose the size of the chessboard, affecting the difficulty. The window might also offer toggles for advanced features like the timer.

## High Scores Window
The high scores window displays a list of high scores achieved by players. Here are the available options:

- **Score List**: Displays a list of high scores, with details such as player name, score (based on moves and time), and board size.

- **Filters**: Allows you to filter scores by board size or difficulty level.

## Tutorial Window
The tutorial window provides an interactive step-by-step guide that introduces you to the game mechanics. It covers topics such as how the knight moves, the objective of the game, and any unique features (e.g., hints, undos).

## Pause Menu (In-Game)
The pause menu appears when you pause the game. It provides several options for managing the game. Here are the available options:

- **Resume Game**: Returns to the game.

- **Restart Game**: Starts a new game with the same settings.

- **Settings**: Opens the options/settings window.

- **Main Menu**: Returns to the main menu (with a warning about losing current game progress).

## Additional Features
The Knight's Tour Puzzle Game includes additional features to enhance the gameplay experience. Here are the additional features:

- **Game Mechanics**: The game implements the knight's legal moves based on chess rules.

- **Prevent Revisiting Squares**: The knight is prevented from visiting a square more than once.

- **Detect Completion**: The game detects when the player has successfully completed the tour or if the tour is no longer possible to complete.

- **Levels and Challenges**: The game offers boards of different sizes (e.g., 8x8, 6x6, 10x10) to cater to various levels of difficulty.

- **Timer and Move Counter**: The game includes a timer and move counter to challenge players to complete the puzzle faster or in fewer moves.

## Conclusion
Congratulations! You are now ready to enjoy the Knight's Tour Puzzle Game. Have fun solving the puzzles and challenging yourself with different board sizes and difficulty levels. Good luck!