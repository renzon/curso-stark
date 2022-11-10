import pyautogui
from time import sleep

# Incializar Chrome
pyautogui.press('win')
pyautogui.write('firefox')
pyautogui.press('enter')
sleep(5)
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('https://google.com')
pyautogui.press('enter')
sleep(5)
pyautogui.moveTo(900, 529)
pyautogui.click()
pyautogui.write('1 USD to BRL')
pyautogui.press('enter')

# pyautogui.moveTo(0, 113)
# pyautogui.click()
