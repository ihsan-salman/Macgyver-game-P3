import pygame
from pygame.locals import *

# importation of moduls
import labyrinth as labyrinth 
import constants as constants



class Macgyver:
	def __init__(self, lab):
		self.lab = lab
		self.pos_x = 0
		self.pos_y = 14
		self.x = 0
		self.y = 14
		
		
	def move_right(self):
		if self.pos_x > (constants.NB_SPRITE - 1):
			if self.lab.structure[self.pos_x + 1][self.pos_y] != 'm':
				self.pos_x += 1
				self.x = self.pos_x * constants.SPRITE_SIZE
				print('move to the right')
