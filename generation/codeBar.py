"""
file :Ce fichier  contient une fonction codebar13c qui genere un  EAN13 codebar dans un dossier spésifique .

date :  30/07/2022
Auteur : Hi_shikuro 
"""

def codebar13c(numeroStr):	
	from barcode import EAN13
	code = EAN13(numeroStr)
	code.save("data/grille/"+numeroStr)

if __name__ == '__main__':
	codebar13c("5901234123453")
	codebar13c("590123412345")
	
