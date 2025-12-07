import numpy as np

with open("input.txt",'r') as f:
    data = np.fromstring(f.read().replace('L','-').replace('R','+'),dtype=np.int64,sep='\n')

data = np.insert(data,0,50)
print("Solution 1:")
print(np.sum(np.mod(np.cumsum(data),100) == 0))

#Sol 2

#Firstly, additional 