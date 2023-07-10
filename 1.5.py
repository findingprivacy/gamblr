import pyautogui
from time import sleep
##### bet info
bankroll = '1'
payout_amount = '5' # float(input('Payout Amount : '))
bet_amount = '0.00001' # float(input('Bet Amount : '))
loss_increase_percentage = '25.5' # int(input('Percentage Increase on Loss : '))

##### game location info zoom 50% chrome
##### a1 = account-1... etc...
a1 = 15, 12
a2 = 38, 12
a3 = 62, 12
a4 = 82, 12
classic_dice_seed_location = 500, 517       
classic_dice_new_seed = 285, 600
classic_dice_tab = 60, 35
classic_dice_payout_location = 302, 407
classic_dice_auto_bet_location = 172, 178
classic_dice_bet_amount_location = 107, 222
classic_dice_enable_loss_increase_location = 81, 396
classic_dice_loss_increase_location = 141, 394
classic_dice_start_location = 133, 509
limbo_seed_location = 501, 514       
limbo_new_seed = 281, 603
limbo_tab = 170, 35
limbo_payout_location = 268, 445
limbo_auto_bet_location = 172, 181
limbo_bet_amount_location = 96, 221
limbo_enable_loss_increase_location = 97, 393
limbo_loss_increase_location = 143, 394
limbo_start_location = 193, 515
ultimate_dice_seed_location = 502, 526       
ultimate_dice_new_seed = 275, 600
ultimate_dice_tab = 280, 35
ultimate_dice_payout_location = 275, 450
ultimate_dice_auto_bet_location = 174, 179
ultimate_dice_bet_amount_location = 91, 222
ultimate_dice_enable_loss_increase_location = 76, 350
ultimate_dice_loss_increase_location = 139, 350
ultimate_dice_start_location = 134, 509
vault_tab = 390, 35
vault_max = 340, 254
vault_transfer = 302, 293
vault_out = 321, 180
vault_in = 225, 180
vault_amount = 214, 254
reload = 86, 73

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
    pyautogui.click(classic_dice_start_location) 
    sleep(0.5)
    pyautogui.click(limbo_tab)
    sleep(10)
    pyautogui.click(limbo_start_location) 
    sleep(0.5)
    pyautogui.click(ultimate_dice_tab)
    sleep(10)
    pyautogui.click(ultimate_dice_start_location)
    sleep(0.5)
def play():
    classicDice()
    limbo()
    ultimateDice()
def main():
    pyautogui.click(a1)
    play()
    pyautogui.click(a2)
    play()
    pyautogui.click(a3)
    play()
    pyautogui.click(a4)
    play()
    sleep(600)
    pyautogui.click(a1)
    stop()
    pyautogui.click(a2)
    stop()
    pyautogui.click(a3)
    stop()
    pyautogui.click(a4)
    stop()
    pyautogui.click(a1)
    vault()
    pyautogui.click(a2)
    vault()
    pyautogui.click(a3)
    vault()
    pyautogui.click(a4)
    vault()
while True:
    main()
