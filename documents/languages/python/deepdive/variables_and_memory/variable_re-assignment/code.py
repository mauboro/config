def hex_id(variable):
    return hex(id(variable))

a = 10
print(hex_id(a))

a = 10 
print(hex_id(a))

a = 1
b = 1
print(hex_id(a))
print(hex_id(b))

