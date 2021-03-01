import random
from typing import List
from client import get_errors
import numpy as np
from io import StringIO
from config import SECRET_KEY
from utils import POPULATION_SIZE, rankify
file1 = open("overfit.txt", "r")
line = file1.read()
# creating a mutable string
str = ''
for i in line:
    if i=='[' or i==']':
        continue
    str += i
str = StringIO(str)
# creating the parameter array out of the string
init_params = list(np.loadtxt(str, dtype=float, delimiter=','))
# init_params contains initial overfitting parameters

#print((get_errors(SECRET_KEY, init_params))[0])

# Genetic Algorithm
# Initialization
params = [init_params for i in range(POPULATION_SIZE)]
#print(params)
# Fitness function: Lower the validation error, more the fitness
fitness_coeff = [0 for i in range(POPULATION_SIZE)]
for i in range(POPULATION_SIZE): 
    fitness_coeff[i] = -1 * ( (get_errors(SECRET_KEY, params[i]))[1] )
# Ranking the population
#print(len(fitness_coeff))
params_rank_pos = rankify(fitness_coeff)
#print(params_rank_pos)
#print(params[1])
# Selection (select POPULATION_SIZE/2 entities)
selected_list = [i for i in range(POPULATION_SIZE//2)]
#for i in range(POPULATION_SIZE//2):
#    for j in range(POPULATION_SIZE):
#        if params_rank_pos[j] == i+1:
#            selected_list[i] = j
#            break
#print(params_rank_pos)
# Crossover
k = 0
offspring = []
#while k < POPULATION_SIZE:
#    a = random.randint(0, POPULATION_SIZE//2)
#    b = random.randint(0, POPULATION_SIZE//2)
#    # Create offspring
#    offspring.append([(])
#    k += 1
#print(offspring)

for i in range(10):
    p = []
    for j in range(11):
        p.append(random.randint(-9, 10))
    print(get_errors(SECRET_KEY, p))
