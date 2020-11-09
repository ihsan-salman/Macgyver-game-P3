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
		
	
	def generate(self):
		#creation of a list from a file
		
		with open(self.file, "r") as file:
			for line in file:
				line = []
				for sprite in line:
					if sprite != '\n':
						line.append(sprite)
				self.structure.append(line)
			
		   
	def display(self):
		# display the structure labyrinth with textures
		
		
		self.wall = pygame.image.load(constants.IMAGE_WALL).convert()
		self.start = pygame.image.load(constants.IMAGE_START).convert()
		self.guardian = pygame.image.load(constants.IMAGE_GUARDIAN).convert_alpha()
		self.macgyver = pygame.image.load(constants.IMAGE_MACGYVER).convert_alpha()
		
		for line in self.structure:
			for sprite in line:
				for element in sprite:
					x = sprite * constants.SPRITE_SIZE
					y = line * constants.SPRITE_SIZE
					if element == 'm':
						self.screen.blit(self.wall, (x, y))
					elif element == 'd':
						self.screen.blit(self.start, (x, y))
					elif element == 'g':
						self.screen.blit(self.guardian, (x, y))
					elif element == 'S':
						self.screen.blit(self.macgyver, (x, y))
		pygame.display.flip()

		
