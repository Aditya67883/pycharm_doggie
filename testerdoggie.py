# import pyautogui
# import time
#
# print("Switch to OBS now!")
# time.sleep(5)
#
# print("Sending Option + ]")
# pyautogui.hotkey("option", "]")
#
# print("Hotkey sent!")
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

print("Switch to OBS now!")
time.sleep(5)

keyboard.press(Key.alt)
keyboard.press("]")
keyboard.release("]")
keyboard.release(Key.alt)

print("Hotkey sent!")