# Knight's Tour Puzzle Game User Manual

## Introduction

Welcome to the Knight's Tour Puzzle Game! This desktop application is based on the mathematical problem known as the "Knight's Tour". The objective of the game is to move a chess knight across a chessboard (or any m x n grid) so that it visits every square exactly once. The challenge increases with the size of the board, and the game offers various levels of difficulty.

In this user manual, you will find instructions on how to install the game, navigate through the user interface, customize settings, play the game, and access additional features. Let's get started!

## Table of Contents

1. Installation
2. User Interface
   - Main Menu
   - Game Window
   - Pause Menu
   - Options/Settings Window
   - Tutorial Window
   - High Scores Window
   - Filters Window
   - Visual Settings Window
   - Difficulty Settings Window
   - Sound Settings Window
3. Gameplay
   - Knight's Legal Moves
   - Preventing Revisiting Squares
   - Completing the Tour
   - Scoring and Progression
   - Tutorials and Hints
   - Customization and Preferences
4. Accessibility Features
   - Keyboard Navigation
   - Screen Reader Support
   - High Contrast Mode
   - Text Size and Font Adjustments
   - Color Blind Mode
   - Magnification and Zoom
   - Feedback and Error Handling

## 1. Installation

To install the Knight's Tour Puzzle Game, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt.

3. Navigate to the directory where you want to install the game.

4. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Once the installation is complete, you are ready to launch the game!

## 2. User Interface

The Knight's Tour Puzzle Game has a user-friendly interface that allows you to navigate through different windows and access various features. Let's explore each window and its functionalities.

### Main Menu

The Main Menu is the starting point of the game. It provides options to start a new game, customize settings, access tutorials, view high scores, and exit the game.

- **Start Game**: Clicking this button will begin a new game. You can select the difficulty level or board size before starting.

- **Options/Settings**: This button opens the Options/Settings window, where you can customize game settings such as sound volume, visual themes, and knight/chessboard appearances.

- **Tutorial**: Clicking this button opens the Tutorial window, which provides a brief interactive or video tutorial on how to play the game and details the knight's legal moves.

- **High Scores**: This button opens the High Scores window, where you can view a list of high scores. You can filter the scores by board size or difficulty level.

- **Exit**: Clicking this button will quit the game.

### Game Window

The Game Window is where the actual gameplay takes place. It displays the chessboard/grid, move counter, timer (optional), undo button, hint button, and pause/menu button.

- **Chessboard/Grid Display**: The game board is centrally displayed in this window. Visited and unvisited squares are clearly distinguished, and the current position of the knight is highlighted.

- **Move Counter**: This label shows the number of moves made by the player.

- **Timer** (Optional): If enabled, this label shows how long the player has been attempting the current puzzle.

- **Undo Button**: Clicking this button allows the player to undo the last move. The number of undo uses may be limited.

- **Hint Button**: Clicking this button provides a hint for the next move. The number of hints may be limited to maintain the game's challenge.

- **Pause/Menu Button**: Clicking this button pauses the game and opens a menu for accessing settings, returning to the main menu, or restarting the game.

### Pause Menu

The Pause Menu is accessed by clicking the Pause/Menu button in the Game Window. It provides options to resume the game, restart the game, access settings, or return to the main menu.

- **Resume Game**: Clicking this button returns to the game and continues from where it was paused.

- **Restart Game**: Clicking this button starts a new game with the same settings.

- **Settings**: Clicking this button opens the Options/Settings window.

- **Main Menu**: Clicking this button returns to the main menu. A warning about losing current game progress may be displayed.

### Options/Settings Window

The Options/Settings Window allows you to customize various game settings, including visual settings and difficulty settings.

- **Visual Settings**: This option allows you to change the theme of the chessboard and the knight. You can choose from different color schemes or graphical styles.

- **Difficulty Settings**: This option allows you to choose the size of the chessboard, which affects the difficulty. You may also find toggles for advanced features like the timer.

### Tutorial Window

The Tutorial Window provides a step-by-step guide on how to play the game and move the knight. It introduces the game mechanics, including the knight's legal moves, the objective of the game, and any unique features like hints and undos.

### High Scores Window

The High Scores Window displays a list of high scores achieved by players. It includes details such as player name, score (based on moves and time), and board size. You can filter the scores by board size or difficulty level.

### Filters Window

The Filters Window is accessed from the High Scores Window. It allows you to apply filters to the high scores list, such as filtering by board size or difficulty level.

### Visual Settings Window

The Visual Settings Window is accessed from the Options/Settings Window. It allows you to customize the appearance of the chessboard and the knight. You can choose different color schemes or graphical styles.

### Difficulty Settings Window

The Difficulty Settings Window is accessed from the Options/Settings Window. It allows you to choose the size of the chessboard, which affects the difficulty. You may also find toggles for advanced features like the timer.

### Sound Settings Window

The Sound Settings Window is accessed from the Options/Settings Window. It allows you to customize sound settings, such as adjusting the volume or muting sounds/music.

## 3. Gameplay

Playing the Knight's Tour Puzzle Game involves moving the knight across the chessboard to complete the tour. Here are some key aspects of the gameplay:

### Knight's Legal Moves

The knight moves in an L-shape, as it does in traditional chess. It can move two squares horizontally and one square vertically, or two squares vertically and one square horizontally. The knight can jump over other pieces on the board.

### Preventing Revisiting Squares

The objective of the game is to visit every square on the chessboard exactly once. The game mechanics prevent the knight from revisiting a square it has already visited.

### Completing the Tour

The game detects when the player has successfully completed the tour or if the tour is no longer possible to complete. You will receive a notification or message indicating the outcome.

### Scoring and Progression

The game implements a scoring system based on the time taken to complete the tour and the difficulty level of the board. The faster you complete the puzzle and the higher the difficulty, the higher your score will be. The game saves high scores and player progress.

### Tutorials and Hints

The game provides a tutorial to help you understand the game mechanics and how to move the knight. You can also access hints or undo moves to assist beginners.

### Customization and Preferences

The game allows you to customize the appearance of the chessboard and the knight. You can choose different visual themes, color schemes, or graphical styles. You can also mute sounds or adjust the volume according to your preferences.

## 4. Accessibility Features

The Knight's Tour Puzzle Game includes several accessibility features to ensure a user-friendly experience for all players. Here are some of the accessibility features:

- **Keyboard Navigation**: The game can be fully navigated using keyboard shortcuts, allowing users who cannot use a mouse to navigate efficiently through the application.

- **Screen Reader Support**: Alt text is used to describe images, icons, and other non-textual elements. Labels and roles are provided for complex elements to ensure their purpose and state are conveyed to screen reader users.

- **High Contrast Mode**: The game supports high contrast themes that make text, icons, and other elements more distinguishable for users with low vision. All text is readable, and interactive elements are visible against background colors.

- **Text Size and Font Adjustments**: Users can adjust the text size without breaking the layout or losing functionality. The game also supports user-defined system fonts, including those designed for dyslexia.

- **Color Blind Mode**: Color schemes are implemented to be accessible to users with various types of color blindness. Information conveyed with color is also distinguishable through patterns or shapes.

- **Magnification and Zoom**: The game's interface and content can be magnified or zoomed in up to 200% without loss of content or functionality, accommodating users with low vision.

- **Feedback and Error Handling**: The game provides clear and understandable feedback for actions. Error messages are descriptive and offer guidance on how to resolve issues. They are accessible via both text and screen readers.

## Conclusion

Congratulations! You are now familiar with the Knight's Tour Puzzle Game and how to use it. Enjoy playing the game, challenging yourself with different board sizes and difficulty levels, and strive for high scores! If you have any further questions or need assistance, please refer to the documentation or contact our support team.

Happy gaming!
```