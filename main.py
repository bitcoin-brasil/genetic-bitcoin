from random import randrange, choice

# Satoshis you want to spend
VALUE = 1000

# Satoshis you want to pay in fees
FEES = 100

UTXOS_VALUES = [1, 123, 1432, 12, 21]

POPULATION_SIZE = 5

POPULATION = []

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

genetic_algorithm()