# importation of moduls
import pygame 
import constants as constants

class Items:

	def __init__(self, labyrinth):
		self.labyrinth = labyrinth
		self.needle = pygame.image.load(constants.IMAGE_NEEDLE).convert_alpha()
		self.ether = pygame.image.load(constants.IMAGE_ETHER).convert_alpha()
		self.syringe = pygame.image.load(constants.IMAGE_SYRINGE).convert_alpha()

		def pos_items(self):
			self.items_pos = []
			for x in range(len(self.structure)):
				for y in range(len(self.structure[x])):
					element = self.structure[y][x]
					if element == 'o':
						position_items = y, x
						self.items_pos.append(position_items)
						self.pos_items = random.sample(self.items_pos, 3)


		def display(self):
			needle_pos, syringe_pos, ether_pos = self.pos_items
			self.screen.blit(self.needle, (needle_pos[0] * constants.SPRITE_SIZE, needle_pos[1] * constants.SPRITE_SIZE))
			self.screen.blit(self.syringe, (syringe_pos[0] * constants.SPRITE_SIZE, syringe_pos[1] * constants.SPRITE_SIZE))
			self.screen.blit(self.ether, (ether_pos[0] * constants.SPRITE_SIZE, ether_pos[1] * constants.SPRITE_SIZE))


