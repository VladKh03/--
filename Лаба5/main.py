import math


def f(x, y):
    return 1 + 3 * x - math.sqrt(y)


def euler_method(a, b, y0, h):
    x_values = []
    y_values = []
    x = a
    y = y0
    while x <= b:
        x_values.append(x)
        y_values.append(y)
        y += h * f(x, y)
        x += h
    return x_values, y_values

a = 1
b = 4.5
y0 = 1
h = 0.25

x_values, y_values = euler_method(a, b, y0, h)

print(" x\t| y")
print("-------------")
for x, y in zip(x_values, y_values):
    print(f"{x:.2f}\t| {y:.5f}")
