"""
file :Ce fichier  contient une fonction qui lit 
un fichier csv et le tranforme en une liste en 2 dim .

date :  30/07/2022
Auteur : Hi_shikuro 
"""


def lireFileCsv(url):
	import csv
	f = open(r""+url)
	reaDh = csv.reader(f)
	lsteGrille = []
	for rw in reaDh:
		lsteGrille.append(rw[2:-1])
		lsteGrille[-1][-1] = rw[-1]
	return(lsteGrille)
if __name__ == '__main__':
	print(lireFileCsv("./08012022 173045.csv"))