ms = []
sl = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    ms += [[name, score]]
    sl += [score]
'''print(ms)
print(sorted(ms))
print(ms)
print(sl)'''
b = sorted(list(set(sl)))[1]
# print(b)
for a, c in sorted(ms):
    if c == b:
        print(a)
