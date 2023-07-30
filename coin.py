#!/bin/python3
import pyautogui
from time import sleep
bet_amount = '0.0001'
tail = 231, 285
head = 153, 283
amount_location = 157, 224
double = 230, 227
bet_cashout = 190, 320
def heads():
    sleep(0.1)
    win = pyautogui.pixelMatchesColor(481, 320, (59, 193, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
        sleep(0.1)
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
    win = pyautogui.pixelMatchesColor(481, 320, (59, 193, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
        sleep(0.1)
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
    heads()
    tails()
while True:
    main()
