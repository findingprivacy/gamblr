#!/bin/python3
# chromium BROWSER 50% ZOOM
# tab order cb, limbo, ud
import pyautogui
from time import sleep
from os import system
bet_amount = '100' # float(input('Bet Amount : '))
classic_dice_seed_location = 439, 531       
classic_dice_new_seed = 245, 518
classic_dice_tab = 50, 38
classic_dice_payout_location = 263, 456
classic_dice_auto_bet_location = 182, 186
classic_dice_bet_amount_location = 95, 229
classic_dice_enable_loss_increase_location = 122, 354
classic_dice_loss_increase_location = 171, 353
classic_dice_start_location = 137, 502
def classicDice():
    sleep(0.1)
    win = pyautogui.pixelMatchesColor(460, 196, (59, 193, 23))
    sleep(0.25)
    if win:
        pyautogui.click(classic_dice_seed_location) 
        sleep(2.5)
        pyautogui.click(classic_dice_new_seed)
        sleep(2)
        pyautogui.doubleClick(bet_amount_location, interval=0.15)
        sleep(0.1)
        pyautogui.write(bet_amount)
        sleep(0.1)
        pyautogui.click(start_location)
        sleep(0.5)
    else:
        sleep(0.1)
def main():
    classicDice()
    sleep(1)

while True():
    main()