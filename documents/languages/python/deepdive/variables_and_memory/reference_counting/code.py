import sys, ctypes

a = [1, 2, 3]
print(id(a))
print(sys.getrefcount(a))

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

#this is the same as putting the memory address itself on the function because id will have already finished running by the time refcount begins to executing, there releasing the pointer that it used to get to the memory address that the variable a is referencing.
print(ref_count(id(a)))

b = a
print(id(b))

#since they are identical, either a or b can be passed in those functions.
print(sys.getrefcount(a))
print(ref_count(id(a)))

c = a
print(id(c))

print(sys.getrefcount(a))
print(ref_count(id(a)))

c = 2
print(id(c))

print(sys.getrefcount(a))
print(ref_count(id(a)))


#the value on that print statement may vary because as soon as I assign the variable a to None(another object with its own memory address) the Python Memory Manager will notice that the reference count to the address that a was pointing to is now empty and because of that it will throw away the previously stored value what was on it thus freeing its space for a new allocation.
a_id = id(a)
a = None
print(ref_count(a_id))
