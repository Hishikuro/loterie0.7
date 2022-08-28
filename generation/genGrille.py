"""
file :Ce fichier  contient une fonction grilleGen1 qui générer une grille en HTML et CSS .

date :  30/07/2022
Auteur : Hi_shikuro 
"""
def grilleGen1(grille1):
	from codeBar import codebar13c
	listeGB = ["<div><p>"+ str(grille1["grille"][i])+"</p></div>" for i in range(len(grille1["grille"]))]
	listeG=[]
	for nbelement in range(len(listeGB)):
		if "#" in listeGB[nbelement]  : 
			listeG.append(listeGB[nbelement].replace("<div><p>#</p></div>","<div class='bkl'><p>#</p></div>"))
		else :
			listeG.append(listeGB[nbelement])
		
	agez1 = """<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>grille</title>
		<style type="text/css">
			.flex{
				display: flex;
				flex-wrap: nowrap;
				
				

			}
			.flex > div
			{
				
				width: 100px;
				height: 100px;
				border: 10px solid black;
				margin: 1em;


			}
			.grille
			{
				
				text-align: center;
				border: 3px solid black;
			

			}
			p{
				vertical-align: middle;
				margin-top: 40px;
				font-size: 26px;
			}
			.bkl{
				background-color: black;
			}
		</style>
	</head>
	<body>
		<div class="grille">
		<div class="flex">"""

	for nbelt in range(9):
		agez1+= listeG[nbelt]

	agez2 ="""
		</div>
		<div class="flex">"""
	for nbelt in range(9,18):
		agez2+= listeG[nbelt]

	agez3 =	"""</div>
		<div class="flex">"""
	for nbelt in range(18,27):
		agez3+= listeG[nbelt]

	code = ""
	for num in grille1["code"]:
		code+= str(num)


	agez4 =	"""</div>
		<p>"""+code+"""</p>
		<p><img style="width:25%;height:25%"src='00"""+code+"""00.svg'></p>
		</div>

		<div style="width:100%;height: 100%;border: 3px solid black;margin-top: 2em;background-color: black;"></div>
	</body>
	</html>"""
	agez = agez1 + agez2 + agez3 + agez4
	with open("./data/grille/"+code+".html","a") as file :
		file.write(agez)

	codebar13c("00"+code+"00")

if __name__ == '__main__':
	grille1 = {'grille': ['#', 7, '#', 13, 15, '#', '#', 20, 22, '#', 25, '#', 34, 39, '#', 51, 57, 59, '#', 62, 63, '#', 75, 76, 89, 94, '#'], 'numero': [7, 13, 15, 20, 22, 25, 34, 39, 51, 57, 59, 62, 63, 75, 76, 89, 94], 'code': [5, 5, 0, 8, 8, 4, 8, 0, 7]}
	grilleGen1(grille1)