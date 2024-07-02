import random
import numpy as np

import Tetris


random.seed(42)
np.random.seed(42)


def initialize_population(population_size, genes_size):
    '''
    This function initialize a generation weights.

    :param population_size: number of agents per generation.
    :param genes_size: number of weights for the agent.
    :return:the agents weights.
    '''

    chromosomes = []
    for _ in range(population_size):
        l = [np.round(random.uniform(-10, 10), 4) for _ in range(genes_size)]
        chromosomes.append(l)
    return chromosomes


def select_parents(combined_population, selection_rate=0.5):
    '''

    :param combined_population: the generation with corresponding scores
    :param selection_rate: the rate to select from the generation
    :return: the selected agents (parents)
    '''
    # NUMBER OF CHROMOSOMES TO BE SELECTED FROM
    num_selected = int(len(combined_population) * selection_rate)

    # SORT ACCORDING TO HIGHER SCORES
    sorted_population = combined_population

    # GET THE INDICES OF THE num_selected CHROMOSOMES WITH HIGHER SCORES
    selected_population = sorted_population[:num_selected]

    # TWO PARENT RANDOMLY PICKED FROM THE HIGHER SCORES CHROMOSOMES
    selected_parents = random.sample(selected_population, 2)

    # EXTRACT THE CHROMOSOMES
    selected_chromosomes = [chromosome for _, chromosome in selected_parents]

    return selected_chromosomes


def crossover(parent1, parent2):
    '''
    This function performs crossover operation between two parent chromosomes at a random point.

    :param parent1: The first parent chromosome.
    :param parent2: The second parent chromosome.
    :return: A new child chromosome created by combining parts of both parents.
    '''
    # GET RANDOM INDEX POSITION
    crossover_point = random.randint(0, len(parent1) - 1)
    # SWAP THE PART WITH THE OTHER PARENT'S
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


def mutate(chromosome):
    '''
    This function performs mutation operation on a chromosome at a random point.

    :param chromosome: The chromosome to be mutated.
    :return: The mutated chromosome.
    '''
    # GET RANDOM
    mutation_index = random.randint(0, len(chromosome) - 1)
    chromosome[mutation_index] = np.round(random.uniform(-10 , 10), 4)
    return chromosome



def genetic_algorithm():
    '''
    This function executes a genetic algorithm for optimizing a population of chromosomes.

    :return: None. The function operates by side effect, modifying the global population of chromosomes.
    '''
    POPULATION_SIZE = 14
    NO_GENERATIONS = 50
    scores = []
    best_score = -1

    # 1. CHROMOSOMES INITIALIZATION
    chromosomes = initialize_population(POPULATION_SIZE , 8)

    for g in range(NO_GENERATIONS):

        # 2. FITNESS EVALUATION
        for i in range(POPULATION_SIZE):
            scores.append(Tetris.AI_game_mode(max_score= 200000 , test=False , chromosome = chromosomes[i] ,gen = g + 1 , best_score=best_score))
            best_score = max(best_score , scores[i])
            print(f'Agent {i + 1} of Generation {g + 1} with chromosome score = {scores[-1]} with weights = {chromosomes[i]}')

        combined = list(zip(scores, chromosomes))
        combined.sort(reverse=True)
        print(f'Best score = {combined[0][0]} with chromosome = {combined[0][1]}')


        # 3. PARENT SELECTION
        parents = [select_parents(combined) for _ in range(POPULATION_SIZE // 2)]

        new_gen = []


        # 4. CROSSOVER
        for parent1, parent2 in parents:
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            new_gen.append(child1)
            new_gen.append(child2)



        # 5. MUTATION
        r = [random.uniform(0, 1) for _ in range(POPULATION_SIZE)]
        for i in range(len(r)):
            if r[i] <= 0.2:
                new_gen[i] = mutate(new_gen[i])

        if np.sum(scores) >=2000000:
            break

        chromosomes = new_gen

        scores = []


