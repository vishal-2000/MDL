# Assignment 2 (MDL Genetic Algorithms)
## Objective
- Construct a genetic algorithm to find optimal set of values of parameters (Do not overfit)
- Start from a set which has overfit the train set
## Output from get_errors
- MSE of train set, MSE of validation set
## Initial parameters
- Output: [13510723304.19212, 368296592820.6967]
## Genetic algo brief
- Initialization 
    - create population of size N 
- Fitness function 
    - Lower the validation error, higher the fitness of a particular set/entity
    - Fitness function and ranking yet to be decided
    - Rank the population using fitness function
- Selection 
    - Select best K out of N entities in population (based on their ranks)
    - Use the concepts of Elitism and Roulette wheel
- Crossover
    - Select two out of K entities and perform cross over
    - Repeat the above two steps until the new population equals the POPULATION_SIZE
- Mutation
    - Mutate all the offspring
Repeat all the steps (except initialization) until you reach an optimum