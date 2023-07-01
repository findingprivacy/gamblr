#!/bin/python3
# chromium BROWSER 50% ZOOM
# tab order cb, limbo, ud
import pyautogui
from time import sleep
from os import system


payout_amount = '1.65' # float(input('Payout Amount : '))
bet_amount = '0.001' # float(input('Bet Amount : '))
loss_increase_percentage = '250' # int(input('Percentage Increase on Loss : '))
reload = 89, 74

classic_dice_seed_location = 441, 514       
classic_dice_new_seed = 250, 516
classic_dice_tab = 70, 35
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
    pyautogui.click(classic_dice_tab)
    sleep(0.25)
    pyautogui.click(reload)
    sleep(10)
    pyautogui.click(classic_dice_seed_location) # change seed
    sleep(2.5)
    pyautogui.click(classic_dice_new_seed)
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
    sleep(0.1)
#    pyautogui.click(classic_dice_exit_location)

limbo_seed_location = 446, 514       
limbo_new_seed = 250, 516
limbo_tab = 190, 39
limbo_payout_location = 264, 445
limbo_auto_bet_location = 173, 180
limbo_bet_amount_location = 100, 222
limbo_enable_loss_increase_location = 89, 393
limbo_loss_increase_location = 139, 395
limbo_start_location = 165, 512



def limbo():
    #bcgame classic-dice
#    sleep(0.25)
#    with pyautogui.hold('alt'):
#        pyautogui.press('p')
#    sleep(.25)
#    pyautogui.write('opera bc.game/game/classic-dice --new-window')
#    sleep(0.25)
#    pyautogui.press('enter')
    pyautogui.click(limbo_tab)
    sleep(0.25)
    pyautogui.click(reload)
    sleep(10)
    pyautogui.click(limbo_seed_location) # change seed
    sleep(2.5)
    pyautogui.click(limbo_new_seed)
    sleep(1)
    pyautogui.click(limbo_auto_bet_location)
    sleep(0.25)
    pyautogui.doubleClick(limbo_bet_amount_location, interval=0.15)
    sleep(0.25)
    pyautogui.write(bet_amount) 
    sleep(0.25)
    pyautogui.click(limbo_enable_loss_increase_location) 
    sleep(0.25)
    pyautogui.doubleClick(limbo_loss_increase_location, interval=0.15)
    sleep(0.25)
    pyautogui.write(loss_increase_percentage)
    sleep(0.25)
    pyautogui.doubleClick(limbo_payout_location, interval=0.1)
    sleep(0.25)
    pyautogui.write(payout_amount)
    sleep(0.25)
    pyautogui.click(limbo_start_location) # on auto
    sleep(0.1)
#    sleep(60)
#    pyautogui.click(classic_dice_exit_location)


ultimate_dice_seed_location = 440, 529       
ultimate_dice_new_seed = 250, 516
ultimate_dice_tab = 309, 39
ultimate_dice_payout_location = 281, 448
ultimate_dice_auto_bet_location = 173, 180
ultimate_dice_bet_amount_location = 100, 222
ultimate_dice_enable_loss_increase_location = 86, 351
ultimate_dice_loss_increase_location = 150, 351
ultimate_dice_start_location = 165, 512

def ultimateDice():
    #bcgame classic-dice
#    sleep(0.25)
#    with pyautogui.hold('alt'):
#        pyautogui.press('p')
#    sleep(.25)
#    pyautogui.write('opera bc.game/game/classic-dice --new-window')
#    sleep(0.25)
#    pyautogui.press('enter')
    pyautogui.click(ultimate_dice_tab)
    sleep(0.25)
    pyautogui.click(reload)
    sleep(10)
    pyautogui.click(ultimate_dice_seed_location) # change seed
    sleep(2.5)
    pyautogui.click(ultimate_dice_new_seed)
    sleep(1)
    pyautogui.click(ultimate_dice_auto_bet_location)
    sleep(0.25)
    pyautogui.doubleClick(ultimate_dice_bet_amount_location, interval=0.15)
    sleep(0.25)
    pyautogui.write(bet_amount) 
    sleep(0.25)
    pyautogui.click(ultimate_dice_enable_loss_increase_location) 
    sleep(0.25)
    pyautogui.doubleClick(ultimate_dice_loss_increase_location, interval=0.15)
    sleep(0.25)
    pyautogui.write(loss_increase_percentage)
    sleep(0.25)
    pyautogui.doubleClick(ultimate_dice_payout_location, interval=0.1)
    sleep(0.25)
    pyautogui.write(payout_amount)
    sleep(0.25)
    pyautogui.click(ultimate_dice_start_location) # on auto
    sleep(0.1)

def main():
    classicDice()
    limbo()
    ultimateDice()

while True:
    main()
