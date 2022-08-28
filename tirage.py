"""
file :Ce fichier   est un programme
qui permette de tirer des nombre aleatoire entre 1 et 100 compris,
jusqu'a enter au clavier le mot "stop" .

date :  30/07/2022
Auteur : Hi_shikuro 
"""

def tirage():
	from random import randint
	encour=True
	tirageS = []
	while encour:
		print("Taper sur 'Enter'  pour continuer le tirage ou ecrire 'stop' puis taper 'Enter' pour stoper le tirage ")
		choix = input(">")
		if choix == "stop":
			encour=False
			return(tirageS)
		else :
			tirage = randint(1,100)
			while tirage in tirageS:
				tirage = randint(1,100)
			tirageS.append(tirage)
			print(tirage)

if __name__ == '__main__':
	tirage1 = tirage()
	print(tirage1)
