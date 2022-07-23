import keyboard
import time
import pyautogui


def press_key(key):
    time.sleep(0.05)
    keyboard.press_and_release(key)
    print(key)


poke = "poke.png"

while True:
    if pyautogui.locateOnScreen(poke, confidence=0.9):
        press_key('down')
        press_key('down')
        press_key('enter')
        press_key('enter')
        pyautogui.click(button='right')
