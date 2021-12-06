import pyautogui
from time import sleep
import time

sleep(5)

def start_program():
  pyautogui.click()
  pyautogui.write(' commit', interval=0.01)
  #sleep(2)
  pyautogui.hotkey('ctrl', 'enter')
  #sleep(2)
  pyautogui.click()
  pyautogui.write(' commit', interval=0.01)
  #sleep(2)
  pyautogui.hotkey('ctrl', 'enter')

for i in range(6):
  start_program()

pyautogui.hotkey('ctrl', 'alt', 'up')


