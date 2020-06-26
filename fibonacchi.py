def fib1(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for _ in range(n - 2):
            a, b = b, a + b
        return b

def fib2(n):  ## Познаем ужасы неправильно используемой рекурсии :
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return  fib2(n - 1) + fib2(n - 2)

def fib3_cached(n):
    cache = {1: 0, 2: 1}
    def fib3(num):
        if num in cache:
            return cache[num]
        else:
            cache[num] = fib3(num - 1) + fib3(num - 2)
            return cache[num]
    return fib3(n)

my_functions = [fib1, fib2, fib3_cached]

for function in my_functions:
    for num in range(1, 11):
        print(function(num), end=" ")
    print()

assert fib1(6) == fib2(6) == fib3_cached(6)
