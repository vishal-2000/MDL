import os
from params import *

def init_vec():
    vec = {}
    
    for pos in POS:
        vec[pos] = {}
        for mat in MAT:
            vec[pos][mat] = {}
            for arrow in ARROW:
                vec[pos][mat][arrow] = {}
                for state in STATE:
                    vec[pos][mat][arrow][state] = {}
                    for health in HEALTH:
                        vec[pos][mat][arrow][state][health] = 0
    
    return vec


def get_val(og_vec, pos, mat, arrow, state, health):
    all_val = []

    if health == 0: 
        val = {
                    "Action": "NONE",
                    "Value": 0.0
                }

        all_val.append(val)

    elif (state == "R" and (pos == "E" or pos == "C")):

        for action in ACTION:
            if action in IJ[pos].keys():
                
                if (action == "SHOOT" and arrow == 0) or (action == "CRAFT" and mat == 0):
                    continue
                
                temp = 0
                tprob = 0

                for event in IJ[pos][action]:
                    temp += event["Prob"] * (GAMMA * (MM["R"]["D"]*(og_vec[pos][max([0, min([2, mat+event["Mat"]])])][0]["D"][min([100, max([0, health+25])])]) \
                                                        + MM["R"]["R"]*(og_vec[event["Pos"]][max([0, min([2, mat+event["Mat"]])])][max([0, min([3,arrow+event["Arrow"]])])]["R"][min([100, max([0, health-event["Damage"]])])])) \
                                            + MM["R"]["D"]*MM_ATTACK_COST)
                    
                    if (min([100, max([0, health-event["Damage"]])]) == 0):
                        temp += MM["R"]["R"]*event["Prob"]*FINAL_REWARD

                    tprob += event["Prob"]
                    

                if (tprob!=1):
                    print(tprob)   

                if action != "STAY": 
                    temp += STEP_COST

                val = {
                    "Action": action,
                    "Value": temp
                }

                all_val.append(val)

    else:

        for action in ACTION:
            if action in IJ[pos].keys():
                
                if (action == "SHOOT" and arrow == 0) or (action == "CRAFT" and mat == 0):
                    continue

                temp = 0

                for event in IJ[pos][action]:
                    temp += GAMMA*event["Prob"]*(MM[state]["D"]*(og_vec[event["Pos"]][max([0, min([2, mat+event["Mat"]])])][max([0, min([3,arrow+event["Arrow"]])])]["D"][min([100, max([0, health-event["Damage"]])])]) + MM[state]["R"]*(og_vec[event["Pos"]][max([0, min([2, mat+event["Mat"]])])][max([0, min([3,arrow+event["Arrow"]])])]["R"][min([100, max([0, health-event["Damage"]])])]))

                    if (min([100, max([0, health-event["Damage"]])]) == 0):
                        temp += event["Prob"]*FINAL_REWARD
                
                if action != "STAY":
                    temp += STEP_COST

               

                val = {
                    "Action": action,
                    "Value": temp
                }

                all_val.append(val) 

    out_val = all_val[0]

    for val in all_val :
        if val["Value"] > out_val["Value"]:
            out_val = val

    return out_val


def value_iterate(og_vec):
    new_vec = init_vec()
    deltas = []
    action_string = ""

    for pos in POS:
        for mat in MAT:
            for arrow in ARROW:
                for state in STATE:
                    for health in HEALTH:
                        val = get_val(og_vec, pos, mat, arrow, state, health)
                        new_vec[pos][mat][arrow][state][health] = val["Value"]
                        delta = abs(og_vec[pos][mat][arrow][state][health]- new_vec[pos][mat][arrow][state][health])
                        deltas.append(delta)
                        action_string += "(" + str(pos) + "," + str(mat) + "," + str(arrow) + "," + str(state) + "," + str(health) + ")" + ":" + val["Action"] +"=" + "[" + str('%.4f' %val["Value"]) + "]" + "\n"

    output = [new_vec, action_string, False]
    
    if (max(deltas) < DELTA):
        output[2] = True
    
    return output


if __name__ == "__main__":
    V = init_vec()
    iteration = 0
    out_string = ""

    while True:
        out_string += "iteration=" + str(iteration) + "\n"
        
        iteration_out = value_iterate(V)
        V = iteration_out[0]
        out_string += iteration_out[1]
        
        if (iteration_out[2]):
            break

        iteration += 1

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../outputs/part_2.2_trace.txt')
    history_file = open(filename, "w")
    history_file.write(out_string)
    history_file.close()