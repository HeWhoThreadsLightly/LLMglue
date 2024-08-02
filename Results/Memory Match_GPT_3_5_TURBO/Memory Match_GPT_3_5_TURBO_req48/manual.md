# Memory Match Game User Manual

## Introduction

Welcome to the Memory Match Game! This simple yet engaging game is designed to test your memory skills by challenging you to find matching pairs of cards. The objective of the game is to flip over cards and remember their positions to find all the matching pairs.

This user manual will guide you through the installation process, explain the main functions of the game, and provide instructions on how to play.

## Installation

To install and run the Memory Match Game, please follow these steps:

1. Ensure that you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt and navigate to the directory where you want to install the game.

3. Clone the game repository from GitHub by running the following command:

   ```
   git clone https://github.com/your-username/memory-match-game.git
   ```

   Alternatively, you can download the game as a ZIP file from the GitHub repository and extract it to your desired location.

4. Navigate to the game directory:

   ```
   cd memory-match-game
   ```

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including Tkinter, which is used for the game's graphical user interface.

6. Once the installation is complete, you can start the game by running the following command:

   ```
   python main.py
   ```

   The game will open in a new window, and you can begin playing!

## Main Functions

The Memory Match Game offers several main functions to enhance your gaming experience. Let's explore each of them:

### Main Menu

When you start the game, you will be greeted with the Main Menu window. This window provides the following options:

- **Title**: The game title is displayed prominently at the top of the window.

- **Play button**: Clicking this button takes you to the "Select Difficulty" window, where you can choose the difficulty level for the game.

- **High scores button**: Opens a window displaying the high scores from previous games, including the player's name, score, and time.

- **Settings button**: Leads to a settings window where you can adjust sound preferences, choose themes, and view game instructions.

- **Exit button**: Clicking this button exits the game.

### Select Difficulty

In the "Select Difficulty" window, you can choose the difficulty level for the game. This window includes the following options:

- **Instruction text**: A brief instruction on how to select the difficulty level.

- **Difficulty level buttons**: Buttons for each difficulty level (Easy, Medium, Hard). Clicking on one sets the game's difficulty and starts the game.

- **Back button**: Returns to the Main Menu.

### Game Window

Once you have selected the difficulty level, the Game window will open. This window contains the following elements:

- **Game grid**: The central area where the cards are displayed according to the chosen difficulty level. The cards are arranged in a grid layout that changes size based on the difficulty.

- **Score panel**: A panel displaying the current number of attempts, number of matches found, and the elapsed time.

- **Pause/Menu Button**: Pauses the game and opens a small menu with options to resume, restart, change difficulty, or return to the Main Menu.

### Settings Window

The Settings window allows you to customize various aspects of the game. It includes the following options:

- **Sound settings**: Toggle switches for game sound effects and background music.

- **Theme selection**: Dropdown menu or buttons to select the card and background theme.

- **Instructions**: A section that outlines the game rules and controls.

- **Back button**: Saves any changes and returns to the Main Menu.

### High Scores Window

The High Scores window displays the top scores from previous games. It includes the following features:

- **Scores display**: A list or table displaying the top scores, including details such as player name, score (based on attempts and time), and difficulty level.

- **Clear scores button**: An option to clear the high score history.

- **Back button**: Returns to the Main Menu.

### Game Over/Win Window

When you complete the game, the Game Over/Win window will appear. This window includes the following options:

- **Message**: Displays a congratulatory message for completing the game and shows the final score and time.

- **Play Again Button**: Restarts the game at the same difficulty level.

- **Change Difficulty Button**: Returns you to the "Select Difficulty" window to choose a new difficulty level.

- **Main Menu Button**: Returns you to the Main Menu.

## How to Play

To play the Memory Match Game, follow these steps:

1. Start the game by running the `main.py` file as described in the installation instructions.

2. In the Main Menu window, click the "Play" button to proceed to the Select Difficulty window.

3. In the Select Difficulty window, choose the desired difficulty level by clicking on the corresponding button (Easy, Medium, or Hard).

4. The Game window will open, displaying the game grid and score panel. The cards will be face down.

5. Click on any card to flip it over and reveal its face. Remember the position and value of the card.

6. Click on another card to flip it over and reveal its face. If the two cards match, they will remain face up. If they do not match, they will be flipped back face down.

7. Continue flipping cards and finding matching pairs until all pairs have been found.

8. The game will keep track of the number of attempts, matches found, and elapsed time.

9. Once you have found all the matching pairs, the Game Over/Win window will appear, displaying your final score and time.

10. From the Game Over/Win window, you can choose to play again at the same difficulty level, change the difficulty level, or return to the Main Menu.

## Conclusion

Congratulations! You are now ready to enjoy the Memory Match Game. Challenge yourself by improving your memory skills and achieving high scores. Have fun and happy gaming!

If you encounter any issues or have any feedback, please don't hesitate to contact our support team. Enjoy the game!

```