#Source: https://stackoverflow.com/questions/77346201/nameerror-name-bg-img-is-not-defined
import pygame
import pickle
import os
from os import path
import time
import json
import webbrowser
from assets import *
from fonts import * 
# further Code

while run:
    clock.tick(fps)

    screen.blit(bg_img, (0, 0))