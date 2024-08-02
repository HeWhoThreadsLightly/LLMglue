# Knight's Tour Puzzle Game User Manual

## Introduction

Welcome to the Knight's Tour Puzzle Game! This desktop application is based on the mathematical problem known as the "Knight's Tour". The objective of the game is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty.

In this user manual, you will find instructions on how to install the game, navigate through the user interface, and play the game. Let's get started!

## Table of Contents

1. Installation
2. User Interface
   - Main Menu
   - Game Window
   - Options/Settings Window
   - High Scores Window
   - Tutorial Window
   - Pause Menu (In-Game)
3. How to Play
4. Scoring and Progression
5. Additional Features
6. Troubleshooting
7. Credits

## 1. Installation

To install the Knight's Tour Puzzle Game, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a command prompt or terminal window.

3. Navigate to the directory where you want to install the game.

4. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   Note: If you are using a virtual environment, make sure it is activated before running the command.

5. Once the installation is complete, you are ready to play the game!

## 2. User Interface

The Knight's Tour Puzzle Game has a user-friendly interface that allows you to navigate through different windows and interact with the game. Let's explore each window in detail.

### Main Menu

The Main Menu is the starting point of the game. It provides options to start a new game, customize game settings, access the tutorial, view high scores, and exit the game.

![Main Menu](images/main_menu.png)

- **Start Game**: Click on the "Start Game" button to begin a new game. You can select the difficulty level or board size before starting the game.

- **Options/Settings**: Click on the "Options/Settings" button to customize game settings. You can adjust sound volume, choose visual themes, and modify knight/chessboard appearances.

- **Tutorial**: Click on the "Tutorial" button to access a brief interactive or video tutorial on how to play the game. It provides details about the knight's legal moves and the objective of the game.

- **High Scores**: Click on the "High Scores" button to view a list of high scores. You can filter the scores by board size or difficulty level.

- **Exit**: Click on the "Exit" button to quit the game.

### Game Window

The Game Window is where the puzzle game is displayed. It consists of the chessboard/grid display, move counter, timer, undo button, hint button, and pause/menu button.

![Game Window](images/game_window.png)

- **Chessboard/Grid Display**: The centrally displayed chessboard/grid shows a clear distinction between visited and unvisited squares. The current position of the knight is highlighted.

- **Move Counter**: The move counter shows the number of moves made by the player.

- **Timer**: (Optional) The timer shows how long the player has been attempting the current puzzle.

- **Undo Button**: The undo button allows the player to undo the last move. This feature may be limited to a certain number of uses.

- **Hint Button**: The hint button provides a hint for the next move. This feature may be limited to ensure the game remains challenging.

- **Pause/Menu Button**: The pause/menu button pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

### Options/Settings Window

The Options/Settings Window allows you to customize various game settings, including visual settings and difficulty settings.

![Options/Settings Window](images/settings_window.png)

- **Visual Settings**: You can change the theme of the chessboard and the knight. This includes options for color schemes or graphical styles.

- **Difficulty Settings**: You can choose the size of the chessboard, which affects the difficulty. The window may also offer toggles for advanced features like the timer.

### High Scores Window

The High Scores Window displays a list of high scores achieved by players. It includes details such as player name, score (based on moves and time), and board size.

![High Scores Window](images/high_scores_window.png)

- **Score List**: The score list shows the high scores achieved by players. You can see the player name, score, and board size.

- **Filters**: You can filter the scores by board size or difficulty level to view specific high scores.

### Tutorial Window

The Tutorial Window provides an interactive step-by-step guide on how to play the game. It explains the game mechanics, including how the knight moves, the objective of the game, and any unique features like hints and undos.

![Tutorial Window](images/tutorial_window.png)

- **Interactive Tutorial**: The interactive tutorial guides you through the game mechanics. It explains how the knight moves and the objective of the game.

### Pause Menu (In-Game)

The Pause Menu appears when you pause the game. It allows you to resume the game, restart the game, access settings, or return to the main menu.

![Pause Menu](images/pause_menu.png)

- **Resume Game**: Click on the "Resume Game" option to return to the game.

- **Restart Game**: Click on the "Restart Game" option to start a new game with the same settings.

- **Settings**: Click on the "Settings" option to open the Options/Settings window.

- **Main Menu**: Click on the "Main Menu" option to return to the main menu. Note that this will result in losing the current game progress.

## 3. How to Play

To play the Knight's Tour Puzzle Game, follow these steps:

1. Launch the game by running the main.py script.

2. In the Main Menu, click on the "Start Game" button to begin a new game.

3. Select the difficulty level or board size according to your preference.

4. The Game Window will appear, displaying the chessboard/grid and other game elements.

5. Use your mouse to click on an unvisited square on the chessboard/grid to move the knight.

6. The move counter will update with each move you make.

7. Continue moving the knight across the chessboard/grid, aiming to visit every square exactly once.

8. Use the undo button to undo the last move if needed.

9. If you get stuck, you can use the hint button to get a hint for the next move.

10. The game will automatically detect when you have successfully completed the tour or if the tour is no longer possible to complete.

11. Once the game is completed, a message will appear congratulating you on your achievement.

12. You can then choose to start a new game, access settings, or return to the main menu.

## 4. Scoring and Progression

The Knight's Tour Puzzle Game includes a scoring system based on the time taken to complete the tour and the difficulty level of the board. The faster you complete the puzzle and the higher the difficulty level, the higher your score will be.

High scores and player progress are saved, allowing you to track your performance and improve your skills over time.

## 5. Additional Features

The Knight's Tour Puzzle Game includes additional features to enhance your gaming experience:

- **Levels and Challenges**: The game offers boards of different sizes to cater to various levels of difficulty. You can choose from options like 8x8, 6x6, or 10x10.

- **Timer and Move Counter**: The game includes a timer and move counter to challenge players to complete the puzzle faster or in fewer moves.

- **Undo Button**: The undo button allows you to undo the last move. However, this feature may be limited to a certain number of uses.

- **Hint Button**: The hint button provides a hint for the next move. This feature may also be limited to ensure the game remains challenging.

## 6. Troubleshooting

If you encounter any issues while installing or playing the Knight's Tour Puzzle Game, please try the following troubleshooting steps:

1. Make sure you have installed Python on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Double-check that you have installed all the required dependencies by running the command `pip install -r requirements.txt`

3. If the game does not launch or crashes, try restarting your computer and launching the game again.

4. If you are experiencing any specific issues or errors, please refer to the game's documentation or seek assistance from the support team.

## 7. Credits

The Knight's Tour Puzzle Game was developed by ChatDev, a software company powered by multiple intelligent agents. The game was designed and implemented by the Chief Product Officer and the development team at ChatDev.

We would like to express our gratitude to the customer for providing the requirements and allowing us to develop this puzzle game.

If you have any feedback or suggestions for improving the game, please feel free to reach out to us. We hope you enjoy playing the Knight's Tour Puzzle Game!

```