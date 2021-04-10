# find_index(main_list, element_list)
# init_A_matrix(output_meta_data, states)
from config import state_meta
import numpy as np


# finds element index
def find_index(main_list, element_list):
    k = 0
    for temp in main_list:
        if np.all(np.array(temp)==np.array(element_list)):
            break
        k+=1
    if k==len(main_list):
        print("Error:")
        print("Given: "+str(element_list))
        exit(1)
    return k

def init_A_matrix(output_meta_data, states):
    A = np.zeros(shape=(len(states), len(output_meta_data)), dtype=float)
    move_actions=["UP", "DOWN", "LEFT", "RIGHT", "STAY"]
    custom_actions=["SHOOT", "HIT", "CRAFT", "GATHER"]
    other_actions=["NONE"]
    defense_pos=["N", "S", "W"]
    attack_pos=["E", "C"]
    count = -1 # keeps the index of current state-action pair
    for record in output_meta_data:
        # record = [position, material, n_arrows, mm_state, mm_health, action]
        count += 1
        t = find_index(states, record[:5])
        if record[0] in defense_pos:
            if record[5]in move_actions: # Verified
                A[t][count] = 1
                p1 = state_meta[record[0]][record[5]]["p"]
                p_mm = 0.0
                mm_next = ""
                if record[3]=="R":
                    p_mm = 0.5
                    mm_next = "D"
                else:
                    p_mm = 0.2
                    mm_next = "R"
                # mm D->R or R->D agent 
                # move success
                temp = record[:5]
                temp[0] = state_meta[record[0]][record[5]]["s_next"]
                temp[3] = mm_next
                l = find_index(states, temp)
                A[l][count] += -1*p1*(p_mm)
                # move fail
                temp = record[:5]
                temp[0] = state_meta[record[0]][record[5]]["f_next"]
                temp[3] = mm_next
                l = find_index(states, temp)
                A[l][count] += -1*(1-p1)*(p_mm)
                # mm R->R or D->D
                # move success
                temp = record[:5]
                temp[0] = state_meta[record[0]][record[5]]["s_next"]
                l = find_index(states, temp)
                A[l][count] += -1*p1*(1-p_mm)
                # move failed
                temp = record[:5]
                temp[0] = state_meta[record[0]][record[5]]["f_next"]
                l = find_index(states, temp)
                A[l][count] += -1*(1-p1)*(1-p_mm)
            elif record[5] in custom_actions:        # Verified
                if record[5]=="CRAFT":
                    A[t][count] = 1
                    p1 = state_meta[record[0]][record[5]]["p_1"]
                    s1 = state_meta[record[0]][record[5]]["s_1"]
                    p2 = state_meta[record[0]][record[5]]["p_2"]
                    s2 = state_meta[record[0]][record[5]]["s_2"]
                    p3 = state_meta[record[0]][record[5]]["p_3"]
                    s3 = state_meta[record[0]][record[5]]["s_3"]
                    p_mm = 0.0
                    mm_next = ""
                    if record[3]=="R":
                        p_mm = 0.5
                        mm_next = "D"
                    else:
                        p_mm = 0.2
                        mm_next = "R"
                    # R->D or D-> R
                    # create 1 arrow
                    temp = record[:5]
                    temp[1] -= 1
                    temp[2] = min(3, record[2]+s1)
                    temp[3] = mm_next
                    l = find_index(states, temp)
                    A[l][count] += -1*p1*p_mm
                    # create 2 arrow 
                    temp = record[:5]
                    temp[1] -= 1
                    temp[2] = min(3, record[2]+s2)
                    temp[3] = mm_next
                    l = find_index(states, temp)
                    A[l][count] += -1*p2*p_mm
                    # create 3 arrow
                    temp = record[:5]
                    temp[1] -= 1
                    temp[2] = min(3, record[2]+s3)
                    temp[3] = mm_next
                    l = find_index(states, temp)
                    A[l][count] += -1*p3*p_mm
                    # R->R or D-> D
                    # create 1 arrow
                    temp = record[:5]
                    temp[1] -= 1
                    temp[2] = min(3, record[2]+s1)
                    l = find_index(states, temp)
                    A[l][count] += -1*p1*(1-p_mm)
                    # create 2 arrow 
                    temp = record[:5]
                    temp[1] -= 1
                    temp[2] = min(3, record[2]+s2)
                    l = find_index(states, temp)
                    A[l][count] += -1*p2*(1-p_mm)
                    # create 3 arrow
                    temp = record[:5]
                    temp[1] -= 1
                    temp[2] = min(3, record[2]+s3)
                    l = find_index(states, temp)
                    A[l][count] += -1*p3*(1-p_mm)
                elif record[5]=="GATHER":
                    A[t][count] = 1
                    p1 = state_meta[record[0]][record[5]]["p"]
                    s = state_meta[record[0]][record[5]]["s"]
                    p_mm = 0.0
                    mm_next = ""
                    if record[3]=="R":
                        p_mm = 0.5
                        mm_next = "D"
                    else:
                        p_mm = 0.2
                        mm_next = "R"
                    # R->D or D-> R
                    # gather success
                    temp = record[:5]
                    if temp[1]<=1:
                        temp[1] += s
                    temp[3] = mm_next
                    l = find_index(states, temp)
                    A[l][count] += -1*p1*p_mm
                    # gather fail
                    temp = record[:5]
                    temp[3] = mm_next
                    l = find_index(states, temp)
                    A[l][count] += -1*(1-p1)*p_mm
                    # R->R or D-> D
                    # gather success
                    temp = record[:5]
                    if temp[1]<=1:
                        temp[1] += s
                    l = find_index(states, temp)
                    A[l][count] += -1*p1*(1-p_mm)
                    # gather fail
                    temp = record[:5]
                    l = find_index(states, temp)
                    A[l][count] += -1*(1-p1)*(1-p_mm)
                elif record[5]=="SHOOT": # for west
                    A[t][count] = 1
                    p1 = state_meta[record[0]][record[5]]["p"]
                    damage = state_meta[record[0]][record[5]]["damage"]
                    p_mm = 0.0
                    mm_next = ""
                    arrow_exhaust = 1
                    if record[3]=="R":
                        p_mm = 0.5
                        mm_next = "D"
                    else:
                        p_mm = 0.2
                        mm_next = "R"
                        #damage = 0
                    # R->D or D-> R
                    # shoot success
                    temp = record[:5]
                    temp[2] -= arrow_exhaust 
                    temp[3] = mm_next
                    temp[4] = max(0, temp[4] - damage)
                    l = find_index(states, temp)
                    A[l][count] += -1*p1*p_mm
                    # shoot fail
                    temp = record[:5]
                    temp[2] -= arrow_exhaust
                    temp[3] = mm_next
                    l = find_index(states, temp)
                    A[l][count] += -1*(1-p1)*p_mm
                    # R->R or D->D
                    # shoot success
                    temp = record[:5]
                    temp[2] -= arrow_exhaust
                    temp[4] = max(0, temp[4] - damage)
                    l = find_index(states, temp)
                    A[l][count] += -1*p1*(1-p_mm)
                    # shoot fail
                    temp = record[:5]
                    temp[2] -= arrow_exhaust
                    l = find_index(states, temp)
                    A[l][count] += -1*(1-p1)*(1-p_mm)
            elif record[5] in other_actions: # implies None
                A[t][count] = 1.0
        elif record[0] in attack_pos:   
            if record[5] in move_actions:   # Verified (almost)
                A[t][count] = 1
                #if record[3]=="D":
                #    A[t][count] = 1
                #elif record[3]=="R":
                #    A[t][count] += 1
                p1 = state_meta[record[0]][record[5]]["p"]
                p_mm = 0.0
                mm_next = ""
                if record[3]=="R":
                    p_mm = 0.5
                    mm_next = "D"
                else:
                    p_mm = 0.2
                    mm_next = "R"
                # mm D->R or R->D 
                # attack success
                # move success or fail
                temp = record[:5]
                if record[3]=="R":
                    temp[2] = 0
                    temp[3] = mm_next
                    temp[4] = min(100, temp[4] + 25)
                    l = find_index(states, temp)
                    A[l][count] += -1*(p_mm)
                elif record[3]=="D":
                    # move success
                    temp = record[:5]
                    temp[0] = state_meta[record[0]][record[5]]["s_next"]
                    temp[3] = mm_next
                    l = find_index(states, temp)
                    A[l][count] += -1*p1*(p_mm)
                    # move fail
                    temp = record[:5]
                    temp[0] = state_meta[record[0]][record[5]]["f_next"]
                    temp[3] = mm_next
                    l = find_index(states, temp)
                    A[l][count] += -1*(1-p1)*(p_mm)
                # mm D->D and R->R
                # move success
                temp = record[:5]
                if record[3]=="R":
                    temp[0] = state_meta[record[0]][record[5]]["s_next"]
                    l = find_index(states, temp)
                    A[l][count] += -1*p1*(1-p_mm)
                elif record[3]=="D":
                    temp[0] = state_meta[record[0]][record[5]]["s_next"]
                    l = find_index(states, temp)
                    A[l][count] += -1*p1*(1-p_mm)
                
                # mm D->D and R->R 
                # move fail
                temp = record[:5]
                if record[3]=="R":
                    temp[0] = state_meta[record[0]][record[5]]["f_next"]
                    l = find_index(states, temp)
                    A[l][count] += -1*(1-p1)*(1-p_mm)
                elif record[3]=="D":
                    temp[0] = state_meta[record[0]][record[5]]["f_next"]
                    l = find_index(states, temp)
                    A[l][count] += -1*(1-p1)*(1-p_mm)
            elif record[5] in custom_actions:         # Verified
                #print(record)
                A[t][count] = 1
                #if record[3]=="D":
                #    A[t][count] = 1
                #elif record[3]=="R":
                #    A[t][count] = 1
                p = 0.0
                damage = 0
                arrow_exhaust = 0
                p_mm = 0.0
                mm_next = ""
                if record[3]=="R":
                    p_mm = 0.5
                    mm_next = "D"
                else:
                    p_mm = 0.2
                    mm_next = "R"
                if record[5]=="SHOOT":
                    p = state_meta[record[0]][record[5]]["p"]
                    damage = 25
                    arrow_exhaust = 1
                elif record[5]=="HIT":
                    p = state_meta[record[0]][record[5]]["p"]
                    damage = 50
                    arrow_exhaust = 0
                # mm D->R or R->D 
                # attack success
                # move success or fail
                temp = record[:5]
                if record[3]=="R":
                    temp[2] = 0
                    temp[3] = mm_next
                    temp[4] = min(100, temp[4]+25)
                    l = find_index(states, temp)
                    A[l][count] += -1*(p_mm)
                elif record[3]=="D":
                    # move success
                    temp = record[:5]
                    temp[2] -= arrow_exhaust 
                    temp[3] = mm_next
                    temp[4] = max(0, temp[4] - damage) 
                    l = find_index(states, temp)
                    A[l][count] += -1*p*(p_mm)
                    temp = record[:5]
                    # move fail
                    temp = record[:5]
                    temp[2] -= arrow_exhaust 
                    temp[3] = mm_next
                    l = find_index(states, temp)
                    A[l][count] += -1*(1-p)*(p_mm)
                # mm D->D and R->R
                # move success
                temp = record[:5]
                if record[3]=="R":
                    temp[2] -= arrow_exhaust 
                    temp[4] = max(0, temp[4] - damage) 
                    l = find_index(states, temp)
                    A[l][count] += -1*p*(1-p_mm)
                elif record[3]=="D":
                    temp[2] -= arrow_exhaust 
                    temp[4] = max(0, temp[4] - damage) 
                    l = find_index(states, temp)
                    A[l][count] += -1*p*(1-p_mm)
                
                # mm D->D and R->R 
                # move fail
                temp = record[:5]
                if record[3]=="R":
                    temp[2] -= arrow_exhaust 
                    l = find_index(states, temp)
                    A[l][count] += -1*(1-p)*(1-p_mm)
                elif record[3]=="D":
                    temp[2] -= arrow_exhaust 
                    l = find_index(states, temp)
                    A[l][count] += -1*(1-p)*(1-p_mm)
            elif record[5] in other_actions: # implies None    # Verified
                A[t][count] = 1.0
    return A