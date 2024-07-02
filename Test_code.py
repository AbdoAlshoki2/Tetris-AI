
import Genetic_Algorithm as GA
import Tetris
import numpy as np

optimal_chromosomes = [[9.1443, -8.7555, -6.732, -2.4109, 9.7905, 2.0745, 9.137, 4.5946],
                       [9.1443, -4.7405, -8.1451, -0.5974, 6.9499, 2.0745, 6.1426, -4.7322]]

choice = int(input('Do you want to:\n1- play the game.\n2- play the AI game mode.\n'))
if choice == 1:
    Tetris.MANUAL_GAME = True
    Tetris.main()

else:
    choice = int(input('Do you want to:\n1- see the progress of training.\n2- see the optimal agent plays.\n'))
    if choice == 1:
        GA.genetic_algorithm()
    else:
        for i in range(2):
            print(f'the weights is {optimal_chromosomes[i]}')
            scores = []
            for g in range(50):
                score = Tetris.AI_game_mode(max_score=10000000, test=True, chromosome=optimal_chromosomes[i])
                scores.append(score)
                print(f'Game {g + 1} got score = {score}')
            print('Scores:', scores)
            print('Best score:', max(scores))

