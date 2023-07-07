import pyautogui
from time import sleep
bankroll = '1'
vault_tab = 306, 46
vault_max = 380, 269
vault_transfer = 346, 310
vault_out = 372, 194
vault_in = 275, 194
vault_amount = 281, 272
payout_amount = '1.5' # float(input('Payout Amount : '))
bet_amount = '0.0001' # float(input('Bet Amount : '))
loss_increase_percentage = '250' # int(input('Percentage Increase on Loss : '))
reload = 144, 86
classic_dice_seed_location = 496, 528       
classic_dice_new_seed = 303, 603
classic_dice_tab = 100, 45
classic_dice_payout_location = 337, 420
classic_dice_auto_bet_location = 230, 196
classic_dice_bet_amount_location = 156, 233
classic_dice_enable_loss_increase_location = 138, 408
classic_dice_loss_increase_location = 207, 408
classic_dice_start_location = 193, 518
limbo_seed_location = 502, 530       
limbo_new_seed = 310, 606
limbo_tab = 152, 48
limbo_payout_location = 315, 459
limbo_auto_bet_location = 230, 196
limbo_bet_amount_location = 156, 233
limbo_enable_loss_increase_location = 138, 408
limbo_loss_increase_location = 207, 408
limbo_start_location = 193, 518
ultimate_dice_seed_location = 497, 538       
ultimate_dice_new_seed = 307, 602
ultimate_dice_tab = 236, 42
ultimate_dice_payout_location = 335, 463
ultimate_dice_auto_bet_location = 235, 193
ultimate_dice_bet_amount_location = 160, 236
ultimate_dice_enable_loss_increase_location = 139, 366
ultimate_dice_loss_increase_location = 199, 366
ultimate_dice_start_location = 195, 524
def vault():
    pyautogui.click(vault_tab)
    sleep(0.1)
    pyautogui.click(vault_in)
    sleep(0.1)
    pyautogui.click(vault_max)
    sleep(0.1)
    pyautogui.click(vault_transfer)
    sleep(0.1)
    pyautogui.click(vault_out)
    sleep(0.1)
    pyautogui.doubleClick(vault_amount, interval=0.25)
    sleep(0.1)
    pyautogui.write(bankroll)
    sleep(0.1)
    pyautogui.click(vault_transfer)
def classicDice():
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
def limbo():
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
def ultimateDice():
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
def stop():
    pyautogui.click(classic_dice_tab)
    sleep(0.25)
    pyautogui.click(classic_dice_start_location) # on auto
    sleep(0.1)
    pyautogui.click(limbo_tab)
    sleep(0.25)
    pyautogui.click(limbo_start_location) # on auto
    sleep(0.1)
    pyautogui.click(ultimate_dice_tab)
    sleep(0.25)
    pyautogui.click(ultimate_dice_start_location) # on auto
    sleep(0.1)
def main():
    classicDice()
    limbo()
    ultimateDice()
    sleep(120)
    stop()
    vault()
while True:
    main()
