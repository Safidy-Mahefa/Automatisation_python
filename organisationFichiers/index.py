"""
# Objectif : Creer un script python qui :
    - Prend un dossier
    - Regarde chaque fichier dans ce dossier,
    - Ranger automatiquement les fichiers dans des dossiers (par type)
"""
import os       # Manipulation de fichiers/Dossiers
import shutil   # Pour déplacer un fichier...

scriptFilePath = os.path.abspath(__file__)
folderPath = os.path.dirname(scriptFilePath)    # chemin du dossier contenant index.py
filepath = ""    
                               # variable pour stocker le chemin d'un fichier...
# Lister le contenu d'un dossier
listeFichiers = os.listdir(folderPath) 

# Fonction pour creer le dossier si il n'existe pas encore
def createFolder(folderName):
    os.makedirs(folderName,exist_ok=True)
    return os.path.join(os.getcwd(),folderName) #retourner le chemin du dossier 

# couper fonction pour couper fichier dans le dossier correspondant
def cutFile(folderPath,filePath):
    shutil.move(filePath,folderPath)

# deplacer les fichiers dans les dossiers correspondant à son type:
for i in range(len(listeFichiers)):
    # Separer le nom du fichier et l'extension
    filepath = os.path.join(folderPath,listeFichiers[i])
    splited = os.path.splitext(filepath)
    extension = splited[1]

    extension = extension.lower()
    # déplacer chaque fichiers
    # alternative à switch case:
    match extension:
        case ".png":
            cutFile(createFolder("Images"),filepath)
        case ".txt":
            cutFile(createFolder("Documents_Texte"),filepath)
        case ".jpg": 
            cutFile(createFolder("Images"),filepath)
        case ".mp4": 
            cutFile(createFolder("Videos"),filepath)
        case ".mp3": 
            cutFile(createFolder("Audios"),filepath)
        case ".pdf": 
            cutFile(createFolder("PDF"),filepath)
        case ".docx": 
            cutFile(createFolder("Docx"),filepath)
        case ".py":
            print("Hello py !")
        case "":
            print("Hello User !")
        case _:
            cutFile(createFolder("Autres_Fichiers"),filepath)