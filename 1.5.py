import pyautogui
from time import sleep
bankroll = '2.5'
address_bar = 175, 73
vault_url = 'https://bc.game/'
vault_tab = 321, 37
vault_profile = 441, 112
vault_wallet = 377, 147
vault_pro = 97, 307
vault_max = 327, 256
vault_transfer = 289, 293
vault_out = 310, 180
vault_amount = 204, 254
payout_amount = '1.5' # float(input('Payout Amount : '))
bet_amount = '0.00025' # float(input('Bet Amount : '))
loss_increase_percentage = '250' # int(input('Percentage Increase on Loss : '))
address_bar = 175, 73
classic_dice_url = 'https://bc.game/game/classic-dice'
classic_dice_seed_location = 441, 514       
classic_dice_new_seed = 250, 516
classic_dice_tab = 50, 38
classic_dice_payout_location = 289, 406
classic_dice_auto_bet_location = 173, 180
classic_dice_bet_amount_location = 100, 222
classic_dice_enable_loss_increase_location = 89, 393
classic_dice_loss_increase_location = 139, 395
classic_dice_start_location = 165, 512
limbo_url = 'https://bc.game/game/limbo'
limbo_seed_location = 446, 514       
limbo_new_seed = 250, 516
limbo_tab = 141, 39
limbo_payout_location = 264, 445
limbo_auto_bet_location = 173, 180
limbo_bet_amount_location = 100, 222
limbo_enable_loss_increase_location = 89, 393
limbo_loss_increase_location = 139, 395
limbo_start_location = 165, 512
ultimate_dice_url = 'https://bc.game/game/ultimate-dice'
ultimate_dice_seed_location = 440, 529       
ultimate_dice_new_seed = 250, 516
ultimate_dice_tab = 234, 39
ultimate_dice_payout_location = 281, 448
ultimate_dice_auto_bet_location = 173, 180
ultimate_dice_bet_amount_location = 100, 222
ultimate_dice_enable_loss_increase_location = 86, 351
ultimate_dice_loss_increase_location = 150, 351
ultimate_dice_start_location = 165, 512
def vault():
    pyautogui.click(vault_tab)
    sleep(0.25)
    pyautogui.click(address_bar)
    sleep(0.25)
    pyautogui.write(vault_url)
    sleep(0.25)
    pyautogui.press('enter')
    sleep(10)
    pyautogui.moveTo(vault_profile)
    sleep(0.25)
    pyautogui.click(vault_wallet)
    sleep(5)
    pyautogui.click(vault_pro)
    sleep(5)
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
    pyautogui.click(address_bar)
    sleep(0.25)
    pyautogui.write(classic_dice_url)
    sleep(0.25)
    pyautogui.press('enter')
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
    pyautogui.click(address_bar)
    sleep(0.25)
    pyautogui.write(limbo_url)
    sleep(0.25)
    pyautogui.press('enter')
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
    pyautogui.click(address_bar)
    sleep(0.25)
    pyautogui.write(ultimate_dice_url)
    sleep(0.25)
    pyautogui.press('enter')
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
    sleep(60)
    stop()
    vault()
while True:
    main()
