import pyautogui
import mouse
    
while True:
    img = pyautogui.screenshot(region=(760,265, 1, 1))
    if img.getpixel((0,0))[1] ==219:
        mouse.click(button="left")