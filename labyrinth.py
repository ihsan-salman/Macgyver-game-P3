import pygame
import constants as constants

"""labyrinth class definition
   and initialization of its structure with pygame"""

class Labyrinth:
	def __init__(self, screen):
		
		self.structure = []
		self.file = 'level.txt'
		self.screen = screen
		self.element = 0
		self.generate()
		self.display()
	
	def generate(self):
		#creation of a list from a file
		with open(self.file, "r") as file:
			for line in file:
				ligne = []
				for sprite in line: 
					if sprite != '\n':
						ligne.append(sprite)
				self.structure.append(ligne)
	
	def guardian_pos(self):
		for x in range(len(self.structure)):
			for y in range(len(self.structure[x])):
				element = self.structure[y][x]
				if element == 'g':
					self.guardian_pos = [y, x]
	"""
	
	def pos_items(self):
		self.items_pos = []
		for x in range(len(self.structure)):
			for y in range(len(self.structure[x])):
				element = self.structure[y][x]
				if element == 'o':
					position_items = (y, x)
					self.items_pos.append(position_items)
			self.pos_items = random.sample(self.items_pos, 3)
		"""	
			
	def display(self):
		# display the structure labyrinth with all elements
		
		self.wall = pygame.image.load(constants.IMAGE_WALL).convert()
		self.start = pygame.image.load(constants.IMAGE_START).convert()
		self.guardian = pygame.image.load(constants.IMAGE_GUARDIAN).convert_alpha()
		"""self.needle = pygame.image.load(constants.IMAGE_NEEDLE).convert_alpha()
		self.ether = pygame.image.load(constants.IMAGE_ETHER).convert_alpha()
		self.syringe = pygame.image.load(constants.IMAGE_SYRINGE).convert_alpha()
		
		needle_pos, syringe_pos, ether_pos = self.pos_items
		
		self.screen.blit(self.needle, (needle_pos[0] * constants.SPRITE_SIZE, needle_pos[1] * constants.SPRITE_SIZE))
		self.screen.blit(self.syringe, (syringe_pos[0] * constants.SPRITE_SIZE, syringe_pos[1] * constants.SPRITE_SIZE))
		self.screen.blit(self.ether, (ether_pos[0] * constants.SPRITE_SIZE, ether_pos[1] * constants.SPRITE_SIZE))
        """	
		
		for x in range(len(self.structure)):
			for y in range(len(self.structure[x])):
				element = self.structure[y][x]
				if element == 'm':
					self.screen.blit(self.wall, (x * constants.SPRITE_SIZE, y * constants.SPRITE_SIZE))
				elif element == 'd':
					self.screen.blit(self.start, (x * constants.SPRITE_SIZE, y * constants.SPRITE_SIZE))
				elif element == 'g':
					self.screen.blit(self.guardian, (x * constants.SPRITE_SIZE, y * constants.SPRITE_SIZE))
				elif element == 's':
					self.screen.blit(self.start, (x * constants.SPRITE_SIZE, y * constants.SPRITE_SIZE))
		 	
				
	def display_hero(self, pos_mac_x, pos_mac_y):
		# diplay the hero with the position given by the choice of the player
		
		self.macgyver = pygame.image.load(constants.IMAGE_MACGYVER).convert_alpha()
		for x in range(len(self.structure)):
			for y in range(len(self.structure[x])):
				element = self.structure[y][x]
				if element == 's':
						self.screen.blit(self.macgyver, (pos_mac_x * constants.SPRITE_SIZE, pos_mac_y * constants.SPRITE_SIZE))
		
