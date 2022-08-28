"""
file :Ce fichier  contient une fonction genFile qui générer un fichier CSV avec la datetime comme nom dans un dossier pecifique de facon specifique  .

date :  30/07/2022
Auteur : Hi_shikuro 
"""
def genFilecsv(data):
	import csv
	import datetime
	lst = []
	for nbGrille in range(len(data)):
		lst.append({"id":nbGrille+1,"data":[data[nbGrille]]})
	dateT= str(datetime.datetime.now().strftime("%m%d%Y %H%M%S"))
	# for elt in lst:
	# 	with open("./data/liste/"+dateT+".json","a") as file :
	# 		json.dump(elt,file)

	for elt in lst:
		with open("./data/liste/"+dateT+".csv","a") as file :
				file.write(str(elt["id"])+",:,")
				#numero
				for eltNum in elt["data"][0]["numero"]:
					file.write(str(eltNum) +",")
				file.write("@,")

				#code
				code=""
				for eltCode in elt["data"][0]["code"]:
					code+= str(eltCode) 
				file.write(code)
				file.write("\n")
				
if __name__ == '__main__':
	data =[{'grille': [1, 3, '#', 8, 10, 11, 14, 19, 20, '#', 26, 29, '#', '#', 41, '#', '#', '#', 57, 59, 61, '#', '#', 89, 90, 91, 96], 'numero': [1, 3, 8, 10, 11, 14, 19, 20, 26, 29, 41, 57, 59, 61, 89, 90, 91, 96], 'code': [0, 0, 1, 2, 9, 3, 7, 3, 9]},{'grille': [1, 3, '#', 8, 10, 11, 14, 19, 20, '#', 26, 29, '#', '#', 41, '#', '#', '#', 57, 59, 61, '#', '#', 89, 90, 91, 96], 'numero': [1, 3, 8, 10, 11, 14, 19, 20, 26, 29, 41, 57, 59, 61, 89, 90, 91, 96], 'code': [0, 0, 1, 2, 9, 3, 7, 3, 9]},{'grille': [1, 3, '#', 8, 10, 11, 14, 19, 20, '#', 26, 29, '#', '#', 41, '#', '#', '#', 57, 59, 61, '#', '#', 89, 90, 91, 96], 'numero': [1, 3, 8, 10, 11, 14, 19, 20, 26, 29, 41, 57, 59, 61, 89, 90, 91, 96], 'code': [0, 0, 1, 2, 9, 3, 7, 3, 9]}]
	genFilecsv(data)