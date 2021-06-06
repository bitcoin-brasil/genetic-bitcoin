from random import randrange, choice

# Satoshis you want to spend
VALUE = 60000

# Satoshis you want to pay in fees in satoshis
FEES = 1000

# UTXO values in satoshis
UTXOS_VALUES = [309, 357, 314, 481, 488, 747, 741, 600, 
1454, 1543, 1196, 2830, 12528, 14962, 20836, 34551, 37042, 29824, 49121]

POPULATION_SIZE = 5

GENERATIONS = 1000

def mutation(population):
    best_individual = population[0]
    population = create_population(UTXOS_VALUES, POPULATION_SIZE - 1)
    population.append(best_individual)
    return population
    

def crossover(population):
    best_individual = fitness(population)
    print(best_individual)
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(best_individual)
    return mutation(population)

def fitness(population):
    best = 2100000091203921039021931
    best_individual = []
    for individual in population:
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
def create_population(utxos_values, population_size):
    population = []
    utxos_size = len(utxos_values)
    
    for _ in range(0, population_size):
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
        population.append(individual)
    
    return population
    
    
def genetic_algorithm():
    population = create_population(UTXOS_VALUES, POPULATION_SIZE)
    
    for _ in range(GENERATIONS):
        population = crossover(population)
        

genetic_algorithm()