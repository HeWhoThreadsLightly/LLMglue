# Memory Match Game User Manual

## Introduction

Welcome to the Memory Match Game! This simple yet engaging game challenges your memory and concentration skills. The objective of the game is to find all the matching pairs of cards by remembering their locations. The game features different themes, difficulty levels, and a timer to make it more challenging and fun.

## Installation

To play the Memory Match Game, you need to have Python installed on your computer. Follow these steps to install the necessary dependencies and run the game:

1. Open a terminal or command prompt.

2. Clone the repository or download the source code from [GitHub](https://github.com/your-repo-url).

3. Navigate to the project directory.

4. Create a virtual environment (optional but recommended).

   ```shell
   python -m venv venv
   ```

5. Activate the virtual environment (optional but recommended).

   - For Windows:

     ```shell
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```shell
     source venv/bin/activate
     ```

6. Install the required dependencies.

   ```shell
   pip install -r requirements.txt
   ```

7. Run the game.

   ```shell
   python main.py
   ```

## Main Menu

When you run the game, you will see the Main Menu window. The Main Menu provides several options to start, customize, and exit the game.

### Title

The game title is displayed prominently at the top of the Main Menu window.

### Play Button

Clicking the "Play" button takes you to the "Select Difficulty" window, where you can choose the difficulty level and start the game.

### High Scores Button

Clicking the "High Scores" button opens a window displaying the high scores from previous games. The high scores include the player's name, score, and time.

### Settings Button

Clicking the "Settings" button leads to a settings window where you can adjust sound preferences, choose themes, and view game instructions.

### Exit Button

Clicking the "Exit" button closes the game.

## Select Difficulty

In the "Select Difficulty" window, you can choose the difficulty level for the game. The difficulty level determines the size of the game grid and the number of cards to match.

### Instruction Text

A brief instruction is provided on how to select the difficulty level.

### Difficulty Level Buttons

There are three difficulty level buttons: Easy, Medium, and Hard. Clicking on one of these buttons sets the game's difficulty and starts the game.

### Back Button

The "Back" button returns you to the Main Menu.

## Game Window

The Game Window is where the Memory Match game is played. It consists of the game grid and a score panel.

### Game Grid

The game grid is the central area where the cards are displayed. The grid layout changes size based on the chosen difficulty level. Each card is initially face down.

### Score Panel

The score panel displays the current number of attempts, the number of matches found, and the elapsed time.

### Pause/Menu Button

The Pause/Menu button pauses the game and opens a small menu with options to resume, restart, change difficulty, or return to the Main Menu.

## Settings Window

The Settings Window allows you to customize various aspects of the game.

### Sound Settings

Toggle switches are provided for game sound effects and background music. You can turn these on or off according to your preference.

### Theme Selection

You can choose different themes for the cards and the background of the game board. Themes include animals, space, and plants.

### Instructions

A section is provided that outlines the game rules and controls. It explains how to play the game and find matching pairs.

### Back Button

The "Back" button saves any changes made in the settings and returns you to the Main Menu.

## High Scores Window

The High Scores Window displays the top scores from previous games.

### Scores Display

A list or table is shown, displaying the player's name, score (based on attempts and time), and difficulty level.

### Clear Scores Button

An option is provided to clear the high score history. Clicking this button will remove all the saved high scores.

### Back Button

The "Back" button returns you to the Main Menu.

## Game Over/Win Window

When you complete the game by finding all the matching pairs, the Game Over/Win Window is displayed.

### Message

A congratulatory message is shown for completing the game. The final score and time taken to complete the game are also displayed.

### Play Again Button

Clicking the "Play Again" button restarts the game at the same difficulty level.

### Change Difficulty Button

The "Change Difficulty" button returns you to the "Select Difficulty" window, where you can choose a new difficulty level.

### Main Menu Button

Clicking the "Main Menu" button returns you to the Main Menu.

## Additional Features

The Memory Match Game includes additional features to enhance your gaming experience.

### Game Logic

- The game shuffles and randomly places the cards at the start of each game.

- You can flip cards and reveal their faces by clicking on them.

- The game checks for matches when two cards are flipped. If they match, they remain face up. Otherwise, they are flipped back.

- The game keeps track of the number of attempts made and matches found.

- A win condition is implemented when all matches are found.

### Difficulty Levels

- The game provides three levels of difficulty: Easy, Medium, and Hard. The grid size and the number of cards to match vary based on the difficulty level.

### Themes and Customization

- You can choose from different themes for the cards, such as animals, space, and plants. Themes also change the background of the game board and the card designs.

### Score and Timing

- The game includes a timer to track how long it takes for you to complete the game.

- Your score is calculated based on the number of attempts made and the time taken to complete the game.

- A high score feature is implemented to save your best scores.

### Settings and Controls

- You can restart the game, change difficulty levels, and switch themes without restarting the application.

- Sound effects are included for flipping cards, finding a match, and winning the game. You can mute the sounds if desired.

### Development Considerations

- Data persistence is implemented for high scores and settings. The game saves your high scores and settings locally.

### Bonus Features

- A multiplayer mode is available where two players take turns to find matches.

- Animations are added for flipping cards and winning the game.

- Leaderboards are implemented for high scores among different players.

## Conclusion

Congratulations! You are now ready to enjoy the Memory Match Game. Have fun challenging your memory and concentration skills, and strive to achieve the highest scores. If you have any questions or need further assistance, please refer to the documentation or contact our support team.

```