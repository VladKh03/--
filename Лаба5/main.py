import numpy as np
import math

def euler_method(f, x0, y0, h, interval):
    num_steps = int((interval[1] - interval[0]) / h)
    x = np.zeros(num_steps + 1)
    y = np.zeros(num_steps + 1)
    y_prime = np.zeros(num_steps + 1)
    x[0] = x0
    y[0] = y0

    for i in range(num_steps):
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + h * f(x[i], y[i])
        y_prime[i] = f(x[i], y[i])

    y_prime[-1] = f(x[-1], y[-1])

    return x, y, y_prime

def f(x, y):
    return 1 + 3 * x - math.sqrt(y)

x0 = 1  
y0 = 1  
h = 0.25  
interval = [1, 4.5]  

x, y, y_prime = euler_method(f, x0, y0, h, interval)


print("   i    |     x     |     y     |   y_prime ")
print("-------------------------------------------")
for i in range(len(x)):
    print(f"  {i:4d}  |  {x[i]:8.5f}  | {y[i]:9.5f} | {y_prime[i]:9.5f} ")

