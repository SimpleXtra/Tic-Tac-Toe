# Tic Tac Toe
A simple Python 3 game project to learn and explore machine learning.

## About
In this program, you will play a series of games of Tic-tac-toe with a computer. The catch, for every game you play, the computer will learn to play better and eventually master the game (i.e. prevents your attempt at winning everytime).

This passion project demonstrates a simple machine learning algorithm by exploring the game tree and making the optimal decision.

## Installation
Simply download the source code and run the file.

## Gameplay
According to [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe),
> **Tic-tac-toe** is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner. It is a solved game with a forced draw assuming best play from both players.

### **Marking your spot**
This game is using CLI. Every new game, the terminal will look something like this:
```
Options: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Your move: 
```
Each numbers inside the brackets represents a vacant position in the board. The numbers change as you play the game. The distribution is:
```
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  1  ██  2  ██  3  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  4  ██  5  ██  6  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
██▀▀▀▀▀██▀▀▀▀▀██▀▀▀▀▀██
██  7  ██  8  ██  9  ██
██▄▄▄▄▄██▄▄▄▄▄██▄▄▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
```
Type the number location where you want to mark your symbol when prompted with `Your move: `. After that, the computer will automatically make his move. This goes on until either someone wins the game or the board is full and results in a draw.

### **Endgame**
After the game ends, the terminal then displays the result (win/lose/draw) and the current score. For example:
```
You win!
Score: 5 VS 2
Type 'r' to retry.

```
The score on the left is your score, and the right one is the computer's score. You will also be prompted to retry the game. Simply type `r` to replay. If you do, then the game will restart with the first turn swapped. If you typed anything else, or nothing at all, the application will close.

Please note that every game you play, the computer learns to play better. It doesn't look like it at first, but if you play some significant amount of games, the computer will try to prevent your attempt at winning every time.

**WARNING: If you quit the application, all of the computer progress will not be saved. The save feature will be added soon.**

## Developer Mode
Developer mode grants access to extra features of the game. Please read the [docs](docs/devmode.md) for further information on how to use it.

## Roadmap
The current features of the game are:

- Command-Line Interface
- Single-player mode with a computer (who is learning to play better)
- Alternating first-turn
- Scorekeeping
- Error handling (ex. invalid input from user)
- Developer Mode
  - Accessible game tree
  - Autoplay

There are some future planned features, such as:

- Swap symbols (X/O)
- Load/save game tree
- Further optimizations
- Adding a GUI

## Problems?
If you found any bugs, or would like to suggest a feature, please post it in Issues.