import pygame
from constantes import *
from labyrinthe import *


class MacGyver:
	def __init__(self):
		"""Classe permettant de créer un personnage"""
		
		self.avance=pygame.image.load(avance).convert_alpha()
		self.case_x=0
		self.case_y=0
		self.x=0
		self.y=0
		self.direction=self.avance
		self.objets=[]
	
	
	def se_deplace(self):
		"""Methode permettant de déplacer le personnage"""
		
		#déplacement vers la droite
		if direction=="droite":
			if self.case<(nb_sprite-1):
				if self.structure[self.case_y][self.case_x+1] !='m':
					self.case_x+=1
					self.x=self.case_x*taille_sprite
				self.direction=self.avance
		
		#déplacement vers la gauche
		if direction=="gauche":
			if self.case<0:
				if self.structure[self.case_y][self.case_x-1] !='m':
					self.case_x-=1
					self.x=self.case_x*taille_sprite
				self.direction=self.avance
		
		#déplacement vers le haut
		if direction=="haut":
			if self.case<0:
				if self.structure[self.case_y-1][self.case_x] !='m':
					self.case_y-=1
					self.y=self.case_y*taille_sprite
				self.direction=self.avance
		
		#déplacement vers le bas
		if direction=="haut":
			if self.case<(nb_sprite - 1):
				if self.structure[nombre_sprite_cote +1][self.case_x] !='m':
					self.case_y+=1
					self.y=self.case_y*taille_sprite
				self.direction=self.avance
	
	
	def ramasser(self):
		"""méthode permettant de ramasser des objets"""
		
		
		
		
		
	
