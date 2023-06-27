#!/bin/python3

import pyautogui
from time import sleep
from os import system


payout_amount = '99' # float(input('Payout Amount : '))
bet_amount = '0.0002' # float(input('Bet Amount : '))
loss_increase_percentage = '1.015' # int(input('Percentage Increase on Loss : '))
seed_location = 441, 526       
new_seed = 246, 516


classic_dice_payout_location = 285, 404
classic_dice_auto_bet_location = 175, 179
classic_dice_bet_amount_location = 101, 221
classic_dice_enable_loss_increase_location = 70, 394
classic_dice_loss_increase_location = 141, 393
classic_dice_start_location = 131, 511



def classicDice():
    #bcgame classic-dice
    sleep(0.1)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    sleep(1)
    pyautogui.write('chromium bc.game/game/classic-dice --new-window')
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
    sleep(0.1)


limbo_payout_location = 260, 444
limbo_auto_bet_location = 175, 179
limbo_bet_amount_location = 101, 221
limbo_enable_loss_increase_location = 70, 394
limbo_loss_increase_location = 141, 393
limbo_start_location = 131, 511

def limbo():
    #bcgame classic-dice
    sleep(0.1)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    sleep(1)
    pyautogui.write('chromium bc.game/game/limbo --new-window')
    sleep(1)
    pyautogui.press('enter')
    sleep(10)
    pyautogui.click(seed_location) # change seed
    sleep(2.5)
    pyautogui.click(new_seed)
    sleep(1)
    pyautogui.click(limbo_auto_bet_location)
    sleep(0.1)
    pyautogui.doubleClick(limbo_bet_amount_location, interval=0.15)
    sleep(0.1)
    pyautogui.write(bet_amount) 
    sleep(0.1)
    pyautogui.click(limbo_enable_loss_increase_location) 
    sleep(0.1)
    pyautogui.doubleClick(limbo_loss_increase_location, interval=0.15)
    sleep(0.1)
    pyautogui.write(loss_increase_percentage)
    sleep(0.1)
    pyautogui.doubleClick(limbo_payout_location, interval=0.1)
    sleep(0.1)
    pyautogui.write(payout_amount)
    sleep(0.1)
    pyautogui.click(limbo_start_location) # on auto
    sleep(0.1)

ultimate_dice_payout_location = 268, 450
ultimate_dice_auto_bet_location = 175, 179
ultimate_dice_bet_amount_location = 101, 221
ultimate_dice_enable_loss_increase_location = 70, 394
ultimate_dice_loss_increase_location = 141, 393
ultimate_dice_start_location = 131, 511

def ultimateDice():
    #bcgame classic-dice
    sleep(0.1)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    sleep(1)
    pyautogui.write('chromium bc.game/game/ultimate-dice --new-window')
    sleep(1)
    pyautogui.press('enter')
    sleep(10)
    pyautogui.click(seed_location) # change seed
    sleep(2.5)
    pyautogui.click(new_seed)
    sleep(1)
    pyautogui.click(ultimate_dice_auto_bet_location)
    sleep(0.1)
    pyautogui.doubleClick(ultimate_dice_bet_amount_location, interval=0.15)
    sleep(0.1)
    pyautogui.write(bet_amount) 
    sleep(0.1)
    pyautogui.click(ultimate_dice_enable_loss_increase_location) 
    sleep(0.1)
    pyautogui.doubleClick(ultimate_dice_loss_increase_location, interval=0.15)
    sleep(0.1)
    pyautogui.write(loss_increase_percentage)
    sleep(0.1)
    pyautogui.doubleClick(ultimate_dice_payout_location, interval=0.1)
    sleep(0.1)
    pyautogui.write(payout_amount)
    sleep(0.1)
    pyautogui.click(ultimate_dice_start_location) # on auto
    sleep(0.1)

def clear():
     sleep(0.1)
     with pyautogui.hold('shift'):
        with pyautogui.hold('alt'):
            sleep(0.1)
            pyautogui.press('c')
            sleep(0.1)
            pyautogui.press('c')
            sleep(0.1)
            pyautogui.press('c')


def main():
    classicDice()
    limbo()
    ultimateDice()
    sleep(900)
    clear()

while True:
    main()
