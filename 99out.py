#!/bin/python3

import pyautogui
from time import sleep
from os import system


payout_amount = '99' # float(input('Payout Amount : '))
bet_amount = '0.0002' # float(input('Bet Amount : '))
loss_increase_percentage = '1.015' # int(input('Percentage Increase on Loss : '))
seed_location = 460, 375       
new_seed = 267, 458


classic_dice_payout_location = 318, 299
classic_dice_auto_bet_location = 239, 146
classic_dice_bet_amount_location = 188, 176
classic_dice_enable_loss_increase_location = 168, 290
classic_dice_loss_increase_location = 219, 291
classic_dice_start_location = 211, 367



def classicDice():
    #bcgame classic-dice
    sleep(0.1)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    sleep(1)
    pyautogui.write('opera bc.game/game/classic-dice --new-window')
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


limbo_payout_location = 300, 325
limbo_auto_bet_location = 239, 148
limbo_bet_amount_location = 187, 177
limbo_enable_loss_increase_location = 168, 291
limbo_loss_increase_location = 217, 292
limbo_start_location = 212, 369

def limbo():
    #bcgame classic-dice
    sleep(0.1)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    sleep(1)
    pyautogui.write('opera bc.game/game/limbo --new-window')
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

ultimate_dice_payout_location = 315, 330
ultimate_dice_auto_bet_location = 238, 148
ultimate_dice_bet_amount_location = 188, 177
ultimate_dice_enable_loss_increase_location = 169, 261
ultimate_dice_loss_increase_location = 220, 263
ultimate_dice_start_location = 212, 368

def ultimateDice():
    #bcgame classic-dice
    sleep(0.1)
    with pyautogui.hold('alt'):
        pyautogui.press('p')
    sleep(1)
    pyautogui.write('opera bc.game/game/ultimate-dice --new-window')
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
