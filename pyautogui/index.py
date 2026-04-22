import pyautogui

pyautogui.moveTo(500,300) #Bouger la souris à une position de l'ecran / params : (x,y)
#Simuler un drag  de souris avec une duree (drag absolu par rapport à l'ecran)
#dragRel() permet de faire un drag relatif par rapport aus souris
pyautogui.dragTo(700,500,duration=1)
pyautogui.click() #Clique à al position où la souris se trouve / params : (x,y)
#Appuyer sur une touche
pyautogui.press("enter")
pyautogui.write("Hello World") #Ecrit du texte là ou il y a un input
#Combinaison de touches
pyautogui.hotkey("ctrl","a")

#Maintenir le clic gauche de la souris / params: (button = "...") left, right, middle?
pyautogui.mouseDown()
pyautogui.mouseUp() #Relacher le clic

