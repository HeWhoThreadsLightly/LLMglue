# Knight's Tour Puzzle Game User Manual

## Introduction
Welcome to the Knight's Tour Puzzle Game! This desktop application is based on the mathematical problem known as the "Knight's Tour". The objective of the game is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty. The knight moves in an L-shape, as it does in traditional chess.

## Installation
To install and run the Knight's Tour Puzzle Game, please follow the steps below:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a terminal or command prompt.

3. Clone the repository or download the source code files from the following link: [Knight's Tour Puzzle Game Repository](https://github.com/your-repository-link)

4. Navigate to the directory where you cloned or downloaded the source code files.

5. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

6. Once the dependencies are installed, you can start the game by running the following command:
   ```
   python main.py
   ```

7. The game window will open, and you can now start playing the Knight's Tour Puzzle Game!

## Main Menu
When you start the game, you will see the main menu. The main menu provides several options:

- **Start Game**: Begins a new game. You can select the difficulty level or board size here.
- **Options/Settings**: Allows you to customize game settings, including sound volume, visual themes, and knight/chessboard appearances.
- **Tutorial**: Provides a brief interactive or video tutorial on how the game is played, detailing the knight's legal moves.
- **High Scores**: Displays a list of high scores, possibly with filters for different board sizes.
- **Exit**: Quits the game.

## Game Window
Once you start a new game, the game window will open. The game window consists of the following elements:

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
The high scores window displays a list of high scores achieved by players. It includes details such as player name, score (based on moves and time), and board size. You can also apply filters to view scores for different board sizes or difficulty levels.

## Tutorial Window
The tutorial window provides an interactive step-by-step guide that introduces you to the game mechanics. It explains how the knight moves, the objective of the game, and any unique features such as hints and undos.

## Pause Menu (In-Game)
When you pause the game, a pause menu will appear. The pause menu provides the following options:

- **Resume Game**: Returns to the game.
- **Restart Game**: Starts a new game with the same settings.
- **Settings**: Opens the options/settings window.
- **Main Menu**: Returns to the main menu (with a warning about losing current game progress).

## Additional Features
The Knight's Tour Puzzle Game includes additional features to enhance your gaming experience:

- **Game Mechanics**: The game implements the knight's legal moves based on chess rules. The knight is prevented from visiting a square more than once. The game also detects when the player has successfully completed the tour or if the tour is no longer possible to complete.
- **Levels and Challenges**: The game offers boards of different sizes (e.g., 8x8, 6x6, 10x10) to cater to various levels of difficulty. It includes a timer and move counter to challenge players to complete the puzzle faster or in fewer moves.
- **Scoring and Progression**: The game implements a scoring system based on the time taken to complete the tour and the difficulty level of the board. High scores and player progress are saved.
- **Tutorials and Hints**: The game provides a brief interactive tutorial on how to play the game and move the knight. It also offers hints and allows users to undo moves to help beginners.
- **Customization and Preferences**: The game allows players to customize the appearance of the chessboard and the knight. Options to mute sounds or music are also available.
- **Accessibility**: The game supports keyboard navigation, ensuring that users who cannot use a mouse can navigate efficiently through the application using keyboard shortcuts.

## Conclusion
Thank you for choosing the Knight's Tour Puzzle Game! We hope you enjoy playing and challenging yourself with this mathematical puzzle. If you have any questions or feedback, please don't hesitate to contact us. Happy gaming!

```