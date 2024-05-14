#Source: https://stackoverflow.com/questions/51717417/nameerror-name-move-is-note-defined-function
import os

from classes.carte import Carte

from fonctions.receiveRobotMoves import *
from fonctions.move import *
...
isOnExit = False
while isOnExit == False: #Tant que le robot n'est pas sur la sortie...
    #On demande au joueur la direction qu'il veut prendre
    receiveRobotMoves()

    #On fait avancer le robot
    conteneur = move(Labyrinthe, movesInformation['direction'], 
movesInformation['steps'])
    #On met à jour le labyrinthe
    Labyrinthe = conteneur