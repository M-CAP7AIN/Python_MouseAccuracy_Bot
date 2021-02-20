import pyautogui
import time
from PIL import ImageGrab,ImageOps
from numpy import *
import keyboard


def RestartGame():
    time.sleep(1)
    pyautogui.click(299 , 619)
    time.sleep(1)

    

def PressSpace(x,y,w,h):
    pyautogui.click(x+(w/2),y+(h/2)+10)

def FindKeys():
    tbox  = pyautogui.locateOnScreen('sample.png' , region=(0,140 , 1363 , 736))
    if(tbox != None):
        print("Find: " + str(tbox))
        PressSpace(tbox.left , tbox.top , tbox.width , tbox.height)

def Banner():
    print("""
███╗   ███╗       ██████╗ █████╗ ██████╗ ███████╗ █████╗ ██╗███╗   ██╗
████╗ ████║      ██╔════╝██╔══██╗██╔══██╗╚════██║██╔══██╗██║████╗  ██║
██╔████╔██║█████╗██║     ███████║██████╔╝    ██╔╝███████║██║██╔██╗ ██║
██║╚██╔╝██║╚════╝██║     ██╔══██║██╔═══╝    ██╔╝ ██╔══██║██║██║╚██╗██║
██║ ╚═╝ ██║      ╚██████╗██║  ██║██║        ██║  ██║  ██║██║██║ ╚████║
╚═╝     ╚═╝       ╚═════╝╚═╝  ╚═╝╚═╝        ╚═╝  ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
    """)
    print('Press Q:Exit. ')

def Main():
    try:
        Banner()
        RestartGame()
        while keyboard.is_pressed('q')==False:
            FindKeys()
            time.sleep(0)

    except Exception as e:
        print("Exit." + str(e))

Main()
