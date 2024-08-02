# Memory Match Game User Manual

## Introduction

Welcome to the Memory Match Game! This simple yet engaging game is designed to test your memory skills. The objective of the game is to find all the matching pairs of cards by remembering their locations. The game can be played on your desktop and offers different themes, difficulty levels, and even a timer to challenge yourself further.

## Installation

To play the Memory Match Game, you need to install the following dependencies:

- Python (version 3.6 or higher)
- Tkinter library

To install the dependencies, follow these steps:

1. Open a terminal or command prompt.
2. Run the following command to install Python:

```
pip install python
```

3. Run the following command to install the Tkinter library:

```
pip install tkinter
```

4. Download the game files from the provided source.

## Starting the Game

Once you have installed the dependencies and downloaded the game files, follow these steps to start the game:

1. Open a terminal or command prompt.
2. Navigate to the directory where you downloaded the game files.
3. Run the following command to start the game:

```
python main.py
```

4. The game's main menu window will appear.

## Main Menu

The main menu window is the starting point of the game. It consists of the following elements:

- Title: The game title is displayed prominently at the top of the window.
- Play button: Clicking this button will take you to the "Select Difficulty" window.

## Select Difficulty

In the "Select Difficulty" window, you can choose the difficulty level of the game. The available options are:

- Easy: A grid of 4x4 cards.
- Medium: A grid of 6x6 cards.
- Hard: A grid of 8x8 cards.

To select a difficulty level, click on the corresponding button. Once you have selected a difficulty level, the game will start.

## Gameplay

The gameplay consists of the following steps:

1. The game will present you with a grid of face-down cards.
2. Click on a card to flip it and reveal its value.
3. Click on another card to flip it as well.
4. If the two flipped cards have the same value, they will remain face-up.
5. If the two flipped cards have different values, they will be flipped face-down again.
6. Repeat steps 2-5 until you have found all the matching pairs.
7. The game ends when all the pairs have been found.

## Themes

The Memory Match Game offers different themes to customize the appearance of the cards. To change the theme, follow these steps:

1. Open the `game.py` file in a text editor.
2. Locate the `create_grid` method.
3. Modify the `button` variable to set the desired theme. For example:

```python
button = tk.Button(text="?", command=lambda c=card: self.flip_card(c), bg="blue", fg="white")
```

4. Save the changes and restart the game.

## Difficulty Levels

The Memory Match Game offers three difficulty levels: Easy, Medium, and Hard. The difficulty level determines the size of the grid and the number of cards. To change the difficulty level, follow these steps:

1. Open the `game.py` file in a text editor.
2. Locate the `__init__` method.
3. Modify the `self.grid_size` variable to set the desired difficulty level. For example:

```python
self.grid_size = 6  # Medium difficulty
```

4. Save the changes and restart the game.

## Timer

The Memory Match Game can be enhanced with a timer to challenge yourself further. To add a timer to the game, follow these steps:

1. Open the `game.py` file in a text editor.
2. Locate the `start` method.
3. Add a timer widget to the game window. For example:

```python
timer_label = tk.Label(self.root, text="00:00", font=("Arial", 16))
timer_label.pack()
```

4. Implement the timer logic in the game. For example, update the timer label every second:

```python
def update_timer(self):
    # Update the timer label every second
    current_time = time.strftime("%M:%S", time.gmtime(self.elapsed_time))
    self.timer_label.config(text=current_time)
    self.elapsed_time += 1
    self.root.after(1000, self.update_timer)
```

5. Save the changes and restart the game.

## Conclusion

Congratulations! You are now ready to enjoy the Memory Match Game. Test your memory skills, challenge yourself with different difficulty levels, and have fun finding all the matching pairs. Good luck!