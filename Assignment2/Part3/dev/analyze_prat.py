import json
  
# Opening JSON file
#f = open('pratyush_output.json',)
f = open('pulak.json',)

output = json.load(f)

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
#print(output["policy"][10:20])
for record in output["policy"]:
    if record[0][:4]==['C', 2, 1, 'R']:
        print(record)