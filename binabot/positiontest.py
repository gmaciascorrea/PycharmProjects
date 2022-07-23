import pyautogui
import time

time.sleep(2)
iml = pyautogui.screenshot(region=(150, 400, 250, 600))
iml.save(r"C:\Users\Gabriel M\PycharmProjects\binabot\savedimage.png")
# For interface use 1490,650,330,330
# For square to look use 500,200,900,400
