# A generic genetic algorithm helpers
import random
import numpy as np
import matplotlib.pyplot as plt
from client import get_errors
from io import StringIO
from config import SECRET_KEY
from utils import POPULATION_SIZE, SPLIT_POINT, FEATURE_VECTOR_SIZE, MUTATION_COEFF

from errno import EEXIST
from os import makedirs, path

# Used to create directory 
def mkdir_p(mypath):
    '''Creates a directory. equivalent to using mkdir -p on the command line'''
    try:
        makedirs(mypath)
    except OSError as exc: # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else: raise
        
# Initialize parameters
def initialize_params():
	file = open("overfit.txt", "r")
	line = file.read()
	# Create a string which does not contain '[' and ']'
	str1 = ''
	for i in line:
		if i=='[' or i==']':
		    continue
		str1 += i
	str1 = StringIO(str1)
	# Extracting the parameters from the string and putting them in a list
	init_overfit_params = list(np.loadtxt(str1, dtype=float, delimiter=',')) 
	
	np.random.seed(40)
	#params = np.random.uniform(-9, 10, size=(11, POPULATION_SIZE))
	params = np.zeros(shape=(11, POPULATION_SIZE), dtype=float)
	for i in range(POPULATION_SIZE):
		np.copyto(params[:, i], init_overfit_params)
	init_params = np.zeros(shape= (11, POPULATION_SIZE))
	for i in range(POPULATION_SIZE):
		init_params[:, i] += mutate(params[:, i], 0.1)
	#np.copyto(init_params, params)
	print(init_params)
	return init_overfit_params, init_params

# Returns Train and validation errors
def get_train_validation_errors(SECRET_KEY, POPULATION_SIZE, params):
    return [get_errors(SECRET_KEY, list(params[:, i])) for i in range(params.shape[1])]

# Calculates fitness and return the array of fitness scores
def fitness(train_validation_error):
    fitness_score = -1 * train_validation_error[:, 1] 
    return fitness_score

# Ranks the parents according to their fitness scores
def get_rank_and_probabilities(fitness_score_array):
    rank_indices = np.zeros(shape = (fitness_score_array.size, ), dtype=int)
    # assign ranks to index positions
    min_index = 0 # index with max fitness score
    visited = [False for i in range(fitness_score_array.size)]
    for i in range(fitness_score_array.size):
        for j in range(fitness_score_array.size):
            if visited[j]==False:
                min_index = j
        for j in range(fitness_score_array.size):
            if j==min_index:
                continue
            elif fitness_score_array[j] > fitness_score_array[min_index] and visited[j]==False:
                min_index = j
        visited[min_index] = True
        rank_indices[min_index] = i+1
        # selection probability array
        selection_probabilities = ((POPULATION_SIZE - rank_indices[:] + 1)*2)/float(POPULATION_SIZE*(POPULATION_SIZE + 1))
    return rank_indices, selection_probabilities

# Out of a set of potential parents selects two parents randomly based on their ranks
def select_parents(selection_prob):
    parent1 = parent2 = -1
    k = 0
    parent = -1
    while True:
        p = np.random.uniform(0, 1)
        k = 0
        parent = -1
        for i in range(selection_prob.size):
            k += selection_prob[i]
            if i!=parent1 and p <= k:
                parent = i
                break
        if parent == -1:
            continue
        elif parent1 == -1:
            parent1 = parent
        elif parent2 == -1:
            parent2 = parent
            break
    return parent1, parent2

# Takes parents as parameters and returns two offsprings 
# by crossing over the parents
def cross_over(parent1, parent2, SPLIT_POINT):
    offspring1 = np.zeros(shape=(11))
    offspring2 = np.zeros(shape=(11))
    
    offspring1[0:SPLIT_POINT] += parent1[0:SPLIT_POINT]
    offspring1[SPLIT_POINT:] += parent2[SPLIT_POINT:]
    
    offspring2[0:SPLIT_POINT] += parent2[0:SPLIT_POINT]
    offspring2[SPLIT_POINT:] += parent1[SPLIT_POINT:]
    #for i in range(SPLIT_POINT):
    #    offspring1[i] = parent1[i]
    #    offspring2[i] = parent2[i]
    #for i in range(SPLIT_POINT, 11):
    #    offspring1[i] = parent2[i]
    #    offspring2[i] = parent1[i]
    return offspring1, offspring2

# Mutates the child offsprings
def mutate(offspring, mutation_coeff = 0.1): # default 0.1
    
    p = np.random.uniform(0, 1, size=(11))
    a = np.abs(np.floor(np.add(p, -1*mutation_coeff))) # one where p < 0.1 and zero where p > 0.1
    b = np.abs(np.ceil(np.add(p, -1*mutation_coeff))) # zero where p < 0.1 and one where p > 0.1
    c = np.random.uniform(-10, 10, size=(11))
    offspring = offspring*b + a*c
    
    #for i in range(offspring.size):
    #    p = np.random.uniform(0, 1)
    #    if p < mutation_coeff:
    #        offspring[i] = np.random.uniform(-10, 10)
    return offspring

def plot_graph(NO_OF_GENERATIONS, generation_errors, target_directory):
	fig, ax = plt.subplots() # Create a figure and an axis
	generation = [i+1 for i in range(NO_OF_GENERATIONS)]
	ax.plot(generation, generation_errors[:, 0], label='Train Error vs generation')
	ax.plot(generation, generation_errors[:, 1], label='Validation Error vs generation')
	#ax.plot(x_ax, y_ax, label='Simulated Data')
	ax.set_xlabel('Generation')
	ax.set_ylabel('Error')
	ax.set_title('First two initial parents are init_overfit_params')
	ax.legend()  # Add a legend
	fig.savefig("{}/plot.png".format(target_directory))
	fig.show()
