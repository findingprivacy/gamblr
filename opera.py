import pyautogui
from time import sleep
from waiting import wait
##### bet info
bankroll = '1'
payout_amount = '5' # float(input('Payout Amount : '))
bet_amount = '0.001' # float(input('Bet Amount : '))
loss_increase_percentage = '25.5' # int(input('Percentage Increase on Loss : '))

##### game location info zoom 50% chrome

classic_dice_seed_location = 500, 517       
classic_dice_new_seed = 302, 602
classic_dice_tab = 100, 40
classic_dice_bet_amount_location = 153, 236
classic_dice_start_location = 191, 526
limbo_seed_location = 501, 525       
limbo_new_seed = 303, 603
limbo_tab = 175, 40
limbo_bet_amount_location = 153, 236
limbo_start_location = 191, 526
ultimate_dice_seed_location = 496, 541       
ultimate_dice_new_seed = 307, 605
ultimate_dice_tab = 240, 40
ultimate_dice_bet_amount_location = 153, 236
ultimate_dice_start_location = 191, 526
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
    pyautogui.click(classic_dice_seed_location) # change seed
    sleep(2.5)
    pyautogui.click(classic_dice_new_seed)
    sleep(2)
    pyautogui.doubleClick(classic_dice_bet_amount_location, interval=0.15)
    sleep(0.25)
    pyautogui.write(bet_amount) 
    sleep(0.25)
    pyautogui.click(classic_dice_start_location) # on auto
    sleep(0.1)
def limbo():
    pyautogui.click(limbo_tab)
    sleep(0.25)
    pyautogui.click(limbo_seed_location) # change seed
    sleep(2.5)
    pyautogui.click(limbo_new_seed)
    sleep(2)
    pyautogui.doubleClick(limbo_bet_amount_location, interval=0.15)
    sleep(0.25)
    pyautogui.write(bet_amount) 
    sleep(0.25)
    pyautogui.click(limbo_start_location) # on auto
    sleep(0.1)
def ultimateDice():
    pyautogui.click(ultimate_dice_tab)
    sleep(0.25)
    pyautogui.click(ultimate_dice_seed_location) # change seed
    sleep(2.5)
    pyautogui.click(ultimate_dice_new_seed)
    sleep(2)
    pyautogui.doubleClick(ultimate_dice_bet_amount_location, interval=0.15)
    sleep(0.25)
    pyautogui.write(bet_amount) 
    sleep(0.25)
    pyautogui.click(ultimate_dice_start_location) 
    sleep(0.1)
def stop():
    pyautogui.click(classic_dice_tab)
    sleep(2)
    win = pyautogui.pixelMatchesColor(517, 193, (59, 193, 23))
    wait(win, timeout_seconds=10)
    pyautogui.click(classic_dice_start_location) 
    sleep(0.5)
    pyautogui.click(limbo_tab)
    sleep(2)
    win = pyautogui.pixelMatchesColor(517, 193, (59, 193, 23))
    wait(win, timeout_seconds=10)
    pyautogui.click(limbo_start_location) 
    sleep(0.5)
    pyautogui.click(ultimate_dice_tab)
    sleep(2)
    win = pyautogui.pixelMatchesColor(517, 193, (59, 193, 23))
    wait(win, timeout_seconds=10)
    pyautogui.click(ultimate_dice_start_location)
    sleep(0.5)
def play():
    classicDice()
    limbo()
    ultimateDice()
def main():
    play()
    stop()
    vault()
while True:
    main()
