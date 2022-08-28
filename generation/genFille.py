"""
file :Ce fichier  contient une fonction genFile qui générer un fichier JSON avec la datetime comme nom dans un dossier pecifique de facon specifique  .

date :  30/07/2022
Auteur : Hi_shikuro 
"""

def genFile(data):
	import json
	import datetime
	lst = []
	for nbGrille in range(len(data)):
		lst.append({"id":nbGrille+1,"data":[data[nbGrille]]})
	dateT= str(datetime.datetime.now().strftime("%m%d%Y %H%M%S"))
	for elt in lst:
		with open("./data/liste/"+dateT+".json","a") as file :
			json.dump(elt,file)
			if elt != lst[-1]:
				file.write(",")

if __name__ == '__main__':
	data = [{"grille":[],"numero":"","code":""},{"grille":[],"numero":"","code":""},{"grille":[],"numero":"","code":""}]
	genFile(data)