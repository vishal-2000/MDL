# A generic genetic algorithm
import random
import numpy as np
import matplotlib.pyplot as plt
from client import get_errors, get_overfit_vector, submit
from io import StringIO
from config import SECRET_KEY
from utils import POPULATION_SIZE, SPLIT_POINT, FEATURE_VECTOR_SIZE, MUTATION_COEFF
from helpers import mkdir_p, get_train_validation_errors, get_rank_and_probabilities, fitness, select_parents, cross_over, mutate, plot_graph, initialize_params, select_the_best, return_elite, list_to_array, file_name, return_order, single_mutate

from errno import EEXIST
from os import makedirs, path


init_overfit_params, init_params = initialize_params()
NO_OF_GENERATIONS = 5
generation_errors = np.zeros(shape=(NO_OF_GENERATIONS, 2), dtype=float)
params = np.zeros(shape=(11, POPULATION_SIZE), dtype=float)
np.copyto(params, init_params)
print("Initial params:\n")
print(init_params)
#target_directory = "Results/3-04/run2"
target_directory = file_name()
mkdir_p(target_directory)
f = open("{}/params.txt".format(target_directory), "w")
#f.write("Run 3 of 3rd March is continued, we started with the final parameters of previous run i.e. run3 and simulated x more generations where x =\n" + str(NO_OF_GENERATIONS) + "\n")
f.write("Fitness funtion: -1 * (train_error)\n")
f.write("Initialed with the best that we have until now\n")
f.write("Starting all over again with new root population\n")
f.write("No of generations: " + str(NO_OF_GENERATIONS) + "\n")
f.write("Population size: " + str(POPULATION_SIZE) + "\n")
f.write("Mutation coefficient: " + str(MUTATION_COEFF) + "\n")
f.write("Split point: " + str(SPLIT_POINT) + "\n")
f.write("Two offspring per pair\n")

Col_vec = np.zeros(shape=(NO_OF_GENERATIONS, POPULATION_SIZE, 11), dtype=float)
for i in range(NO_OF_GENERATIONS):
    Col_vec[i, :, :] += np.transpose(np.array(params))
    train_validation_errors = None
    fitness_score_array = None
    rank_array = None
    # fitness
    train_validation_errors = get_train_validation_errors(SECRET_KEY, POPULATION_SIZE, params)
    fitness_score_array = fitness(np.array(train_validation_errors))
    rank_array, selection_prob = get_rank_and_probabilities(fitness_score_array)
    elite_parents = return_elite(rank_array, POPULATION_SIZE, 2)
    final_parents = select_the_best(rank_array, POPULATION_SIZE, int(POPULATION_SIZE*0.6))
    parents = []
    parent_fitness = np.zeros(shape = (len(final_parents), ), dtype = float)
    k = 0
    temp_errors = list_to_array(train_validation_errors)
    elite_params = []
    for j in elite_parents:
        elite_params.append(params[:, j])
        #parent_fitness[k] = fitness_score_array[j]
        #k += 1
    for j in final_parents:
        parents.append(params[:, j])
        parent_fitness[k] = fitness_score_array[j]
        k += 1
    print(parent_fitness)
    # Parents are ready
    elite_params = list_to_array(elite_params)
    parents = list_to_array(parents)
    parent_rank_array, parent_selection_prob = get_rank_and_probabilities(parent_fitness)
    
    f.write("\nPopulation:\n")
    f.write(str(np.transpose(np.array(params))))
    f.write("\nTrain validation errors\n")
    f.write(str(np.array(train_validation_errors)))
    f.write("\nSelected parents:\n")
    f.write(str(np.transpose(np.array(parents))))
    for j in range(POPULATION_SIZE):
        if rank_array[j]==1:
            generation_errors[i, :] += train_validation_errors[j]
    print("Rank array")
    print(rank_array)
    print("All errors")
    print(train_validation_errors)
    print("Best offspring Gen errors")
    print(generation_errors)
    # crossover and mutation
    temp_count = 2
    offspring_params = np.zeros(shape=(11, POPULATION_SIZE), dtype=float)
    offspring_params[:, 0] = elite_params[0, :]
    offspring_params[:, 1] = elite_params[1, :]
    while temp_count < POPULATION_SIZE:
        k, l = select_parents(parent_selection_prob)
        #print(k, l)
        print("What's the matter with you")
        offspring1, offspring2 = cross_over(parents[k, :], parents[l, :], SPLIT_POINT)
        #print(offspring)
        offspring1 = mutate(offspring1)
        offspring2 = mutate(offspring2)
        #print(offspring)
        offspring_params[:, temp_count] += offspring1[:]
        offspring_params[:, temp_count+1] += offspring2[:]
        #print(offspring_params)
        temp_count += 2
    #print("Errors")
    #print(generation_errors)
    #print("params")
    #print(offspring_params)
    f.write("\nAfter cross over and mutation:\n")
    f.write(str(np.transpose(np.array(offspring_params))))
    np.copyto(params, offspring_params)
f.write('Best offspring gen errors:\n')
f.write(str(generation_errors))
f.close()
plot_graph(NO_OF_GENERATIONS, generation_errors, target_directory)