# 

"""
file :Ce fichier  contient une fonction isEgalList qui vérifie si deux listes sont égales.

date :  30/07/2022
Auteur : Hi_shikuro 
"""

def isEgalList(lst1 , lst2) :
	if not(len(lst1) == len(lst2)):
		return(False)
	else :
		for nbElt in range(len(lst1)):
			if not(lst1[nbElt] == lst2[nbElt]):
				return False
			
		return(True)
if __name__ == '__main__':
	print(isEgalList(["10","11"],["10","11"]))
	print(isEgalList(["10","11"],["10","12"]))