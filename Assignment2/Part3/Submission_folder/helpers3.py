import numpy as np

def return_alpha(states, start_state):
    alpha = []
    for state in states:
        if np.all(start_state==state):
            alpha.append(1.0)
        else:
            alpha.append(0.0)
    return alpha

def return_policy(x_values, output_meta_data, states):
    policy = []
    k = -1
    for state in states:
        k+=1
        possible_action_indices = []
        count = -1
        for record in output_meta_data:
            count+=1
            if state==record[:5]:
                possible_action_indices.append(count)
        x_vals = [x_values[i] for i in possible_action_indices]
        #print(possible_action_indices)
        best_action_index = np.argmax(np.array(x_vals))
        #print(possible_action_index(best_action_index), k, state)
        temp = [output_meta_data[possible_action_indices[best_action_index]][:5], output_meta_data[possible_action_indices[best_action_index]][5]]
        #print(temp)
        policy.append(temp)
    return policy