# importation of moduls
import pygame 
from random import randint
import constants as constants

class Items:

	def __init__(self, labyrinth):

		self.labyrinth = labyrinth
		self.x = 0
		self.y = 0
		self.needle = pygame.image.load(constants.IMAGE_NEEDLE).convert_alpha()
		self.ether = pygame.image.load(constants.IMAGE_ETHER).convert_alpha()
		self.syringe = pygame.image.load(constants.IMAGE_SYRINGE).convert_alpha()
		self.display()


	def item_pos(self):
		self.pos_item = []	
		while self.pos_item == []:
			self.x = randint(1, 14)
			self.y = randint(1, 14)
			if self.labyrinth.structure[self.y][self.x] != 'm' and [self.y, self.x] != self.pos_item:
				self.pos_item.append(self.y)
				self.pos_item.append(self.x)
		return self.pos_item


	def display(self):

		self.needle_pos = self.item_pos()
		self.labyrinth.screen.blit(self.needle, (self.needle_pos[1] * constants.SPRITE_SIZE, self.needle_pos[0] * constants.SPRITE_SIZE))
			
		self.syringe_pos = self.item_pos()
		self.labyrinth.screen.blit(self.syringe, (self.syringe_pos[1] * constants.SPRITE_SIZE, self.syringe_pos[0] * constants.SPRITE_SIZE))

		self.ether_pos = self.item_pos()
		self.labyrinth.screen.blit(self.ether, (self.ether_pos[1] * constants.SPRITE_SIZE, self.ether_pos[0] * constants.SPRITE_SIZE))
		print(self.needle_pos, self.syringe_pos, self.ether_pos)


