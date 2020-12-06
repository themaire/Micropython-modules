# Outils pour exploiter des fichiers
import os
dirs = ("utils", "picts")
sep = "/"

def scanDir(d):
    '''
    Stock dans un dict le contenu du dossier passé en parametre. Dans le cas du dossier
    picts, les images seront chargées dans la valeur du tableau.

    @return : dictionnaire clé:nom du fichier / valeurs:chemin complet ou image chargée en
    mémoire.
    '''
    liste = {}
    root = os.listdir("/")
    if(d in dirs and d in root):
        listRep = os.listdir(sep+d)
        for i in listRep:
            cheminFichier = sep + d + sep + i # Chemin complet du fichier
            if(d == "utils"):
                liste[i[:-4]] = cheminFichier
            elif(d == "picts"):   
                liste[i[:-4]] = loadImage(cheminFichier)
        return liste
    else:
        print(d + " n'est pas un répertoire valide.")

def lireF(file):
    """
    Utilisé pour lire le fichier des mots de passe wifi.
    """
    f = open(file,'r')
    string =  f.read()
    f.close()
    return str(string)

def loadImage(name):
    """
    Charge une image *.pbm en guise de tuple contenant l'image en bytearray
    ainsi que les coordonnées de l'image.

    @param:name = Le nom/chemin de l'image dans la mémoire de l'esp
    @return     = Un tuple contenant les données de l'image
    """
    with open(name, 'rb') as f:
            f.readline() # Magic number
            f.readline() # Creator comment

            dim = f.readline() # Dimensions de l'image
            dim = str(dim).split(" ") # Obtenir une liste / Oui str() car c'était de type bytes
            dimensions = (int(dim[0][2:]), int(dim[1][:2])) # Convert en tuple

            image = bytearray(f.read())
            data = {"image" : image, "dimensions" : dimensions}
            return data

if __name__ == '__main__':

    lireF('utils/ssis_password.txt')
