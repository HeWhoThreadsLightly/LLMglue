# Knight's Tour Puzzle Game User Manual

Welcome to the Knight's Tour Puzzle Game! This user manual will guide you through the installation process, explain the main functions of the game, and provide instructions on how to play.

## Table of Contents
1. [Installation](#installation)
2. [Game Overview](#game-overview)
3. [Main Menu](#main-menu)
4. [Game Window](#game-window)
5. [Options/Settings Window](#options-settings-window)
6. [High Scores Window](#high-scores-window)
7. [Tutorial Window](#tutorial-window)
8. [Pause Menu (In-Game)](#pause-menu-in-game)
9. [Additional Features](#additional-features)
10. [Customization and Preferences](#customization-and-preferences)

## 1. Installation <a name="installation"></a>

To install the Knight's Tour Puzzle Game, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt.

3. Use the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Once the installation is complete, you can run the game by executing the following command:

   ```
   python main.py
   ```

   The game will open in a new window.

## 2. Game Overview <a name="game-overview"></a>

The Knight's Tour Puzzle Game is based on the mathematical problem known as the "Knight's Tour". The objective of the game is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The knight moves in an L-shape, as it does in traditional chess.

The game offers various levels of difficulty, with larger board sizes increasing the challenge. You can customize the game settings, including sound volume, visual themes, and knight/chessboard appearances. The game also includes features such as a move counter, timer, undo button, hint button, and pause/menu button.

## 3. Main Menu <a name="main-menu"></a>

The main menu is the starting point of the game. It provides options to start a new game, access game settings, view the tutorial, check high scores, and exit the game.

### Start Game
- Begins a new game.
- Players can select the difficulty level or board size here.

### Options/Settings
- Allows players to customize game settings.
- Options include sound volume, visual themes, and knight/chessboard appearances.

### Tutorial
- Provides a brief interactive or video tutorial on how the game is played.
- Details the knight's legal moves and other game mechanics.

### High Scores
- Displays a list of high scores.
- High scores can be filtered by board size or difficulty level.

### Exit
- Quits the game.

## 4. Game Window <a name="game-window"></a>

The game window is where the puzzle game is played. It displays the chessboard/grid, move counter, timer, undo button, hint button, and pause/menu button.

### Chessboard/Grid Display
- Centrally displays the game board.
- Clearly distinguishes between visited and unvisited squares.
- The current position of the knight is highlighted.

### Move Counter
- Shows the number of moves made by the player.

### Timer (Optional)
- Displays the time elapsed since the player started the current puzzle.

### Undo Button
- Allows the player to undo the last move.
- Limited to a certain number of uses.

### Hint Button
- Provides a hint for the next move.
- Limited to ensure the game remains challenging.

### Pause/Menu Button
- Pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

## 5. Options/Settings Window <a name="options-settings-window"></a>

The options/settings window allows players to customize various aspects of the game.

### Visual Settings
- Options to change the theme of the chessboard and the knight.
- Includes color schemes or graphical styles.

### Difficulty Settings
- Allows users to choose the size of the chessboard, affecting the difficulty.
- May offer toggles for advanced features like the timer.

## 6. High Scores Window <a name="high-scores-window"></a>

The high scores window displays a list of high scores achieved by players. It includes details such as player name, score (based on moves and time), and board size.

### Score List
- Displays a list of high scores.

### Filters
- Allows users to filter scores by board size or difficulty level.

## 7. Tutorial Window <a name="tutorial-window"></a>

The tutorial window provides an interactive step-by-step guide on how to play the game. It introduces the player to the game mechanics, including how the knight moves, the objective of the game, and any unique features such as hints and undos.

### Interactive Tutorial
- Guides the player through the game mechanics.

## 8. Pause Menu (In-Game) <a name="pause-menu-in-game"></a>

The pause menu appears when the player pauses the game. It provides options to resume the game, restart the game, access settings, or return to the main menu.

### Resume Game
- Returns to the game.

### Restart Game
- Starts a new game with the same settings.

### Settings
- Opens the options/settings window.

### Main Menu
- Returns to the main menu.
- Displays a warning about losing current game progress.

## 9. Additional Features <a name="additional-features"></a>

The Knight's Tour Puzzle Game includes additional features to enhance the gameplay experience.

### Game Mechanics
- Implements the knight's legal moves based on chess rules.
- Prevents the knight from visiting a square more than once.
- Detects when the player has successfully completed the tour or if the tour is no longer possible to complete.

### Levels and Challenges
- Offers boards of different sizes to cater to various levels of difficulty.
- Includes a timer and move counter to challenge players to complete the puzzle faster or in fewer moves.

### Scoring and Progression
- Implements a scoring system based on the time taken to complete the tour and the difficulty level of the board.
- Saves high scores and player progress.

### Tutorials and Hints
- Provides a brief interactive tutorial on how to play the game and move the knight.
- Offers hints or allows users to undo moves to help beginners.

## 10. Customization and Preferences <a name="customization-and-preferences"></a>

The Knight's Tour Puzzle Game allows players to customize the appearance of the chessboard and the knight.

### Customization Options
- Change the theme of the chessboard and the knight.
- Includes color schemes or graphical styles.

### Sound and Music
- Options to mute sounds or music.

---

Congratulations! You are now ready to enjoy the Knight's Tour Puzzle Game. Have fun solving the puzzles and challenging yourself with different board sizes and difficulty levels!