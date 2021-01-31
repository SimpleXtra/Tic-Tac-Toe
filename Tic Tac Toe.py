from math import floor
from random import choice
from datetime import datetime, timedelta
from traceback import print_exc

DEV_MODE = False

class Gameplay:	
	def __init__(self):
		self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
		self.stats.options = list(range(1, 10))
	
	def printBoard(self):
		for row in self.board:
			if row is self.board[0]: print("\u2584"*23)
			print(("\u2588"*2 + "\u2580"*5)*3 + "\u2588"*2)
			print("\u2588"*2, end = "  ")
			print(*row, sep = "  \u2588\u2588  ", end = "  \u2588\u2588\n")
			print(("\u2588"*2 + "\u2584"*5)*3 + "\u2588"*2)
			if row is self.board[2]: print("\u2580"*23)
	
	def draw(self, position: int, symbol: str):
		try:
			int(position)
		except ValueError:
			if position == "dev":
				global DEV_MODE
				DEV_MODE = not DEV_MODE
				print("Developer Mode:", DEV_MODE)
			elif DEV_MODE:
				try:
					if position == "": raise SyntaxError
					
					builtinAccess = {"print": print, "len": len, "str": str, "quit": quit, "True": True, "False": False}
					globalAccess = {"ai": ai, "cells": ai.cells, "train": train, "autoplay": train.autoplay}
					parse = compile(position, "<string>", "eval")
					for keyword in parse.co_names:
						if keyword not in builtinAccess and keyword not in globalAccess:
							raise NameError(keyword)
					
					result = eval(position, {"__builtins__": builtinAccess}, globalAccess)
					if result is not None: print(result)
				except NameError as keyword:
					keywords = list()
					root = list(globals().keys())
					level = 1
					
					for globalDirectory in root: keywords.append(globalDirectory)

					while level <= 3:
						nextLevelDirectories = list()
						
						for directory in root:
							subdirectories = dir(eval(directory))
							for subdirectory in subdirectories:
								keywords.append(subdirectory)
								nextLevelDirectories.append(subdirectory)
						
						nextLevelDirectories = root
						level += 1
					
					if str(keyword) in keywords:
						print(f"Error: Access blocked to keyword '{keyword}'.")
					else:
						print(f"Error: Keyword '{keyword}' does not exist.")
				except SyntaxError:
					if position == "": print("Error: No input given.")
					else: print("Error: Invalid syntax.")
				except Exception as message:
					print("Error:", message)
			else:
				print("Error: Invalid input.")
			
			if not train.isRunning:
				self.draw(input("Your move: "), symbol)
		else:
			position = int(position)
			
			if position not in self.stats.options:
				print("Error: Position unavailable.")
				self.draw(input("Your move: "), symbol)
			else:
				row = floor((position - 1) / 3)
				column = position - 1 - row * 3
				self.board[row][column] = symbol
				self.stats.options.remove(position)
				ai.history += symbol + str(position)
	
	def check(self):
		diagonalNWSE = list()
		diagonalSWNE = list()

		for index in range(3):
			if (len(set(self.board[index])) == 1 and self.board[index][0] != " ") or (self.board[0][index] == self.board[1][index] == self.board[2][index] and self.board[0][index] != " "):
				return True
			
			inversedRow = (2, 1, 0)
			diagonalNWSE.append(self.board[index][index])
			diagonalSWNE.append(self.board[inversedRow[index]][index])
		
		return (len(set(diagonalNWSE)) == 1 and diagonalNWSE[0] != " ") or (len(set(diagonalSWNE)) == 1 and diagonalSWNE[0] != " ")
	
	def end(self, result: bool = None):
		if result:
			if train.visible: print("You Win!")
			self.stats.score["player"] += 1
		elif result == False:
			if train.visible: print("You Lose!")
			self.stats.score["computer"] += 1
		elif result == None and train.visible:
			print("It's a draw!")
		
		if train.visible: print("Score:", self.stats.score["player"], "VS", self.stats.score["computer"])
		
		if train.isRunning:
			train.gameNo += 1
			train.updateTimeInfo()
		else:
			print("Type 'r' to retry.")
	
	class stats:
		options = list(range(1, 10))
		score = {"player": 0, "computer": 0}
		players = ("computer", "player")
		playerTurn = True
		firstTurn = players[int(playerTurn)]

		def changeTurn(self):
			self.playerTurn = not self.playerTurn

		def changeFirstTurn(self):
			self.firstTurn = self.players[int(not bool(self.players.index(self.firstTurn)))]
			self.playerTurn = bool(self.players.index(self.firstTurn))

class Computer:
	cells = dict()
	history = ""

	def analyze(self, result: bool = None):
		if result == False:		#Computer wins
			lastMove = int(self.history[-1])
			self.cells[self.history[0:-2]].append(lastMove)
		elif result:			#Computer loses
			trimIndex = -4
			lastMoveIndex = -3
			self.cells[self.history[0:-4]].remove(int(self.history[lastMoveIndex]))
			
			while len(self.cells[self.history[0:trimIndex]]) == 0:
				trimIndex -= 4
				lastMoveIndex -= 4
				self.cells[self.history[0:trimIndex]].remove(int(self.history[lastMoveIndex]))

	def move(self):
		if self.history not in self.cells.keys(): self.cells[self.history] = game.stats.options.copy()
		selection = choice(self.cells[self.history])
		if train.visible: print("Computer's move:", selection)
		game.draw(selection, "O")
	
	class Training:
		def __init__(self):
			self.isRunning = False
			self.visible = True
		
		def autoplay(self, iterations: int, showProgress: bool):
			if not self.isRunning:
				self.limit = iterations
				self.gameNo = 0
				self.startTime = datetime.now()
				self.timeSinceLastUpdate = datetime.now() - timedelta(seconds = 5)
				game.draw(choice(game.stats.options), "X")
			
			self.isRunning = self.gameNo < iterations
			self.visible = showProgress if self.isRunning else True

			elapsed = datetime.now() - self.startTime + datetime.strptime("0", "%S")
			if not self.isRunning: print("Autoplay finished after", iterations, "games in", elapsed.strftime("%M:%S.%f")[:-4], "\n")
		
		def updateTimeInfo(self):
			if datetime.now() - self.timeSinceLastUpdate >= timedelta(seconds = 5) and not self.visible:
				elapsedTime = (datetime.now() - self.startTime).total_seconds()
				estimatedTime = datetime.fromtimestamp(float(self.limit / self.gameNo) * elapsedTime)
				remaining = estimatedTime - datetime.now() + self.startTime
				speed = round(self.gameNo / elapsedTime)
				print("Estimated Total Time:", estimatedTime.strftime("%M:%S.%f")[:-4])
				print("Time Left:", remaining.strftime("%M:%S.%f")[:-4])
				print("Speed:", speed, "games/s\n")
				self.timeSinceLastUpdate = datetime.now()

game = Gameplay()
ai = Computer()
train = ai.Training()

while True:
	try:
		if game.stats.playerTurn:
			if train.visible: print("Options:", str(game.stats.options))
			playerMove = choice(game.stats.options) if train.isRunning else input("Your move: ")
			game.draw(playerMove, "X")
		else:
			ai.move()
		
		if train.visible:
			game.printBoard()
			print()
			if DEV_MODE: print("Past moves: ", ai.history)
		
		win = game.stats.playerTurn if game.check() else None
		
		if game.check() or len(game.stats.options) == 0:
			game.end(win)
			ai.analyze(win)
			prompt = input() if not train.isRunning else "r"
			
			if prompt == "r":
				del game
				game = Gameplay()
				game.stats.changeFirstTurn(game.stats)
				ai.history = ""
				if train.visible: print("#"*50)
				if train.isRunning: train.autoplay(train.limit, train.visible)
				continue
			else:
				quit()
		
		game.stats.changeTurn(game.stats)
	except Exception:
		print_exc()
		
		if input("\nPrint backup data? (Yes/No) ").lower() == "yes":
			print("-"*50 + "\n" + "BACKUP DATA".center(50) + "\n" + "-"*50)
			print("Moves history on last game:", ai.history)
			print("Last board situation:")
			game.printBoard()
			print("Computer's dictionary based on last history:", ai.cells.get(ai.history))
			if input("Print full dictionary? (Yes/No) ").lower() == "yes":
				print("Computer's full dictionary:", ai.cells, sep = "\n")
		
		print("Session ended.")
		input("Press enter/return to close the application.")
		quit()