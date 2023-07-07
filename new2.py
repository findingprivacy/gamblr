#!/bin/python3
#1024x768
#zoom 50%
import pyautogui
from time import sleep
tail = 174, 250
head = 155, 261
amount_location = 159, 225
double = 235, 225
bet_cashout = 195, 300
bet_amount = '0.00001'
bankroll = '0.87381'
vault_tab = 250, 45
vault_max = 384, 267
vault_transfer = 345, 310
vault_in = 275, 193
vault_out = 375, 193
vault_amount = 275, 270
coin_tab = 118, 45
def heads():
    sleep(0.1)
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
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
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
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
def vault():
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.click(vault_tab)
        sleep(0.1)
        pyautogui.click(vault_in)
        sleep(0.1)
        pyautogui.click(vault_max)
        sleep(0.1)
        pyautogui.click(vault_transfer)
        sleep(0.1)
        pyautogui.click(vault_out)
        sleep(0.1)
        pyautogui.doubleClick(vault_amount, interval=0.25)
        sleep(0.1)
        pyautogui.write(bankroll)
        sleep(0.1)
        pyautogui.click(vault_transfer)
        sleep(0.1)
        pyautogui.click(coin_tab)
        sleep(0.1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
        sleep(0.1)
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.click(head)
        sleep(1)
    else:
        sleep(0.1)
        pyautogui.click(vault_tab)
        sleep(0.1)
        pyautogui.click(vault_in)
        sleep(0.1)
        pyautogui.click(vault_max)
        sleep(0.1)
        pyautogui.click(vault_transfer)
        sleep(0.1)
        pyautogui.click(vault_out)
        sleep(0.1)
        pyautogui.doubleClick(vault_amount, interval=0.25)
        sleep(0.1)
        pyautogui.write(bankroll)
        sleep(0.1)
        pyautogui.click(vault_transfer)
        sleep(0.1)
        pyautogui.click(coin_tab)
        sleep(0.1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
        sleep(0.1)
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.click(head)
        sleep(1)
def main():
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
    vault()
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
    tails()
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
    heads()
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
    tails()
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
    heads()
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
    tails()
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
    heads()
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
    tails()
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
    heads()
    win = pyautogui.pixelMatchesColor(484, 321, (42, 45, 51))
    tails()

while True:
    main()
