#!/bin/python3
# chromium BROWSER 50% ZOOM
# tab order cb, limbo, ud
import pyautogui
from time import sleep
from os import system
bankroll = '5'
address_bar = 175, 73
vault_url = 'https://bc.game/'
vault_tab = 321, 37
vault_profile = 410, 112
vault_wallet = 382, 147
vault_pro = 90, 307
vault_max = 327, 256
vault_transfer = 289, 293
vault_out = 310, 180
vault_amount = 204, 254
def vault():
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
def main():
    vault()
    sleep(300)
while True:
    main()
