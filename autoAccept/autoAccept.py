import pydirectinput
import pyautogui
import time

aceitar = 'aceitar.png'

def autoAccept(): 
    cont = 1                
    while True:                                                     #Loop inifinito    
        accept = pyautogui.locateOnScreen(aceitar,confidence=0.9)   #Localiza a imagem na tela
        if accept:                                                  #Se conseguir localizar
            pyautogui.moveTo(accept)                                #Move o mouse até o meio da onde foi localizado
            pydirectinput.click()                                   #Clica no mesmo lugar onde ta o mouse
            print(f"CONVITE ACEITO ({cont})")       
            cont += 1                                               #Aumenta 1 no contador
            time.sleep(1)                                           #Espera 1 segundo e repete o loop

autoAccept()                                                        #Chama a função autoAccept
