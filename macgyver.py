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
		self.bag = []
		# Initialize first postion 
		self.display()

	
	# Character's display method
	def display(self):
		self.labyrinth.screen.blit(self.macgyver, (self.pos_x * constants.SPRITE_SIZE, self.pos_y * constants.SPRITE_SIZE))
	

	# Deleting last hero position's picture method
	def display_font(self):
		self.labyrinth.screen.blit(self.font, (self.pos_x * constants.SPRITE_SIZE, self.pos_y * constants.SPRITE_SIZE))


	# Displacement method	
	def move_right(self):
		# Check two conditions to be sure that the movement is possible
		if ((self.pos_x) < (constants.NB_SPRITE - 1)) and (self.labyrinth.structure[self.pos_y][self.pos_x + 1] != 'm'):
			self.display_font()
			self.labyrinth.display()
			self.pos_x += 1
			self.display()
			self. collect(self.items)
	def move_left(self):
		if (self.pos_x > 0) and (self.labyrinth.structure[self.pos_y][self.pos_x - 1] != 'm'):
			self.display_font()
			self.pos_x -= 1
			self.display()
			self. collect(self.items)
	
	
	def move_up(self):
		if (self.pos_y > 0) and (self.labyrinth.structure[self.pos_y - 1][self.pos_x] != 'm'):
			self.display_font()
			self.pos_y -= 1
			self.display()
			self. collect(self.items)
			
			
	def move_down(self):
		if (self.pos_y < (constants.NB_SPRITE - 1)) and (self.labyrinth.structure[self.pos_y + 1][self.pos_x] != 'm'):
				self.display_font()
				self.pos_y += 1
				self.display()
				self. collect(self.items)

	def collect(self, items):
		self.items = items
		if [self. pos_y, self.pos_x] == self.items.needle_pos:
			self.bag.append('needle')
			self.items.needle_pos = [13,0]
			print('You have a needle', len(self.bag))
		elif [self.pos_y, self.pos_x] == self.items.syringe_pos:	
			self.bag.append('syringe')
			self.items.syringe_pos = [13,0]
			print('You have a syringe', len(self.bag))
		elif [self.pos_y, self.pos_x] == self.items.ether_pos:
			self.bag.append('ether')
			self.items.ether_pos = [13,0]
			print('You have an ethter', len(self.bag))
		if len(self.bag) == 3:
			print('You have all items! : Direction to the evil guardian ')

	"""def win(self):
		if [self.pos_y, self.pos_x] == [0,7] and len(self.bag) == 3:
			print('you win')"""




