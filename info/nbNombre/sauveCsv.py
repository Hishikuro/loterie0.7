
"""
file :Ce fichier  contient des fonctions :
- saveCsv_v1:cette fonction sauvegarde une lsite d'éléménet dans un fichier csv
- saveCsv_v2:cette fonction sauvegarde  dans un fichier csv
- geneCsvStat: cette fonction sauvegarde une lsite d'éléménet dans un fichier csv 

date :  30/07/2022
Auteur : Hi_shikuro 
"""

def saveCsv_v1(nom,lst):
	import csv 
	fichier = open(nom+'.csv','w')
	obj = csv.writer(fichier)
	for element in lst:
	    obj.writerow(element)
	fichier.close()


def saveCsv_v2(nom,elt):
	with open(nom+".csv", "a") as fichier:
		fichier.write(elt)
		
def geneCsvStat(lst):
	nom ="lol"
	for elt in lst :
		for sselt in elt:
			saveCsv_v1(nom,sselt)
if __name__ == '__main__':
	lst = [(1,2,3),(4,5,6)]
	saveCsv_v1("pop",lst)
	