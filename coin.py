#!/bin/python3

import pyautogui
from time import sleep

tail = 350, 480
head = 200, 480
amount_location = 160, 440
double = 431, 441
bet_cashout = 292, 521
bet_amount = '0.025'


def heads():
    #bcgame coin flip martingale
    
    sleep(1)
    
    win = pyautogui.pixelMatchesColor(401, 268, (42, 45, 51))

    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.1)
        pyautogui.write(bet_amount)
        sleep(0.1)

    else:
        pyautogui.click(double)
        sleep(0.1)

    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(head)

def tails():
    #bcgame coin flip martingale
    
    sleep(1)
    
    win = pyautogui.pixelMatchesColor(401, 268, (42, 45, 51))

    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.1)
        pyautogui.write(bet_amount)
        sleep(0.1)

    else:
        pyautogui.click(double)
        sleep(0.1)

    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(tail)



def main():
    sleep(0.5)
    win = pyautogui.pixelMatchesColor(401, 268, (42, 45, 51))
    heads()
    sleep(0.5)
    win = pyautogui.pixelMatchesColor(401, 268, (42, 45, 51))
    tails()
    

while True:
    main()
