# importation of moduls
import pygame 
import constants as constants

"""character's responsible class"""

class Macgyver:
	def __init__(self, labyrinth):
		self.labyrinth = labyrinth
		self.pos_x = 0
		self.pos_y = 14
		self.macgyver = pygame.image.load(constants.IMAGE_MACGYVER).convert_alpha()
		self.display()
	
	def display(self):
		self.labyrinth.screen.blit(self.macgyver, (self.pos_x * constants.SPRITE_SIZE, self.pos_y * constants.SPRITE_SIZE))
		
		
	def move_right(self):
		# Checking two conditions to be sure that the movement is possible
		if ((self.pos_x) <= (constants.NB_SPRITE - 1)) and (self.labyrinth.structure[self.pos_y][self.pos_x + 1] != 'm'):
			self.pos_x += 1
			self.display()
			print('you choose to move to the right')
			
			
	def move_left(self):
		if (self.pos_x > 0) and (self.lab.structure[self.pos_x - 1][self.pos_y] != 'm'):
				self.pos_x -= 1
				print('you choose to move to the left')
	
	
	def move_up(self):
		if self.pos_y < (constants.NB_SPRITE - 1):
			if self.lab.structure[self.pos_x][self.pos_y + 1] != 'm':
				self.pos_y += 1
				print('you choose to move to the top')
			
			
	def move_down(self):
		if self.pos_y > 0:
			if self.lab.structure[self.pos_x][self.pos_y - 1] != 'm':
				self.pos_y -= 1
				print('you choose to move down')