import pygame
from constantes import *

#définition de la classe labyrinthe 
#et initialisation de sa structure avec pygame

class Labyrinthe:
	def __init__(self):
		"""méthode permettant de générer le labyrinthe 
		   à partir du fichier .txt"""
		self.structure = 0
		self.fichier = 'labyrinthe.txt'
		
	
	def generer(self):
		"""méthode permettant d'afficher la structure 
		   du labyrinthe avec les textures"""
		
		with open(self.fichier, "r") as fichier:
			structure = []
			for ligne in fichier:
				ligne_niveau = []
				for sprite in ligne:
					if sprite != '\n':
						ligne_niveau.append(sprite)
				structure.append(ligne_niveau)
			self.structure = structure
			
		   
	def afficher(self , fenetre):
		"""méthode permettant d'afficher la structure 
		   du labyrinthe avec les textures"""
		
		self.fenetre = 0
		self.mur = pygame.image.load(IMAGE_MUR).convert()
		self.depart = pygame.image.load(IMAGE_DEPART).convert()
		self.gardien = pygame.image.load(IMAGE_GARDIEN).convert_alpha()
		
		nb_ligne = 0
		for ligne in self.structure:
			nb_case = 0
			for sprite in ligne:				
				x = nb_case * TAILLE_SPRITE
				y = nb_ligne * TAILLE_SPRITE
				if sprite == 'm':
					fenetre.blit(self.mur,(x,y))
				elif sprite == 'd':
					fenetre.blit(self.depart,(x,y))
				elif sprite == 'g':
					fenetre.blit(self.gardien,(x,y))
				nb_case += 1
			nb_ligne += 1
		pygame.display.flip()
			

                
