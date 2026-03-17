import functools

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res

def my_genn():
    """Сопрограмма"""
    while True:
        number_of_fib_elem = yield
        g = fib_elem_gen()
        l = [next(g) for _ in range(number_of_fib_elem)]
        yield l

def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner

my_gen = fib_coroutine(my_genn)
gen = my_gen()
print(gen.send(10))



             