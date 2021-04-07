meta_data = {
            "position": ['W', 'N', 'E', 'S', 'C'],
            "material": [0, 1, 2],
            "no_of_arrow": [0, 1],
            "MM_state": ['D', 'R'],
            "MM_health": [0, 25, 50, 75, 100],
            "action": ['UP', 'LEFT', 'DOWN', 'RIGHT', 'STAY', 'SHOOT', 'HIT', 'CRAFT', 'GATHER', 'NONE']
        }

def return_valid_lists():
    valid_states = []
    #k = 0
    for position in meta_data['position']:
        for material in meta_data['material']:
            for n_arrows in meta_data['no_of_arrow']:
                for mm_state in meta_data['MM_state']:
                    for mm_health in meta_data['MM_health']:
                        for action in meta_data['action']:
                            #k+=1
                            # North
                            if position=="N":
                                if mm_health == 0:
                                    continue
                                if action=="DOWN" or action=="STAY" or action=="NONE":
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                    continue
                                if material>=1 and action=="CRAFT":
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                    continue
                            # South   
                            if position=="S":
                                if mm_health == 0:
                                    continue
                                if action=="UP" or action=="STAY" or action=="NONE" or action=="GATHER" :
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                    continue
                                #pass
                            #East
                            if position=="E":
                                if action=="LEFT" or action=="STAY" or action=="NONE" or action=="HIT":
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                    continue
                                if action=="SHOOT" and n_arrows>0:
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                    continue
                                #pass
                            # West
                            if position=="W":
                                if action=="RIGHT" or action=="STAY" or action=="NONE":
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                    continue
                                if action=="SHOOT" and n_arrows>0:
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                    continue
                                #pass
                            # Centre
                            if position=="C":
                                if action=="RIGHT" or action=="LEFT" or action=="UP" or action=="DOWN" or action=="STAY" or action=="NONE":
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                    continue
                                if action=="SHOOT" and n_arrows>0:
                                    valid_states.append([position, material, n_arrows, mm_state, mm_health, action])
                                    continue               
                                #pass
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
    for record in output_meta_data:
        # record = [position, material, n_arrows, mm_state, mm_health, action]
        #print(record)
        #print(record[0])
        if record[0]=='N' or record[0]=='S':
            R.append(-1.0)
        if record[0]=='E' or record[0]=='W' or record[0]=='C':
            if record[4]==0:
                R.append(0.0)
            elif record[3]=='D':
                R.append(-1.0)
            elif record[3]=='R' and record[5]!='STAY':
                R.append(0.5*(-40) + 0.5*(-1))
            elif record[5]=='STAY':
                R.append(-1)
            else:
                print("WTF")
            #pass
    return R

if __name__=="__main__":
    print("This script performs very basic testing of helper functions")
    X, R, output_meta_data = init_X_and_R()
    if len(X)==1238:
        print("init_X_and_R() Works fine!")
    else:
        #print(len(meta_data))
        print("Error with init_X_R() function")
        print("Expected output: {0}, but recieved output: {1}".format(1238, len(X)))

    R = update_R(output_meta_data)
    if len(R)==1238:
        print("update_R() Works fine!")
    else:
        #print(len(meta_data))
        print("Error with update_R() function")
        print("Expected output: {0}, but recieved output: {1}".format(1238, len(R)))