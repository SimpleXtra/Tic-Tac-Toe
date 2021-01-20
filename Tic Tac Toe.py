import math
import random
import time
import datetime

DEV_MODE = False

class Gameplay:	
	def __init__(self):
		self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
		self.stats.options = list(range(1, 10))
	
	def printBoard(self):
		for row in self.board:
			print(*row, sep = " | ")
			if row is not self.board[2]:
				print("-"*9)
	
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
					builtinAccess = {"print": print, "len": len, "str": str, "True": True, "False": False}
					globalAccess = {"comp": comp, "cells": comp.cells, "autoplay": autoplay}
					parse = compile(position, "<string>", "eval")
					for keyword in parse.co_names:
						if keyword not in builtinAccess and keyword not in globalAccess:
							raise NameError(keyword)
					eval(position, {"__builtins__": builtinAccess}, globalAccess)
				except NameError as keyword:
					keywords = list(dir(__builtins__) + dir(globals()) + dir(locals()) + dir(Gameplay) + dir(Computer) + list(globals().keys()) + list(locals().keys()))
					if str(keyword) in keywords:
						print(f"Error: Access blocked to keyword '{keyword}'.")
					else:
						print(f"Error: Keyword '{keyword}' does not exist.")
				except SyntaxError:
					if position == "": print("Error: No input given.")
					else: print("Error: Invalid syntax.")
				except Exception as message:
					print("Error: ", message)
			else:
				print("Error: Invalid input.")
			if not isAutoplay:
				self.draw(input("Your move: "), symbol)
		else:
			position = int(position)
			if position not in self.stats.options:
				print("Error: Position unavailable.")
				self.draw(input("Your move: "), symbol)
			else:
				row = math.floor((position - 1) / 3)
				column = position - 1 - row * 3
				self.board[row][column] = symbol
				self.stats.options.remove(position)
				comp.history += symbol + str(position)
	
	def check(self):
		diagList = list()
		diagList2 = list()

		for x in range(3):
			if (len(set(self.board[x])) == 1 and self.board[x][0] != " ") or (self.board[0][x] == self.board[1][x] == self.board[2][x] and self.board[0][x] != " "):
				return True
			y = (2, 1, 0)
			diagList.append(self.board[x][x])
			diagList2.append(self.board[y[x]][x])
		
		return (len(set(diagList)) == 1 and diagList[0] != " ") or (len(set(diagList2)) == 1 and diagList2[0] != " ")
	
	def end(self, result: bool = None):
		global isAutoplay
		global progressVisible
		if result == True:
			if progressVisible: print("You Win!")
			self.stats.score["player"] += 1
		elif result == False:
			if progressVisible: print("You Lose!")
			self.stats.score["computer"] += 1
		elif result == None and progressVisible:
			print("It's a draw!")
		if progressVisible: print("Score:", self.stats.score["player"], "VS", self.stats.score["computer"])
		if isAutoplay:
			autoplay.round += 1
			if time.time() - autoplay.timeSinceLastUpdate >= 5:
				delta = time.time() - autoplay.startTime
				estTime = (float(autoplay.limit) / autoplay.round) * delta
				remaining = autoplay.startTime + estTime - time.time()
				print("Estimated Total Time:", datetime.timedelta(seconds = estTime))
				print("Time Left:", datetime.timedelta(seconds = remaining), "\n")
				autoplay.timeSinceLastUpdate = time.time()
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
	
	def __init__(self):
		self.history = ""
	
	def insertNewCell(self):
		if self.history not in self.cells.keys():
			self.cells[self.history] = game.stats.options.copy()

	def analyze(self, result: bool = None):
		if result == False:		#Computer wins
			lastMove = int(self.history[-1])
			self.cells[self.history[0:-2]].append(lastMove)
		elif result:			#Computer loses
			lastMove = int(self.history[-3])
			trim = -4
			prev = -3
			self.cells[self.history[0:-4]].remove(lastMove)
			while len(self.cells[self.history[0:trim]]) == 0:
				trim -= 4
				prev -= 4
				self.cells[self.history[0:trim]].remove(int(self.history[prev]))

	def move(self):
		self.insertNewCell()
		selection = random.choice(self.cells[self.history])
		if progressVisible: print("Computer's move:", selection)
		game.draw(selection, "O")

def autoplay(iterations: int, showProgress: bool):
	global isAutoplay
	global progressVisible
	
	if not isAutoplay:
		autoplay.limit = iterations
		autoplay.round = 0
		autoplay.startTime = time.time()
		autoplay.timeSinceLastUpdate = time.time() - 5
		game.draw(random.choice(game.stats.options), "X")
	
	isAutoplay = autoplay.round < iterations
	progressVisible = showProgress if autoplay.round < iterations else True
	if autoplay.round >= iterations: print("Autoplay finished after", iterations, "games in", time.time() - autoplay.startTime, "seconds.\n")

game = Gameplay()
comp = Computer()
isAutoplay = False
progressVisible = True

while True:
	try:
		if game.stats.playerTurn:
			if progressVisible: print("Options:", str(game.stats.options))
			playerMove = random.choice(game.stats.options) if isAutoplay else input("Your move: ")
			game.draw(playerMove, "X")
		else:
			comp.move()
		if progressVisible:
			game.printBoard()
			print()
			if DEV_MODE: print("Past moves: ", comp.history)
		win = game.stats.playerTurn if game.check() else None
		if game.check() or len(game.stats.options) == 0:
			game.end(win)
			comp.analyze(win)
			prompt = input() if not isAutoplay else "r"
			if prompt == "r":
				del game
				game = Gameplay()
				game.stats.changeFirstTurn(game.stats)
				comp.history = ""
				if progressVisible: print("#"*50)
				if isAutoplay: autoplay(autoplay.limit, progressVisible)
				continue
			else:
				quit()
		game.stats.changeTurn(game.stats)
	except Exception as e:
		print("Something went wrong. Error:", e)
		print("BACKUP DATA")
		print("Moves History on last game:", comp.history)
		print("Last board situation:")
		game.printBoard()
		print("Computer's dictionary based on last history:", comp.cells.get(comp.history))
		if input("Print full dictionary?") == "Yes":
			print("Computer's full dictionary:", comp.cells, sep = "\n")
		print("Session ended.")
		quit()