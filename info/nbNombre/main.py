
"""
file :Ce fichier  contient des  fonction:
- nbNombre : compte le nombre de nombre présent dans une liste 
-  len_verifie: Vérifit que un dictionnaires est de la forme souyaiter   .
Ce fichier est programme principale qui affiche des graphs sur les donnees d'un fichier csv 

date :  30/07/2022
Auteur : Hi_shikuro 
"""
from lecteurCsv import lireFileCsv
from graphique import traceGraphiqueLine
from graphique import traceGraphiqueHist
from sauveCsv import saveCsv_v1

def nbNombre(lst) :
	lsteNub ={str(i):0 for i in range(1,101)}
	for eltLst in lst:
		for elt in eltLst[:-1]:
			lsteNub[elt]+= 1
	return(lsteNub)
		
	

def len_verifier(dictData,nb):
	summ= 0
	for  dta in dictData.values():
		summ+= int(dta)
	return(summ == nb * 15 )

if __name__ == '__main__':
	data= lireFileCsv("./08012022 173045.csv")
	nombre2Nb = nbNombre(data)
	print(nombre2Nb)
	print(len_verifier(nombre2Nb,10001))
	traceGraphiqueLine("represtation",nombre2Nb.keys(),nombre2Nb.values())
	#traceGraphiqueHist("title",nombre2Nb.keys(),nombre2Nb.values())
	#saveCsv_v1("pop",[nombre2Nb.keys(),nombre2Nb.values()])
	# import numpy as np
	# matrix = np.array([nombre2Nb.keys(),nombre2Nb.values()])
	# print(matrix)