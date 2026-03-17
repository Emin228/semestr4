import mpmath as mp

# константы
g = 9.81                 # ускорение свободного падения
r_earth = 6.377e6        # радиус Земли (м)
R = 60.27 * r_earth      # начальное расстояние

# подынтегральная функция
def f(r):
    return mp.sqrt((r * R) / (2 * g * r_earth**2 * (R - r)))

# численное интегрирование
t = mp.quad(f, [r_earth, R])

print("Falling time (seconds):", t)
print("Falling time (hours):", t/3600)
print("Falling time (days):", t/86400)


import mpmath as mp

# параметры
a = 1
b = 2

# функция y
def y(x):
    return (a/2) * (mp.e**(x/a) + mp.e**(-x/a))

# подынтегральная функция
def f(x):
    return mp.pi * (y(x)**2)

# численное интегрирование
V = mp.quad(f, [0, b])

print(V)