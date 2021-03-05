# Developer Mode Docs
Developer Mode grants access to the extra features in the source code.

## **How it works**
Developer Mode acts similar to the Python interpreter. You can input a statement and the program will execute it. However, the accessible keywords (functions, variables, objects, etc.) are limited for security reasons. The accessible keywords will be listed later in the docs.

>**Note:** The interface in this documentation uses the classic version (not connected to a terminal) to visualize the progress in which it could not be seen otherwise. The new version will not display things such as `Options`.
---
## **Toggle Developer Mode**
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
---
## **Using the extra features**
Because the Developer Mode acts similarly to a Python interpreter, it can interpret any valid Python statement. However, this can also be dangerous. Because of this, the number of _keywords_ you can use are limited. The list of accessible _keywords_ are:

1. Built-in Functions
   - `print()`
   - `len()`
   - `str()`
   - `quit()`

2. Custom names
   - `ai.cells`
   - `train.autoplay()`

### **Training with `train.autoplay()`**
`train.autoplay()` is commonly used to speed up the learning process of the computer. With `train.autoplay()`, you don't have to play with the computer for hundreds of thousands of games. Instead, the function will play for you for an arbitrary number of games. Every time it's your turn, `train.autoplay()` will fill your move automatically so the computer can quickly provide a response.

>**Note:** You can use `autoplay()` alternatively.

The `train.autoplay()` function takes two parameters:
```
train.autoplay(iterations, showProgress)
```
`iterations`: Required. Takes an integer and plays the game automatically for an amount of games (rounds).

`showProgress`: Required. True means the board will be displayed during the process. False means the board will not be printed and only displays how much time is left until the whole process ends.

Take a look at these two examples:

#### **Using `showProgress = True`**
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
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██     ██     ██     ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Autoplay finished after 1 games in 0.2555263042449951 seconds.
```
#### **Using `showProgress = False`**
Input:
```
Your move: train.autoplay(100, False)
```
Output:
```
Estimated Total Time: 00:00.05
Time Left: 00:00.04
Speed: 1669 games/s

Autoplay finished after 100 games in 00:00.07
```
Notice how `showProgress = False` is faster than `showProgress = True` even with more games played? This is because printing the progress takes more time, thus slowing the entire process. `showProgress = False` only prints the time information, so it saves time by processing the game in the background.

It is recommended to use `showProgress = False` to make the process more efficient. Use `showProgress = True` if you really want to see the process in detail.

### **`ai.cells`, the decision tree**
`ai.cells` is a dictionary that stores the explored game tree. When the application starts, `ai.cells` is just an empty dictionary. As you play (or `train.autoplay()`), the computer stores information about every game. Then, the computer will try to eliminate the losing moves so it can play optimally. This process is done automaticallyevery time a game ends.

>**Note:** You can use `cells` alternatively.

You can access `ai.cells` to examine the decision tree which the computer generated. Below is the example after playing five games.
```
Your move: print(ai.cells)
{'X7': [1, 2, 3, 4, 5, 6, 8, 9], 'X7O5X1': [2, 3, 4, 6, 8, 9], 'X7O5X1O4X9': [2, 3, 6, 8], 'X7O5X1O4X9O3X2': [6, 8], '': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'O2X8': [1, 3, 4, 5, 6, 7, 9], 'O2X8O9X5': [1, 3, 4, 6, 7], 'O2X8O9X5O7X1': [3, 4, 6], 'O2X8O9X5O7X1O4X6': [3], 'X8': [1, 2, 3, 4, 5, 6, 7, 9], 'X8O7X3': [1, 2, 4, 5, 6, 9], 'X8O7X3O6X2': [1, 4, 5, 9], 'X8O7X3O6X2O5X4': [1], 'O7X2': [1, 3, 4, 5, 6, 8, 9], 'O7X2O4X6': [1, 3, 5, 8, 9], 'O7X2O4X6O9X3': [1, 5, 8, 1], 'X8O5X3': [1, 2, 4, 6, 7, 9], 'X8O5X3O6X4': [1, 2, 7, 9], 'X8O5X3O6X4O2X9': [1, 7]}
```
We can see how the computer thinks what to move. However, if you try to do the same thing (`print(ai.cells)`) after playing thousands or even millions of games, there will be too many text to print. So it is not recommended to do after a lot of training, because it will print a lot of text. Really. **A LOT.**

Alternatively, you can try to visualize the size of the decison tree using this:
```
Your move: print(len(ai.cells))
19
```
Now you can imagine how big the game tree is, without having to display an enormous amount of text.