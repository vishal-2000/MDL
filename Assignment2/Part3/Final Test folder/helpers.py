# return_valid_lists()
# init_X_and_R()
# update_R(output_meta_data)
from config import meta_data

def return_states():
    states = []
    #k = 0
    for position in meta_data['position']:
        for material in meta_data['material']:
            for n_arrows in meta_data['no_of_arrow']:
                for mm_state in meta_data['MM_state']:
                    for mm_health in meta_data['MM_health']:
                        states.append([position, material, n_arrows, mm_state, mm_health])
    return states

def return_valid_lists():
    valid_states = []
    #k = 0
    for position in meta_data['position']:
        for material in meta_data['material']:
            for n_arrows in meta_data['no_of_arrow']:
                for mm_state in meta_data['MM_state']:
                    for mm_health in meta_data['MM_health']:
                        for action in meta_data['action']:
                            if mm_health==0 and action!="NONE":
                                continue
                            if n_arrows==0 and action=="SHOOT":
                                continue
                            if mm_health!=0 and action=="NONE":
                                continue
                            # North
                            if position=="N":
                                if action=="DOWN" or action=="STAY" or action=="NONE":
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                elif material>=1 and action=="CRAFT":
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                            # South   
                            if position=="S":
                                if action=="UP" or action=="STAY" or action=="GATHER" or action=="NONE": # or action=="NONE":
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                            #East
                            if position=="E":
                                if action=="LEFT" or action=="STAY" or action=="HIT" or action=="NONE":
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                elif action=="SHOOT" and n_arrows>0:
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                            # West
                            if position=="W":
                                if action=="RIGHT" or action=="STAY" or action=="NONE":
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                elif action=="SHOOT" and n_arrows>0:
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                            # Centre
                            if position=="C":
                                if action=="RIGHT" or action=="LEFT" or action=="UP" or action=="DOWN" or action=="STAY" or action=="HIT" or action=="NONE":
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                elif action=="SHOOT" and n_arrows>0:
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
    #print(k)
    return valid_states

def init_X_and_R():
    output_meta_data = []
    X = []
    R = []
    valid_states = return_valid_lists()
    #print(len(valid_states))
    for position in meta_data['position']:
        for material in meta_data['material']:
            for n_arrows in meta_data['no_of_arrow']:
                for mm_state in meta_data['MM_state']:
                    for mm_health in meta_data['MM_health']:
                        for action in meta_data['action']:
                            a = [position, material, n_arrows, mm_state, mm_health, action]
                            if a in valid_states:
                                output_meta_data.append([ position, material, n_arrows, mm_state, mm_health, action ])
                                X.append(0.0)
                                R.append(0.0)
    return X, R, output_meta_data

def update_R(output_meta_data):
    R = []
    step_cost = 5.0 # Make it 10
    for record in output_meta_data:
        # record = [position, material, n_arrows, mm_state, mm_health, action]
        #print(record)
        #print(record[0])
        if record[0]=='N' or record[0]=='S' or record[0]=='W':
            if record[4]==0:
                R.append(0.0)
            else:
                R.append(-1.0*step_cost)
        if record[0]=='E' or record[0]=='C':
            if record[4]==0:
                if record[5]=="NONE":
                    R.append(0.0)
                else:
                    print("ERR1: ERROR in update_R function")
            elif record[3]=='D':
                R.append(-1.0*step_cost)
            elif record[3]=='R' and record[5]!='NONE':
                R.append(0.5*(-40-1*step_cost) + 0.5*(-1*step_cost))
            elif record[5]=='NONE':
                R.append(-1.0*step_cost)
            else:
                print("WTF")
            #pass
    return R

if __name__=="__main__":
    print("This script performs very basic testing of helper functions")
    X, R, output_meta_data = init_X_and_R()
    if len(X)==1936:
        print("init_X_and_R() Works fine!")
    else:
        #print(len(meta_data))
        print("Error with init_X_R() function")
        print("Expected output: {0}, but recieved output: {1}".format(1936, len(X)))

    R = update_R(output_meta_data)
    if len(R)==1936:
        print("update_R() Works fine!")
    else:
        #print(len(meta_data))
        print("Error with update_R() function")
        print("Expected output: {0}, but recieved output: {1}".format(1936, len(R)))