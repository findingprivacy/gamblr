import pyautogui
from time import sleep

tails = 345, 465
heads = 175, 465
amount_location = 170, 425
double = 435, 425
bet_cashout = 285, 500
win = pyautogui.pixelMatchesColor(416, 244, (42, 45, 51))

def game(win):

    if win:
        pyautogui.click(bet_cashout)
        sleep(1)
    else:
        return

    def amount():
        if win:
            x = 0.0001
        else:
            x = bet + 0.0001
        bet = x
        return bet
    bet = str(amount()) 

    pyautogui.doubleClick(amount_location, interval=0.25)
    sleep(0.1)
    pyautogui.write(bet)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(heads)

    sleep(1)

    if win:
    pyautogui.click(bet_cashout)
    sleep(1)
    else:
        return

    def amount():
        if win:
            x = 0.0001
        else:
            x = bet + 0.0001
        bet = x
        return bet
    bet = str(amount()) 

    pyautogui.doubleClick(amount_location, interval=0.25)
    sleep(0.1)
    pyautogui.write(bet)
    pyautogui.click(bet_cashout)
    sleep(1)
    pyautogui.click(tails)

def main():
    main = game(win)
    return

while True:
    main()
