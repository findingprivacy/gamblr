
#!/bin/python3
import pyautogui
from time import sleep
tail = 174, 250
head = 79, 250
amount_location = 93, 209
double = 177, 212
half = 154, 213
bet_cashout = 133, 290
bet_amount = '0.001'
bankroll = '1'
address_bar = 175, 73
vault_url = 'https://bc.game/'
vault_tab = 321, 37
vault_profile = 441, 112
vault_wallet = 377, 147
vault_pro = 97, 307
vault_max = 327, 256
vault_transfer = 289, 293
vault_in = 215, 180
vault_out = 310, 180
vault_amount = 204, 254
coin_url = 'https://bc.game/game/coinflip'
coin_tab = 50, 38
def game():
    sleep(0.1)
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
    else:
        pyautogui.click(double)
        sleep(0.1)
        pyautogui.click(double)
        sleep(0.1)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(head)
    sleep(1)
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
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
        sleep(0.1)
        pyautogui.click(coin_tab)
        sleep(0.1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
    else:
        pyautogui.click(half)
        sleep(0.1)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(tail)
    sleep(1)
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
    else:
        pyautogui.click(double)
        sleep(0.1)
        pyautogui.click(double)
        sleep(0.1)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(head)
    sleep(1)
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    if win:
        pyautogui.click(bet_cashout)
        pyautogui.click(bet_cashout)
        sleep(1)
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
        sleep(0.1)
        pyautogui.click(coin_tab)
        sleep(0.1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
    else:
        pyautogui.click(double)
        sleep(0.1)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(tail)
    sleep(1)
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    if win:
        pyautogui.click(bet_cashout)
        pyautogui.click(bet_cashout)
        sleep(1)
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
        sleep(0.1)
        pyautogui.click(coin_tab)
        sleep(0.1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
    else:
        pyautogui.click(double)
        sleep(0.1)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(head)
    sleep(1)
    win = pyautogui.pixelMatchesColor(456, 304, (59, 192, 23))
    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
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
        sleep(0.1)
        pyautogui.click(coin_tab)
        sleep(0.1)
        pyautogui.doubleClick(amount_location, interval=0.25)
        sleep(0.25)
        pyautogui.write(bet_amount)
    else:
        pyautogui.click(half)
        sleep(0.1)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(tail)
    sleep(1)
while True:
    game()
