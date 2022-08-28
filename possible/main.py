"""
file :Ce fichier  est le  programme principal
qui liste les numeros serie des  possible gagnant 
en saisisant des  numeros qui est dans une liste  dans un fichier  .

date :  30/07/2022
Auteur : Hi_shikuro 
"""

import csv 
from dans import listIn
from iss import chaineNonNum 
from lecteurCsv import lireFileCsv

lsteGrille = lireFileCsv("./08012022 173045.csv")

etat = True
lstNum =[]
while etat :
	print("! Entrer les numéros  gagnant un part un !")
	nb = input(">")
	if  chaineNonNum(nb):
		etat=False
	else:
		lstNum.append(nb)
		print(listIn(lsteGrille , lstNum) )

