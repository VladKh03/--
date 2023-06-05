import math

def runge_kutta(f, a, b, h, y0):
    x_values = [a]
    y_values = [y0]
    delta_y_values = [0] 
    k_values = [0] 
    x = a
    y = y0

    while x < b:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h

        delta_y = (k1 + 2*k2 + 2*k3 + k4) / 6  
        k = h * f(x, y) 
        x_values.append(x)
        y_values.append(y)
        delta_y_values.append(delta_y)
        k_values.append(k)

    return x_values, y_values, delta_y_values, k_values


def f(x, y):
    return 1 + 3 * x - math.sqrt(y)

a = 1
b = 1.5
h = 0.1
y0 = 1

x_values, y_values, delta_y_values, k_values = runge_kutta(f, a, b, h, y0)

print("    x     |      y      |  delta_y  |     K    ")
print("------------------------------------------------")
for x, y, delta_y, k in zip(x_values, y_values, delta_y_values, k_values):
    print(f"{x:8.2f}  | {y:10.4f} | {delta_y:10.4f} | {k:9.4f}")
