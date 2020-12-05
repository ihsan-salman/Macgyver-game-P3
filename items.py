# importation of moduls
import pygame
from random import randint
import constants as constants


class Items:

	def __init__(self, labyrinth):
		# Initialize the class
		self.labyrinth = labyrinth
		self.needle = pygame.image.load(constants.IMAGE_NEEDLE).convert_alpha()
		self.ether = pygame.image.load(constants.IMAGE_ETHER).convert_alpha()
		self.syringe = pygame.image.load(constants.IMAGE_SYRINGE).convert_alpha()
		self.display()

	def item_position(self):
		# Choose 3 random position and check 2 conditions to add in the list
		self.list_position = []
		# until 3 position in accordance with the conditions
		while len(self.list_position) != 3:
			# 2 randown integer between 1 and 13
			self.x = randint(1, 13)
			self.y = randint(1, 13)
			# Check if the position isn'n a wall
			# And not even contain in the position list
			if self.labyrinth.structure[self.y][self.x] != 'm' \
				and (self.y, self.x) not in self.list_position:
				# Add the position to the list
				self.list_position.append((self.y, self.x))

	def display(self):
		# initialize items position and display them
		self.item_position()
		self.needle_position = self.list_position[0]
		self.labyrinth.screen.blit(self.needle, (self.needle_position[1] *
			constants.SPRITE_SIZE, self.needle_position[0] * constants.SPRITE_SIZE))

		self.syringe_position = self.list_position[1]
		self.labyrinth.screen.blit(self.syringe, (self.syringe_position[1] *
			constants.SPRITE_SIZE, self.syringe_position[0] * constants.SPRITE_SIZE))

		self.ether_position = self.list_position[2]
		self.labyrinth.screen.blit(self.ether, (self.ether_position[1] *
			constants.SPRITE_SIZE, self.ether_position[0] * constants.SPRITE_SIZE))
