# This is the main execution file
import numpy as np
import cvxpy as cp
import json
from helpers import init_X_and_R, return_states, update_R
from helpers2 import init_A_matrix
from helpers3 import return_alpha, return_policy

start_state=["C",2,3,"R",100]

X, R, output_meta_data = init_X_and_R()
states = return_states()
R = update_R(output_meta_data)
A = init_A_matrix(output_meta_data, states)
alpha = return_alpha(states, start_state)

alph = np.array(alpha).reshape((len(alpha), 1))
x = cp.Variable(shape=(len(output_meta_data),1), name="x")
v = cp.matmul(np.transpose(np.array(R)), x)
constraints = [cp.matmul(A, x) == alph, x>=0]
objective = cp.Maximize(cp.sum(v, axis=0))
problem = cp.Problem(objective, constraints)

solution = problem.solve() # on solving, the objective value will be in solution and the x values in x.value

policy = return_policy(x.value, output_meta_data, states)
dictionary = {
    "a": np.array(A).reshape((len(states), len(output_meta_data))).tolist(), 
    "r": np.array(R).reshape((len(output_meta_data), 1)).tolist(), 
    "alpha": np.array(alpha).reshape((len(states), 1)).tolist(), 
    "x": x.value.reshape((len(output_meta_data), 1)).tolist(),
    "policy": policy,
    "objective": solution
}
with open('part_3_output.json', 'w') as outfile:
    json.dump(dictionary, outfile)