#!/bin/python3
import pyautogui
from time import sleep
tail = 174, 250
head = 79, 250
amount_location = 93, 209
double = 177, 212
bet_cashout = 133, 290
bet_amount = '0.01'
bankroll = '1'
address_bar = 175, 73
vault_url = 'https://bc.game/'
vault_tab = 321, 37
vault_profile = 441, 112
vault_wallet = 377, 147
vault_pro = 97, 307
vault_max = 327, 256
vault_transfer = 289, 293
vault_out = 310, 180
vault_amount = 204, 254
coin_url = 'https://bc.game/game/coinflip'
coin_tab = 50, 38
def game():
    sleep(0.1)
    pyautogui.click(coin_tab)
    sleep(0.1)
    pyautogui.click(address_bar)
    sleep(0.1)
    pyautogui.write(coin_url)
    sleep(0.1)
    pyautogui.press('enter')
    sleep(10)
    pyautogui.doubleClick(amount_location, interval=0.25)
    sleep(0.25)
    pyautogui.write(bet_amount)
    sleep(0.25)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(head)
    sleep(0.1)
def heads():
    sleep(0.1)
    pyautogui.click(coin_tab)
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(0.1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
    else:
        pyautogui.click(double)
        sleep(0.1)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(head)
    sleep(1)
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(0.1)
    else:
        pass
        sleep(0.1)
def vault():
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(0.1)
    else:
        pass
        sleep(0.1)
    pyautogui.click(vault_tab)
    sleep(0.25)
    pyautogui.click(address_bar)
    sleep(0.25)
    pyautogui.write(vault_url)
    sleep(0.25)
    pyautogui.press('enter')
    sleep(10)
    pyautogui.moveTo(vault_profile)
    sleep(0.25)
    pyautogui.click(vault_wallet)
    sleep(5)
    pyautogui.click(vault_pro)
    sleep(5)
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
def main():
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    heads()
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    vault()
while True:
    main()
