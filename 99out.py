#!/bin/python3
# chromium BROWSER 50% ZOOM
import pyautogui
from time import sleep
from os import system


payout_amount = '1.65' # float(input('Payout Amount : '))
bet_amount = '0.001' # float(input('Bet Amount : '))
loss_increase_percentage = '250' # int(input('Percentage Increase on Loss : '))
seed_location = 441, 514       
new_seed = 250, 516
reload = 89, 74
classic_dice_payout_location = 289, 406
classic_dice_auto_bet_location = 173, 180
classic_dice_bet_amount_location = 100, 222
classic_dice_enable_loss_increase_location = 89, 393
classic_dice_loss_increase_location = 139, 395
classic_dice_start_location = 165, 512




def classicDice():
    #bcgame classic-dice
#    sleep(0.25)
#    with pyautogui.hold('alt'):
#        pyautogui.press('p')
#    sleep(.25)
#    pyautogui.write('opera bc.game/game/classic-dice --new-window')
#    sleep(0.25)
#    pyautogui.press('enter')
    pyautogui.click(reload)
    sleep(10)
    pyautogui.click(seed_location) # change seed
    sleep(2.5)
    pyautogui.click(new_seed)
    sleep(1)
    pyautogui.click(classic_dice_auto_bet_location)
    sleep(0.25)
    pyautogui.doubleClick(classic_dice_bet_amount_location, interval=0.15)
    sleep(0.25)
    pyautogui.write(bet_amount) 
    sleep(0.25)
    pyautogui.click(classic_dice_enable_loss_increase_location) 
    sleep(0.25)
    pyautogui.doubleClick(classic_dice_loss_increase_location, interval=0.15)
    sleep(0.25)
    pyautogui.write(loss_increase_percentage)
    sleep(0.25)
    pyautogui.doubleClick(classic_dice_payout_location, interval=0.1)
    sleep(0.25)
    pyautogui.write(payout_amount)
    sleep(0.25)
    pyautogui.click(classic_dice_start_location) # on auto
    sleep(60)
#    pyautogui.click(classic_dice_exit_location)

while True:
    classicDice()
