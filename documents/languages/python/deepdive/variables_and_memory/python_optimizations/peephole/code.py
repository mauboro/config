import string, time

def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = "abc" * 5
    d = "ab" * 31
    e = "the quick brown fox"
    f = ["a", "b"] * 11


print(my_func.__code__.co_consts)

def list_into_tuple():
    if e in [1, 2, 3]:
        pass

print(list_into_tuple.__code__.co_consts)

def set_into_frozenset():
    if e in {1, 2, 3}:
        pass

print(set_into_frozenset.__code__.co_consts)

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

def test_membership(n, container):
    for i in range(n):
        if "z" in container:
            pass

start = time.perf_counter()
test_membership(10000000, char_list)
end = time.perf_counter()
print(f"list: {end - start}")

start = time.perf_counter()
test_membership(10000000, char_tuple)
end = time.perf_counter()
print(f"tuple: {end - start}")

start = time.perf_counter()
test_membership(10000000, char_set)
end = time.perf_counter()
print(f"set: {end - start}")

