import pygame
from pygame.locals import *

from labyrinthe import *
from constantes import *


pygame.init()
#white=(255,255,255)
#initialisation de la fenetre

screen = pygame.display.set_mode((cote_fenetre,cote_fenetre))
pygame.display.set_caption(titre_fenetre)




# main loop
run = True

pygame.display.flip()
pygame.time.Clock().tick(30)

while run:
	
	pygame.display.flip()
	
	for e in pygame.event.get():
		if e.type==K_a:
			lab=labyrinthe()
			lab.afficher()
		elif e.type == pygame.QUIT or e.type==KEYDOWN and e.key==K_SPACE:
        	 run = False
       
			
				
       
