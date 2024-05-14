#Source: https://stackoverflow.com/questions/60910850/pygame-typeerror-join-argument-must-be-str-bytes-or-os-pathlike-object-not
"""Contains the class used to generate towers"""
import os
import pygame
from scaling import get_scaling_info

get_scaling_info()

class Tower:
    """Tower information"""
    selection_dict = {49:"elf_tower.png", 50:"dwarf_tower.png"} #pygame keypress of 1 corresponds to value 49, 2 to 50.
    towers = []
    def __init__(self, img, x, y, display_surface="game_surface"):
        x_scale, y_scale = get_scaling_info()[1:]
        self.img = pygame.image.load(os.path.join('assets', img))
        print(self.img) # returns <Surface(40x40x32 SW)>
        self.x_coord = x * x_scale
        self.y_coord = y * y_scale
        self.display_surface = display_surface

    def create_tower(self):
        """Creates a tower of the selected type and scales to the correct size"""
        Tower.towers.append(Tower(self.img, self.x_coord, self.y_coord))
        print(Tower.towers)

    def draw(self):
        """Draws the tower on the screen using the specified image at coordinates x and y"""
        pygame.transform.scale(self.img, (32, 32))
        self.display_surface.blit(self.img, (self.x_coord, self.y_coord))
        print(self.img)

 #   def attack(self):
 #       """Causes the tower to attack enemies in range
 #       Not yet written"""