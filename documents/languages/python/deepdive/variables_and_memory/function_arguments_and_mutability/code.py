def process(s):
    print(f"Initial # of s: {id(s)}")
    s += " world"
    print(f"Final # of s: {id(s)}")

my_var = "hello"
print(f"my_var: {my_var}")
print(f"id of my_var: {id(my_var)}")

print()

process(my_var)
print()
print(f"my_var: {my_var}")
print(f"id of my_var: {id(my_var)}")

def modify_list(l):
    print(f"Initial # of s: {id(l)}")
    l.append(100)
    print(f"Final # of s: {id(l)}")

print()
print()

my_list = [1, 2, 3]
print(f"my_list: {my_list}")
print(f"id of my_list: {id(my_list)}")

print()

modify_list(my_list)
print()
print(f"my_list: {my_list}")
print(f"id of my_list: {id(my_list)}")


def modify_tuple(l):
    print(f"Initial # of s: {id(l)}")
    l[0].append(100)
    print(f"Final # of s: {id(l)}")

my_tuple = ([1, 2], "a")
print(f"my_tuple: {my_tuple}")
print(f"id of my_tuple: {id(my_tuple)}")

modify_tuple(my_tuple)
print(f"my_tuple: {my_tuple}")
print(f"id of my_tuple: {id(my_tuple)}")
