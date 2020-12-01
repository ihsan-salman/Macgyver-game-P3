# importation of moduls
import pygame
import constants as constants

"""character's responsible class"""


class Macgyver:

	def __init__(self, labyrinth):
		# Initialize the class
		self.labyrinth = labyrinth
		self.pos_x = 0
		self.pos_y = 14
		self.bag = []
		# Initialize first postion
		self.display()

	def display(self):
		# Display the character
		self.macgyver = pygame.image.load(constants.IMAGE_MACGYVER).convert_alpha()
		self.labyrinth.screen.blit(self.macgyver,
			(self.pos_x * constants.SPRITE_SIZE, self.pos_y * constants.SPRITE_SIZE))

	def display_font(self):
		# Deleting last hero position's picture method
		self.font = pygame.image.load(constants.IMAGE_FONT_SPRITE).convert_alpha()
		self.labyrinth.screen.blit(self.font,
			(self.pos_x * constants.SPRITE_SIZE, self.pos_y * constants.SPRITE_SIZE))

	def move_right(self):
		# Right movement method
		# Check two conditions to be sure that the movement is possible
		if ((self.pos_x) < (constants.NB_SPRITE - 1)) \
			and (self.labyrinth.structure[self.pos_y][self.pos_x + 1] != 'm'):
			# Delete each picture of the last posistion before the movement
			self.display_font()
			# Display again the labyrinth to save start picture
			self.labyrinth.display()
			# Add 1 to the last position
			self.pos_x += 1
			# display to the new position
			self.display()
			# Collect an item if the new position corresponds
			self.collect(self.items)

	def move_left(self):
		# Same method as move_right
		if (self.pos_x > 0) \
			and (self.labyrinth.structure[self.pos_y][self.pos_x - 1] != 'm'):
			self.display_font()
			self.pos_x -= 1
			self.display()
			self.collect(self.items)

	def move_up(self):
		# Same method as move_right
		if (self.pos_y > 0) \
			and (self.labyrinth.structure[self.pos_y - 1][self.pos_x] != 'm'):
			self.display_font()
			self.pos_y -= 1
			self.display()
			self.collect(self.items)

	def move_down(self):
		# Same method as move_right
		if (self.pos_y < (constants.NB_SPRITE - 1)) \
			and (self.labyrinth.structure[self.pos_y + 1][self.pos_x] != 'm'):
			self.display_font()
			self.pos_y += 1
			self.display()
			self.collect(self.items)

	def collect(self, items):
		# collect method
		self.items = items

		self.needle = pygame.image.load(constants.IMAGE_NEEDLE).convert_alpha()
		self.ether = pygame.image.load(constants.IMAGE_ETHER).convert_alpha()
		self.syringe = pygame.image.load(constants.IMAGE_SYRINGE).convert_alpha()

		# Collect condition
		if (self. pos_y, self.pos_x) == items.needle_position\
			and 'needle' not in self.bag:
			# Adding item to the bag
			self.bag.append('needle')
			# display the item in the down black field to show the contenant of the bag
			self.labyrinth.screen.blit(self.needle, (100, 660))
			print('You have a needle', len(self.bag))

		elif (self.pos_y, self.pos_x) == items.syringe_position\
			and 'syringe' not in self.bag:
			self.bag.append('syringe')
			self.labyrinth.screen.blit(self.syringe, (300, 660))
			print('You have a syringe', len(self.bag))

		elif (self.pos_y, self.pos_x) == items.ether_position\
			and 'ether' not in self.bag:
			self.bag.append('ether')
			self.labyrinth.screen.blit(self.ether, (500, 660))
			print('You have an ethter', len(self.bag))