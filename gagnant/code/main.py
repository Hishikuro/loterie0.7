
"""
file :Ce fichier  contient un programme principal qui verifie le numero  d'une  grille en donnant le numero de serie ( code : XXXXXXXXX )  
date :  30/07/2022
Auteur : Hi_shikuro 
"""
import csv 
from utileDisp import print_numero
from iss import chaineNonNum 
from lecteurCsv import lireFileCsv

lsteGrille = lireFileCsv("./08012022 173045.csv")

etat = True
while etat :
	print("Enter le numero de serie de la grille ( code : XXXXXXXXX ) ou Enter un ou plus de caractere autre que  des chiffres pour arreter :")
	code = input("code -=> ")
	if  chaineNonNum(code):
		etat=False
	else :

		for elt in lsteGrille:
			if code == elt[-1]:
				print_numero (elt)
	print("\nFIN DE LA RECHERCHE")

