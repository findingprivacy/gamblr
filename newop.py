#opera zoom 50, payout 99, increase 1.25, on win -100, 50 games check res or double
import pyautogui
from time import sleep
bet_amount = '0.1'
bet_amount_location = 120, 192
start_location = 145, 383
classic_dice_seed_location = 455, 388       
classic_dice_new_seed = 279, 462
def wait():
    sleep(1)
    vault()
def vault():
    win = pyautogui.pixelMatchesColor(468, 165, (59, 193, 23))
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
        wait()
def main():
    vault()
    sleep(1)
while True:
    main()
