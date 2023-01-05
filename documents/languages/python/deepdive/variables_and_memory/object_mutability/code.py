my_list = [1, 2, 3]

print(my_list)
print(type(my_list))
print(id(my_list))

my_list.append(4)

print(my_list)
print(type(my_list))
print(id(my_list))

another_list = [1, 2, 3]

print(another_list)
print(type(another_list))
print(id(another_list))

another_list = another_list + [4]

print(another_list)
print(type(another_list))
print(id(another_list))

my_dict = dict(first_key=1, second_key='a')

print(my_dict)
print(type(my_dict))
print(id(my_dict))

my_dict['third_key'] = 10.9

print(my_dict)
print(type(my_dict))
print(id(my_dict))

my_tuple = (1, 2, 3)

print(my_tuple)
print(type(my_tuple))
print(id(my_tuple))

print(my_tuple[0])
print(type(my_tuple[0]))
print(id(my_tuple[0]))

another_tuple = ([1, 2], [3, 4])

print(another_tuple)
print(type(another_tuple))
print(id(another_tuple))

print(another_tuple[0])
print(type(another_tuple[0]))
print(id(another_tuple[0]))

another_tuple[0].append(3)

print(another_tuple)
print(type(another_tuple))
print(id(another_tuple))

print(another_tuple[0])
print(type(another_tuple[0]))
print(id(another_tuple[0]))

