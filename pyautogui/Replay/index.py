# Projet poujr rejouer ce que l'utilisateur a fait pendant l'enregistrement avec pyautogui et pynput
import pyautogui
from pynput.keyboard import Listener #Listener prend des fonctions callbacks q'on cree
import time #Pour la gestion des temps

"""
Etapes  :
    - Ecoute des evenements (souris et claviers)
    - Stopper l'écoute à un moment donné
    - Enregistrer les evenements (type,coordonnees,timestamp) en les stockant dans une liste
    - Convertir les enregistrements en json
    - Relire et rejouer les evenements avec pyautogui
"""
start_timer = time.perf_counter() #Démarrer le chrono en stockant le temps de demarrage.
#Liste pour stocker les touches
listeTouches = []
# Fonction callback qui est appellee quand on clique sur une touche
def maFonction(key):
    #Enregistrement des touches pressés dans un tableau avec timestamp
    print("La touche pressee est : ", key)
    #Temps écoulé
    tempsEcoule = time.perf_counter() - start_timer
    listeTouches.append(["keyboard",key,tempsEcoule]) # [type,touche,temps]

    #Cliquer sur F7 pour quiter le recording...
    if str(key) == "Key.f7":
        listener.stop()

# Creation du listener
listener = Listener(on_press = maFonction)
listener.start()
listener.join(5) #attendre (bloque le programme) jusqu'a ce qu'on termine par : timeout, conditions. => 5 secondes
# .stop() pour stopper l'ecoute
print(listeTouches)

