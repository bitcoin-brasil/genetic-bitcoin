from random import randrange, choice

# Satoshis you want to spend
VALUE = 10000

# Satoshis you want to pay in fees in satoshis
FEES = 100

# UTXO values in satoshis
UTXOS_VALUES = [100, 12300, 1432, 3500, 120, 500, 1234]

POPULATION_SIZE = 5

POPULATION = []

def crossover():
    for individual in POPULATION:
        individual = fitness()

def fitness():
    best = 2100000091203921039021931
    best_individual = []
    for individual in POPULATION:
        fitness = (sum(individual) - (VALUE + FEES))
        if fitness >= 0 and fitness < best:
            best = fitness
            best_individual = individual
            if best == 0:   
                break
    return best_individual
        

'''
1. Each individual of our population is a UTXO combination
2. Individuals don't have a fixed gene size
'''
def create_population(utxos_values):
    utxos_size = len(utxos_values)
    
    for _ in range(0, POPULATION_SIZE):
        genes_num = randrange(1, utxos_size)
        individual = []
        choice_value = 0
        for _ in range(genes_num):
            while True:
                choice_value = choice(utxos_values)
                if choice_value in individual:
                    choice_value = choice(utxos_values)
                else:
                    individual.append(choice_value)
                    break
        POPULATION.append(individual)
    
    
def genetic_algorithm():
    create_population(UTXOS_VALUES)
    print(POPULATION)
    fitness()

genetic_algorithm()