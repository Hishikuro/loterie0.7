
"""
file :Ce fichier  contient des fonctions :
- traceGraphiqueLine:cette fonction trace un graphique line avec des données  
- traceGraphiqueCam:cette fonction trace un graphique cammanbere avec des données 
- traceGraphiqueHist: cette fonction trace un graphique histogramme avec des données 

date :  30/07/2022
Auteur : Hi_shikuro 
"""
#traceAGraphiqueLine
def traceGraphiqueLine(titre,x,y):
	import numpy as np
	import matplotlib.pyplot as plt

	fig, ax = plt.subplots()
	ax.plot(x,y)
	ax.set_title(titre)

	plt.show()
def traceGraphiqueCam(nameLst,dataLst):
	from matplotlib import pyplot as plt 
	import numpy as np 

	fig = plt.figure(figsize =(10, 10)) 
	plt.pie(dataLst, labels = nameLst) 
	  
	plt.show() 

def traceGraphiqueHist(title,nameLst,dataLst):
	import matplotlib.pyplot as plt  # Module pour tracer les graphiques
	import numpy as np

	
	plt.hist(dataLst, bins=nameLst)  # Création de l'histogramme
	plt.xlabel('Valeurs')
	plt.xticks(dataLst)
	plt.ylabel('Nombres')
	plt.title(title)
	plt.show()
if __name__ == '__main__':
	from random import randint
	lsiteNb = [ randint(0,100) for i in range(100)]
	nb = [ i for i in range(100)]
	print(nb)
	print(lsiteNb)
	traceGraphiqueLine("tirage de 100 nombres entre 0,100 ", nb , lsiteNb)
	traceGraphiqueCam(nb , lsiteNb)
	traceGraphiqueHist("histo",nb , lsiteNb)