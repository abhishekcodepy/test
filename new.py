import numpy
n = int(input())
array_a = []
array_b = []
for i in range(n):
    a = list(map(int, input().split()))
    array_a.append(a)

for i in range(n):
    b = list(map(int, input().split()))
    array_b.append(b)

array_a = numpy.array(array_a)
array_b = numpy.array(array_b)
print(numpy.dot(array_a, array_b))
