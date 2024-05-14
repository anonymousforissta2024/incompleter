#Source: https://stackoverflow.com/questions/60849825/typeerror-kollision-missing-1-required-positional-argument-self
#Laden der Pygame Bibliothek
import pygame
import time
import random
#Initialisierung der Pygame Bibliothek
pygame.init()

# Spiel-Fenster erstellen
size = [700, 500]
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
# Noetig um die fps zu begrenzen
clock = pygame.time.Clock()

# Speichert ob das Spiel-Fenster geschlossen wurde
done = False


class Schlitten():
    def __init__(self, px, py, pscreen):
        self.FARBE1 = (139,87,66)
        self.FARBE2 = (139,90,43)
        self.braun = (104,73,71)
        self.x = px
        self.grau = (118,122,121)
        self.y = py
        self.red = (255,0,0)
        self.screen = pscreen
        self.treffer = False    