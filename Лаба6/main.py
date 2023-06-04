import numpy as np
import math


def runge_kutta_modified(f, x_init, y_init, step_size, num_steps):
    x_vals = np.zeros(num_steps)
    y_vals = np.zeros(num_steps)
    x_vals[0] = x_init
    y_vals[0] = y_init

    for i in range(1, num_steps):
        k1 = step_size * f(x_vals[i - 1], y_vals[i - 1])
        k2 = step_size * f(x_vals[i - 1] + 0.5 *
                           step_size, y_vals[i - 1] + 0.5 * k1)
        k3 = step_size * f(x_vals[i - 1] + 0.5 *
                           step_size, y_vals[i - 1] + 0.5 * k2)
        k4 = step_size * f(x_vals[i - 1] + step_size, y_vals[i - 1] + k3)

        x_vals[i] = x_vals[i - 1] + step_size
        y_vals[i] = y_vals[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0

    return x_vals, y_vals


def func(x, y):
    return 1 + 3 * x - math.sqrt(y)


initial_x = 1
initial_y = 1.0
step_size = 0.25
num_steps = 1000

x_values, y_values = runge_kutta_modified(
    func, initial_x, initial_y, step_size, num_steps)

for x_val, y_val in zip(x_values, y_values):
    if x_val == 1:
        y_val_rounded = round(y_val, 5)
        print("Approximation for x = 1:")
        print(f"y = {y_val_rounded}")
        print()
    elif x_val == 4.5:
        y_val_rounded = round(y_val, 5)
        print("Approximation for x = 4.5:")
        print(f"y = {y_val_rounded}")
        print()
