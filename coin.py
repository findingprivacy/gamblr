#!/bin/python3
import pyautogui
from time import sleep
tail = 233, 262
head = 155, 262
amount_location = 157, 224
double = 232, 225
bet_cashout = 192, 303
bet_amount = '0.00001'
def heads():
    sleep(0.1)
    win = pyautogui.pixelMatchesColor(481, 325, (59, 193, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
    else:
        pyautogui.click(double)
        sleep(0.1)
        pyautogui.click(double)
        sleep(0.1)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(head)
    sleep(1)
def tails():
    sleep(0.1)
    win = pyautogui.pixelMatchesColor(481, 325, (59, 193, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
    else:
        pyautogui.click(double)
        sleep(0.1)
        pyautogui.click(double)
        sleep(0.1)       
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(tail)
    sleep(1)
def main():
    win = pyautogui.pixelMatchesColor(481, 325, (59, 193, 23))
    heads()
    win = pyautogui.pixelMatchesColor(481, 325, (59, 193, 23))
    tails()
while True:
    main()
