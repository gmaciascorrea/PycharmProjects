import random
import time
import keyboard
import pyautogui
import win32api
import win32con


# Here is the click function:
def click(x, y):
    time.sleep(random.uniform(0.2, 0.3))
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def press_key(key):
    time.sleep(random.uniform(0.2, 0.3))
    keyboard.press_and_release(key)
    print(key)



def bot():
    blue = "sampleSBlue.png"
    red = "sampleSRed.png"
    green = "sampleSGreen.png"
    yellow = "sampleSYellow.png"
    square_region = (500, 200, 900, 400)

    while not keyboard.is_pressed('q'):                           # X: 1639 Y:  686 RGB: ( 41, 131, 200)
        pic = pyautogui.screenshot(region=(0, 0, 1920, 1080))
        r, g, b = pic.getpixel((1639, 686))
        if 50 > r > 0 and 140 > g > 80 and 210 > b > 180:
            if pyautogui.locateOnScreen(blue, region=square_region, confidence=0.5) is not None:
                press_key('w')
            elif pyautogui.locateOnScreen(green, region=square_region, confidence=0.55) is not None:
                press_key('a')
            elif pyautogui.locateOnScreen(yellow, region=square_region, confidence=0.58) is not None:
                press_key('d')
            elif pyautogui.locateOnScreen(red, region=square_region, confidence=0.1) is not None:
                press_key('s')
        # sssss
        else:
            print('I am unable to see it')
            time.sleep(0.25)


def main():
    time.sleep(2)
    bot()


main()
