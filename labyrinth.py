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
			
		   
	def display(self):
		# display the structure labyrinth with textures
		
		self.wall = pygame.image.load(constants.IMAGE_WALL).convert()
		self.start = pygame.image.load(constants.IMAGE_START).convert()
		self.guardian = pygame.image.load(constants.IMAGE_GUARDIAN).convert_alpha()
		
		
		for x in range(len(self.structure)):
			for y in range(len(self.structure[x])):
				element = self.structure[y][x]
				if element == 'm':
					self.screen.blit(self.wall, (x * 44, y * 44))
				elif element == 'd':
					self.screen.blit(self.start, (x * 44, y * 44))
				elif element == 'g':
					self.screen.blit(self.guardian, (x * 44, y * 44))
				elif element == 's':
					self.screen.blit(self.start, (x * 44, y * 44))
		
		
	def display_hero(self, pos_mac_x, pos_mac_y):
		
		self.macgyver = pygame.image.load(constants.IMAGE_MACGYVER).convert_alpha()
			
		for x in range(len(self.structure)):
			for y in range(len(self.structure[x])):
				element = self.structure[y][x]
				if element == 's':
						self.screen.blit(self.macgyver, (pos_mac_x * 44, pos_mac_y * 44))
		
