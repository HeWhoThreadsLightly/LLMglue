# Memory Match Game User Manual

## Introduction
Welcome to the Memory Match Game! This simple yet engaging game challenges your memory and concentration skills. The objective of the game is to find all the matching pairs of cards by remembering their locations. The game offers different difficulty levels, themes, and even a timer to make it more challenging and fun.

## Installation
To play the Memory Match Game, you need to install the following dependencies:

- Python (version 3.7 or higher)
- Tkinter library (version 8.6)

You can install the dependencies by running the following command in your terminal:

```
pip install -r requirements.txt
```

## Starting the Game
To start the Memory Match Game, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the game files are located.
3. Run the following command:

```
python main.py
```

4. The main menu window will appear.

## Main Menu
The main menu window is the starting point of the game. It provides several options for you to choose from. Here are the available options:

- **Title**: The game title is displayed prominently at the top of the window.
- **Play button**: Clicking this button takes you to the "Select Difficulty" window.
- **High scores button**: Opens a window displaying the high scores from previous games, including the player's name, score, and time.
- **Settings button**: Leads to a settings window where you can adjust sound preferences, choose themes, and view game instructions.
- **Exit button**: Clicking this button exits the game.

## Select Difficulty Window
In the "Select Difficulty" window, you can choose the difficulty level for the game. Here's how to use this window:

- **Instruction text**: A brief instruction on how to select the difficulty level.
- **Difficulty level buttons**: Buttons for each difficulty level (Easy, Medium, Hard). Clicking on one sets the game's difficulty and starts the game.
- **Back button**: Returns to the Main Menu.

## Game Window
The game window is where the actual gameplay takes place. Here's what you can expect in this window:

- **Game grid**: The central area where the cards are displayed according to the chosen difficulty level. Cards are arranged in a grid layout that changes size based on the difficulty.
- **Score panel**: A panel displaying the current number of attempts, number of matches found, and the elapsed time.
- **Pause/Menu Button**: Pauses the game and opens a small menu with options to resume, restart, change difficulty, or return to the Main Menu.

## Settings Window
The settings window allows you to customize various aspects of the game. Here's what you can do in this window:

- **Sound settings**: Toggle switches for game sound effects and background music.
- **Theme selection**: Dropdown menu or buttons to select the card and background theme.
- **Instructions**: A section that outlines the game rules and controls.
- **Back button**: Saves any changes and returns to the Main Menu.

## High Scores Window
The high scores window displays the top scores achieved in previous games. Here's what you can do in this window:

- **Scores display**: A list or table displaying the top scores, including details such as player name, score (based on attempts and time), and difficulty level.
- **Clear scores button**: An option to clear the high score history.
- **Back button**: Returns to the Main Menu.

## Game Over/Win Window
When you complete the game, the game over/win window will appear. Here's what you can do in this window:

- **Message**: Displays a congratulatory message for completing the game and shows the final score and time.
- **Play Again Button**: Restarts the game at the same difficulty level.
- **Change Difficulty Button**: Returns you to the "Select Difficulty" window to choose a new difficulty level.
- **Main Menu Button**: Returns you to the Main Menu.

## Additional Features
The Memory Match Game also includes some additional features to enhance your gaming experience. Here are the details:

- **Game logic**: The game has the ability to shuffle and randomly place the cards at the start of each game.
- **Difficulty levels**: The game offers three levels of difficulty: Easy (4x4 grid), Medium (6x6 grid), and Hard (8x8 grid). The difficulty level affects the number of cards and matches that need to be found.
- **Themes and customization**: You can choose from different themes for the cards, such as animals, space, and plants. Themes can change the background of the game board and the card designs.
- **Score and timing**: The game includes a timer to track how long it takes for you to complete the game. You will be scored based on the number of attempts made and the time taken to complete the game. The game also implements a high score feature that saves your best scores.
- **Settings and controls**: You can restart the game, change difficulty levels, and switch themes without restarting the application. The game also includes sound effects for flipping cards, finding a match, and winning the game, with an option to mute the sounds.
- **Development considerations**: The game implements data persistence for high scores and settings using local storage or a simple file-based approach.
- **Bonus features**: The game offers bonus features such as multiplayer mode where two players take turns to find matches, animations for flipping cards and winning the game, and leaderboards for high scores among different players.

## Accessibility Features
The Memory Match Game is designed with accessibility in mind. Here are the accessibility features included:

- **Keyboard navigation**: The game provides full functionality accessible via keyboard shortcuts to ensure that users who cannot use a mouse can navigate efficiently through the application. Tab navigation is implemented through all interactive elements in a logical order.
- **Screen reader support**: The game makes use of alt text to describe images, icons, and other non-textual elements. Labels and roles are used for complex elements to ensure their purpose and state are conveyed to screen reader users.
- **High contrast mode**: The game supports high contrast themes that make text, icons, and other elements more distinguishable for users with low vision. All text is readable, and interactive elements are visible against background colors.
- **Text size and font adjustments**: Users can adjust the text size without breaking the layout or losing functionality. The game supports the use of user-defined system fonts, including those designed for dyslexia.
- **Color blind mode**: The game implements color schemes that are accessible to users with various types of color blindness. Information conveyed with color is also distinguishable through patterns or shapes.
- **Magnification and zoom**: The game's interface and content can be magnified or zoomed in up to 200% without loss of content or functionality, accommodating users with low vision.
- **Feedback and error handling**: The game provides clear, understandable feedback for actions and descriptive error messages that offer guidance on how to resolve issues, accessible via both text and screen readers.

## Conclusion
The Memory Match Game is a fun and challenging game that tests your memory and concentration skills. With different difficulty levels, themes, and additional features, it offers a customizable and engaging gaming experience. Enjoy playing and have fun!