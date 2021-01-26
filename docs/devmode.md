# Developer Mode Docs
Developer Mode grants access to the extra features in the source code.

## How it works
Developer Mode acts similar to the Python interpreter. You can input a statement and the program will execute it. However, the accessible keywords (functions, variables, objects, etc.) are limited for security reasons. The accessible keywords will be listed later in the docs.

## Toggle Developer Mode
To enable Developer Mode, type `dev` when prompted:
```
Options: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Your move: dev
Developer Mode: True
Your move: 
```
When the terminal prints `Developer Mode: True`, you have successfully toggled on Developer Mode. To disable it, type `dev` while in Developer Mode:
```
Options: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Your move: dev
Developer Mode: True
Your move: dev
Developer Mode: False
Your move: 
```

## Using the extra features
Because the Developer Mode acts similarly to a Python interpreter, it can interpret any valid Python statement. However, this can also be dangerous. Because of this, the number of _keywords_ you can use are limited. The list of accessible _keywords_ are:

1. Built-in Functions
   - `print()`
   - `len()`
   - `str()`
2. Custom names
   - `ai.cells`
   - `train.autoplay()`

### Training with `train.autoplay()`
`train.autoplay()` is commonly used to speed up the learning process of the computer. With `train.autoplay()`, you don't have to play with the computer for hundreds of thousands of games. Instead, the function will play for you for an arbitrary number of games. Every time it's your turn, `train.autoplay()` will fill your move automatically so the computer can quickly provide a response.

>**Note:** You can use `autoplay()` alternatively.

The `train.autoplay()` function takes two parameters:
```
train.autoplay(iterations, showProgress)
```
`iterations`: Required. Takes an integer and plays the game automatically for an amount of games (rounds).

`showProgress`: Required. True means the board will be displayed during the process. False means the board will not be printed and only displays how much time is left until the whole process ends.

Take a look at these two examples:

#### **showProgress = True**
Input:
```
Your move: train.autoplay(1, True)
```
Output:
```
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  X  ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Past moves:  X4
Computer's move: 5
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  X  ██  O  ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Past moves:  X4O5
Options: [1, 2, 3, 6, 7, 8, 9]
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  X  ██  O  ██  X  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Past moves:  X4O5X6
Computer's move: 8
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  X  ██  O  ██  X  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██  O  ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Past moves:  X4O5X6O8
Options: [1, 2, 3, 7, 9]
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  X  ██  O  ██  X  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██  O  ██  X  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Past moves:  X4O5X6O8X9
Computer's move: 7
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  X  ██  O  ██  X  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  O  ██  O  ██  X  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Past moves:  X4O5X6O8X9O7
Options: [1, 2, 3]
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██  X  ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  X  ██  O  ██  X  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  O  ██  O  ██  X  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Past moves:  X4O5X6O8X9O7X2
Computer's move: 3
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██  X  ██  O  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  X  ██  O  ██  X  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  O  ██  O  ██  X  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Past moves:  X4O5X6O8X9O7X2O3
You Lose!
Score: 0 VS 1
##################################################
Autoplay finished after 1 games in 0.2555263042449951 seconds.
```
#### **showProgress = False**
Input:
```
Your move: train.autoplay(100, False)
```
Output:
```
Estimated Total Time: 0:00:00
Time Left: 0:00:00

Autoplay finished after 100 games in 0.019994020462036133 seconds.
```
Notice how `showProgress = False` is faster than `showProgress = True` even with more games played? This is because printing the progress takes more time, thus slowing the entire process. `showProgress = False` only prints the time information, so it saves time by processing the game in the background.

It is recommended to use `showProgress = False` to make the process more efficient. Use `showProgress = True` if you really want to see the process in detail.

### `ai.cells`, the decision tree
`ai.cells` is a dictionary that stores the explored game tree. When the application starts, `ai.cells` is just an empty dictionary. As you play (or `train.autoplay()`), the computer stores information about every game. Then, the computer will try to eliminate the losing moves so it can play optimally. This process is done automaticallyevery time a game ends.

>**Note:** You can use `cells` alternatively.

You can access `ai.cells` to examine the decision tree which the computer generated. For example:
```
Your move: print(ai.cells)
{'X7': [1, 2, 3, 4, 5, 6, 8, 9], 'X7O3X1': [2, 4, 5, 6, 8, 9], 'X7O3X1O4X9': [2, 5, 8], '': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'O4X2': [1, 3, 5, 6, 7, 8, 9], 'O4X2O1X6': [3, 5, 7, 8, 9], 'O4X2O1X6O9X5': [3, 7, 8, 7], 'X7O1X3': [2, 4, 5, 6, 8, 9], 'X7O1X3O2X6': [4, 5, 8, 9], 'X7O1X3O2X6O5X8': [9], 'O1X8': [2, 3, 4, 5, 6, 7, 9], 'O1X8O3X5': [2, 4, 6, 7, 9], 'O1X8O3X5O9X7': [2, 4, 6, 2], 'X1': [2, 3, 4, 5, 6, 7, 8, 9], 'X1O8X2': [3, 4, 5, 6, 7, 9], 'X1O8X2O4X6': [3, 5, 7, 9], 'X1O8X2O4X6O9X5': [3, 7], 'O8X4': [1, 2, 3, 5, 6, 7, 9], 'O8X4O3X6': [1, 2, 5, 7, 9], 'O8X4O3X6O7X2': [1, 5, 9, 5], 'X4': [1, 2, 3, 5, 6, 7, 8, 9], 'X4O9X6': [1, 2, 3, 5, 7, 8], 'X4O9X6O7X1': [2, 3, 5, 8], 'X4O9X6O7X1O3X8': [5], 'O5X1': [2, 3, 4, 6, 7, 8, 9], 'O5X1O2X3': [4, 6, 7, 8, 9, 8], 'X3': [1, 2, 4, 5, 6, 7, 8, 9], 'X3O8X5': [2, 4, 6, 7, 9], 'O5X8': [1, 2, 3, 4, 6, 7, 9], 'O5X8O4X3': [1, 2, 6, 7, 9], 'O5X8O4X3O9X1': [2, 6, 7], 'O5X8O4X3O9X1O2X7': [6, 6], 'X7O2X8': [1, 3, 4, 5, 6, 9], 'X7O2X8O3X4': [1, 5, 6, 9], 'X7O2X8O3X4O9X6': [1], 'O7X8': [1, 2, 3, 4, 5, 6, 9], 'O7X8O3X1': [2, 4, 5, 6, 9], 'O7X8O3X1O6X4': [2, 5, 9, 9], 'X5': [1, 2, 3, 4, 6, 7, 8, 9], 'X5O7X3': [1, 2, 4, 6, 8, 9], 'X5O7X3O2X1': [4, 6, 8, 9], 'X5O7X3O2X1O4X6': [9], 'O3X2': [1, 4, 5, 6, 7, 8, 9], 'O3X2O6X4': [1, 5, 7, 8, 9, 9], 'X7O6X2': [1, 3, 4, 5, 8, 9], 'X7O6X2O1X9': [3, 4, 5, 8], 'X7O6X2O1X9O3X5': [4, 8], 'O8X3': [1, 2, 4, 5, 6, 7, 9], 'O8X3O7X1': [2, 4, 5, 6, 9], 'O8X3O7X1O2X5': [4, 6, 9, 9], 'X5O4X7': [1, 2, 3, 6, 8, 9], 'X5O4X7O3X1': [2, 6, 8, 9], 'X5O4X7O3X1O2X8': [9], 'O8X5': [1, 2, 3, 4, 6, 7, 9], 'O8X5O1X6': [2, 3, 4, 7, 9], 'O8X5O1X6O3X2': [4, 9], 'X5O9X8': [1, 2, 3, 4, 6, 7], 'X5O9X8O2X4': [1, 3, 6, 7], 'X5O9X8O2X4O6X3': [1, 7], 'O1X7': [2, 3, 4, 5, 6, 8, 9], 'O1X7O5X9': [2, 3, 4, 6, 8], 'O1X7O5X9O3X6': [2, 4, 8, 2], 'X3O5X7': [1, 2, 4, 6, 8, 9], 'X3O5X7O4X1': [2, 6, 8, 9], 'X3O5X7O4X1O9X8': [2, 6], 'O3X5': [1, 2, 4, 6, 7, 8, 9], 'O3X5O7X4': [1, 6, 8, 9], 'X4O9X6O1X3': [2, 5, 7, 8, 5], 'O9X4': [1, 2, 3, 5, 6, 7, 8], 'O9X4O1X7': [2, 3, 5, 6, 8], 'O9X4O1X7O2X3': [5, 6, 8, 5], 'X4O6X3': [1, 2, 5, 7, 8, 9], 'X4O6X3O9X2': [1, 7, 8], 'O9X3': [1, 2, 4, 5, 6, 7, 8], 'O9X3O4X6': [1, 2, 5, 7, 8], 'O9X3O4X6O2X8': [1, 5, 7], 'O9X3O4X6O2X8O5X1': [7], 'X5O1X4': [2, 3, 6, 7, 8, 9], 'X5O1X4O3X7': [2, 6, 8, 9, 2], 'O8X6': [1, 2, 3, 4, 5, 7, 9], 'O8X6O7X1': [2, 3, 4, 5, 9], 'O8X6O7X1O4X2': [3, 9], 'X7O2X5': [1, 3, 4, 6, 8, 9], 'X7O2X5O6X8': [1, 3, 4, 9], 'X7O2X5O6X8O1X4': [3], 'O3X5O8X2': [1, 4, 6, 7, 9], 'O3X5O8X2O9X1': [4, 6, 7, 6], 'X5O6X2': [1, 3, 4, 7, 8, 9], 'X5O6X2O8X7': [1, 3, 4, 9], 'X5O6X2O8X7O3X1': [9], 'O5X7': [1, 2, 3, 4, 6, 8, 9], 'O5X7O8X4': [1, 2, 3, 6, 9, 2], 'X9': [1, 2, 3, 4, 5, 6, 7, 8], 'X9O2X3': [1, 4, 5, 6, 7, 8], 'X9O2X3O1X8': [4, 5, 6], 'O7X6': [1, 2, 3, 4, 5, 8, 9], 'O7X6O5X4': [1, 2, 3, 8, 9, 3], 'X9O6X2': [1, 3, 4, 5, 7, 8], 'X9O6X2O3X1': [4, 5, 7, 8], 'X9O6X2O3X1O5X4': [7], 'O9X5': [1, 2, 3, 4, 6, 7, 8], 'O9X5O2X4': [1, 3, 6, 7, 8], 'O9X5O2X4O8X7': [1, 3], 'X1O3X9': [2, 4, 5, 6, 7], 'X1O3X9O5X2': [4, 6, 7, 8], 'X1O3X9O5X2O4X8': [6, 7, 7], 'O3X9': [1, 2, 4, 5, 6, 7, 8], 'O3X9O8X5': [1, 2, 4, 6, 7], 'O3X9O8X5O6X2': [1, 4], 'X4O9X6O8X7': [1, 2, 3, 5], 'X4O9X6O8X7O1X2': [3, 5, 5], 'O7X8O9X4': [1, 2, 3, 5, 6], 'O7X8O9X4O5X2': [1, 3, 6], 'O7X8O9X4O5X2O6X1': [3, 3], 'X4O9X5': [1, 2, 3, 6, 7, 8], 'X4O9X5O1X2': [3, 6, 7, 8], 'X4O9X5O1X2O7X3': [6, 8, 8], 'O9X7': [1, 2, 3, 4, 5, 6, 8], 'O9X7O4X3': [1, 2, 5, 8], 'X3O9X1': [2, 4, 5, 6, 7, 8], 'X3O9X1O7X8': [2, 4, 5], 'O2X5': [1, 3, 4, 6, 7, 8, 9], 'O2X5O9X1': [3, 4, 6, 7, 8], 'O2X5O9X1O3X7': [4, 6, 8], 'O2X5O9X1O3X7O4X6': [8], 'X3O5X2': [1, 4, 6, 7, 8, 9], 'X3O5X2O7X4': [1, 6, 8], 'O8X2': [1, 3, 4, 5, 6, 7, 9], 'O8X2O1X6': [3, 4, 5, 7, 9], 'O8X2O1X6O5X4': [3, 7, 9], 'O8X2O1X6O5X4O7X3': [9, 9], 'X8': [1, 2, 3, 4, 5, 6, 7, 9], 'X8O2X4': [1, 3, 5, 6, 7, 9], 'X8O2X4O5X9': [1, 6, 7], 'O1X3': [2, 4, 5, 6, 7, 8, 9], 'O1X3O8X6': [2, 4, 5, 7, 9], 'O1X3O8X6O7X5': [2, 4, 9, 4], 'X4O1X3': [2, 5, 6, 7, 8, 9], 'X4O1X3O7X8': [2, 5, 6, 9], 'X4O1X3O7X8O6X9': [2, 5], 'O1X6': [2, 3, 4, 5, 7, 8, 9], 'O1X6O2X5': [3, 4, 8, 9], 'X6': [1, 2, 3, 4, 5, 7, 8, 9], 'X6O1X7': [2, 3, 4, 5, 8, 9], 'X6O1X7O9X4': [2, 3, 5, 8], 'X6O1X7O9X4O2X8': [3, 5, 3], 'O2X8': [1, 3, 4, 5, 6, 7, 9], 'O2X8O9X7': [1, 3, 4, 5, 6], 'O2X8O9X7O4X3': [1, 5, 6], 'O2X8O9X7O4X3O6X1': [5, 5], 'X7O1X9': [2, 3, 4, 6, 8], 'O8X6O4X5': [1, 2, 3, 7, 9], 'O8X6O4X5O7X3': [1, 2, 9, 9], 'X6O9X7': [1, 2, 3, 4, 5, 8], 'X6O9X7O5X3': [1, 2, 4, 8, 1], 'O5X4': [1, 2, 3, 6, 7, 8, 9], 'O5X4O7X3': [1, 2, 6, 8, 9], 'O5X4O7X3O6X9': [1, 2, 8], 'O5X4O7X3O6X9O8X1': [2, 2], 'X7O9X6': [1, 2, 3, 4, 5, 8], 'X7O9X6O4X1': [2, 3, 5, 8], 'X7O9X6O4X1O5X8': [2, 3], 'O3X8': [1, 2, 4, 5, 6, 7, 9], 'O3X8O2X6': [1, 4, 5, 7, 9], 'O3X8O2X6O5X9': [1, 4, 7, 1], 'X6O8X7': [1, 2, 3, 4, 5, 9], 'X6O8X7O1X5': [2, 3, 9], 'O6X2': [1, 3, 4, 5, 7, 8, 9], 'O6X2O7X9': [1, 3, 4, 5, 8], 'O6X2O7X9O8X4': [1, 3, 5], 'O6X2O7X9O8X4O3X1': [5, 5], 'X1O5X8': [2, 3, 4, 6, 7, 9], 'X1O5X8O9X2': [3, 4, 6, 7], 'X1O5X8O9X2O4X6': [3, 7], 'O3X7': [1, 2, 4, 5, 6, 8, 9], 'O3X7O4X6': [1, 2, 5, 8, 9], 'O3X7O4X6O2X8': [1, 5, 9, 1], 'X6O3X7': [1, 2, 4, 5, 8, 9], 'X6O3X7O2X1': [4, 5, 9], 'O9X4O1X8': [2, 3, 5, 6, 7], 'O9X4O1X8O2X6': [3, 5, 7, 5], 'X5O9X7': [1, 2, 3, 6, 8], 'O8X9': [1, 2, 3, 4, 5, 6, 7], 'O8X9O4X5': [1, 2, 3, 6, 7], 'O8X9O4X5O3X7': [1, 2, 6], 'O8X9O4X5O3X7O1X6': [2, 2], 'X3O9X6': [1, 2, 4, 5, 7, 8], 'X3O9X6O7X2': [1, 5, 8], 'O2X6': [1, 3, 4, 5, 7, 8, 9], 'O2X6O8X9': [3, 4, 5, 7], 'X8O6X9': [1, 2, 3, 4, 5, 7], 'X8O6X9O4X5': [2, 3, 7], 'O9X3O4X8': [1, 2, 5, 6, 7], 'O9X3O4X8O5X6': [1, 2, 7, 1], 'X5O6X9': [1, 2, 3, 4, 7, 8], 'X5O6X9O1X2': [3, 4, 7, 8], 'X5O6X9O1X2O4X7': [3], 'O3X5O6X7': [1, 2, 4, 8, 9], 'O3X5O6X7O1X4': [2, 8, 9], 'O3X5O6X7O1X4O8X9': [2, 2], 'O3X7O4X5': [1, 2, 6, 8, 9], 'O3X7O4X5O1X9': [2, 6, 8, 2], 'X7O4X1': [2, 3, 5, 6, 8, 9], 'X7O4X1O8X6': [2, 3, 5, 9], 'X7O4X1O8X6O5X9': [2, 3], 'O1X9': [2, 3, 4, 5, 6, 7, 8], 'O1X9O3X7': [2, 4, 5, 6, 8, 2], 'X4O6X1': [2, 3, 5, 7, 8, 9], 'X4O6X1O7X5': [2, 3, 8, 9], 'X4O6X1O7X5O3X8': [9], 'O9X5O4X6': [1, 2, 3, 7, 8], 'O9X5O4X6O7X8': [1, 2, 3, 1], 'X2': [1, 3, 4, 5, 6, 7, 8, 9], 'X2O6X3': [1, 4, 5, 7, 8, 9], 'X2O6X3O4X8': [1, 5, 9], 'O1X6O3X5': [2, 4, 7, 8, 9], 'O1X6O3X5O9X8': [2, 7], 'X4O9X8': [1, 2, 3, 5, 6, 7], 'X4O9X8O2X5': [1, 3, 6, 7], 'X4O9X8O2X5O7X1': [6], 'O8X3O1X6': [2, 4, 5, 7, 9], 'O8X3O1X6O4X7': [2, 9], 'X2O6X3O9X5': [4, 7, 8], 'O9X8': [1, 2, 3, 4, 5, 6, 7], 'O9X8O5X2': [1, 3, 4, 6, 7, 1], 'X6O9X7O2X8': [1, 3, 4, 5], 'X6O9X7O2X8O1X5': [3, 4, 3], 'O8X1': [2, 3, 4, 5, 6, 7, 9], 'O8X1O2X5': [3, 4, 6, 7, 9], 'O8X1O2X5O3X4': [6, 9], 'X7O5X6': [1, 2, 3, 4, 8, 9], 'X7O5X6O8X4': [1, 2, 3, 9, 2], 'O6X7': [1, 2, 3, 4, 5, 8, 9], 'O6X7O8X9': [1, 2, 3, 4, 5], 'O6X7O8X9O3X1': [2, 5], 'X5O9X2': [1, 3, 4, 6, 7, 8], 'X5O9X2O1X3': [6, 7, 8], 'O2X8O7X3': [1, 4, 5, 6, 9], 'O2X8O7X3O1X4': [5, 6, 9], 'O2X8O7X3O1X4O9X6': [5, 5], 'X8O9X1': [2, 3, 4, 5, 6, 7], 'X8O9X1O7X3': [2, 5, 6], 'O6X3': [1, 2, 4, 5, 7, 8, 9], 'O6X3O7X9': [1, 2, 4, 5, 8], 'O6X3O7X9O4X1': [2, 5, 8, 5], 'X6O7X4': [1, 2, 3, 5, 9], 'O2X9': [1, 3, 4, 5, 6, 7, 8], 'O2X9O1X3': [4, 5, 6, 7, 8], 'O2X9O1X3O6X5': [4, 7, 8], 'O2X9O1X3O6X5O7X4': [8], 'X6O1X7O2X4': [3, 5, 8, 9], 'X6O1X7O2X4O8X3': [5], 'O3X2O9X1': [4, 5, 6, 7, 8], 'O3X2O9X1O4X7': [5, 6, 8, 6], 'X6O2X8': [1, 3, 4, 5, 7, 9], 'X6O2X8O1X7': [3, 4, 5, 9, 3], 'O5X3': [1, 2, 4, 6, 7, 8, 9], 'O5X3O1X8': [2, 4, 6, 7, 9], 'O5X3O1X8O7X4': [2, 6, 9, 9], 'X9O7X8': [1, 2, 3, 4, 5, 6], 'X9O7X8O5X6': [1, 2, 3], 'O5X3O9X7': [1, 2, 4, 6, 8], 'O5X3O9X7O6X1': [4, 8]}
```
That was super long! If you do this after playing thousands or even millions of games, probably there will be not enough spaces to display it all. So it is not recommended to do after a lot of training, because it will print a lot of text. Really. **A LOT.**

You can also do this alternatively:
```
Your move: print(len(ai.cells))
263
```
Now you know how long the game tree is, with a more efficient space.