#!/bin/python3
# OPERA BROWSER 33% ZOOM
import pyautogui
from time import sleep
from os import system


payout_amount = '1.5' # float(input('Payout Amount : '))
bet_amount = '0.01' # float(input('Bet Amount : '))
loss_increase_percentage = '250' # int(input('Percentage Increase on Loss : '))
seed_location = 456, 389       
new_seed = 277, 465
classic_dice_payout_location = 265, 326
classic_dice_auto_bet_location = 174, 163
classic_dice_bet_amount_location = 134, 195
classic_dice_enable_loss_increase_location = 115, 306
classic_dice_loss_increase_location = 156, 309
classic_dice_start_location = 147, 383
classic_dice_exit_location = 481, 44



def classicDice():
    #bcgame classic-dice
    sleep(0.1)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    sleep(1)
    pyautogui.write('opera bc.game/game/classic-dice')
    sleep(1)
    pyautogui.press('enter')
    sleep(10)
    pyautogui.click(seed_location) # change seed
    sleep(2.5)
    pyautogui.click(new_seed)
    sleep(1)
    pyautogui.click(classic_dice_auto_bet_location)
    sleep(0.1)
    pyautogui.doubleClick(classic_dice_bet_amount_location, interval=0.15)
    sleep(0.1)
    pyautogui.write(bet_amount) 
    sleep(0.1)
    pyautogui.click(classic_dice_enable_loss_increase_location) 
    sleep(0.1)
    pyautogui.doubleClick(classic_dice_loss_increase_location, interval=0.15)
    sleep(0.1)
    pyautogui.write(loss_increase_percentage)
    sleep(0.1)
    pyautogui.doubleClick(classic_dice_payout_location, interval=0.1)
    sleep(0.1)
    pyautogui.write(payout_amount)
    sleep(0.1)
    pyautogui.click(classic_dice_start_location) # on auto
    sleep(5)
    pyautogui.click(classic_dice_exit_location)



