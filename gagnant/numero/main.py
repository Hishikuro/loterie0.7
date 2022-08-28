
"""
file :Ce fichier  contient un programme principale qui affiche le numero de serie  
d'une grille selon les numero qui la continent

date :  30/07/2022
Auteur : Hi_shikuro 
"""

import csv 
from utileDisp import print_numero
from lst import isEgalList

from lecteurCsv import lireFileCsv
lsteGrille = lireFileCsv("./08012022 173045.csv")


#listeGrilleInput = "1,2,3,4,11,28,30,43,55,74,76,80,88,89,99" 
grille= []
for time in range(15):
	choix = input(f"Enter le '{time+1}' nombre :> ")
	while choix in grille  :
		choix = input(f"Enter a nouveau le '{time+1}' nombre :> ")
		
	grille.append(choix)
	

for elt in lsteGrille :
	if isEgalList(elt[:-1],grille):
		print(f"Le numero serie de la grille gagnant :>{elt[-1]}")