import pyautogui
import time
import keyboard

time.sleep(2)
# True for left lane
# redCar = True, blueCar = False
red = True
blue = False


def isBlockComing(car, lane):
    if car:
        if lane and pyautogui.pixel(909, 710)[0] in range(190, 195):
            return True
        elif not lane and pyautogui.pixel(909, 710)[0] in range(190, 195):
            return True
    else:
        if lane and pyautogui.pixel(1028, 710)[2] in range(190, 195):
            return True
        elif not lane and pyautogui.pixel(1144, 720)[2] in range(190, 195):
            return True
    return False


while not keyboard.is_pressed('q'):
    red = (pyautogui.pixel(786, 813)[0] in range(190, 195))
    blue = (pyautogui.pixel(1028, 813)[2] in range(190, 195))

    if isBlockComing(True, red):  # and pyautogui.pixel(786, 720)[0] in range(190, 195): # Left_lane
        keyboard.press("Left")
        print("Left")
    else:  # and pyautogui.pixel(909, 720)[0] in range(190, 195):
        keyboard.press("Left")
        print("Left")
    if isBlockComing(False, blue):  # and pyautogui.pixel(1028, 720)[2] in range(190, 195): # Left_lane
        keyboard.press("Right")
        print("Right")
    else:  # and pyautogui.pixel(1144, 720)[2] in range(190, 195):

        keyboard.press("Right")
        print("Right")
    time.sleep(0.15)


# if pyautogui.pixel(790, 700)[0] > 170 and red_car_st == 0 or pyautogui.pixel(910, 700)[0] > 170 and red_car_st == 1:
#     if red_car_st == 0:
#         red_car_st = 1
#     if red_car_st == 1:
#         red_car_st = 0
#     keyboard.press("Left")
#     time.sleep(0.2)
