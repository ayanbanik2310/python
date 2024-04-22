#    https://pyautogui.readthedocs.io/en/latest/

import pyautogui
from time import *


sleep(5)
for i in range(0,2):
    pyautogui.write('i love u', interval=0.1)
    pyautogui.press('enter')

sleep(5)
for i in range(0,5):
    for j in range(0,i):
        pyautogui.write('*', interval=0.25)
    pyautogui.press('enter')



