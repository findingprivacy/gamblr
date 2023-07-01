#!/bin/python3
import pyautogui
from time import sleep
tail = 174, 250
head = 79, 250
amount_location = 93, 209
double = 177, 212
bet_cashout = 133, 290
bet_amount = '0.025'
def heads():
    sleep(1)
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
        sleep(0.25)
    else:
        pyautogui.click(double)
        sleep(0.25)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(head)
def tails():
    sleep(1)
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
        sleep(0.25)
    else:
        pyautogui.click(double)
        sleep(0.25)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(tail)
def main():
    sleep(0.5)
    win = pyautogui.pixelMatchesColor(406, 310, (58, 181, 25))
    heads()
    sleep(0.5)
    win = pyautogui.pixelMatchesColor(406, 310, (58, 181, 25))
    tails()
while True:
    main()
