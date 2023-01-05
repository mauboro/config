a = "hello"
b = a

print()
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))

b = "hello world"

print()
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))

a = "hello"
b = "hello"

print()
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))


b = "hello world"

print()
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))


a = [1, 2, 3]
b = a

print()
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))

b.append(100)

print()
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))

a = 10
b = 10

print()
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))


a = 50000
b = 50000

print()
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))
