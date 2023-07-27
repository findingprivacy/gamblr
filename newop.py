#opera zoom 50, payout 99, increase 1.25, on win -100, 50 games check res or double
import pyautogui
from time import sleep
bankroll = '0.01'
vault_tab = 300, 40
vault_max = 385, 268
vault_transfer = 345, 308
vault_out = 375, 192
vault_in = 275, 192
vault_amount = 256, 267
bet_amount = '0.002'
bet_amount_location = 153, 236
start_location = 191, 526
classic_dice_seed_location = 500, 517       
classic_dice_new_seed = 302, 602
classic_dice_tab = 89, 44
def vault():
    pyautogui.click(vault_tab)
    sleep(1)
    pyautogui.click(vault_in)
    sleep(1)
    pyautogui.click(vault_max)
    sleep(1)
    pyautogui.click(vault_transfer)
    sleep(1)
    pyautogui.click(vault_out)
    sleep(1)
    pyautogui.doubleClick(vault_amount, interval=0.25)
    sleep(1)
    pyautogui.write(bankroll)
    sleep(1)
    pyautogui.click(vault_transfer)
    sleep(1)
def classicDice():
    pyautogui.click(classic_dice_tab)
    sleep(0.1)
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

def main():
    vault()
    classicDice()
    sleep(1)


while True:
    main()
