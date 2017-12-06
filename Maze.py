import pygame
import sys
import Ghost
import Pacman
class Maze:

	def __init__(self, imgfile):
		pygame.init()
		"""
		self.walls_file = open('Maze.txt','r')
		self.wallrect_array = []
		for symbol in self.file:
			if symbol == "%":
				#pacman.moveable = False
				for i in range(18):
					for j in range(18):
						wallrect_array[] = pygame.Rect(i, j, 37, 37)
		"""
		self.walls_file = open('Maze(1).txt', 'r')
		for line in self.walls_file:
			if symbol == "%":
				#pacman.moveable = False
				for i in range(18):
					for j in range(18):
						pygame.Rect(i, j, 37, 37)
			elif symbol == ".":
				cookie.insertCookie()
			elif symbol == "o":
				insertSpecialCookie()
			elif symbol == "G":
				insertGhost()
			elif symbol == "P":
				insertPacman()
				
		self.empty_maze = pygame.image.load('empty_maze.png').convert()
		self.pacman = pygame.load('pacman_whole.png').convert()
		
	def showWalls(self):
		return image
	def makeWalls(self):
		pass
	def insertCookie(self):
		pygame.draw.circle(self, white, (mylist[i]), 2, width = 2)
		pacman.moveable = True
	def insertSpecialCookie(self):
		pygame.draw.circle(self, blue, (mylist[i]), 4, width = 4)
		pacman.moveable = True
	def insertGhost(self):
		for i in range(4):
			self.ghost.append(ghost.Ghost("Boogie", x, y, 'ghost.png' ))
			self.sprites = pygame.sprite.Group(self.enemies)
	def insertPacman(self):
		pass
		
