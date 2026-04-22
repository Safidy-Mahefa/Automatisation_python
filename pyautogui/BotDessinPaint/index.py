import pyautogui
import time
import math

time.sleep(5) #Attendre 5 secondes avant de dessiner

"""
Dessiner un carré 

pyautogui.moveTo(500,500)
pyautogui.mouseDown() #Maintenir
#Dessiner
pyautogui.dragTo(700,500,duration=1)
pyautogui.dragTo(700,300,duration=1)
pyautogui.dragTo(500,300,duration=1)
pyautogui.dragTo(500,500,duration=1)
pyautogui.mouseUp() #Relacher

#Dessiner une spirale
distance = 300 
pyautogui.mouseDown()

while distance > 0:
    pyautogui.dragRel(distance,0,duration=0.2) #droite
    distance -= 10 #Decrementer de 10 la distance
    pyautogui.dragRel(0,distance,duration=0.2) #bas
    pyautogui.dragRel(-distance,0,duration=0.2) #gauche
    distance -= 10
    pyautogui.dragRel(0,-distance,duration=0.2) #haut
pyautogui.mouseUp()

#Dessiner une Etoile
pyautogui.mouseDown()
pyautogui.dragRel(100,-200,duration=0.2)
pyautogui.dragRel(100,200,duration=0.2)
pyautogui.dragRel(-200,-120,duration=0.2)
pyautogui.dragRel(200,-0,duration=0.2)
pyautogui.dragRel(-200,120,duration=0.2)
pyautogui.mouseUp()

#Dessiner une rose
pyautogui.mouseDown()
center_x, center_y = pyautogui.position()

scale = 250 #La grandeur
for i in range(0,720,3):
    angle = math.radians(i)
    r = scale * math.sin(10*angle) # 5 est le nombre de petales
    x =center_x + r * math.cos(angle)
    y =center_y + r * math.sin(angle)
    pyautogui.dragTo(x,y)
pyautogui.mouseUp()

"""
#Dessiner une rose
pyautogui.mouseDown()
center_x, center_y = pyautogui.position()

scale = 150 #La grandeur
for i in range(0,720,2):
    angle = math.radians(i)
    r = scale * math.sin(10*angle) # 5 est le nombre de petales #Spirale: r = scale * angle/10
    x =center_x + r * math.cos(angle)
    y =center_y + r * math.sin(angle)
    pyautogui.dragTo(x,y)
pyautogui.mouseUp()
