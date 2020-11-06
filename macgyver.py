import pygame

#importation des modules
import labyrinthe as lb
import constantes as c


lab = lb.Labyrinthe()
lab.generer()


class MacGyver:
	def __init__(self, avance):
		"""Classe permettant de créer un personnage"""
		
		self.avance=pygame.image.load(c.IMAGE_MACGYVER).convert_alpha()
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		self.direction = self.avance
		self.objets = []

	
	def se_deplace(self, direction):
		"""Methode permettant de déplacer le personnage"""
		
		#déplacement vers la droite
		if direction == "droite":
			if self.case_x < (c.NB_SPRITE - 1):
				if lab.structure[self.case_y][self.case_x + 1] != 'm':
					self.case_x += 1
					self.x = self.case_x * c.TAILLE_SPRITE
				self.direction = self.avance
		
		#déplacement vers la gauche
		if direction == "gauche":
			if self.case_x < 0:
				if lab.structure[self.case_y][self.case_x - 1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * c.TAILLE_SPRITE
				self.direction = self.avance
		
		#déplacement vers le haut
		if direction == "haut":
			if self.case_y < 0:
				if lab.structure[self.case_y - 1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * c.TAILLE_SPRITE
				self.direction = self.avance
		
		#déplacement vers le bas
		if direction == "haut":
			if self.case_y < (c.NB_SPRITE - 1):
				if lab.structure[self.case_y + 1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * c.TAILLE_SPRITE
				self.direction = self.avance
	
	
	def ramasser(self):
		"""méthode permettant de ramasser des objets"""
		
		
		
		
		
	
