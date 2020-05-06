from itertools import groupby
a = []
for k, g in groupby(input()):
    print(*[(len(list(g)), int(k))], end="")


#print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
