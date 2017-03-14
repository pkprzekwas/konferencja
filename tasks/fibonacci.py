
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


fibonacci_gen = fib()

for num in fibonacci_gen:
    print(num)
