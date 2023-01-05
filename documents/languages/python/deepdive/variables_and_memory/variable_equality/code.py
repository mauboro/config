a = 10
b = 10

print(hex(id(a)))
print(hex(id(b)))
print(f"a is b: {a is b}")
print(f"a == b: {a == b}")
print()

a = 500
b = 500

print(hex(id(a)))
print(hex(id(b)))
print(f"a is b: {a is b}")
print(f"a == b: {a == b}")
print()

a = [1, 2, 3]
b = [1, 2, 3]

print(hex(id(a)))
print(hex(id(b)))
print(f"a is b: {a is b}")
print(f"a == b: {a == b}")
print()

a = 10 
b = 10.0

print(hex(id(a)))
print(hex(id(b)))
print(f"a is b: {a is b}")
print(f"a == b: {a == b}")
print()

a = 10 + 0j
b = 10.0

print(type(a))
print(type(b))
print(hex(id(a)))
print(hex(id(b)))
print(f"a is b: {a is b}")
print(f"a == b: {a == b}")
print()

a = None
b = None

print(type(a))
print(type(b))
print(hex(id(a)))
print(hex(id(b)))
print(f"a is b: {a is b}")
print(f"a == b: {a == b}")
print()
