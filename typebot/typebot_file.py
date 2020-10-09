import pyautogui
from time import sleep

file = "text_file.txt"

with open(file, 'r') as f:
    words = f.read()

sleep(509)
pyautogui.write(words, interval=0.1)

