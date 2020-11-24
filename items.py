# importation of moduls
import pygame 
from random import randint
import constants as constants

class Items:

	def __init__(self, labyrinth):
		self.labyrinth = labyrinth
		self.x = 0
		self.y = 0
		self.pos_item = []
		self.needle = pygame.image.load(constants.IMAGE_NEEDLE).convert_alpha()
		self.ether = pygame.image.load(constants.IMAGE_ETHER).convert_alpha()
		self.syringe = pygame.image.load(constants.IMAGE_SYRINGE).convert_alpha()
		self.display()


	def item_pos(self):
		while self.pos_item == []:
			self.x = randint(0, 14)
			self.y = randint(0, 14)
			if self.labyrinth.structure[self.y][self.x] != 'm':
				self.pos_item.append(self.y)
				self.pos_item.append(self.x)
		return self.pos_item

	def display(self):
		needle_pos = self.item_pos()
		print(needle_pos)
		syringe_pos = self.item_pos()
		print(syringe_pos)
		self.labyrinth.screen.blit(self.needle, (needle_pos[1] * constants.SPRITE_SIZE, needle_pos[0] * constants.SPRITE_SIZE))
		"""self.labyrinth.screen.blit(self.syringe, (syringe_pos[1] * constants.SPRITE_SIZE, syringe_pos[0] * constants.SPRITE_SIZE))
		self.labyrinth.screen.blit(self.ether, (ether_pos[0] * constants.SPRITE_SIZE, ether_pos[1] * constants.SPRITE_SIZE))
        """

