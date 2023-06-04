def func(val):
    return 2 * val**3 - 10 * val**2 - 6

def chord_method(min_val, max_val, e):
    while abs(func(max_val) - func(min_val)) > e:
        x = (min_val * func(max_val) - max_val * func(min_val)) / (func(max_val) - func(min_val))
        if func(x) == 0:
            return x
        elif func(min_val) * func(x) < 0:
            max_val = x
        else:
            min_val = x
    return (min_val + max_val) / 2

min_val = 1
max_val = 6
e = 0.001

solution = chord_method(min_val, max_val, e)
if solution is not None:
    solution = round(solution, 5)
    print("Result:", solution)
