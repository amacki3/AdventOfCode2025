import numpy as np


data = np.genfromtxt('input.txt',dtype='<U')
values = data[0:-1,:].astype(np.int64)
ops = data[-1,:]
num_calcs = np.size(data,1)

def do_arithmetic(vals,op):
    if op == '+':
        return np.sum(vals)
    elif op == '*':
        return np.prod(vals)

total = 0
for i in range(num_calcs):
    total += do_arithmetic(values[:,i],ops[i])

print("Solution 1:")
print(total)
