
"""
file :Ce fichier  contient une fonction chaineNonNum qui   renvoie vrai si ch est une chaîne non-nombre.

date :  30/07/2022
Auteur : Hi_shikuro 
"""

def chaineNonNum(ch):
	for x in ch:
		if not(x >= '0' and x <= '9'):
			return(True)
	return(False)

if __name__ == '__main__':
	print(chaineNonNum("12"))
	print(chaineNonNum("1A"))
	print(chaineNonNum("m45"))