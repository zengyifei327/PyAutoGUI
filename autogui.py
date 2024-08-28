import pyautogui
import time

# print(pyautogui.size())
# pyautogui.moveTo(100, 100)
# pyautogui.moveRel(0, 100, duration=1)
# print(pyautogui.position())

# pyautogui.click(70, 20, duration=1)

time.sleep(3)
pyautogui.moveTo(500,500, duration=1)
pyautogui.dragRel(100, 0, duration=1)
pyautogui.dragRel(0, 100, duration=1)
pyautogui.dragRel(-100, 0, duration=1)
pyautogui.dragRel(0, -100, duration=1)

# pyautogui.moveTo(1100, 300, duration=1)
# pyautogui.scroll(500)
# pyautogui.scroll(-500)

# keyboard functions
# pyautogui.typewrite('Hello World', interval=0.1)
# pyautogui.hotkey('ctrl', 'a')
