import time

import pyautogui

x = 450
y = 250
t = 10

print('Press Ctrl-C to quit.')

try:
    print("auto click (%i|%i) every %i seconds" % (x, y, t))
    while True:
        pyautogui.click(x, y)
        time.sleep(t)
except KeyboardInterrupt:
    print("Exit!\n")
