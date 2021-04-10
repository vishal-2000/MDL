import json
  
# Opening JSON file
f = open('part_3_output.json',)

dictionary = json.load(f)

f.close()

f = open('pratyush_output.json',)

data = json.load(f)

f.close()

'''
print("No of keys: "+ str(len(output)))
print("Shape of A: ("+str(len(output["a"])) + ", "+str(len(output["a"][0]))+")")
print("Length of R: "+str(len(output["r"])))
print("Length of X: "+str(len(output["x"])))
print("Length of alpha: "+str(len(output["alpha"])))
print("Length of policy: "+str(len(output["policy"])))
print("Value of objective: "+str(output["objective"]))

print("\n\nPrinting first few rows of each of the above matrices/vectors:\n\n")

#print("A matrix (first 5 rows each with first 5 columns):")
#print(output["a"][:5][0])
print("R vector:")
print(output["r"][:5])
print("X vector:")
print(output["x"][:5])
print("alpha vector:")
print(output["alpha"][:5])
print("policy matrix:")
print(output["policy"][:5])
'''

# Policy analysis section (comment this section for general testing)
#print(output["policy"][10:20])
#for record in output["policy"]:
#    if record[0][:4]==['N', 0, 1, 'D']:
#        print(record)
#for record in output["policy"]:
#    if record[0][:4]==['S', 1, 0, 'R']:
#        print(record)

unmatched = 0
matched = 0
k = -1
for record in data["policy"]:
    k+=1
    if record in dictionary["policy"]:
        matched+=1
    else:
        unmatched+=1
        #print(record)
        for l in dictionary["policy"]:
            if l[0]==record[0]:
                print(record, l, k)
if unmatched==0:
    print("Perfect, go for it!")