# importation of moduls
import pygame
import constants as constants

"""labyrinth class definition"""

class Labyrinth:

	def __init__(self, screen):
		# Initialize the class
		self.structure = []
		self.file = 'level.txt'
		self.screen = screen
		self.generate()
		self.display()
	

	def generate(self):
		# Creation of a list from a file
		with open(self.file, "r") as file:
			# List run
			for line in file:
				ligne = []
				for sprite in line: 
					if sprite != '\n':
						# Adding each element one by one
						ligne.append(sprite)
				self.structure.append(ligne)
		
	
	def display(self):
		# Display the labyrinth with all elements
		self.wall = pygame.image.load(constants.IMAGE_WALL).convert()
		self.start = pygame.image.load(constants.IMAGE_START).convert()
		self.guardian = pygame.image.load(constants.IMAGE_GUARDIAN).convert_alpha()

		# List run
		for x in range(len(self.structure)):
			for y in range(len(self.structure[x])):
				element = self.structure[y][x]
				# Condition to display each element
				if element == 'm':
					self.screen.blit(self.wall, (x * constants.SPRITE_SIZE, y * \
						constants.SPRITE_SIZE))
				elif element == 'd':
					self.screen.blit(self.start, (x * constants.SPRITE_SIZE, y * \
						constants.SPRITE_SIZE))
				elif element == 'g':
					self.screen.blit(self.guardian, (x * constants.SPRITE_SIZE, y * \
						constants.SPRITE_SIZE))
				elif element == 's':
					self.screen.blit(self.start, (x * constants.SPRITE_SIZE, y * \
						constants.SPRITE_SIZE))