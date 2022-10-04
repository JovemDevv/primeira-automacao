import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

pyautogui.hotkey("ctrl", "t") #tecla de atalho
pyperclip.copy("https://www.youtube.com/watch?v=L2dOYOhhDtg")
pyautogui.hotkey("ctrl", "v")
#pyautogui.write("https://www.youtube.com/watch?v=L2dOYOhhDtg")
pyautogui.press("enter") #tecla unica

time.sleep(5)

pyautogui.click() # para dar double click(clicks=2)

'''pyautogui.position() "é feito por esse método é
indicar a posição da “setinha” do mouse em um
dado momento(y,x)."'''

pyautogui.sleep(5)
