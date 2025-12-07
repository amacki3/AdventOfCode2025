import numpy as np


def get_digits(num):
    return np.floor(np.log10(num))


ranges = []
with open("input.txt",'r') as f:

    for r in f.read().split(','):
        ranges.append([ int(x) for x in r.split('-')])




invalid_sum = 0
for r in ranges:
    digits = [get_digits(r[0]),get_digits(r[1])]
    if digits[0] == digits[1] and digits[0] % 2 == 1:
        #We can only have bad values with an even digit number
        pass
    
        
    

print(ranges)
