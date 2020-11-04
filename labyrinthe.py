import pygame
from pygame.locals import * 
from constantes import *

#définition de la classe labyrinthe 
#et initialisation de sa structure avec pygame
class labyrinthe:
	def __init__(self):
		"""méthode permettant de générer le labyrinthe 
		   à partir du fichier .txt"""
		self.structure=0
		self.fichier='labyrinthe.txt'
		
	
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
			self.structure=structure
			
		   
	def afficher(self):
		"""méthode permettant d'afficher la structure 
		   du labyrinthe avec les textures"""
		self.fenetre=0
		self.mur = pygame.image.load(image_mur).convert()
		self.depart = pygame.image.load(image_depart).convert()
		self.gardien = pygame.image.load(image_gardien).convert_aplha()
		
		nb_ligne=0
		for ligne in self.structure:
			nb_case=0
			for sprite in ligne:				
				x=nb_case*taille_sprite
				y=nb_ligne*taille_sprite 
				if sprite=='m':
					fenetre.blit(self.mur,(x,y))
				elif sprite=='d':
					fenetre.blit(self.depart,(x,y))
				elif sprit=='g':
					fenetre.blit(self.gardien,(x,y))
				nb_case+=1
				pygame.display.flip()
			nb_ligne+=1
			pygame.display.flip()
			

                
