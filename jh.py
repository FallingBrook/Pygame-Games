from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
from pynput.mouse import Button, Controller

mouse = Controller()

time.sleep(2)
# def click(x, y):
mouse.position = (10, 20)

GroundHeight = 150


def __init__(self, left, height, width):
    self.left = left
    # self.top = top
    self.height = height
    self.width = width
    # self.GroundHeight = GroundHeight


def draw(self, window):
    pygame.Rect(gameDisplay, [self.left, GroundHeight - self.height, self.width, self.height])