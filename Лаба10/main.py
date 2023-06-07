import math


def run():
    x0 = enter_double("Enter the starting point: ")
    xn = enter_double("Enter the endpoint: ")
    h = enter_double("Enter a step: ")
    extrapolation_point = enter_double("Enter the extrapolation point x: ")
    number_of_points = int((xn - x0) / h) + 1
    x = [0.0] * number_of_points
    y = [0.0] * number_of_points

    for i in range(number_of_points):
        x[i] = x0 + i * h
        y[i] = 1.0 / (6*x[i]*x[i]*x[i]*x[i]+5)

    print("Points")
    for i in range(number_of_points):
        print("x = {0} | y = {1:.5f} |".format(x[i], y[i]))


    if extrapolation_point < x[0]:
        extrapolated_value = extrapolate_newton(x, y, extrapolation_point)
        print("Extrapolated value at a point {0}: {1}".format(extrapolation_point, extrapolated_value))

    if extrapolation_point > xn:
        coefficients = newton_interpolation(x, y)
        extrapolated_value = evaluate_newton(x, y, coefficients, extrapolation_point)
        print("Extrapolated value at a point {0}: {1}".format(extrapolation_point, extrapolated_value))


def newton_interpolation(x, y):
    n = len(x)
    coefficients = [0.0] * n

    for i in range(n):
        coefficients[i] = y[i]

    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            coefficients[j] = (coefficients[j] - coefficients[j - 1]) / (x[j] - x[j - i])

    return coefficients


def extrapolate_newton(x, y, extrapolation_point):
    n = len(x)
    coefficients = newton_interpolation(x, y)
    result = coefficients[n - 1]

    for i in range(n - 2, -1, -1):
        result = result * (extrapolation_point - x[i]) + coefficients[i]

    return result


def evaluate_newton(x, y, coefficients, evaluation_point):
    n = len(x)
    result = coefficients[n - 1]

    for i in range(n - 2, -1, -1):
        result = result * (evaluation_point - x[i]) + coefficients[i]

    return result


def enter_double(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid number format. Try again.")



run()