#opera zoom 50, payout 99, increase 1.25, on win -100, 50 games check res or double
import pyautogui
from time import sleep
numbet = '49'
bet_amount = '0.0017'
bet_amount_location = 153, 236
start_location = 191, 526
double = 232, 237
numbetloc = 174, 281
classic_dice_seed_location = 500, 517       
classic_dice_new_seed = 302, 602
classic_dice_tab = 89, 44
def classicDice():
    pyautogui.click(classic_dice_tab)
    sleep(0.1)
    win = pyautogui.pixelMatchesColor(495, 195, (59, 193, 23))
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
    else:
        pyautogui.click(double) 
        sleep(0.1)
    pyautogui.doubleClick(numbetloc, interval=0.15)
    sleep(0.1)
    pyautogui.write(numbet) 
    sleep(0.1)
    pyautogui.click(start_location)
    sleep(0.5)
limbo_seed_location = 503, 529       
limbo_new_seed = 302, 602
limbo_tab = 175, 44
def limbo():
    pyautogui.click(limbo_tab)
    sleep(0.1)
    win = pyautogui.pixelMatchesColor(495, 195, (59, 193, 23))
    sleep(0.25)
    if win:
        pyautogui.click(limbo_seed_location) 
        sleep(2.5)
        pyautogui.click(limbo_new_seed)
        sleep(2)
        pyautogui.doubleClick(bet_amount_location, interval=0.15)
        sleep(0.1)
        pyautogui.write(bet_amount) 
        sleep(0.1)
    else:
        pyautogui.click(double) 
        sleep(0.1)
    pyautogui.doubleClick(numbetloc, interval=0.15)
    sleep(0.1)
    pyautogui.write(numbet) 
    sleep(0.1)
    pyautogui.click(start_location)
    sleep(0.5)
ultimate_dice_seed_location = 497, 539       
ultimate_dice_new_seed = 302, 602
ultimate_dice_tab = 240, 44
def ultimateDice():
    pyautogui.click(ultimate_dice_tab)
    sleep(0.1)
    win = pyautogui.pixelMatchesColor(495, 195, (59, 193, 23))
    sleep(0.25)
    if win:
        pyautogui.click(ultimate_dice_seed_location) 
        sleep(2.5)
        pyautogui.click(ultimate_dice_new_seed)
        sleep(2)
        pyautogui.doubleClick(bet_amount_location, interval=0.15)
        sleep(0.1)
        pyautogui.write(bet_amount) 
        sleep(0.1)
    else:
        pyautogui.click(double) 
        sleep(0.1)
    pyautogui.doubleClick(numbetloc, interval=0.15)
    sleep(0.1)
    pyautogui.write(numbet) 
    sleep(0.1)
    pyautogui.click(start_location)
    sleep(0.5)
while True:
    classicDice()
    limbo()
    ultimateDice()
    sleep(20)