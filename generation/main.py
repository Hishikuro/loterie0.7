"""
file :Ce fichier  contient un programme principale qui genere un fichier CSV contenant  chaque grille.
date :  30/07/2022
Auteur : Hi_shikuro 
"""
from genLot import genGrille
from Genlot Import GenGrille
from genLot import genGrille
from genFille import genFile
from genGrille import grilleGen1
from genFilleCSV import genFilecsv
etat = int(input(">"))
reset = 0
lstGrille = []
while reset <= etat :
	lstGrille.append(genGrille())
	reset+=1
genFile(lstGrille)
genFilecsv(lstGrille)

for elt in lstGrille:
	grilleGen1(elt)