import pyautogui
from time import sleep
classic_dice_tab = 100, 45
classic_dice_start_location = 193, 518
limbo_tab = 152, 48
limbo_start_location = 193, 518
ultimate_dice_tab = 236, 42
ultimate_dice_start_location = 195, 524
number_of_bets = 130, 279
bets = '5'
def classicDice():
    pyautogui.click(classic_dice_tab)
    sleep(0.25)
    pyautogui.doubleClick(number_of_bets, interval=0.15)
    sleep(0.25)
    pyautogui.write(bets) 
    sleep(0.25)
    pyautogui.click(classic_dice_start_location) # on auto
    sleep(0.1)
def limbo():
    pyautogui.click(limbo_tab)
    sleep(0.25)
    pyautogui.doubleClick(number_of_bets, interval=0.15)
    sleep(0.25)
    pyautogui.write(bets) 
    sleep(0.25)
    pyautogui.click(limbo_start_location) # on auto
    sleep(0.1)
def ultimateDice():
    pyautogui.click(ultimate_dice_tab)
    sleep(0.25)
    pyautogui.doubleClick(number_of_bets, interval=0.15)
    sleep(0.25)
    pyautogui.write(bets) 
    sleep(0.25)
    pyautogui.click(ultimate_dice_start_location) # on auto
    sleep(0.1)
def main():
    classicDice()
    limbo()
    ultimateDice()
while True:
    main()
