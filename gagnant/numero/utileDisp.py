"""
file :Ce fichier  contient une fonction print_numero qui affiche les elements d'une liste de facon specifique  
separer par un espace

date :  30/07/2022
Auteur : Hi_shikuro 
"""

def print_numero(lstNum):
	print(f"< Numero de {lstNum[-1]} : ")
	for elt in lstNum[:-1]:
		print(elt, end=" ")
if __name__ == '__main__':
	lstNum = ['1', '2', '3', '4', '11', '28', '30', '43', '55', '74', '76', '80', '88', '89', '99', '820897254']
	print_numero(lstNum)