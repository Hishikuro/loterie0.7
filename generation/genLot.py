"""
file :Ce fichier  contient une fonction genGrille qui générer une grille de nombre aléatoire avec un numero de serie sous forme d'un dictionnaire .

date :  30/07/2022
Auteur : Hi_shikuro 
"""
#Générer une calandre aléatoire
def genGrille() :
	from random import randint
	#genere des nombre entre 1 et 100 , les nombres sont générer 27 fois
	entreAaB = [1,100]
	grilleLotterie = [""] * 27

	for i in range(27):
		gen = randint(entreAaB[0],entreAaB[1])
		while gen in grilleLotterie  :
			gen= randint(entreAaB[0],entreAaB[1])
		grilleLotterie[i] = gen

	grilleLotterie.sort()

	#puis genere 12 nombre compris entre 1 et 27 
	entre1a26 =[1-1,27-1]
	nb12 =[""] * 12

	for i in range(12):
		genM = randint(entre1a26[0],entre1a26[1])
		while genM in nb12  :
			genM= randint(entre1a26[0],entre1a26[1])
		nb12[i] = genM

	# masque dans les 27 nombre , les nombre au position des 12 générer 
	grilleLotterieMasquer = grilleLotterie
	for elt in nb12:
		grilleLotterieMasquer[elt]="#"

	#générer la lsite des numeros dans la grille 
	listNumGrille = [ elt for elt in grilleLotterieMasquer if elt != "#"  ]

	#génére code bare et qr code 
	code = [""] * 9
	for nb in range(9):
		code[nb] = randint(0,9)

	#genere grille html + comninaison
	z=0
	grilleLotteriePrens = []


	lst1 = []
	for x1x in range(0,9):
			lst1.append(grilleLotterieMasquer[x1x])
	grilleLotteriePrens.append(lst1)
	lst1 = []
	for x1x in range(9,18):
			lst1.append(grilleLotterieMasquer[x1x])
	grilleLotteriePrens.append(lst1)
	lst1 = []
	for x1x in range(18,27):
			lst1.append(grilleLotterieMasquer[x1x])
	grilleLotteriePrens.append(lst1)

	return({"grille":grilleLotterieMasquer,"numero":listNumGrille,"code":code})

if __name__ == '__main__':
	grille1 =genGrille()
	print(grille1)
	print(len(grille1["grille"]))
	print(len(grille1["numero"]))
# html to pdf