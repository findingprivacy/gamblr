import pyautogui
from time import sleep
##### bet info
bankroll = '1.59'
payout_amount = '99' # float(input('Payout Amount : '))
bet_amount = '0.001' # float(input('Bet Amount : '))
loss_increase_percentage = '1.025' # int(input('Percentage Increase on Loss : '))

##### game location info zoom 50% chrome

classic_dice_seed_location = 500, 517       
classic_dice_new_seed = 302, 602
classic_dice_tab = 100, 40
classic_dice_bet_amount_location = 153, 236
classic_dice_start_location = 191, 526

vault_tab = 300, 40
vault_max = 385, 268
vault_transfer = 345, 308
vault_out = 375, 192
vault_in = 275, 192
vault_amount = 256, 267
#####
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
    sleep(0.25)
    pyautogui.click(classic_dice_seed_location) 
    sleep(2.5)
    pyautogui.click(classic_dice_new_seed)
    sleep(2)
    pyautogui.doubleClick(classic_dice_bet_amount_location, interval=0.15)
    sleep(0.25)
    pyautogui.write(bet_amount) 
    sleep(0.25)
    pyautogui.click(classic_dice_start_location)
    sleep(1)
def main():
    vault()
    classicDice()
    sleep(110)
while True:
    main()
