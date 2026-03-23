import pyautogui
import time
import math

radius = 100      # size of circle
speed = 0.05     # delay between movements

# center position
center_x, center_y = pyautogui.position()

while True:
    for angle in range(0, 360, 5):
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        
        pyautogui.moveTo(x, y, duration=0)
        time.sleep(speed)