#!/bin/python3
import pyautogui
from time import sleep
bet_amount = '0.0001'
bankroll = '.3069'
tail = 233, 262
head = 155, 262
amount_location = 157, 224
double = 232, 225
half = 211, 227
bet_cashout = 192, 303
coin_tab = 100, 40
coin_seed = 501, 531
coin_new_seed = 304, 604
vault_tab = 300, 40
vault_max = 385, 268
vault_transfer = 345, 308
vault_out = 375, 192
vault_in = 275, 192
vault_amount = 256, 267
def heads():
    sleep(0.1)
    win = pyautogui.pixelMatchesColor(481, 325, (59, 193, 23))
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
        sleep(1)
        pyautogui.click(vault_out)
        sleep(0.1)
        pyautogui.doubleClick(vault_amount, interval=0.25)
        sleep(0.1)
        pyautogui.write(bankroll)
        sleep(0.1)
        pyautogui.click(vault_transfer)
        sleep(1)
        pyautogui.click(coin_tab)
        sleep(0.1)
        pyautogui.click(coin_seed)
        sleep(1)
        pyautogui.click(coin_new_seed)
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
        pyautogui.click(vault_tab)
        sleep(0.1)
        pyautogui.click(vault_in)
        sleep(0.1)
        pyautogui.click(vault_max)
        sleep(0.1)
        pyautogui.click(vault_transfer)
        sleep(1)
        pyautogui.click(vault_out)
        sleep(0.1)
        pyautogui.doubleClick(vault_amount, interval=0.25)
        sleep(0.1)
        pyautogui.write(bankroll)
        sleep(0.1)
        pyautogui.click(vault_transfer)
        sleep(1)
        pyautogui.click(coin_tab)
        sleep(0.1)
        pyautogui.click(coin_seed)
        sleep(1)
        pyautogui.click(coin_new_seed)
        sleep(1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
        sleep(0.1)
    else:
        pyautogui.click(half)
        sleep(0.1)

    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(head)
    sleep(1)
def vault():
    win = pyautogui.pixelMatchesColor(481, 325, (59, 193, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
    else:
        pass
    pyautogui.click(vault_tab)
    sleep(0.1)
    pyautogui.click(vault_in)
    sleep(0.1)
    pyautogui.click(vault_max)
    sleep(0.1)
    pyautogui.click(vault_transfer)
    sleep(1)
    pyautogui.click(vault_out)
    sleep(0.1)
    pyautogui.doubleClick(vault_amount, interval=0.25)
    sleep(0.1)
    pyautogui.write(bankroll)
    sleep(0.1)
    pyautogui.click(vault_transfer)
    sleep(1)
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
def game():
    vault()
    tails()
    heads()
    tails()
def newSeed():
    pyautogui.click(coin_seed)
    sleep(1)
    pyautogui.click(coin_new_seed)
    sleep(1)
def main():
    heads()
    tails()
while True:
    main()
