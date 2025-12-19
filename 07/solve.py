splits = 0

with open("input.txt") as f:
    start = f.readline()
    locs = [start.find('S')]    
    for line in f.readlines():
        new_locs = set()
        for loc in locs:
            if line[loc] == '^':
                splits += 1
                new_locs.add(loc-1)
                new_locs.add(loc+1)
            else:
                new_locs.add(loc)     
        locs = new_locs
    
print(splits)