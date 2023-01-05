a = 10
b = 10

print(a)
print(a)
print(type(a))
print(type(b))

c = int()

print(c)
print(type(c))

c = int("1101", base=2)

print(c)
print(type(c))

def square(n):
    return n**2

print(square)
print(square(2))
print(type(square))

f = square

print(f)
print(f(2))
print(type(square))

def cube(n):
    return n**3

def select_function(func_id):
    if func_id == 1:
        return square
    else:
        return cube

f = select_function(1)
print(f(2))
print(f is square)

f = select_function(0)
print(f(2))
print(f is cube)

print(select_function(1)(2))
print(select_function(0)(2))

def exec_function(fn, n):
    return fn(n)

print(exec_function(square, 2))
print(exec_function(cube, 2))
