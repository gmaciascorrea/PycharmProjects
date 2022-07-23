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
    # red = "sampleSRed.png"
    # green = "sampleSGreen.png"
    # yellow = "sampleSYellow.png"
    square_region = (500, 200, 900, 400)

    while not keyboard.is_pressed('q'):
        if pyautogui.locateOnScreen(blue, region=(1490, 650, 330, 330), confidence=0.3) is not None:

            print('I can see it')
            pic = pyautogui.screenshot(region=square_region)

            width, height = pic.size

            for x in range(0, width, 20):
                for y in range(0, height, 20):
                    r, g, b = pic.getpixel((x, y))
                    if r < 5 and g > 50 and b > 140:
                        press_key('w')
                    elif r < 5 and g > 100 and b < 20:
                        press_key('a')
                    elif r > 140 and g > 60 and b < 45:  #
                        press_key('d')
                    elif r > 140 and g < 10 and b < 10:
                        press_key('s')
                    else:
                        ()
        else:
            print('I am unable to see it')
            time.sleep(0.25)


def main():
    time.sleep(2)
    bot()


main()
