# Memory Match Game User Manual

## Introduction
Welcome to the Memory Match Game! This simple yet engaging game will test your memory skills as you try to find matching pairs of cards. The objective is to flip over cards and remember their positions to find all the matching pairs. The game can be customized with different themes, difficulty levels, and even a timer to challenge yourself further.

## Installation
To play the Memory Match Game, you need to have Python installed on your computer. Follow these steps to install the necessary dependencies and run the game:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have downloaded or cloned the game files.
3. Create a virtual environment (optional but recommended):
   - Run `python -m venv venv` to create a virtual environment named "venv".
   - Activate the virtual environment:
     - On Windows: Run `venv\Scripts\activate`.
     - On macOS and Linux: Run `source venv/bin/activate`.
4. Install the required dependencies:
   - Run `pip install -r requirements.txt` to install the necessary packages.
5. Run the game:
   - Run `python main.py` to start the game.

## Main Menu
When you start the game, you will see the Main Menu window. Here are the options available in the Main Menu:

- **Title**: The game title is displayed prominently at the top of the window.
- **Play button**: Clicking this button takes you to the "Select Difficulty" window.
- **High scores button**: Opens a window displaying the high scores from previous games, including the player's name, score, and time.
- **Settings button**: Leads to a settings window where you can adjust sound preferences, choose themes, and view game instructions.
- **Exit button**: Clicking this button exits the game.

## Select Difficulty
In the "Select Difficulty" window, you can choose the difficulty level for the game. Here are the options available in the Select Difficulty window:

- **Instruction text**: A brief instruction on how to select the difficulty level.
- **Difficulty level buttons**: Buttons for each difficulty level (Easy, Medium, Hard). Clicking on one sets the game's difficulty and starts the game.
- **Back button**: Returns to the Main Menu.

## Game Window
Once you have selected the difficulty level, the Game Window will appear. Here are the elements of the Game Window:

- **Game grid**: The central area where the cards are displayed according to the chosen difficulty level. Cards are arranged in a grid layout that changes size based on the difficulty.
- **Score panel**: A panel displaying the current number of attempts, number of matches found, and the elapsed time.
- **Pause/Menu Button**: Pauses the game and opens a small menu with options to resume, restart, change difficulty, or return to the Main Menu.

## Settings Window
In the Settings Window, you can customize various aspects of the game. Here are the options available in the Settings Window:

- **Sound settings**: Toggle switches for game sound effects and background music.
- **Theme selection**: Dropdown menu or buttons to select the card and background theme.
- **Instructions**: A section that outlines the game rules and controls.
- **Back button**: Saves any changes and returns to the Main Menu.

## High Scores Window
The High Scores Window displays the top scores from previous games. Here are the options available in the High Scores Window:

- **Scores display**: A list or table displaying the top scores, including details such as player name, score (based on attempts and time), and difficulty level.
- **Clear scores button**: An option to clear the high score history.
- **Back button**: Returns to the Main Menu.

## Game Over/Win Window
When you complete the game, the Game Over/Win Window will appear. Here are the options available in the Game Over/Win Window:

- **Message**: Displays a congratulatory message for completing the game and shows the final score and time.
- **Play Again Button**: Restarts the game at the same difficulty level.
- **Change Difficulty Button**: Returns you to the "Select Difficulty" window to choose a new difficulty level.
- **Main Menu Button**: Returns you to the Main Menu.

## Additional Features
The Memory Match Game includes additional features to enhance your gaming experience:

- **Shuffling**: The game shuffles and randomly places the cards at the start of each game.
- **Card flipping**: You can flip cards and reveal their faces when clicked.
- **Matching**: The game checks for matches when two cards are flipped. If they match, they remain face up. Otherwise, they are flipped back.
- **Tracking**: The game keeps track of the number of attempts made and matches found.

## Conclusion
Now that you are familiar with the Memory Match Game and its features, you are ready to start playing! Have fun testing your memory skills and enjoy the game!