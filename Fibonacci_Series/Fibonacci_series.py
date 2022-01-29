def fib_1(N):
    '''
    This function will print Fibonacci Series N elements
    '''
    a = 0
    b = 1
    for i in range(N):
        print(a)
        a,b = b,a+b

fib_1(7)

def fib_2(N):
    '''
    This function will generate Fibonacci Series N elements
    It will use generator concept
    '''
    a = 0
    b = 1
    for i in range(N):
        yield a
        a,b = b,a+b

fib_7 = fib_2(7)
print(fib_7)
for i in fib_7:
    print(i)

def fib_3(N):
    '''
    This function will generate Fibonacci using recursion
    It will use generator concept
    '''
    if N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        return (fib_3(N-1) + fib_3(N-2))

print(fib_3(7))

def fib_4(N):
    '''
    This function will generate Fibonacci using recursion and cache
    It will use generator concept
    '''
    if N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        if (N-1 in fib_4.d):
            min_1 = fib_4.d[N-1]
        else:
            min_1 = fib_4(N-1)
            fib_4.d[N-1] = min_1
        if (N-2 in fib_4.d):
            min_2 = fib_4.d[N-2]
        else:
            min_2 = fib_4(N-2)
            fib_4.d[N-2] = min_2
        return (min_1 + min_2)
fib_4.d = {}
print(fib_4(10))
print(fib_4.d)
