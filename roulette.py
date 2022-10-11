# -*- coding: utf-8 -*-
from re import X
import pyautogui as pg
from PIL import ImageGrab
from functools import partial
import screeninfo
import time

img_go_btn = r'C:\python\image_processing\roulette\go_btn.png'
img_x_btn = r'C:\python\image_processing\roulette\x_btn.png'
img_x2_btn = r'C:\python\image_processing\roulette\x2_btn.png'

def find_and_clik(img):
    Flag = False
    confi = 0.9
    
    find_img = pg.locateOnScreen(img, confidence=confi)
    time.sleep(0.01)

    if find_img != None:
        time.sleep(0.01)
        pg.click(find_img, clicks=1, duration=0.1)
        Flag = True

    return Flag


if __name__ =='__main__':

    try:
        while True:
            
            find_and_clik(img_go_btn)
            find_and_clik(img_x_btn)            
            find_and_clik(img_x2_btn)            

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass