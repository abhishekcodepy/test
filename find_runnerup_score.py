# find the runnerup numer from list
n = int(input())
arr = list(map(int, input().split()))

z = max(arr)

for i in range(n):
    if z == max(arr):
        arr.remove(max(arr))
print(max(arr))
