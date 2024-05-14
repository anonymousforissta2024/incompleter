#Source: https://stackoverflow.com/questions/60910850/pygame-typeerror-join-argument-must-be-str-bytes-or-os-pathlike-object-not
"""Gets the scaling info used in the other modules of the game"""
import pygame

def get_scaling_info():
    """Gathers display info for scaling elements of the game"""
    pygame.init()
    display_info = pygame.display.Info()
    scaling_info = pygame.display.Info()
    x_ratio = display_info.current_w/scaling_info.current_w
    y_ratio = display_info.current_h/scaling_info.current_h
    return scaling_info, x_ratio, y_ratio