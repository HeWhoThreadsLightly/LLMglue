# Knight's Tour Puzzle Game User Manual

## Introduction

Welcome to the Knight's Tour Puzzle Game! This desktop application is based on the mathematical problem known as the "Knight's Tour". The objective of the game is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty.

## Installation

To install and run the Knight's Tour Puzzle Game, please follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Clone or download the game code from the repository: [link to repository]

3. Open a terminal or command prompt and navigate to the directory where you downloaded the game code.

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

## Main Menu

When you run the game, you will see the main menu. The main menu allows you to start a new game and select the difficulty level or board size.

![Main Menu](images/main_menu.png)

To start a new game, follow these steps:

1. Select the difficulty level from the dropdown menu. The available options are "Easy", "Medium", and "Hard".

2. Click the "Start Game" button to begin the game.

## Game Interface

Once you start the game, you will see the chessboard with the knight positioned on a square. Your goal is to move the knight across the board, visiting every square exactly once.

![Game Interface](images/game_interface.png)

To move the knight, simply click on a valid square on the chessboard. The knight will move to the selected square, and the board will be updated accordingly.

## Difficulty Levels

The game offers three difficulty levels: "Easy", "Medium", and "Hard". The difficulty level determines the size of the chessboard and the challenge of the game.

- Easy: 5x5 chessboard
- Medium: 6x6 chessboard
- Hard: 8x8 chessboard

## Game Over

The game is considered complete when the knight has visited every square on the chessboard exactly once. Once you achieve this, a message will be displayed indicating that you have successfully completed the game.

![Game Over](images/game_over.png)

## Quitting the Game

To quit the game at any time, simply close the game window or press the "X" button in the top-right corner of the window.

## Conclusion

Congratulations on completing the Knight's Tour Puzzle Game user manual! You are now ready to enjoy the game and challenge yourself with different difficulty levels. Have fun and happy gaming!