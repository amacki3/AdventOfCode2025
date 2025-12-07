import numpy as np

with open('input.txt','r') as f:
    map = []
    for line in f.readlines():
        l = line.replace('.','0').replace('@','1').strip()
        map.append([int(c) for c in l])
    map = np.array(map)

print(map)
#we roll the map left, right, up, down etc to give a count as to if something exists there. then its simply a sum of the totals.
def determine_rolls(map):
    r = np.roll(map,-1)
    r[:,-1] = 0 # eliminate the edge of the board
    l = np.roll(map,1)
    l[:,0] = 0
    u = np.roll(map.T,1).T
    u[0,:] = 0
    d = np.roll(map.T,-1).T
    d[-1,:] = 0
    ur =np.roll(u,-1)
    ur[:,-1] = 0
    ul = np.roll(u,1)
    ul[:,0] = 0
    dr = np.roll(d,-1)
    dr[:,-1] = 0
    dl = np.roll(d,1)
    dl[:,0] = 0

    locs = r+l+u+d+ur+ul+dr+dl

    total = np.sum(locs[map == 1] <4)
    map[np.logical_and(locs < 4, map == 1)] = 0
    return total, map


total = 0
print("Solution 1:")
t,m = determine_rolls(map)
print(t)
total += t
while t > 0:
    t,m = determine_rolls(m)
    total += t

print("Solution 2:")
print(total)