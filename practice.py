import numpy

n, m = map(int, input().split())
print(n, m)
my_array = []
for i in range(n):
    a = list(map(int, input().split()))
    my_array.append(a)

my_array = numpy.array(my_array)

numpy.set_printoptions(legacy='1.13')
print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))
print(numpy.std(my_array))
