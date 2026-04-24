# Projet poujr rejouer ce que l'utilisateur a fait pendant l'enregistrement avec pyautogui et pynput
import pyautogui
from pynput import keyboard #Listener prend des fonctions callbacks q'on cree
from pynput import mouse #Listener pour la souris
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

# FONCTIONS CALLBACKS
# Fonction callback qui est appellee quand on clique sur une touche du clavier
def onClickKeyboard(key):
    global keyboard_listener #La variable globale listener clavier
    global mouse_listener

    #Enregistrement des touches CLAVIERS pressés dans un tableau avec timestamp
    print("La touche pressee est : ", key)
    #Temps écoulé
    tempsEcoule = time.perf_counter() - start_timer
    listeTouches.append(["keyboard",key,tempsEcoule]) # [type,touche,temps]

    #Cliquer sur F7 pour quiter le recording...
    if str(key) == "Key.f7":
        keyboard_listener.stop()
        mouse_listener.stop()

# Fonction callback qui est appellee quand on clique sur la souris
def onClickMouse(x,y,button,pressed):
    if pressed:
        #Temps écoulé
        tempsEcoule = time.perf_counter() - start_timer
        #Stocker le type,coordonnees et temps
        listeTouches.append(["mouse",[x,y],tempsEcoule])
        print(f"Souris cliqué : {x},{y}")


# CREATION DES LISTENERS
keyboard_listener = keyboard.Listener(on_press = onClickKeyboard)
mouse_listener = mouse.Listener(on_click= onClickMouse)

#Démarrage de l'écoute
keyboard_listener.start()
mouse_listener.start()

#garder lécoute active
keyboard_listener.join()
mouse_listener.join() #attendre (bloque le programme) jusqu'a ce qu'on termine par : timeout, conditions...
# .stop() pour stopper l'ecoute


print(listeTouches)

