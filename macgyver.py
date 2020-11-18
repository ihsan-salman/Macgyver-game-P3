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
		self.font = pygame.image.load(constants.IMAGE_FONT_SPRITE).convert_alpha()
		self.display()
	
	def display(self):
		self.labyrinth.screen.blit(self.macgyver, (self.pos_x * constants.SPRITE_SIZE, self.pos_y * constants.SPRITE_SIZE))
	
	def display_font(self):
		self.labyrinth.screen.blit(self.font, (self.pos_x * constants.SPRITE_SIZE, self.pos_y * constants.SPRITE_SIZE))

		
	def move_right(self):
		# Checking two conditions to be sure that the movement is possible
		if ((self.pos_x) < (constants.NB_SPRITE - 1)) and (self.labyrinth.structure[self.pos_y][self.pos_x + 1] != 'm'):
			self.display_font()
			self.labyrinth.display()
			self.pos_x += 1
			self.display()
			print('you choose to move to the right', self.pos_y, self.pos_x)
			
			
	def move_left(self):
		if (self.pos_x > 0) and (self.labyrinth.structure[self.pos_y][self.pos_x - 1] != 'm'):
			self.display_font()
			self.pos_x -= 1
			self.display()
			print('you choose to move to the left', self.pos_y, self.pos_x)
	
	
	def move_up(self):
		if (self.pos_y > 0) and (self.labyrinth.structure[self.pos_y - 1][self.pos_x] != 'm'):
			self.display_font()
			self.pos_y -= 1
			self.display()
			print('you choose to move to the top', self.pos_y, self.pos_x)
			
			
	def move_down(self):
		if (self.pos_y < (constants.NB_SPRITE - 1)) and (self.labyrinth.structure[self.pos_y + 1][self.pos_x] != 'm'):
				self.display_font()
				self.pos_y += 1
				self.display()
				print('you choose to move down', self.pos_y, self.pos_x)