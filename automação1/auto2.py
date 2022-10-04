import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

pyautogui.hotkey("ctrl", "t") #tecla de atalho
pyperclip.copy("https://www.youtube.com/")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=432, y=571)
pyautogui.click(x=336, y=609)
pyautogui.click(x=724, y=618)
time.sleep(2)