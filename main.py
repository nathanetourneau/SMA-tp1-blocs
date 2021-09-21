#########################################
#           MONDE DES BLOCS             #
#########################################

from agent import Agent
import numpy as np
import string
import random

nb_blocs = 4
board = np.array([["-" for i in range(nb_blocs)] for j in range(3)])
bloc_names = list(string.ascii_uppercase[:nb_blocs])
input = random.sample(bloc_names, k=nb_blocs)

# initial state of the game
board[0, :] = input

print(board)
