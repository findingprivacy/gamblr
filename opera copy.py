import pyautogui
from time import sleep
numbet = '99'
bet_amount = '0.001'
double = 232, 237
numbetloc = 174, 281
classic_dice_seed_location = 500, 517       
classic_dice_new_seed = 302, 602
classic_dice_tab = 100, 40
classic_dice_bet_amount_location = 153, 236
classic_dice_start_location = 191, 526
def classicDiceStarter():
    win = pyautogui.pixelMatchesColor(495, 195, (59, 193, 23))
    sleep(0.25)
    if win:
        pyautogui.click(classic_dice_seed_location) 
        sleep(2.5)
        pyautogui.click(classic_dice_new_seed)
        sleep(2)
    else:
        sleep(0.1)
    pyautogui.doubleClick(classic_dice_bet_amount_location, interval=0.15)
    sleep(0.1)
    pyautogui.write(bet_amount) 
    sleep(0.1)
    pyautogui.doubleClick(numbetloc, interval=0.15)
    sleep(0.1)
    pyautogui.write(numbet) 
    sleep(0.1)
    pyautogui.click(classic_dice_start_location)
    sleep(75)
def classicDiceHelper():
    win = pyautogui.pixelMatchesColor(495, 195, (59, 193, 23))
    sleep(0.25)
    if win:
        sleep(0.1)
    else:
        pyautogui.click(double) 
        sleep(0.1)
        pyautogui.click(double) 
        sleep(0.1)
        pyautogui.doubleClick(numbetloc, interval=0.15)
        sleep(0.1)
        pyautogui.write(numbet) 
        sleep(0.1)
        pyautogui.click(classic_dice_start_location)
        sleep(75)
def main():
    classicDiceStarter()
    classicDiceHelper()
while True:
    main()
