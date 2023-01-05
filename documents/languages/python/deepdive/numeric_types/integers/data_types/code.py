import sys, time

print(type(100))

#it states that that it is using 24 bytes because of the memory overhead that comes with the creation of the object, but it is actually using 0 bytes to store 0.
print(sys.getsizeof(0))

print(sys.getsizeof(1))

print(sys.getsizeof(2**1000))

print((160 - 24) * 8)

def calc(n):
    n * 2

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
calc(2 ** 1000)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
calc(2 ** 10000)
end = time.perf_counter()
print(end - start)

