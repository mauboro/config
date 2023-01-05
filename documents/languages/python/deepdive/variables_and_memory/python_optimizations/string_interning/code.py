import sys
import time

a = "hello"
b = "hello"

print(id(a), id(b))
print(a is b)
print(a == b)

a = "hello world bla bla bla bla bla bla"
b = "hello world bla bla bla bla bla bla"

print(id(a), id(b))
print(a is b)
print(a == b)

a = "_this_is_a_long_string_that_could_be_used_as_an_identifier"
b = "_this_is_a_long_string_that_could_be_used_as_an_identifier"

print(id(a), id(b))
print(a is b)
print(a == b)

a = sys.intern("hello world")
b = sys.intern("hello world")
c = 'hello world'

print(id(a), id(b))
print(a is b)
print(a == b)
print(id(a), id(c))
print(a is c)
print(a == c)

def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    for i in range(n):
        if a is b:
            pass

start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()
print(end - start)
