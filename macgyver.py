import pygame
from pygame.locals import *

# importation of moduls
import labyrinth as labyrinth
import constants as constants



class Macgyver:
	def __init__(self, struc):
		self.pos_x = 0
		self.pos_y = 0
		self.x = 0
		self.y = 14
		self.map = struc
		
		
	def move_right(self):
		if self.pos_x > 0:
			if self.map.structure[self.pos_x][self.pos_y + 1] != 'm':
				self.pos_x += 1 
				self.x = self.pos_x * constants.SPRITE_SIZE
				
	"""	
		
	def move_down(self):
		
		
	def move_right(self):
		
		
	def move_left(self):"""
	
