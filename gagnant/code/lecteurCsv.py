"""
file :Ce fichier  contient une fonction lireFileCsv qui lit un fichier CSV et renvoie  de 2dim pour un cas spécifique de fichier

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