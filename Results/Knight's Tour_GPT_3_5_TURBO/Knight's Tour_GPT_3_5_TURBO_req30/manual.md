# Knight's Tour Puzzle Game User Manual

## Introduction
Welcome to the Knight's Tour Puzzle Game! This desktop application is based on the mathematical problem known as the "Knight's Tour". The objective of the game is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty.

## Installation
To install and run the Knight's Tour Puzzle Game, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a command prompt or terminal window.

3. Install the required dependencies by running the following command:
   ```
   pip install numpy pandas tkinter
   ```

4. Download the game code from the following GitHub repository: [link to the repository]

5. Extract the downloaded ZIP file to a location of your choice.

6. Open a command prompt or terminal window and navigate to the extracted folder.

7. Run the game by executing the following command:
   ```
   python main.py
   ```

8. The game window will open, and you can start playing the Knight's Tour Puzzle Game!

## Main Menu
When you open the game, you will see the main menu. The main menu provides several options for you to choose from:

- Start Game: Begins a new game. You can select the difficulty level or board size here.
- Options/Settings: Allows you to customize game settings, including sound volume, visual themes, and knight/chessboard appearances.
- Tutorial: Provides a brief interactive or video tutorial on how the game is played, detailing the knight's legal moves.
- High Scores: Displays a list of high scores, possibly with filters for different board sizes.
- Exit: Quits the game.

## Game Window
Once you start a new game, the game window will open. The game window consists of the following elements:

- Chessboard/Grid Display: Centrally displays the game board with a clear distinction between visited and unvisited squares. The current position of the knight is highlighted.
- Move Counter: Shows the number of moves made by the player.
- Timer: (Optional) A timer showing how long the player has been attempting the current puzzle.
- Undo Button: Allows the player to undo the last move. This could be limited to a certain number of uses.
- Hint Button: Provides a hint for the next move. This could be limited to ensure the game remains challenging.
- Pause/Menu Button: Pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

## Options/Settings Window
In the options/settings window, you can customize various aspects of the game:

- Visual Settings: Options to change the theme of the chessboard and the knight. This could include color schemes or graphical styles.
- Difficulty Settings: Allows you to choose the size of the chessboard, affecting the difficulty. The window might also offer toggles for advanced features like the timer.

## High Scores Window
The high scores window displays a list of high scores achieved by players. It includes details such as player name, score (based on moves and time), and board size. You can also filter the scores by board size or difficulty level.

## Tutorial Window
The tutorial window provides an interactive step-by-step guide that introduces you to the game mechanics. It explains how the knight moves, the objective of the game, and any unique features (e.g., hints, undos).

## Pause Menu (In-Game)
While playing the game, you can pause the game by clicking the Pause/Menu button. This opens a pause menu that allows you to perform the following actions:

- Resume Game: Returns to the game.
- Restart Game: Starts a new game with the same settings.
- Settings: Opens the Options/Settings window.
- Main Menu: Returns to the main menu (with a warning about losing current game progress).

## Additional Features
The Knight's Tour Puzzle Game includes several additional features to enhance your gaming experience:

- Game Mechanics: The knight's legal moves are implemented based on chess rules. The knight is prevented from visiting a square more than once. The game also detects when the player has successfully completed the tour or if the tour is no longer possible to complete.
- Levels and Challenges: The game offers boards of different sizes (e.g., 8x8, 6x6, 10x10) to cater to various levels of difficulty. It includes a timer and move counter to challenge players to complete the puzzle faster or in fewer moves.
- Scoring and Progression: The game implements a scoring system based on the time taken to complete the tour and the difficulty level of the board. High scores and player progress are saved.
- Tutorials and Hints: The game provides a brief interactive tutorial on how to play the game and move the knight. It also offers hints and allows users to undo moves to help beginners.
- Customization and Preferences: Players can customize the appearance of the chessboard and the knight, including color schemes and graphical styles.

## Conclusion
Enjoy playing the Knight's Tour Puzzle Game! Challenge yourself to complete the tour in the fewest moves and the shortest time possible. Have fun and improve your problem-solving skills with this exciting puzzle game!