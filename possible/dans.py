"""
file :Ce fichier  contient des fonctions :
- eltIn:cette fonction parcour une liste de 2 dim et retorune les liste de la liste contenant un element
- listIn:Cette fonction parcout une liste de 2 dim et retourne les liste de la lsite conteant une liste d'élement 

date :  30/07/2022
Auteur : Hi_shikuro 
"""


def eltIn(grille,elt):
	lxw = []
	for g in grille:
		
		if elt in g:
			lxw.append(g)
	return(lxw)
def listIn(grille , lstNum) : 
	lst = grille
	for elt in lstNum:
		lst = eltIn(lst,elt)
	return(lst)
if __name__ == '__main__':
	lst = [ ['1', '12', '37', '38', '40', '47', '53', '55', '58', '60', '63', '79', '89', '96', '98', '004017141'], ['1', '6', '7', '15', '17', '21', '24', '38', '52', '53', '85', '91', '92', '95', '99', '245743504'], ['14', '36', '37', '41', '42', '43', '49', '50', '52', '68', '71', '76', '81', '1', '12', '213759003']]
	print(listIn(lst,["1","12"]))
	
