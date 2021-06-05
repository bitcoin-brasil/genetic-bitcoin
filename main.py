from random import randrange

POPULATION_SIZE = 5

POPULATION = []

def create_population(utxos_values):
    utxos_size = len(utxos_values)
    
    for _ in range(0, POPULATION_SIZE):
        genes_num = randrange(1, utxos_size)
        for _ in range(0, genes_num):
            individual = []
            individual.push()



def genetic_algorithm():
    create_population([1, 123, 1432, 12, 21])

genetic_algorithm()