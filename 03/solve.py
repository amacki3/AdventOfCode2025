import numpy as np

with open('input.txt','r') as f:
    lines = f.readlines()


joltage = 0
for l in lines:
    l = l.strip()
    sz = len(l)
    first = 0
    second = 0

    for idx,char in enumerate(l):
        #walk the length, this should be order n
        #There is maybe some optimisation to be done by finding a first char as a 9 and not continuing...
        val = int(char)
        if val > first and idx + 1 < sz: 
            first = val
            second = int(l[idx+1])
        elif val > second:
            second = val

    joltage += first*10 + second

print("Solution 1:")
print(joltage)

print("Solution 2")
#What might be elegant is starting 12 from the right and walking back, keeping track of the 12 largest nums we have found and rotating them along?
#Once we reach the end or all nums are 9s then it must be maximal.

#What is easier to implement is some numpy max on data slices!

def find_largest_with_spare(data,start_num,spare_num):
    largest = np.max(data[start_num:-(spare_num+1)])
    loc = np.array(np.argmax(data[start_num:-(spare_num+1)]))
    return largest,loc+1 + start_num

joltage = 0
for l in lines:
    vals = [int(x) for x in l.strip()]
    vals.append(0) #hack to make slicing easier!
    remaining_numbers = 11
    start_num = 0
    for nums in range(12):
        j,start_num = find_largest_with_spare(vals,start_num,remaining_numbers-nums)
        joltage += j * 10 ** (11-nums)
print(joltage)