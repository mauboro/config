import ctypes, gc

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id: int):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return f"Object exists, its name is {obj}"
    return "Object not found"

def hex_id(obj):
    return hex(id(obj))


class A:
    def __init__(self):
        self.b = B(self) 
        print(f"A: {hex(id(self))}, b: {hex(id(self.b))}")

class B:
    def __init__(self, a):
        self.a = a
        print(f"B: {hex(id(self))}, a: {hex(id(self.a))}")

#disabling the Garbage Collector in that script wont make a difference because of the one time execution, I guess. 
gc.disable()

my_var = A()

print(f"""
    hex id of my_var: {hex_id(my_var)}
    hex id of my_var.b: {hex_id(my_var.b)}
    hex id of my_var.b.a: {hex_id(my_var.b.a)}
""")

#this will be 2 since my_var and the b instance variable is pointing to it.
a_id = id(my_var)

#this will be 1 because only the a instance variable is pointing to it.
b_id = id(my_var.b)

print(f"hex id of a_id: {hex(a_id)}")
print(f"hex id of b_id: {hex(b_id)}")

print(ref_count(a_id))
print(ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))

#up until this point this code was written in order to create the circular reference situation, now its time to destroy the reference in the A object by assigning the initial reference made by my_var to None, thus creating the circular reference.

my_var = None

print(ref_count(a_id))
print(ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))

#manually collecting garbage with the gc module, how fucking cool is that??
gc.collect()

print(ref_count(a_id))
print(ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))
