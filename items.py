# importation of moduls
import pygame 
from random import randint
import constants as constants

class Items:

	def __init__(self, labyrinth):
		# Initialize the class
		self.labyrinth = labyrinth
		self.x = 0
		self.y = 0
		self.needle = pygame.image.load(constants.IMAGE_NEEDLE).convert_alpha()
		self.ether = pygame.image.load(constants.IMAGE_ETHER).convert_alpha()
		self.syringe = pygame.image.load(constants.IMAGE_SYRINGE).convert_alpha()
		self.display()


	def item_pos(self):
		# Choose 2 number and check the corresponding position 
		self.pos_item = []	
		while self.pos_item == []:
			self.x = randint(1, 13)
			self.y = randint(1, 13)
			# Condition checking if the position isn'n a wall 
			# And not the same previous position
			if self.labyrinth.structure[self.y][self.x] != 'm' \
			and [self.y, self.x] != self.pos_item:
				self.pos_item.append(self.y)
				self.pos_item.append(self.x)
		return self.pos_item


	def display(self):
		# initialize items position and display 
		self.needle_pos = self.item_pos()
		self.labyrinth.screen.blit(self.needle, (self.needle_pos[1] * \
			constants.SPRITE_SIZE, self.needle_pos[0] * constants.SPRITE_SIZE))
			
		self.syringe_pos = self.item_pos()
		self.labyrinth.screen.blit(self.syringe, (self.syringe_pos[1] * \
			constants.SPRITE_SIZE, self.syringe_pos[0] * constants.SPRITE_SIZE))

		self.ether_pos = self.item_pos()
		self.labyrinth.screen.blit(self.ether, (self.ether_pos[1] * \
			constants.SPRITE_SIZE, self.ether_pos[0] * constants.SPRITE_SIZE))
		print(self.needle_pos, self.syringe_pos, self.ether_pos)