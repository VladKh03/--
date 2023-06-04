import numpy as np

a = 0
b = 1
n = 10


def f(x):
    return x**2 * np.sin(x)


def rectangle_rule(f, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    x_mid = x[:-1] + dx/2
    return dx * np.sum(f(x_mid))


def trapezoid_rule(f, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    return dx * (np.sum(f(x[:-1])) + np.sum(f(x[1:]))) / 2


def simpsons_rule(f, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    return dx / 3 * (f(x[0]) + 4*np.sum(f(x[1:-1:2])) + 2*np.sum(f(x[2:-1:2])) + f(x[-1]))


result_rectangle = rectangle_rule(f, a, b, n)
result_trapezoid = trapezoid_rule(f, a, b, n)
result_simpsons = simpsons_rule(f, a, b, n)

print("The result according to the formula of rectangles:", result_rectangle)
print("The result according to the trapezoidal formula:", result_trapezoid)
print("Result according to Simpson's formula:", result_simpsons)
