#!/bin/bash
function pause(){
 read -s -n 1 -p "Press "Enter" to logon as root . . ."
 echo ""
}
sudo apt update -y &&
sudo apt install dwm suckless-tools surf xrdp -y &&
sudo apt install python3-pip -y &&
sudo apt install python3-tk -y &&
sudo apt install python3-dev -y &&
sudo apt install python-is-python3 -y &&
sudo apt install scrot -y &&
sudo apt install chromium-browser -y &&
python -m pip install pyautogui &&
sudo apt upgrade -y &&
pause &&
sudo su &&
bash strap/run/su.sh
