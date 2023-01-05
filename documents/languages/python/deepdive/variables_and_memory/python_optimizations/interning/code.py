#it is important to note here that the in my current version(CPython 3.8) the interning of numbers seems to have expanded the range, so the practical side of this lesson won't me illustrated properly. EDIT: now I actually know the reason behind it! It turns out that Python is able to recognize that two immutable objects are the same and therefore re-use the same object! If I were to set a = 500 in a module and then set b = 500 in another and then import one module into another and check their identity, it would show that those are different objects!

a = 10 
b = 10

print(a is b)
print(hex(id(a)), hex(id(b)))

a = -5 
b = -5

print(a is b)
print(hex(id(a)), hex(id(b)))

a = 256
b = 256

print(a is b)
print(hex(id(a)), hex(id(b)))

a = 257
b = 257

print(a is b)
print(hex(id(a)), hex(id(b)))

a = 10
b = 10
c = int("10")
d = int("1010", base=2)

print(a is b)
print(a is c)
print(a is d)
print(hex(id(a)), hex(id(b)))
print(hex(id(a)), hex(id(c)))
print(hex(id(a)), hex(id(d)))
