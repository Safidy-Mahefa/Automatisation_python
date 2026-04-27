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
delai = 0 #Le delai du sleep

# La fonction pour démarrer le recording
def startRecording():
    for i,val in enumerate(listeTouches): #Parcourir le tableau avec l'index
        if i == 0:
           delai = val[2]
        else:
            delai = val[2] - listeTouches[i-1][2] #Le current - precedent
        time.sleep(delai) #Attendre le delai
        print(delai)

        #On appuie ou clique sur les touches correspondants.
        if val[0] == "keyboard":
            pyautogui.write(str(val[1])) #Pour des chaines seulement..
        elif val[0] == "mouse":
            pyautogui.click(val[1][0],val[1][1])

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
    print(listeTouches)

# Fonction callback qui est appellee quand on clique sur la souris
def onClickMouse(x,y,button,pressed):
    if pressed:
        #Temps écoulé
        tempsEcoule = time.perf_counter() - start_timer
        #Stocker le type,coordonnees et temps
        listeTouches.append(["mouse",[x,y],tempsEcoule])
        print(f"Souris cliqué : {x},{y}")

def onPlay(key):
     # Pour démarrer l'enregistrement
    if str(key) == "Key.enter":
        print("L'enregistrement a demarre")
        startRecording()


# CREATION DES LISTENERS
keyboard_listener = keyboard.Listener(on_press = onClickKeyboard)
startPlayingListener = keyboard.Listener(on_press = onPlay)
mouse_listener = mouse.Listener(on_click= onClickMouse)

#Démarrage de l'écoute
keyboard_listener.start()
mouse_listener.start()
startPlayingListener.start()

#garder lécoute active
keyboard_listener.join()
mouse_listener.join() #attendre (bloque le programme) jusqu'a ce qu'on termine par : timeout, conditions...Key.enter
startPlayingListener.join()


# .stop() pour stopper l'ecoute


print(listeTouches)

