import pynput
import time

print("It's working!")

from pynput.keyboard import Key, Controller

keyboard = Controller();


time.sleep(5);

keyboard.type('Hello, Tommy');