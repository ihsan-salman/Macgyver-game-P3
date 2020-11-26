# importation of moduls
import pygame
import constants as constants

"""labyrinth class definition
   and initialization of its structure with pygame"""

class Labyrinth:
	def __init__(self, screen):
		
		self.structure = []
		self.file = 'level.txt'
		self.screen = screen
		self.generate()
		self.display()
	

	# Creation of a list from a file
	def generate(self):
		with open(self.file, "r") as file:
			for line in file:
				ligne = []
				for sprite in line: 
					if sprite != '\n':
						ligne.append(sprite)
				self.structure.append(ligne)
		
	
	# Display the structure labyrinth with all elements
	def display(self):
		
		self.wall = pygame.image.load(constants.IMAGE_WALL).convert()
		self.start = pygame.image.load(constants.IMAGE_START).convert()
		self.guardian = pygame.image.load(constants.IMAGE_GUARDIAN).convert_alpha()
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
