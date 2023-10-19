"""
Pour ce deuxième exercice, le but est de trier les fichiers présents dans le dossier 'unsorted_files' par extension
Afin d'y arriver, vous aurez besoin de deux modules python : os, shutil

os : module qui permet l'interaction avec le système d'exploitation, nous aurons besoin de deux methodes
	(1) os.listdir(<chemin_du_dossier>) : renvoie une liste avec les elements que contient le dossier spécifié
	(2) os.path.splitext(<fichier>) : renvoie un tuple de deux elements, le premier est le nom du fichier et le deuxième est son extension, ex : os.path.splitext('main.py') -> ('main', '.py')
	(3) os.path.exists(<chemin_du_dossier>) : renvoie 'True' si le chemin existe dans l'ordinateur, False sinon.
	(4) os.makedirs(<nom_du_dossier>) : crée un dossier dans le chemin spécifié.
	pour plus de méthodes : https://www.w3schools.com/python/module_os.asp

shutil : permet, avec des methodes, d'effectuer des operations sur des fichiers et dossiers (copier, couper, supprimer)
	(1) shutil.move(<ancien_chemin>, <nouveau chemin>) : déplace le fichier d'un dossier vers un autre
	(2) shutil.copy2(<ancien_chemin_avec_nom_du_fichier>, <nouveau_chemin_avec_nom_du_fichier>) : permet d'effectuer la copie d'un fichier tout en gardant les meta-données
	
	Autres méthodes de copie de fichiers:

	| Function         | Inclue les meta-données  | besoin du fichier de destination | Copie le contenu du fichier |
	| ---------------- | ------------------------ | -------------------------------- | --------------------------- |
	| `.copy()`        | non                      | oui                              | non                         |
	| `.copyfile()`    | non                      | non                              | non                         |
	| `.copy2()`       | oui                      | oui                              | non                         |
	| `.copyfileobj()` | non                      | non                              | oui                         |

Pour faire l'exercice, l'idée est de lister les fichiers non triés du dossier 'unsorted_files' avec leur extension, puis de passer par chaque fichier, si c'est une nouvelle extension de fichier, on crée un dossier correspondant à l'extension dans le dossier 'sorted_files' et on copie le fichier, sinon on ne fait que copier le fichier dans le dossier approprié
"""


import os
import shutil


chemin_du_dossier = ''


liste_des_fichiers = #..

print(liste_des_fichiers)


for fichier in liste_des_fichiers:
    
    nom, extension = #..
    print(extension)
    
    # Enlever le point de la chaine 'extensions' ('.py' -> 'py')
	#..
    print(extension)

	chemin_dossier_par_extension = #..
    if #.. : # si le dossier de l'extension existe déjà
        # on copie le fichier vers la nouvelle destination
    else :   # sinon, on crée le dossier, et on copie le fichier
        nom_dossier = #..
		#..
		#..
