def add_1(a,b):
    return (a-(-b))

def add_2(a,b):
    for i in range(b):
        a += 1
    return a

def add_3(a,b):
    while not b == 0:
        carry = a&b
        a = a^b
        b = carry << 1
    return a

def add_4(a,b):
    if b == 0:
        return a
    return add_4(a^b, (a&b)<<1)

print(add_4(5,6))
